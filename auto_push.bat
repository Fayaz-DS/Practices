@echo off
REM Automatic Git Push Batch Script for Windows
REM This script automatically commits and pushes changes to GitHub

echo 🚀 Starting automatic push process...
echo ==================================================

REM Check if we're in a git repository
if not exist ".git" (
    echo ❌ Not in a Git repository. Please run 'git init' first.
    pause
    exit /b 1
)

REM Check for changes
git status --porcelain > temp_status.txt
if %errorlevel% neq 0 (
    echo ❌ Error checking git status
    del temp_status.txt
    pause
    exit /b 1
)

REM Check if there are any changes
for /f %%i in (temp_status.txt) do (
    echo 📝 Changes detected. Proceeding with commit and push...
    goto :commit_changes
)

echo 📝 No changes detected. Repository is up to date.
del temp_status.txt
pause
exit /b 0

:commit_changes
del temp_status.txt

REM Add all changes
echo 🔄 Adding all changes...
git add .
if %errorlevel% neq 0 (
    echo ❌ Failed to add changes
    pause
    exit /b 1
)
echo ✅ Changes added successfully

REM Create commit with timestamp
for /f "tokens=1-6 delims=: " %%a in ("%time%") do set timestamp=%%a:%%b:%%c
set commit_message=Auto-commit: %date% %timestamp%

echo 🔄 Committing changes...
git commit -m "%commit_message%"
if %errorlevel% neq 0 (
    echo ❌ Failed to commit changes
    pause
    exit /b 1
)
echo ✅ Changes committed successfully

REM Push to remote
echo 🔄 Pushing to GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo ⚠️  Push failed. You may need to set up the remote repository first.
    echo    Run: git remote add origin ^<your-github-repo-url^>
    pause
    exit /b 1
)
echo ✅ Successfully pushed to GitHub

echo ==================================================
echo 🎉 Automatic push completed successfully!
pause
