def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Fill missing values in 'tempo_emprego' with the median
    df['tempo_emprego'].fillna(df['tempo_emprego'].median(), inplace=True)
    
    # Remove unnecessary columns
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)
    
    # Convert 'data_ref' to datetime
    df['data_ref'] = pd.to_datetime(df['data_ref'])
    
    return df

def plot_boxplot(df, x, y, title):
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x, y=y, data=df)
    plt.title(title)
    plt.show()

def plot_scatter(df, x, y, title):
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, data=df, alpha=0.3)
    plt.title(title)
    plt.show()

def plot_correlation_matrix(df):
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Blues')
    plt.title('Matriz de Correlação')
    plt.show()