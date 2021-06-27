@echo off
Setlocal enabledelayedexpansion
rem Replace spaces with underscores
Set "Pattern= "
Set "Replace=_"

For %%a in (*.png) Do (
    Set "File=%%~a"
    Ren "%%a" "!File:%Pattern%=%Replace%!"
)

Pause&Exit