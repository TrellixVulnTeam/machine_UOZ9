import numpy as np
import pandas as pa
import matplotlib.pyplot as plt
from  sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import  sklearn.metrics as me
def readFile():
    dataset=pa.read_csv('Social_Network_Ads.csv')
    x=dataset.iloc[:,[2,3]].values
    y=dataset.iloc[:,4].values
    trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.2,random_state=0)
    scaler=StandardScaler()
    #这连个的区别
    trainx=scaler.fit_transform(trainx)
    testx=scaler.transform(testx)
    print(trainx,testx)
    classify=SVC(kernel='rbf',random_state=0)
    classify.fit(trainx,trainy)
    predity=classify.predict(testx)
    re=me.classification_report(testy,predity)
    print(re)
    #可视化
    from matplotlib.colors import ListedColormap
    X_set, y_set = trainx, trainy
    X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                         np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
    plt.contourf(X1, X2, classify.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha=0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                    c=ListedColormap(('red', 'green'))(i), label=j)
    plt.title('Decision Tree Classification (Training set)')
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()
    X_set, y_set = trainx, trainy
    X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                         np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
    plt.contourf(X1, X2, classify.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha=0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                    c=ListedColormap(('red', 'green'))(i), label=j)
    plt.title('Decision Tree Classification (Test set)')
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()
if __name__=='__main__':
    readFile()