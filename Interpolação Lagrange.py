import scipy
import matplotlib.pyplot as plt
import numpy as np
 
x = scipy.array([-1,-0.8,-0.6,-0.4,-0.2,0.0,0.2,0.4,0.6,0.8,1])
y = scipy.array([0.038,0.058,0.1,0.2,0.5,1,0.5,0.2,0.1,0.058,0.038])
result = scipy.poly1d([0.0])
 
for i in range(0,len(x)):
    temp_numerator = scipy.poly1d([1.0])
    denumerator = 1.0
    for j in range(0,len(x)):
        if i != j:
            temp_numerator *= scipy.poly1d([1.0,-x[j]])
            denumerator *= x[i]-x[j]
    result += (temp_numerator/denumerator) * y[i]
 
print("The result is: ")
print(result)
 
x_val = np.arange(min(x),max(x)+1, 0.1)
plt.xlabel('x'); plt.ylabel('p(x)')
plt.grid(True)
for i in range(0,len(x)):
    plt.plot([x[i]],[y[i]],'ro')
plt.plot(x_val, result(x_val))
plt.axis([min(x)-1, max(x)+ 1, min(y)-1, max(y)+1])
plt.show()
