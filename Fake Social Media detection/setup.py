#!/usr/bin/env python3
"""
Setup script for Fake Social Media Account Detection Project
"""

import os
import sys
import subprocess
import importlib.util

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Error installing packages")
        sys.exit(1)

def create_directories():
    """Create necessary directories"""
    directories = ['data', 'models', 'static']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Created directory: {directory}")

def generate_data():
    """Generate synthetic data"""
    print("📊 Generating synthetic data...")
    try:
        subprocess.check_call([sys.executable, "data_generator.py"])
        print("✅ Data generated successfully")
    except subprocess.CalledProcessError:
        print("❌ Error generating data")
        sys.exit(1)

def train_model():
    """Train the machine learning model"""
    print("🤖 Training machine learning model...")
    try:
        subprocess.check_call([sys.executable, "model_trainer.py"])
        print("✅ Model trained successfully")
    except subprocess.CalledProcessError:
        print("❌ Error training model")
        sys.exit(1)

def check_setup():
    """Check if setup is complete"""
    print("🔍 Checking setup...")
    
    # Check if data file exists
    if not os.path.exists('data/synthetic_social_media_data.csv'):
        print("❌ Data file not found")
        return False
    
    # Check if model file exists
    if not os.path.exists('models/fake_account_detector.pkl'):
        print("❌ Model file not found")
        return False
    
    print("✅ Setup is complete!")
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up Fake Social Media Account Detection Project")
    print("=" * 60)
    
    # Check Python version
    check_python_version()
    
    # Create directories
    create_directories()
    
    # Install requirements
    install_requirements()
    
    # Generate data
    generate_data()
    
    # Train model
    train_model()
    
    # Check setup
    if check_setup():
        print("\n🎉 Setup completed successfully!")
        print("\n📋 Next steps:")
        print("1. Run the application: python app.py")
        print("2. Open your browser and go to: http://localhost:5000")
        print("3. Start detecting fake accounts!")
    else:
        print("\n❌ Setup failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 