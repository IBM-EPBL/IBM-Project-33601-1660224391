@echo off
cd cpred\Scripts
CALL activate.bat
cd..
cd..
pip install -r requirements.txt
python main.py 
pause