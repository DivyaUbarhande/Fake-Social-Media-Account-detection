import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import string

def generate_synthetic_data(n_samples=10000):
    """
    Generate synthetic social media account data for fake account detection
    """
    np.random.seed(42)
    random.seed(42)
    
    data = []
    
    for i in range(n_samples):
        # Determine if account is fake (30% fake accounts)
        is_fake = np.random.choice([0, 1], p=[0.7, 0.3])
        
        # Account creation date
        if is_fake:
            # Fake accounts are usually newer
            days_ago = np.random.randint(1, 365)
        else:
            # Real accounts have more varied creation dates
            days_ago = np.random.randint(1, 2000)
        
        created_date = datetime.now() - timedelta(days=days_ago)
        
        # Username characteristics
        if is_fake:
            # Fake usernames often have patterns
            username_patterns = [
                f"user{np.random.randint(1000, 9999)}",
                f"fake{np.random.randint(100, 999)}",
                f"bot{np.random.randint(1000, 9999)}",
                ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
                f"spam{np.random.randint(100, 999)}"
            ]
            username = random.choice(username_patterns)
        else:
            # Real usernames are more varied
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=np.random.randint(5, 15)))
        
        # Profile features
        if is_fake:
            # Fake accounts often have incomplete profiles
            has_profile_pic = np.random.choice([0, 1], p=[0.4, 0.6])
            has_bio = np.random.choice([0, 1], p=[0.6, 0.4])
            has_location = np.random.choice([0, 1], p=[0.7, 0.3])
            verified = 0
        else:
            # Real accounts have more complete profiles
            has_profile_pic = np.random.choice([0, 1], p=[0.1, 0.9])
            has_bio = np.random.choice([0, 1], p=[0.2, 0.8])
            has_location = np.random.choice([0, 1], p=[0.3, 0.7])
            verified = np.random.choice([0, 1], p=[0.95, 0.05])
        
        # Activity metrics
        if is_fake:
            # Fake accounts often have suspicious activity patterns
            followers = np.random.poisson(50) if np.random.random() < 0.7 else np.random.poisson(1000)
            following = np.random.poisson(200) if np.random.random() < 0.6 else np.random.poisson(50)
            posts_count = np.random.poisson(5) if np.random.random() < 0.8 else np.random.poisson(100)
            
            # Fake accounts often have high follower/following ratios or very low activity
            if np.random.random() < 0.3:
                followers = np.random.poisson(1000)
                following = np.random.poisson(10)
        else:
            # Real accounts have more natural activity patterns
            followers = np.random.poisson(150)
            following = np.random.poisson(200)
            posts_count = np.random.poisson(50)
        
        # Engagement metrics
        if is_fake:
            # Fake accounts often have low engagement
            avg_likes = max(0, np.random.normal(2, 5))
            avg_comments = max(0, np.random.normal(0.5, 2))
            avg_shares = max(0, np.random.normal(0.2, 1))
        else:
            # Real accounts have higher engagement
            avg_likes = max(0, np.random.normal(20, 15))
            avg_comments = max(0, np.random.normal(5, 8))
            avg_shares = max(0, np.random.normal(2, 5))
        
        # Account age in days
        account_age_days = (datetime.now() - created_date).days
        
        # Suspicious patterns
        if is_fake:
            # Fake accounts often have suspicious patterns
            followers_following_ratio = followers / max(following, 1)
            engagement_rate = (avg_likes + avg_comments + avg_shares) / max(followers, 1)
            
            # Add some suspicious patterns
            if np.random.random() < 0.4:
                # Very high follower/following ratio
                followers = following * np.random.randint(10, 50)
            elif np.random.random() < 0.3:
                # Very low engagement
                avg_likes = np.random.randint(0, 3)
                avg_comments = 0
                avg_shares = 0
        else:
            followers_following_ratio = followers / max(following, 1)
            engagement_rate = (avg_likes + avg_comments + avg_shares) / max(followers, 1)
        
        # Additional features
        has_website = np.random.choice([0, 1], p=[0.8, 0.2]) if is_fake else np.random.choice([0, 1], p=[0.6, 0.4])
        has_pinned_posts = np.random.choice([0, 1], p=[0.9, 0.1]) if is_fake else np.random.choice([0, 1], p=[0.7, 0.3])
        
        # Suspicious indicators
        suspicious_username = 1 if any(pattern in username.lower() for pattern in ['bot', 'fake', 'spam', 'user']) else 0
        low_activity = 1 if posts_count < 5 and account_age_days > 30 else 0
        high_follower_ratio = 1 if followers_following_ratio > 10 else 0
        low_engagement = 1 if engagement_rate < 0.01 and followers > 100 else 0
        
        data.append({
            'username': username,
            'is_fake': is_fake,
            'account_age_days': account_age_days,
            'followers': followers,
            'following': following,
            'posts_count': posts_count,
            'avg_likes': avg_likes,
            'avg_comments': avg_comments,
            'avg_shares': avg_shares,
            'has_profile_pic': has_profile_pic,
            'has_bio': has_bio,
            'has_location': has_location,
            'verified': verified,
            'has_website': has_website,
            'has_pinned_posts': has_pinned_posts,
            'followers_following_ratio': followers_following_ratio,
            'engagement_rate': engagement_rate,
            'suspicious_username': suspicious_username,
            'low_activity': low_activity,
            'high_follower_ratio': high_follower_ratio,
            'low_engagement': low_engagement,
            'created_date': created_date.strftime('%Y-%m-%d')
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Generate synthetic data
    df = generate_synthetic_data(10000)
    
    # Save to CSV
    df.to_csv('data/synthetic_social_media_data.csv', index=False)
    print(f"Generated {len(df)} synthetic social media accounts")
    print(f"Fake accounts: {df['is_fake'].sum()} ({df['is_fake'].mean()*100:.1f}%)")
    print(f"Real accounts: {(df['is_fake'] == 0).sum()} ({(df['is_fake'] == 0).mean()*100:.1f}%)") 