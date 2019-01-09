import numpy as np
x = np.array([1,2])
y = np.array([1,2,3])
p_xy = np.array([[0.1, 0.1, 0.25], [0.25, 0.1 , 0.2]])

mu_x = np.dot(np.sum(p_xy, axis=1).flatten(),x.T)
mu_y = np.dot(np.sum(p_xy, axis=0).flatten(),y.T) 
print(mu_x, mu_y)

covariance = 0
for i, _x in enumerate(x):
    for j, _y in enumerate(y):
        covariance += (_x - mu_x) * (_y - mu_y) * p_xy[i,j]
print(covariance)

marg_entr_x = -np.sum(-np.multiply(np.sum(p_xy, axis=1).flatten(), np.log(np.sum(p_xy, axis=1).flatten())))
marg_entr_y = -np.sum(-np.multiply(np.sum(p_xy, axis=0).flatten(), np.log(np.sum(p_xy, axis=0).flatten())))
print(marg_entr_x, marg_entr_y)