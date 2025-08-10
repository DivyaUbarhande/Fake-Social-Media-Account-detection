#!/usr/bin/env python3
"""
Run script for Fake Social Media Account Detection Project
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if all required files exist"""
    required_files = [
        'data/synthetic_social_media_data.csv',
        'models/fake_account_detector.pkl'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        print("\n💡 Please run setup first: python setup.py")
        return False
    
    return True

def main():
    """Main run function"""
    print("🚀 Starting Fake Social Media Account Detection System")
    print("=" * 55)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("✅ All dependencies found")
    print("🌐 Starting Flask application...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 55)
    
    try:
        # Run the Flask application
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"\n❌ Error running application: {e}")

if __name__ == "__main__":
    main() 