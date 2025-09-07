#!/usr/bin/env python3
"""
GitHub Repository Setup Script
This script helps you set up a GitHub repository and connect it to your local project.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a shell command and return the result."""
    try:
        print(f"🔄 {description}...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
            return True, result.stdout
        else:
            print(f"❌ {description} failed")
            print(f"   Error: {result.stderr.strip()}")
            return False, result.stderr
    except Exception as e:
        print(f"❌ Error running command: {e}")
        return False, str(e)

def setup_github_repo():
    """Set up GitHub repository connection."""
    print("🚀 GitHub Repository Setup")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("❌ Not in a Git repository. Please run 'git init' first.")
        return False
    
    # Get repository name from current directory
    repo_name = os.path.basename(os.getcwd())
    print(f"📁 Repository name: {repo_name}")
    
    # Check if remote already exists
    success, output = run_command("git remote -v", "Checking existing remotes")
    if success and "origin" in output:
        print("⚠️  Remote 'origin' already exists.")
        print("   Current remotes:")
        print(f"   {output}")
        
        choice = input("Do you want to update the remote URL? (y/n): ").lower()
        if choice != 'y':
            print("Setup cancelled.")
            return True
    
    # Get GitHub repository URL from user
    print("\n📝 Please provide your GitHub repository URL:")
    print("   Example: https://github.com/username/repository-name.git")
    repo_url = input("GitHub URL: ").strip()
    
    if not repo_url:
        print("❌ No URL provided. Setup cancelled.")
        return False
    
    # Add or update remote
    if "origin" in output:
        command = f"git remote set-url origin {repo_url}"
        description = "Updating remote origin URL"
    else:
        command = f"git remote add origin {repo_url}"
        description = "Adding remote origin"
    
    if not run_command(command, description):
        return False
    
    # Verify remote setup
    if not run_command("git remote -v", "Verifying remote setup"):
        return False
    
    # Push to GitHub
    print("\n🚀 Ready to push to GitHub!")
    choice = input("Do you want to push now? (y/n): ").lower()
    if choice == 'y':
        if not run_command("git push -u origin main", "Pushing to GitHub"):
            print("⚠️  Push failed. You may need to:")
            print("   1. Create the repository on GitHub first")
            print("   2. Check your GitHub credentials")
            print("   3. Verify the repository URL")
            return False
    
    print("=" * 50)
    print("🎉 GitHub setup completed successfully!")
    print("\n📋 Next steps:")
    print("   1. Use 'python auto_push.py' for automatic pushing")
    print("   2. Or use 'auto_push.bat' on Windows")
    print("   3. Set up Git hooks for automatic pushing on every commit")
    
    return True

if __name__ == "__main__":
    setup_github_repo()
