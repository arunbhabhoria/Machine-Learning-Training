# Machine-Learning-Training

Q.1 - Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.
sol:- 
import numpy as np
from array import *
a=np.random.rand(10,1) # random array of shape(10,1)
m=np.mean(a)
print("Mean:",m)

Output:- Mean: 0.463464465994

Q.2 - Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements.
SOl:-
import numpy as np
from array import *
a=np.random.rand(20,1) # random array of shape(20,1)
v=np.var(a)
s=np.std(a)
print("Variance:", v)
print("Standard deviation:",s)

Output:- Variance: 0.0699995456471
         Standard deviation: 0.264574272459


 Q.3 - Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix 
  multiplication of A and B.The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.
  
  Sol:-
