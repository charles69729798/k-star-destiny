@echo off
echo =======================================================
echo     K-Destiny AI Local Development Environment Setup
echo =======================================================
echo.

echo [1/3] Cleaning up zombie processes...
echo Killing any existing uvicorn/node processes...
taskkill /F /IM uvicorn.exe /T 2>nul
taskkill /F /IM node.exe /T 2>nul
taskkill /F /IM python.exe /T 2>nul

echo Killing processes bound to ports 8000 (Backend) and 5173 (Frontend)...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do taskkill /F /PID %%a 2>nul
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :5173') do taskkill /F /PID %%a 2>nul
echo Done.
echo.

echo [2/3] Preparing Docker environment...
echo Restarting Docker containers with Volume Mounts (Hot Reload Enabled)...
docker-compose down
docker-compose up -d --build
echo Done.
echo.

echo [3/3] Status Check
echo Waiting for containers to initialize...
timeout /t 5 /nobreak >nul
docker ps
echo.
echo =======================================================
echo ✅ Environment is READY!
echo.
echo 🌐 Frontend : http://localhost
echo 📡 Backend  : http://localhost:8000
echo.
echo ✏️  Just edit files in VSCode and save.
echo    Changes will be automatically hot-reloaded!
echo =======================================================
pause
