# Streamlit Credit Scoring Application

This project implements a credit scoring application using Streamlit. The application allows users to upload a CSV file containing customer data, preprocess the data, and score it using a pre-trained model.

## Project Structure

```
streamlit-scoring-app
├── app
│   ├── __init__.py
│   ├── main.py
│   └── utils
│       ├── __init__.py
│       └── preprocessing.py
├── model_final.pkl
├── requirements.txt
└── README.md
```

## Requirements

To run this application, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Running the Application

1. Ensure you have Python installed on your machine.
2. Navigate to the project directory.
3. Run the Streamlit application using the following command:

```
streamlit run app/main.py
```

4. Open your web browser and go to the URL provided in the terminal (usually `http://localhost:8501`).

## Usage

- Upload a CSV file containing the necessary customer data.
- The application will preprocess the data and use the trained model to generate credit scores.
- You can download the results as a CSV file after scoring.

## Model

The model used for scoring is saved in the `model_final.pkl` file. It is a pre-trained model that has been optimized for predicting credit risk.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.