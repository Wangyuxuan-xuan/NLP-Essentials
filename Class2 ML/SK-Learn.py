from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_wine(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state=0)

clf = RandomForestClassifier(random_state=0)
clf.fit(X_train, y_train)

score = accuracy_score(clf.predict(X_test), y_test)
print(score)

