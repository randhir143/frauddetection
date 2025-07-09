# importing library
import pandas as pd
import numpy as np
# importing datas
df = pd.read_csv(r"C:\Users\rshar\Downloads\onlinefraud.csv")
df.head()


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
preprocessor = ColumnTransformer(
    transformers = [
        ("num",StandardScaler(),numeric),
        ("cat",OneHotENcoder(drop = "first"),
         categorical)
    ],
    remainder ="drop"
)
pipeline = Pipeline([
    ("prep",preprocessor),
    ("clt",LogisticRegression(class_weight="balance",max_iter=1000))])
pipeline.fit(x_train,y_train)
pipeline.score(x_test,y_test)