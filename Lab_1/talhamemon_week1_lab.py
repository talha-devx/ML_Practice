#A
#Q1
print("Q1")
a = 10
b = 20
a, b = b, a
print("After swapping:")
print("Value of a:", a)
print("Value of b:", b)

#Q2
print("\nQ2")
#_isPrime
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Is 17 a prime number?", isPrime(17))
print("Is 18 a prime number?", isPrime(18))

#Q3
print("\nQ3")
n = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

#Q4
print("\nQ4")
def remove_duplicates(lst):
    return list(set(lst))
my_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", my_list)
print("List after removing duplicates:", remove_duplicates(my_list))

#Q5
print("\nQ5")
def multiply(*args):
    result = 1
    for number in args:
        result *= number
    return result
print("Product of 2, 3, 4:", multiply(2, 3, 4))

#Q6
print("\nQ6")
text = "Hi, Talha! How are you? I hope you are doing well.5"
frequency = {char: text.count(char) for char in set(text)}
print(frequency)

#Q7
print("\nQ7")
employees = [
    {"name": "Talha", "department": "IT", "salary": 50000},
    {"name": "Ali", "department": "HR", "salary": 60000},
    {"name": "Zara", "department": "Finance", "salary": 55000},
    {"name": "Fatima", "department": "IT", "salary": 52000}
]
highest_paid_employee = max(employees , key = lambda x: x["salary"])
print(highest_paid_employee)

#Q8
print("\nQ8")
listofnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 11, 31, 55]
listofoddnumbers = list(filter(lambda x: x % 2 != 0, listofnumbers))
print(listofoddnumbers)



#B
import numpy as np

#Q9
print("\nQ9")
arr = np.arange(1, 31)
reshaped_arr = arr.reshape(5, 6)
print(reshaped_arr)


# Q10
print("Q10:")
matrix = np.eye(6)
np.fill_diagonal(matrix, [1, 2, 3, 4, 5, 6])
print(matrix)


# Q11
print("\nQ11:")
numbers = np.random.randint(1, 101, 25)
print("Array:", numbers)
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Standard Deviation:", np.std(numbers))


# Q12
print("\nQ12:")
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

diagonal = np.diag(arr)
print("Diagonal:", diagonal)
print("Diagonal Sum:", np.sum(diagonal))


# Q13
print("\nQ13:")
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
print("Element-wise multiplication:")
print(a * b)

print("Matrix multiplication:")
print(a @ b)


# Q14
print("\nQ14:")
temperatures = np.array([
    32, 34, 36, 38, 35, 37, 33,
    31, 39, 40, 34, 36, 37, 32,
    35, 38, 41, 33, 34, 36, 39,
    30, 32, 37, 38, 35, 36, 40, 34, 31
])
hot_days = temperatures[temperatures > 35]
print("Days above 35°C:", hot_days)
print("Number of days:", len(hot_days))


# Q15
print("\nQ15:")
arr = np.array([10, 20, 30, 40, 50])
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print("Original array:", arr)
print("Normalized array:", normalized)


# Q16
print("\nQ16:")
marks = np.array([
    [78, 85, 90],
    [65, 70, 75],
    [88, 92, 84],
    [55, 60, 58],
    [90, 86, 95]
])
total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)

print("Total marks:", total)
print("Average marks:", average)


# Q17
print("\nQ17:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# replace even numbers with -1
result = np.where(arr % 2 == 0, -1, arr)
print("Original array:", arr)
print("After replacing even numbers:", result)

#C
import pandas as pd


# Q18
students = pd.DataFrame({
    "name": ["Ali", "Talha", "Sara", "Hassan", "Ayesha", "Usman"],
    "subject": ["Math", "English", "Math", "English", "Computer", "Computer"],
    "marks": [78, 65, 88, 72, 91, 56]
})

print("Q18:")
print(students)

print("\nDescription:")
print(students.describe())


# Q19
# making a small csv file for the example
data = {
    "name": ["Ali", "Talha", "Sara", "Hassan", "Ayesha"],
    "marks": [78, np.nan, 88, 65, np.nan],
    "attendance": [85, 72, np.nan, 90, 68]
}
pd.DataFrame(data).to_csv("students.csv", index=False)
# load the csv file
df = pd.read_csv("students.csv")
print("\nQ19:")
print("Missing values:")
print(df.isnull().sum())
# fill missing numeric values with column mean
numeric_columns = df.select_dtypes(include=np.number).columns
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())
print("\nAfter filling missing values:")
print(df)


# Q20
print("\nQ20:")
# students with marks below 50
below_50 = students.loc[students["marks"] < 50, ["name", "marks"]]
print(below_50)


# Q21
print("\nQ21:")
# mean and maximum marks for each section
section_marks = students.groupby("subject")["marks"].agg(["mean", "max"])
print(section_marks)


# Q22
print("\nQ22:")
students_data = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105],
    "name": ["Ali", "Talha", "Sara", "Hassan", "Ayesha"]
})
attendance = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105],
    "attendance": [85, 68, 92, 73, 60]
})
# merge using student ID
merged = pd.merge(students_data, attendance, on="student_id")
# students with attendance below 75%
low_attendance = merged.loc[merged["attendance"] < 75]
print("Students with attendance below 75%:")
print(low_attendance)

#D
import matplotlib.pyplot as plt


# Q23
students = pd.DataFrame({
    "name": ["Ali", "Ahmed", "Sara", "Hassan", "Ayesha", "Usman", "Zain", "Hina"],
    "section": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "marks": [78, 45, 88, 62, 39, 91, 55, 73]
})
# get average marks of each section
section_avg = students.groupby("section")["marks"].mean()
plt.bar(section_avg.index, section_avg.values)
plt.xlabel("Section")
plt.ylabel("Average Marks")
plt.title("Average Marks per Section")
plt.show()


# Q24
plt.hist(students["marks"], bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.show()
# The distribution is spread across the marks range with no clear strong skew.


# Q25
marks = students["marks"]
plt.figure(figsize=(10, 4))
# line plot
plt.subplot(1, 2, 1)
plt.plot(range(1, len(marks) + 1), marks, marker="o")
plt.xlabel("Student Number")
plt.ylabel("Marks")
plt.title("Marks Trend")
# scatter plot
plt.subplot(1, 2, 2)
plt.scatter(marks, range(1, len(marks) + 1))
plt.xlabel("Marks")
plt.ylabel("Student Number")
plt.title("Marks Scatter Plot")

plt.tight_layout()
plt.show()