import numpy as np
import math

day=365
x = np.linspace(0, 10000, day)
drandom=np.random.randint(0,day,1)
y = x[drandom]
print("Guadagno effettivo del giorno: ",drandom," ",y)

# weights
a = np.random.randn()
b = np.random.randint(1)
c = np.random.randn()


learning_rate = 1e-6
for t in range(200000):
    y_pred = a
    drandom_pred = b
    domani_pred = c
    # Compute and print loss
    loss = (y_pred - y).sum()
    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred =50*(y_pred - y)
    grad_a = sum(grad_y_pred)
    grad_drandom_pred =50*(drandom_pred - drandom)
    grad_b = grad_drandom_pred.sum()
    grad_domani_pred=50*(y_pred -y)
    grad_c = grad_domani_pred.sum()
    # Update weights using gradient descent
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c


print('Guadagno stimato: Giorno: ',b," ",a, )
