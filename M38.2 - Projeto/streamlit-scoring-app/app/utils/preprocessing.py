from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
import numpy as np

class OutlierClipper(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
        self.bounds = {}

    def fit(self, X, y=None):
        for col in self.columns:
            Q1 = X[col].quantile(0.25)
            Q3 = X[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            self.bounds[col] = (lower, upper)
        return self

    def transform(self, X):
        X_ = X.copy()
        for col in self.columns:
            lower, upper = self.bounds[col]
            X_[col] = X_[col].clip(lower, upper)
        return X_

def build_preprocessing_pipeline():
    quant_cols = ['qtd_filhos', 'idade', 'tempo_emprego', 'qt_pessoas_residencia', 'renda']
    cat_cols = ['posse_de_veiculo']

    quant_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('outlier', OutlierClipper(columns=quant_cols)),
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=5))
    ])

    cat_pipeline = Pipeline([
        ('onehot', OneHotEncoder(drop='first', sparse_output=False))
    ])

    preprocessamento = ColumnTransformer([
        ('quant', quant_pipeline, quant_cols),
        ('cat', cat_pipeline, cat_cols)
    ])

    return preprocessamento