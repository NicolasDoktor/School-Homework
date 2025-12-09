@echo off
echo ================================================
echo   ARC Raiders - Jednoduchy HTTP Server
echo ================================================
echo.
echo Spoustim HTTP server na portu 8000...
echo.
echo Otevrete v prohlizeci: http://localhost:8000
echo.
echo Pro zastaveni serveru stisknete Ctrl+C
echo.
echo ================================================
echo.

py -m http.server 8000

pause
