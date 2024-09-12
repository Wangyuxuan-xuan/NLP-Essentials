from sklearn.model_selection import train_test_split

xFile = open("/training/news-commentary-v12.cs-en.en")
yFIle = open("/training/news-commentary-v12.de-en.de")

X = xFile.readlines()
y = yFIle.readlines()

print(X)
train_test_split(X, y,test_size=0.25, random_state=0)



