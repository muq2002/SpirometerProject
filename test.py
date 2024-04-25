import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
csv_file_path = "C:/Users/mktad/OneDrive/Desktop/test.csv"
df = pd.read_csv(csv_file_path)

# Step 2: Explore the data briefly (optional)
print(df.head())  # Print the first few rows of the DataFrame
print(df.info())  # Print info about the DataFrame

# Step 3: Plot data using matplotlib
# Customize the plot according to your requirements
# For example, plotting 'time' and 'pressure' columns

x = df['time']
y = df['pressure']

# Handle missing values (optional)
# df.dropna(subset=['time', 'pressure'], inplace=True)

plt.figure(figsize=(10, 6))  # Create a figure with a specific size

# Customize plot style (line style, color, marker style)
plt.plot(x, y, label='Pressure over Time', linestyle='-', color='blue', marker='o')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Plot of Time vs Pressure')
plt.legend()  # Add a legend

# Optionally, save the plot as an image
# plt.savefig('plot.png')

# Show the plot
plt.show()
