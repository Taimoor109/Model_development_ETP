import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load your SIEM cybersecurity dataset (replace 'your_dataset.csv' with your actual dataset file)
df = pd.read_csv('your_dataset.csv')

# Assume the dataset has a 'timestamp' column, convert it to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract features from timestamp
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

# Feature engineering for categorical columns
label_encoder = LabelEncoder()
df['source_ip_encoded'] = label_encoder.fit_transform(df['source_ip'])
df['destination_ip_encoded'] = label_encoder.fit_transform(df['destination_ip'])

# Feature engineering for text data using TF-IDF and dimensionality reduction
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
text_features = tfidf_vectorizer.fit_transform(df['log_message'])

# Perform dimensionality reduction on text features
svd = TruncatedSVD(n_components=50, random_state=42)
text_features_svd = svd.fit_transform(text_features)

# Combine text features with the main dataset
df = pd.concat([df, pd.DataFrame(text_features_svd, columns=[f'text_feature_{i}' for i in range(50)])], axis=1)

# Impute missing values
imputer = SimpleImputer(strategy='mean')
df['missing_values_imputed'] = imputer.fit_transform(df[['column_with_missing_values']])

# Standardize numerical features
numerical_features = ['feature1', 'feature2', 'text_feature_0', 'text_feature_1', ...]
scaler = StandardScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])

# Drop unnecessary columns
columns_to_drop = ['timestamp', 'log_message', 'source_ip', 'destination_ip', 'column_with_missing_values']
df = df.drop(columns=columns_to_drop)

# Now 'df' contains the engineered features that can be used for training your machine learning model.
