import streamlit as st
import pandas as pd
import joblib 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Função para criar o pipeline de pré-processamento
def build_preprocessing_pipeline():
    quant_cols = ['qtd_filhos', 'idade', 'tempo_emprego', 'qt_pessoas_residencia', 'renda']
    cat_cols = ['posse_de_veiculo']

    quant_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    cat_pipeline = Pipeline([
        ('onehot', OneHotEncoder(drop='first', sparse_output=False))
    ])

    preprocessamento = ColumnTransformer([
        ('quant', quant_pipeline, quant_cols),
        ('cat', cat_pipeline, cat_cols)
    ])

    return preprocessamento

def main():
    st.title("Carregador de CSV, Pré-processamento e Scoring")

    uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Primeiras linhas do arquivo carregado:")
        st.dataframe(df.head())

        # Checa se as colunas necessárias existem
        colunas = ['qtd_filhos', 'idade', 'tempo_emprego', 'qt_pessoas_residencia', 'renda', 'posse_de_veiculo']
        missing = [col for col in colunas if col not in df.columns]
        if missing:
            st.error(f"Colunas faltando no arquivo: {missing}")
            return

        # Pré-processamento
        pipeline = build_preprocessing_pipeline()
        X_proc = pipeline.fit_transform(df)

        st.write("Dados pré-processados (primeiras linhas):")
        st.dataframe(pd.DataFrame(X_proc).head())

        # Carregar modelo treinado
        try:
            model = joblib.load('./model_final.pkl')
        except Exception as e:
            st.error(f"Erro ao carregar o modelo: {e}")
            return

        # Fazer predições
        preds = model.predict(X_proc)
        st.write("Predições do modelo (primeiras linhas):")
        st.dataframe(pd.DataFrame(preds, columns=['score']).head())
        
        # Mostrar a quantidade de cada categoria das predições
        st.write("Quantidade de cada categoria prevista:")
        st.write(pd.Series(preds).value_counts().rename_axis('score').reset_index(name='quantidade'))
if __name__ == "__main__":
    main()
