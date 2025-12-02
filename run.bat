@echo off
echo ========================================
echo   Roadside Assistant Application
echo ========================================
echo.
echo Starting Flask server...
echo.
echo The application will be available at:
echo   http://localhost:5000
echo   http://127.0.0.1:5000
echo.
echo Demo Login:
echo   Username: demo
echo   Password: demo123
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

cd /d "%~dp0"
python app.py

pause
