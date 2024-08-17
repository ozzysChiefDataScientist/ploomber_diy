# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Add description here
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %%
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = ['get', 'petal-feature', 'sepal-feature']

# This is a placeholder, leave it as None
product = None

# %%
# your code here...
from pathlib import Path
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

raw = pd.read_csv(upstream['get']['data'])

sepal  = pd.read_csv(upstream['sepal-feature']['data'])
petal  = pd.read_csv(upstream['petal-feature']['data'])

df = raw.join(sepal).join(petal)


X = df.drop('target', axis='columns')

y = df.target

model = RandomForestClassifier()

model.fit(X,y)

y_pred = model.predict(X)

confusion_matrix(y, y_pred)

model_bytes = pickle.dumps(model)
Path(product['model']).write_bytes(model_bytes)