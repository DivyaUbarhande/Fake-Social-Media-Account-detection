import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import xgboost as xgb
import joblib
import os

class FakeAccountDetector:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        
    def load_data(self, filepath):
        self.df = pd.read_csv(filepath)
        print(f"Data loaded: {len(self.df)} samples")
        return self.df
    
    def preprocess_data(self):
        feature_columns = [
            'account_age_days', 'followers', 'following', 'posts_count',
            'avg_likes', 'avg_comments', 'avg_shares', 'has_profile_pic',
            'has_bio', 'has_location', 'verified', 'followers_following_ratio', 
            'engagement_rate', 'suspicious_username', 'low_activity', 
            'high_follower_ratio', 'low_engagement'
        ]
        
        self.X = self.df[feature_columns].copy()
        self.y = self.df['is_fake'].copy()
        
        # Handle missing values
        self.X = self.X.fillna(self.X.median())
        
        # Split the data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42, stratify=self.y
        )
        
        # Scale the features
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print(f"Training set: {len(self.X_train)} samples")
        print(f"Test set: {len(self.X_test)} samples")
        
        return self.X_train_scaled, self.y_train, self.X_test_scaled, self.y_test
    
    def train_model(self):
        print("Training XGBoost model...")
        self.model = xgb.XGBClassifier(random_state=42, n_estimators=100)
        self.model.fit(self.X_train_scaled, self.y_train)
        
        # Evaluate model
        y_pred = self.model.predict(self.X_test_scaled)
        y_pred_proba = self.model.predict_proba(self.X_test_scaled)[:, 1]
        
        accuracy = (y_pred == self.y_test).mean()
        auc = roc_auc_score(self.y_test, y_pred_proba)
        
        print(f"Accuracy: {accuracy:.4f}")
        print(f"AUC: {auc:.4f}")
        print("\nClassification Report:")
        print(classification_report(self.y_test, y_pred, target_names=['Real', 'Fake']))
        
        return accuracy, auc
    
    def save_model(self, filepath='models/fake_account_detector.pkl'):
        os.makedirs('models', exist_ok=True)
        
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'feature_columns': list(self.X.columns)
        }
        
        joblib.dump(model_data, filepath)
        print(f"Model saved to {filepath}")

def main():
    os.makedirs('data', exist_ok=True)
    
    detector = FakeAccountDetector()
    detector.load_data('data/synthetic_social_media_data.csv')
    detector.preprocess_data()
    detector.train_model()
    detector.save_model()
    
    print("Model training completed!")

if __name__ == "__main__":
    main() 