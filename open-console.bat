@echo off
cd /d %~dp0
call conda activate "%cd%\env_vevo"
cmd /k