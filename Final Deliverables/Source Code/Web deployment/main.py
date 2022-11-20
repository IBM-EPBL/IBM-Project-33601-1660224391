from flask import Flask,render_template,request,redirect,session,url_for,flash
from predictor import predict
app = Flask(__name__)
app.secret_key = "helo"
app.config['UPLOAD_DIR']='static'
app.static_folder = 'static'

@app.route("/")
@app.route("/home",methods=['GET','POST'])
def home():
    if 'user' in session:
        if(request.method=='POST'):
            result = predict(request.form.values())
            session.pop('user')
            return render_template("success.html",data=result)
        else:
            return render_template("home.html")
    else:
        return redirect(url_for("login"))

@app.route("/login",methods=['GET','POST'])
def login():
    if(request.method=='POST'):
        session['user']="xyz"
        return redirect(url_for("home"))
    else:
      return render_template("login.html")

app.run(debug=True)     