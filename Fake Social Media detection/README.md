# Fake Social Media Account Detection

An advanced machine learning system to detect fake social media accounts using Python and Flask. This project uses XGBoost algorithm to analyze various account features and identify suspicious patterns.

## 🚀 Features

- **AI-Powered Detection**: Advanced machine learning algorithms analyze multiple account features
- **Real-time Analysis**: Instant detection results with confidence scores
- **Comprehensive Analytics**: Detailed insights and statistics about detection patterns
- **Modern Web Interface**: Beautiful, responsive UI built with Bootstrap 5
- **API Endpoints**: RESTful API for integration with other applications

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **XGBoost** - Machine learning algorithm
- **Scikit-learn** - Data preprocessing and evaluation
- **Pandas & NumPy** - Data manipulation
- **Joblib** - Model serialization

### Frontend
- **HTML5 & CSS3**
- **Bootstrap 5** - Responsive design
- **JavaScript** - Interactive features
- **Chart.js** - Data visualization
- **Font Awesome** - Icons

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd fake-social-media-detection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Synthetic Data
```bash
python data_generator.py
```

### 4. Train the Model
```bash
python model_trainer.py
```

### 5. Run the Application
```bash
python app.py
```

### 6. Access the Application
Open your browser and navigate to: `http://localhost:5000`

## 📁 Project Structure

```
fake-social-media-detection/
├── app.py                 # Flask web application
├── data_generator.py      # Synthetic data generation
├── model_trainer.py       # ML model training
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── data/                 # Data directory
│   └── synthetic_social_media_data.csv
├── models/               # Trained models
│   └── fake_account_detector.pkl
└── templates/            # HTML templates
    ├── base.html
    ├── index.html
    ├── detect.html
    ├── dashboard.html
    └── about.html
```

## 🎯 How It Works

### 1. Data Generation
The system generates synthetic social media account data with realistic patterns:
- Account age, followers, following, posts count
- Engagement metrics (likes, comments, shares)
- Profile completeness indicators
- Suspicious behavior patterns

### 2. Feature Engineering
The model analyzes 17 key features:
- **Basic Metrics**: Account age, followers, following, posts
- **Engagement**: Average likes, comments, shares
- **Profile**: Has profile pic, bio, location, verification
- **Suspicious Indicators**: Username patterns, activity levels, ratios

### 3. Machine Learning
- **Algorithm**: XGBoost (Extreme Gradient Boosting)
- **Preprocessing**: Standard scaling and feature normalization
- **Evaluation**: Accuracy, AUC, classification reports

### 4. Web Interface
- **Home Page**: Overview and feature introduction
- **Detection Page**: Account analysis form
- **Dashboard**: Analytics and visualizations
- **About Page**: Technical details and methodology

## 🔧 API Usage

### Predict Account
```bash
POST /api/predict
Content-Type: application/json

{
    "account_age_days": 365,
    "followers": 1000,
    "following": 500,
    "posts_count": 50,
    "avg_likes": 25.5,
    "avg_comments": 5.2,
    "avg_shares": 2.1,
    "has_profile_pic": 1,
    "has_bio": 1,
    "has_location": 1,
    "verified": 0
}
```

### Response
```json
{
    "prediction": 0,
    "probability": 0.15,
    "is_fake": false,
    "confidence": 0.85
}
```

## 📊 Model Performance

The XGBoost model typically achieves:
- **Accuracy**: ~85-90%
- **AUC**: ~0.90-0.95
- **Precision**: ~85% for fake account detection
- **Recall**: ~80% for fake account detection

## 🎨 Features Analyzed

### Account Activity
- Account age in days
- Number of posts
- Posting frequency patterns

### Network Metrics
- Follower count
- Following count
- Follower/following ratio
- Network growth patterns

### Engagement Analysis
- Average likes per post
- Average comments per post
- Average shares per post
- Engagement rate calculation

### Profile Completeness
- Profile picture presence
- Bio information
- Location information
- Verification status

### Suspicious Indicators
- Username patterns (bot, fake, spam keywords)
- Low activity indicators
- High follower ratio flags
- Low engagement warnings

## 🔒 Security Considerations

- Input validation and sanitization
- Rate limiting for API endpoints
- Secure model storage
- Error handling and logging

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- XGBoost developers for the excellent ML library
- Flask team for the web framework
- Bootstrap team for the UI components
- Chart.js for data visualization

## 📞 Support

For questions or support, please open an issue in the repository.

---

**Note**: This is a demonstration project using synthetic data. For production use, ensure you have proper data sources and comply with relevant privacy and data protection regulations. 