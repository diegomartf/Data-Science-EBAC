# Streamlit Project for Income Prediction

This project is a Streamlit application designed to predict income based on customer characteristics. It utilizes a dataset containing various socio-economic features of clients to build a predictive model using machine learning techniques.

## Project Structure

```
streamlit-projeto-2
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── data
│       └── previsao_de_renda.csv
├── requirements.txt
├── README.md
└── .streamlit
    └── config.toml
```

## Installation

To run this project, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:

```
streamlit run app/main.py
```

This will start the Streamlit server and open the application in your default web browser.

## Features

- Data visualization of income predictions based on various socio-economic factors.
- Interactive components to explore the dataset and model predictions.
- Model evaluation metrics to assess the performance of the income prediction model.

## Dataset

The dataset used for this project is located in the `app/data/previsao_de_renda.csv` file. It contains 15,000 records with 15 variables related to customer demographics and income.

## Acknowledgments

- This project is based on the CRISP-DM methodology for data mining.
- Special thanks to the contributors and libraries used in this project.

Feel free to explore and modify the application as needed!