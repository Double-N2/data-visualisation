import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Raw data.csv')
print(data.head())
# data.info()
print(data.columns)
# What Factors influence exam performance
data["Time"]  = data["Sleep_Hours"] + data["Study_Hours_Per_Day"] + data["Internet_Usage_Hours"]
test = data.groupby("Final_Exam_Score")["Time"].sum()
print(test.sort_values(ascending=False))
# print(data.head())

# Do students who study more perform better
test2 = data.groupby("Final_Exam_Score")["Study_Hours_Per_Day"].mean()
print(test2.sort_values(ascending=False))

# Does attendance affect grades
test1 =data.groupby("Attendance_Percentage")["Previous_Grades"].mean()
print(test1.sort_values(ascending=False))

# Which course has the highest performance
test3 =data.groupby("Course")["Final_Exam_Score"].mean()
print(test3.sort_values(ascending=False))

# Which students are at risk of failing
print(data.loc[data["Final_Exam_Score"] < 50])

# Are there relationships between lifestyle and academic success
test5 =data.groupby("Final_Exam_Score")[["Final_Exam_Score", "Time"]].count()
print(test5.sort_values("Final_Exam_Score", ascending=False))
# Are there common patterns among high-performing students
test4 = data.groupby("Student_ID")[["Final_Exam_Score","Time"]].mean()
print(test4.sort_values("Student_ID", ascending=False))

# Visualising

plt.figure()
plt.scatter(data["Final_Exam_Score"], data["Time"])
plt.xlabel("Final Exam Score")
plt.ylabel("Number of Students")
plt.title("What factors influence exam performance?")
plt.show()
plt.figure()
plt.scatter(data["Final_Exam_Score"], data["Study_Hours_Per_Day"])
plt.xlabel("Final Exam Score")
plt.ylabel("Study_Hours_Per_Day")
plt.title("Do students who study more perform better?")
plt.show()
plt.figure()
plt.scatter(data["Attendance_Percentage"], data["Previous_Grades"])
plt.xlabel("Attendance Percentage")
plt.ylabel("Previous Grades")
plt.title("Does attendance affect grades?")
plt.show()
plt.figure()
plt.scatter(data["Course"], data["Final_Exam_Score"])
plt.xlabel("Course")
plt.ylabel("Final Exam Score")
plt.title("Which course has the highest performance?")
plt.show()
plt.figure()
plt.scatter(data["Student_ID"], data["Final_Exam_Score"])
plt.xlabel("Student ID")
plt.ylabel("Final Exam Score")
plt.title("Which students are at risk of failing?")
plt.show()
plt.figure()
plt.title("Are there relationship between lifestyle and academic success")
plt.scatter(data["Time"],data["Final_Exam_Score"])
plt.xlabel("Time")
plt.ylabel("Final Exam Score")
plt.show()
plt.figure()
plt.scatter(data["Student_ID"], data["Final_Exam_Score"])
plt.scatter(data["Student_ID"], data["Time"])
plt.xlabel("Student ID")
plt.title("Identify patterns among high-performing students")
plt.show()


# | Function         | Purpose                                                  | Example                                    | Answers the question...                 |
# | ---------------- | -------------------------------------------------------- | ------------------------------------------ | --------------------------------------- |
# | `count()`        | Counts non-missing values                                | `df["Score"].count()`                      | "How many values are there?"            |
# | `size()`         | Counts all rows (including rows with missing values)     | `df.groupby("Course").size()`              | "How many records are in each group?"   |
# | `value_counts()` | Counts how often each unique value appears               | `df["Gender"].value_counts()`              | "How many males and females are there?" |
# | `mean()`         | Calculates the average                                   | `df["Score"].mean()`                       | "What is the average?"                  |
# | `sum()`          | Adds values together                                     | `df["Sales"].sum()`                        | "What is the total?"                    |
# | `max()`          | Finds the largest value                                  | `df["Score"].max()`                        | "What is the highest?"                  |
# | `min()`          | Finds the smallest value                                 | `df["Score"].min()`                        | "What is the lowest?"                   |
# | `median()`       | Finds the middle value                                   | `df["Score"].median()`                     | "What is the middle score?"             |
# | `std()`          | Measures how spread out the data is                      | `df["Score"].std()`                        | "How much do the values vary?"          |
# | `corr()`         | Measures the relationship between numerical columns      | `df[["Study_Hours","Score"]].corr()`       | "Are these variables related?"          |
# | `groupby()`      | Splits data into groups before applying another function | `df.groupby("Course")["Score"].mean()`     | "What's the average score per course?"  |
# | `sort_values()`  | Sorts rows by a column                                   | `df.sort_values("Score", ascending=False)` | "Who has the highest score?"            |
# | `head()`         | Shows the first rows                                     | `df.head()`                                | "What does my data look like?"          |
# | `tail()`         | Shows the last rows                                      | `df.tail()`                                | "What are the last records?"            |
# | `info()`         | Displays column types and missing values                 | `df.info()`                                | "What's in this dataset?"               |
# | `describe()`     | Gives summary statistics                                 | `df.describe()`                            | "Summarize my numerical data."          |
# | `loc[]`          | Selects rows/columns by labels or conditions             | `df.loc[df["Score"] > 70]`                 | "Show students scoring above 70."       |
# | `iloc[]`         | Selects rows/columns by position                         | `df.iloc[0:5]`                             | "Show the first five rows."             |
