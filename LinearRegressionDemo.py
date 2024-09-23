#This model will be used to predect
#we will do this by finding the line of best fit then predicting where that point would be on that line
#linear regression always predicts based on the y axis

import pandas as pd
import matplotlib.pyplot as plt

#calculates the total error or how far off we are
def loss_fuction(m,b, points):

    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].YearsExperience # sets x values
        y = points.iloc[i].Salary #set y values
        total_error += (y - (m*x+b))**2 #formula for error
    return total_error / float(len(points))


def gradient_descnet(cur_m, cur_b, points, L): #L is learning rate
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].YearsExperience # sets x values
        y = points.iloc[i].Salary #set y values

        m_gradient += (-2/n) * x * (y - cur_m * x + cur_b) #tells us the amount we need to move the line on m
        b_gradient += (-2/n) * (y - cur_m * x + cur_b) #tells us the amount we need to move the line on b

    m = cur_m - m_gradient * L #moves the m value on are line
    b = cur_b - b_gradient * L #moves the b value on are line

    return m,b

data = pd.read_csv('') #put your data set in here!!

m = 0
b = 0
learningRate = 0.0001
epochs = 1000 #itterations

for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m,b = gradient_descnet(m, b, data, learningRate)

print(m , b)

plt.scatter(data.YearsExperience, data.Salary, color = "black")
plt.plot(list(range(0, 11)), [m*x + b for x in range(0, 11)], color = "red")
plt.show()