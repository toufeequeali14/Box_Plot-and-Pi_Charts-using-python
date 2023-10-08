import matplotlib.pyplot as plt

nationalities = ["Pakistani", "Irani", "American", "Indian"]
students = [70, 60, 42, 62]

explode = [0, 0, 0.1, 0]           # this is for a cell to be some out from grpah.

pairs = zip(students, nationalities)    # little bit like key value pairs in dictionary.
#print(list(pairs))
pairs = sorted(list(pairs))
#print(list(pairs))
students, nationalities = zip(*pairs)        # converting to true list


plt.pie(students, labels=nationalities, autopct="%.2f%%", shadow=True, explode=explode, counterclock=False, startangle=90) 
plt.title("Student Nationality")
plt.show()

