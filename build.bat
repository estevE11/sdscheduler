pip install pyinstaller
pyinstaller.exe --onefile -w --icon=icon.ico main.py
copy icon.ico dist
cd dist
ren main.exe sdscheduler.exe