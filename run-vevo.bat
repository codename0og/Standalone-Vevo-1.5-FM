@echo off

if /i "%cd%"=="C:\Windows\System32" (
    color 0C
    echo The fork shouldn't be run with admin perms. Don't do that.
    echo.
    pause
    exit /b 1
)

setlocal
title Vevo-1.5

if not exist env_vevo (
    echo Please run 'install-vevo.bat' first to set up the environment.
    pause
    exit /b 1
)

env_vevo\python.exe run_vevo.py
echo.
pause
