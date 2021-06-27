@echo off
cd %HOMEDRIVE%%HOMEPATH%\AppData\Local\Programs\Python\Python39
python.exe -m pip install --upgrade pip
pip install requests
cd %HOMEDRIVE%%HOMEPATH%\projects\programs\nmrt
setup.py
