import os
import subprocess
from datetime import datetime

REPO_URL = "https://github.com/nikhil49023/My-Journey"

def sync_progress(message="Update learning progress"):
    """
    Syncs the local learning_lab state to GitHub.
    Ensures README and PATHWAY are updated.
    """
    try:
        # Check if .git exists, if not initialize
        if not os.path.exists(".git"):
            print("Initializing GitHub Sync...")
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "remote", "add", "origin", REPO_URL], check=True)
        
        # Add changes
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit with timestamped message
        full_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {message}"
        subprocess.run(["git", "commit", "-m", full_message], check=True)
        
        # Push to origin (assuming main branch)
        # Note: Using force for the initial 'clear' request if needed, but safer to just push.
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        
        print("✅ Progress synced to GitHub: Learn in Public active.")
    except Exception as e:
        print(f"❌ Sync failed: {e}")

if __name__ == "__main__":
    sync_progress()
