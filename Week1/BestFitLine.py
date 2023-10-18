import csv
import numpy as np
import matplotlib.pyplot as plt

csv_list=[]

with open("Week1_1_LinFit.csv", mode="r") as file:
    filename = csv.reader(file)

    for i in filename:
        csv_list.append(i)

#list1[0] give the axis names
# Zeros give axes values

print(csv_list[0])
print(csv_list[1])

x_list=[]
y_list=[]

yerr1=[]
yerr2=[]

count=1
for i in csv_list[1:]:
    x_list.append(float(i[0]))
    y_list.append(float(i[1]))
    yerr1.append(float(i[2]))
    yerr2.append(float(i[3]))

# Making the plot
x=np.array(x_list)
y=np.array(y_list)

m, c = np.polyfit(x,y,1)

plt.scatter(x,y)
plt.errorbar(x, y, yerr=yerr2, fmt="o")
plt.plot(x, m*x+c)

# Adds equation to the plot
plt.text(1, 350, 'y = ' + '{:.2f}'.format(c) + ' + {:.2f}'.format(m) + 'x', size=14)

plt.show()