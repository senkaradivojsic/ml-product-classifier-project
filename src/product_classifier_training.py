import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# load dataset from GitHub
url = "https://raw.githubusercontent.com/senkaradivojsic/ml-product-reviews-project/main/data/products.csv"
df = pd.read_csv(url)


# Standardize columns names
df.columns = (df.columns.str.strip().str.lower().str.replace('_', ' ').str.replace(r'\s+', '_', regex=True).str.strip('_'))

# Standardize the 'category_label' column
df['category_label'] = df['category_label'].str.strip().str.lower()

df['category_label'] = df['category_label'].replace({
    'fridges': 'fridge freezers',
    'freezers': 'fridge freezers',
    'fridge': 'fridge freezers',
    'cpu': 'cpus',
    'mobile phone': 'mobile phones'
})

# Deleting unnecessary columns
df = df.drop(columns=['product_id', 'merchant_id', 'product_code', 'merchant_rating', 'listing_date', 'number_of_views'])

# Deleting missing values 
df = df.dropna(subset=['category_label', 'product_title'])

# Separate features (X) and labels (y)
X = df["product_title"]
y = df["category_label"]

# Split the data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# Train different classification models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Linear SVC": LinearSVC(max_iter=1000)
}
 
trained_models = {}
for name, classifier in models.items():
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', classifier)
    ])
    pipeline.fit(X_train, y_train)
    trained_models[name] = pipeline 


# Evaluate all models
for name, model in trained_models.items():

    prediction = model.predict(X_test)

    print(f"\n{name}")
    print("Accuracy:", accuracy_score(y_test, prediction))
    print("\nClassification Report:\n",
          classification_report(y_test, prediction))

    print("Confusion Matrix:\n",
          confusion_matrix(y_test, prediction))


# Train the final model on the entire dataset
final_model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', LinearSVC(max_iter=1000))
])

final_model.fit(X, y)

 
# Save the trained model to a file
joblib.dump(final_model, "product_classifier_final_model.pkl")
print(" Model trained and saved as 'product_classifier_final_model.pkl'")


