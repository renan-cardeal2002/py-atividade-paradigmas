
import pandas as pd
from ucimlrepo import fetch_ucirepo

# fetch dataset
adult = fetch_ucirepo(id=2)

# data (as pandas dataframes)
X = adult.data.features
y = adult.data.targets

df = pd.concat([X, y], axis=1)

df = df.drop('fnlwgt', axis=1)
df

df_semnulo = df.dropna()
df_semnulo

X_semnulo = df_semnulo.drop('income', axis=1)


cat = X_semnulo[['workclass', 'education', 'education-num', 'marital-status','occupation', 'relationship', 'race', 'sex','native-country']]
cat


num = X_semnulo[['age','capital-gain','capital-loss', 'hours-per-week']]
num


percentis = [.05,.10,.25,.50,.75,.80,.90,.95,.99]

num.quantile(percentis)



cat['id_pessoa'] = range(len(cat))


cat.loc[cat['native-country'] != 'United-States', "native-country"] = "0"
cat.loc[cat['native-country'] == 'United-States', "native-country"] = "1"