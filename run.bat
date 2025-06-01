@echo off
setlocal

echo === Media Sorter ===

:: Activate the virtual environment
echo [INFO] Activating virtual environment...
call .venv\Scripts\activate.bat

:: Upgrade pip
echo [INFO] Updating pip...
pip install --upgrade pip >nul

:: Run the sorter
echo [INFO] Running media sorter...
python main.py

:: Keep console open
echo.
echo === Done! Press any key to exit. ===
pause >nul
