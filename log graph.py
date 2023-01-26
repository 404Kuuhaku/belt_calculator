import matplotlib.pyplot as plt

# x-axis data (Design Power in HP)
x = [1,2,3,5,10,20,30,50,100,200,500,1000]

# y-axis data (small pulley speed in rpm)
y = [100,200,300,400,500,700,950,1450,2000,2850,4000,5000,7000,10000]

# Create a logarithmic scale for the x-axis
plt.xscale('log')

# Plot the data on the graph
plt.plot(x, y)

# Add labels and a title for the graph
plt.xlabel('Design Power (HP)')
plt.ylabel('small pulley speed (rpm)')
plt.title('Log graph of Design Power vs small pulley speed')

# Display the graph
plt.show()