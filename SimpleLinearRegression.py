from sklearn.linear_model import LinearRegression
reg= LinearRegression()
x= [[1], [2], [3], [4], [5], [6]]
y = [6, 5, 4, 3, 2, 1]
reg.fit(x,y)
print(reg.predict[[5]])