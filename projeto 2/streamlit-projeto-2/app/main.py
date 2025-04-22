import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Previsão de Renda",
    page_icon=":bar_chart:",
    layout="centered", 
)

# carrega o dataset
df = pd.read_csv('D:/DOCUMENTOS/projeto 2/projeto 2/input/previsao_de_renda.csv')

# filtros sidebar
st.sidebar.header("Filtros")

# Remove as colunas 'id_cliente' e 'Unnamed: 0' dos filtros, se existirem
cols_to_filter = [col for col in df.columns if col not in ['id_cliente', 'Unnamed: 0', 'unamed', 'Unnamed']]
filtered_df = df.copy()
for col in cols_to_filter:
    unique_values = df[col].unique()
    # 'data_ref'use slider
    if col == 'data_ref':
        # converta datetime
        df[col] = pd.to_datetime(df[col])
        min_date = df[col].min().to_pydatetime()
        max_date = df[col].max().to_pydatetime()
        selected = st.sidebar.slider(
            f"{col}", min_value=min_date, max_value=max_date, value=(min_date, max_date), format="YYYY-MM-DD"
        )
        filtered_df = filtered_df[
            (pd.to_datetime(filtered_df[col]) >= selected[0]) & (pd.to_datetime(filtered_df[col]) <= selected[1])
        ]
    # 'posse_de_veiculo' e 'posse_de_imovel' multiselect
    elif col in ['posse_de_veiculo', 'posse_de_imovel']:
        options = ['Todos'] + sorted(list(unique_values))
        selected = st.sidebar.multiselect(f"{col}", options, default=['Todos'])
        if 'Todos' not in selected:
            filtered_df = filtered_df[filtered_df[col].isin(selected)]
    elif df[col].dtype == 'object' or df[col].dtype.name == 'category':
        options = ['Todos'] + sorted(list(unique_values))
        selected = st.sidebar.multiselect(f"{col}", options, default=['Todos'])
        if 'Todos' not in selected:
            filtered_df = filtered_df[filtered_df[col].isin(selected)]
    else:
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        selected = st.sidebar.slider(f"{col}", min_val, max_val, (min_val, max_val))
        if selected != (min_val, max_val):
            filtered_df = filtered_df[(filtered_df[col] >= selected[0]) & (filtered_df[col] <= selected[1])]

df = filtered_df
# titulo
st.title("Previsão de Renda")

# mostra dataset
st.subheader("Conjunto de Dados")
st.write(df.head())

# analise univariada
st.subheader("Análise Univariada")
st.write("Distribuição das variáveis numéricas:")
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    if col != 'Unnamed: 0':
        fig, ax = plt.subplots()
        sns.histplot(df[col], bins=30, kde=True, ax=ax)
        ax.set_title(f'Distribuição de {col}')
        st.pyplot(fig)

# analise bivariada
st.subheader("Análise Bivariada")
st.write("Relação entre Sexo e Renda")
fig, ax = plt.subplots()
sns.boxplot(x='sexo', y='renda', data=df, ax=ax)
ax.set_title('Renda por Sexo')
st.pyplot(fig)

st.write("Relação entre Tipo de Renda e Renda")
fig, ax = plt.subplots()
sns.boxplot(x='tipo_renda', y='renda', data=df, ax=ax)
ax.set_title('Renda por Tipo de Renda')
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("Relação entre Escolaridade e Renda")
fig, ax = plt.subplots()
sns.boxplot(x='educacao', y='renda', data=df, ax=ax)
ax.set_title('Renda por Escolaridade')
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("Relação entre Idade e Renda")
fig, ax = plt.subplots()
sns.scatterplot(x='idade', y='renda', data=df, ax=ax, alpha=0.3)
ax.set_title('Renda vs Idade')
st.pyplot(fig)

# correlação heatmap
st.subheader("Matriz de Correlação")
fig, ax = plt.subplots(figsize=(12, 8))  # Aumenta o tamanho da figura
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Blues', ax=ax, fmt=".2f")
ax.set_title('Matriz de Correlação')
st.pyplot(fig)

# conclusao
st.subheader("Conclusão")
st.write("Este aplicativo fornece uma análise exploratória dos dados de previsão de renda, permitindo visualizar as relações entre diferentes variáveis e a renda dos clientes.")