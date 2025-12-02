@echo off
REM Create Desktop Shortcut for Roadside Assistant

set SCRIPT_DIR=%~dp0
set SHORTCUT_NAME=Roadside Assistant.lnk
set TARGET_PATH=%SCRIPT_DIR%run.bat
set ICON_PATH=%SystemRoot%\System32\SHELL32.dll,13

echo Creating desktop shortcut...

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\%SHORTCUT_NAME%'); $Shortcut.TargetPath = '%TARGET_PATH%'; $Shortcut.WorkingDirectory = '%SCRIPT_DIR%'; $Shortcut.IconLocation = '%ICON_PATH%'; $Shortcut.Description = 'Roadside Assistant Application'; $Shortcut.Save()"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo   SUCCESS!
    echo ========================================
    echo.
    echo Desktop shortcut created successfully!
    echo.
    echo You can now double-click "Roadside Assistant"
    echo on your desktop to start the application.
    echo.
) else (
    echo.
    echo Failed to create shortcut.
    echo Please run this script as Administrator.
    echo.
)

pause
