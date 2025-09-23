#!/usr/bin/env python3
"""
Complete Auto-Push Setup Script
This script sets up all the necessary components for automatic GitHub pushing.
"""

import subprocess
import sys
import os
import stat

def run_command(command, description):
    """Run a shell command and return the result."""
    try:
        print(f"🔄 {description}...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"❌ {description} failed")
            print(f"   Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ Error running command: {e}")
        return False

def setup_git_hooks():
    """Set up Git hooks for automatic pushing."""
    print("🔧 Setting up Git hooks...")
    
    hooks_dir = ".git/hooks"
    if not os.path.exists(hooks_dir):
        print("❌ Git hooks directory not found. Make sure you're in a Git repository.")
        return False
    
    # Make post-commit hook executable
    post_commit_path = os.path.join(hooks_dir, "post-commit")
    if os.path.exists(post_commit_path):
        os.chmod(post_commit_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
        print("✅ Post-commit hook is ready")
    else:
        print("⚠️  Post-commit hook not found")
    
    return True

def create_github_workflow():
    """Create GitHub Actions workflow for automatic operations."""
    print("🔧 Setting up GitHub Actions workflow...")
    
    workflow_dir = ".github/workflows"
    os.makedirs(workflow_dir, exist_ok=True)
    
    workflow_content = """name: Auto Sync

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  sync:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    
    - name: Run tests (if any)
      run: |
        if [ -f test_*.py ]; then python -m pytest; fi
    
    - name: Auto-commit and push
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add .
        git diff --staged --quiet || git commit -m "Auto-commit: $(date)"
        git push
"""
    
    workflow_file = os.path.join(workflow_dir, "auto-sync.yml")
    with open(workflow_file, 'w') as f:
        f.write(workflow_content)
    
    print("✅ GitHub Actions workflow created")
    return True

def main():
    """Main setup function."""
    print("🚀 Complete Auto-Push Setup")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("❌ Not in a Git repository. Please run 'git init' first.")
        return False
    
    # Set up Git hooks
    setup_git_hooks()
    
    # Create GitHub Actions workflow
    create_github_workflow()
    
    print("=" * 50)
    print("🎉 Auto-push setup completed!")
    print("\n📋 Available options for automatic pushing:")
    print("   1. 🐍 Python script: python auto_push.py")
    print("   2. 🪟 Windows batch: auto_push.bat")
    print("   3. 🔧 Git hooks: Automatic push after every commit")
    print("   4. ⚡ GitHub Actions: Automatic sync on push")
    print("\n📝 Next steps:")
    print("   1. Run 'python setup_github.py' to connect to GitHub")
    print("   2. Create a repository on GitHub if you haven't already")
    print("   3. Use any of the auto-push methods above")
    
    return True

if __name__ == "__main__":
    main()
