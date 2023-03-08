import matplotlib.pyplot as plt
import math
import numpy as np

# Define a domain from -100 to 100, and plot y=3x+4

xaxis = []
yaxis = []

for x in range(-100, 101):
    y = 3 * x + 4
    xaxis.append(x)
    yaxis.append(y)


xaxis2 = []
yaxis2 = []
for x in range(-100, 100):
    y = (2 * x ** 2) + (4 * x) - 5
    xaxis2.append(x)
    yaxis2.append(y)

xaxis3 = []
yaxis3 = []
for x in range(-1, 101):
    y = math.sqrt(2 * x + 3)
    xaxis3.append(x)
    yaxis3.append(y)

print(xaxis)
print(yaxis)

plt.plot(xaxis, yaxis, color="red")
plt.plot(xaxis2, yaxis2, color="purple")
plt.plot(xaxis3, yaxis3, color="blue")

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')

plt.title('Plot of y = 3x + 4 with a domain from -100 to 100')
plt.grid(True)

plt.show()