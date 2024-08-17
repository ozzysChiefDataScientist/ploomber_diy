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
upstream = {'get': {'nb': 'products/get.ipynb',
                             'data': 'products/get.csv'}}
# This is a placeholder, leave it as None
product = None

# %%
# your code here...

import pandas as pd

df = pd.read_csv(upstream['get']['data'])

df['sepal-feature'] = df['sepal length (cm)']*df['sepal width (cm)']

df[['sepal-feature']].to_csv(product['data'], index=False)