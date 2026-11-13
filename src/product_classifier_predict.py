import joblib

# Load the saved model
model = joblib.load("product_classifier_final_model.pkl")

# Interactive testing
print("\nEnter a product title to predict its category.")
print("Type 'exit' to stop.\n")

while True:
    title = input("Enter product title: ")

    if title.strip().lower() == "exit":
        print("Exiting...")
        break

    prediction = model.predict([title])[0]

    print(f"Predicted category: {prediction}\n" + "-" * 40)
