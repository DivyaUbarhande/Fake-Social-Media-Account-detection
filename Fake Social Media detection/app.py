from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Global variables
model_data = None
loaded_model = None
loaded_scaler = None
feature_columns = None

def load_model():
    """Load the trained model and preprocessing objects"""
    global model_data, loaded_model, loaded_scaler, feature_columns
    
    try:
        model_data = joblib.load('models/fake_account_detector.pkl')
        loaded_model = model_data['model']
        loaded_scaler = model_data['scaler']
        feature_columns = model_data['feature_columns']
        print("Model loaded successfully!")
        return True
    except Exception as e:
        print(f"Error loading model: {e}")
        return False

def predict_account(input_data):
    """Make prediction for a single account"""
    try:
        # Create feature vector
        features = []
        for col in feature_columns:
            if col in input_data:
                features.append(input_data[col])
            else:
                features.append(0)  # Default value for missing features
        
        # Convert to numpy array and reshape
        features = np.array(features).reshape(1, -1)
        
        # Scale features
        features_scaled = loaded_scaler.transform(features)
        
        # Make prediction
        prediction = loaded_model.predict(features_scaled)[0]
        probability = loaded_model.predict_proba(features_scaled)[0][1]  # Probability of being fake
        
        return {
            'prediction': int(prediction),
            'probability': float(probability),
            'is_fake': bool(prediction),
            'confidence': float(max(probability, 1 - probability))
        }
    except Exception as e:
        print(f"Error making prediction: {e}")
        return None

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    """Account detection page"""
    if request.method == 'POST':
        try:
            # Get form data
            data = {
                'account_age_days': int(request.form.get('account_age_days', 0)),
                'followers': int(request.form.get('followers', 0)),
                'following': int(request.form.get('following', 0)),
                'posts_count': int(request.form.get('posts_count', 0)),
                'avg_likes': float(request.form.get('avg_likes', 0)),
                'avg_comments': float(request.form.get('avg_comments', 0)),
                'avg_shares': float(request.form.get('avg_shares', 0)),
                'has_profile_pic': int(request.form.get('has_profile_pic', 0)),
                'has_bio': int(request.form.get('has_bio', 0)),
                'has_location': int(request.form.get('has_location', 0)),
                'verified': int(request.form.get('verified', 0)),
                'followers_following_ratio': float(request.form.get('followers_following_ratio', 0)),
                'engagement_rate': float(request.form.get('engagement_rate', 0)),
                'suspicious_username': int(request.form.get('suspicious_username', 0)),
                'low_activity': int(request.form.get('low_activity', 0)),
                'high_follower_ratio': int(request.form.get('high_follower_ratio', 0)),
                'low_engagement': int(request.form.get('low_engagement', 0))
            }
            
            # Calculate derived features
            if data['following'] > 0:
                data['followers_following_ratio'] = data['followers'] / data['following']
            
            if data['followers'] > 0:
                data['engagement_rate'] = (data['avg_likes'] + data['avg_comments'] + data['avg_shares']) / data['followers']
            
            # Make prediction
            result = predict_account(data)
            
            if result:
                return render_template('detect.html', result=result, form_data=data)
            else:
                return render_template('detect.html', error="Error making prediction")
                
        except Exception as e:
            return render_template('detect.html', error=f"Error: {str(e)}")
    
    return render_template('detect.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Make prediction
        result = predict_account(data)
        
        if result:
            return jsonify(result)
        else:
            return jsonify({'error': 'Prediction failed'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/dashboard')
def dashboard():
    """Analytics dashboard"""
    try:
        # Load sample data for visualization
        df = pd.read_csv('data/synthetic_social_media_data.csv')
        
        # Calculate statistics
        total_accounts = len(df)
        fake_accounts = df['is_fake'].sum()
        real_accounts = total_accounts - fake_accounts
        fake_percentage = (fake_accounts / total_accounts) * 100
        
        # Average metrics
        avg_followers = df['followers'].mean()
        avg_following = df['following'].mean()
        avg_posts = df['posts_count'].mean()
        avg_engagement = df['engagement_rate'].mean()
        
        stats = {
            'total_accounts': total_accounts,
            'fake_accounts': fake_accounts,
            'real_accounts': real_accounts,
            'fake_percentage': round(fake_percentage, 2),
            'avg_followers': round(avg_followers, 2),
            'avg_following': round(avg_following, 2),
            'avg_posts': round(avg_posts, 2),
            'avg_engagement': round(avg_engagement, 4)
        }
        
        return render_template('dashboard.html', stats=stats)
        
    except Exception as e:
        return render_template('dashboard.html', error=str(e))

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    # Load model on startup
    if load_model():
        print("Starting Flask application...")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("Failed to load model. Please train the model first.") 