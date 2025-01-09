import matplotlib.pyplot as plt

# The data you provided for 'train/box_loss'
train_box_loss = [
    3.76615, 2.83133, 2.58141, 2.59146, 2.56245, 2.51853, 2.59089, 2.54884, 
    2.54071, 2.607, 2.57903, 2.48678, 2.46909, 2.46686, 2.54404, 2.46264, 
    2.47033, 2.4509, 2.4419, 2.45532, 2.42704, 2.38443, 2.37448, 2.32485, 
    2.31284, 2.36468, 2.33713, 2.33775, 2.32793, 2.41331, 2.37414, 2.3834, 
    2.30846, 2.42293, 2.29753, 2.39614, 2.24649, 2.25629, 2.24671, 2.24283, 
    2.24512, 2.27412, 2.29157, 2.3012, 2.28767, 2.21371, 2.17745, 2.30682, 
    2.25661, 2.2118, 2.20889, 2.21322, 2.26503, 2.19366, 2.17374, 2.17823, 
    2.17325, 2.2228, 2.14636, 2.06277, 2.14761, 2.09566, 2.15687, 2.07997, 
    2.14053, 2.16542, 2.13874, 2.14067, 2.18386, 2.20559, 2.16767, 2.17663, 
    2.11758, 2.14354, 2.12419, 2.09084, 2.14356, 2.13859, 2.07572, 2.03135, 
    2.06145, 2.07328, 2.07629, 1.99868, 2.09716, 2.04823, 2.05306, 2.01489, 
    2.06014, 2.04515, 2.01543, 2.03419, 2.03323, 1.97598, 1.99785, 2.07544, 
    1.9293, 1.99594, 1.96796, 1.95862, 1.94301, 1.91637, 1.93762, 1.94759, 
    1.95826, 2.01957, 1.92776, 1.91481, 1.87909
]

# Generate corresponding x-axis values (1 to 109)
epochs = list(range(1, 110))

# Create the plot
plt.plot(epochs, train_box_loss, label='train/box_loss', marker='o')

# Set the x and y axis limits
plt.xlim(1, 109)
plt.ylim(1.6, 4)

# Set custom ticks
plt.xticks(range(0, 110, 25))  # x-axis from 1 to 109 with a step of 25
plt.yticks([i * 0.2 for i in range(8, 21)])  # y-axis from 1.6 to 4 with step 0.2

# Adding labels and title
plt.xlabel('Epoch')
plt.ylabel('train/box_loss')
plt.title('Train/Box Loss vs Epoch')

# Display the legend
plt.legend()

# Show the plot
plt.show()

