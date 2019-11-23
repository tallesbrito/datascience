import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Leitura do conjunto de dados
data = pd.read_csv("dataset.csv")

feature_cols = ['panorama','temperatura','umidade','ventoso']
X = data[feature_cols] # Atributos de entrada
Y = data.jogar #Atributo alvo

# Divide o conjunto de dados para treinamento e teste
# 70% para treinamento e 30% para teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) 

# Cria uma árvore de decisão
clf = DecisionTreeClassifier(criterion="entropy", random_state=1)

# Treina o modelo
clf = clf.fit(X_train,Y_train)

# Prever respostas para o conjunto de teste
Y_pred = clf.predict(X_test)

print("Precisão:",metrics.accuracy_score(Y_test, Y_pred))


