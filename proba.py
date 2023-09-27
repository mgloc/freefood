import matplotlib.pyplot as plt

# Step 1: Read the Data
with open("prizes.txt", "r") as file:
    data = file.read().splitlines()

# Step 2: Count the Frequency
prize_frequency = {}
for prize in data:
    if prize in prize_frequency:
        prize_frequency[prize] += 1
    else:
        prize_frequency[prize] = 1

# Step 3: Sort the Prizes by Frequency (in descending order)
sorted_prizes = dict(sorted(prize_frequency.items(), key=lambda item: item[1], reverse=True))

# Step 4: Create the Chart
plt.figure(figsize=(10, 6))

# Assuming you want a bar chart
plt.bar(sorted_prizes.keys(), sorted_prizes.values())

plt.xlabel("Prizes")
plt.ylabel("Frequency")
plt.title("Frequency of Prizes")
plt.xticks(rotation=45)

# Adjust layout to prevent x-axis labels from overlapping
plt.tight_layout()

# Save the chart as an image or display it
plt.savefig("prize_frequency_chart.png")  # Save as an image
# plt.show()  # Display the chart in a window (comment out if saving as image)
