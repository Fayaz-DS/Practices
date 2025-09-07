# PowerShell script for automatic Git push
# This script automatically commits and pushes changes to GitHub

Write-Host "🚀 Starting automatic push process..." -ForegroundColor Green
Write-Host "=" * 50 -ForegroundColor Cyan

# Check if we're in a git repository
if (-not (Test-Path ".git")) {
    Write-Host "❌ Not in a Git repository. Please run 'git init' first." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check for changes
$changes = git status --porcelain
if (-not $changes) {
    Write-Host "📝 No changes detected. Repository is up to date." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 0
}

Write-Host "📝 Changes detected. Proceeding with commit and push..." -ForegroundColor Yellow

# Add all changes
Write-Host "🔄 Adding all changes..." -ForegroundColor Blue
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to add changes" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✅ Changes added successfully" -ForegroundColor Green

# Create commit with timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMessage = "Auto-commit: $timestamp"

Write-Host "🔄 Committing changes..." -ForegroundColor Blue
git commit -m $commitMessage
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to commit changes" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✅ Changes committed successfully" -ForegroundColor Green

# Push to remote
Write-Host "🔄 Pushing to GitHub..." -ForegroundColor Blue
git push origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Push failed. You may need to set up the remote repository first." -ForegroundColor Yellow
    Write-Host "   Run: git remote add origin <your-github-repo-url>" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✅ Successfully pushed to GitHub" -ForegroundColor Green

Write-Host "=" * 50 -ForegroundColor Cyan
Write-Host "🎉 Automatic push completed successfully!" -ForegroundColor Green
Read-Host "Press Enter to exit"
