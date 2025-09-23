#!/usr/bin/env python3
"""
Automatic Git Push Script
This script automatically commits and pushes changes to GitHub repository.
"""

import subprocess
import sys
import os
from datetime import datetime

def run_command(command, description):
    """Run a shell command and return the result."""
    try:
        print(f"🔄 {description}...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {description} failed")
            print(f"   Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ Error running command: {e}")
        return False

def auto_push():
    """Automatically commit and push changes to GitHub."""
    print("🚀 Starting automatic push process...")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("❌ Not in a Git repository. Please run 'git init' first.")
        return False
    
    # Check for changes
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if not result.stdout.strip():
        print("📝 No changes detected. Repository is up to date.")
        return True
    
    # Add all changes
    if not run_command("git add .", "Adding all changes"):
        return False
    
    # Create commit message with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Auto-commit: {timestamp}"
    
    # Commit changes
    if not run_command(f'git commit -m "{commit_message}"', "Committing changes"):
        return False
    
    # Push to remote
    if not run_command("git push origin main", "Pushing to GitHub"):
        print("⚠️  Push failed. You may need to set up the remote repository first.")
        print("   Run: git remote add origin <your-github-repo-url>")
        return False
    
    print("=" * 50)
    print("🎉 Automatic push completed successfully!")
    return True

if __name__ == "__main__":
    auto_push()
