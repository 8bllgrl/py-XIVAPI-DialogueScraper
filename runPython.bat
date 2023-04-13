@echo off
echo Enter the letter that matches the program you wish to run:
echo.
echo Character dialogue and mentioned dialogue (V1) : A
echo Character dialogue only (V2) : B
echo.

set /p letter=""

set letter=%letter:~0,1%
if /i "%letter%"=="A" (
python finderV1.py
) else if /i "%letter%"=="B" (
python finderV2.py
) else (
echo Invalid letter entered.
)

pause