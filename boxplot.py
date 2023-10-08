import matplotlib.pyplot as plt

nationalities = ["Pakistani", "Irani", "American", "Indian"]
students = [70, 60, 42, 62]


# Create a boxplot from the 'students' data
plt.boxplot(students)

# Customize the plot
# plt.title("Boxplot of Students by Nationality")
# plt.ylabel("Number of Students")

# Show the boxplot
plt.show()
