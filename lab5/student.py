import pandas as po

df = po.read_csv('students.csv')
print("the dataset: ", df)
print("the first five rows:",df.head())

rows, columns = df.shape

print(f"Number of rows:{rows}")
print(f"Number of columns:{columns}")

name = df[["name","GPA"]]
print(name)

good_student = df[df["GPA"] >= 3.5]
print(good_student)

sort = df.sort_values(by="GPA")
print("after sort:",sort)

average = df["GPA"].mean()
print("average:",average)