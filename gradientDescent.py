import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

def gradientDescent(x,y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.08
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)]) #M.S.E
        mderivative = -(2/n)*sum(x*(y - y_predicted))
        bderivative = -(2/n)*sum(y - y_predicted)

        m_curr = m_curr - learning_rate * mderivative
        b_curr = b_curr - learning_rate * bderivative

        print("{}. m: {:.3f} | b: {:.3f} | cost: {:.3f}".format(i,m_curr,b_curr,cost))
    
gradientDescent(x,y)