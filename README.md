# 2019-Competiton

This is the code for our 2019 Competition Robot.

settings.json
=============
Depending on your platform, the user settings file is located here:
Windows: %APPDATA%\Code\User\settings.json
Example contents:
{
    "python.pythonPath": "C:\\windows\\py.exe"
}

macOS: $HOME/Library/Application Support/Code/User/settings.json
Example contents:
{
    "python.pythonPath": "/Library/Frameworks/Python.framework/Versions/3.7/bin/python3"
}

Pip
===
Get the python modules required for this project:
pip install -r requirements.txt

PIP Website:
https://pip.pypa.io/en/stable/reference/

Other commands Install, install with upgrade:
pip install wpilib
pip install -U wpilib

Output current set of modules, list the out of date modules:
pip list
pip list -o

Output current set of modules requirements, redirect into file requirements.txt:
pip freeze > requirements.txt





