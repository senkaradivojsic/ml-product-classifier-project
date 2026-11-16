import joblib
import pandas as pd

# Load the saved model
model = joblib.load("model/product_classifier_final_model.pkl")

# Interactive testing
print("\nEnter a product title to predict its category.")
print("Type 'exit' to stop.\n")

while True:
    title = input("Enter product title: ")

    if title.strip().lower() == "exit":
        print("Exiting...")
        break

    input_data = pd.DataFrame({
        'product_title': [title],
        'word_count': [len(title.split())],
        'title_length': [len(title)]
    })

    prediction = model.predict(input_data)[0]

    print(f"Predicted category: {prediction}\n" + "-" * 40)
