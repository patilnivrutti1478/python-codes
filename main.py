import pandas as pd 
df = pd.read_csv("Data.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print("Math avrage =" , df["Math "].mean())
print("statistics avrage =" , df["Statistics "].mean())

print("Highest  Math  =", df["Math "].max())
print("Highest Statistics =", df["Statistics "].max())
print("Lowest  Math = ", df["Math "].min())
print("Lowest Statistics =", df["Statistics "].min())

df["total"] = df["Math "] + df["Statistics "]
print(df.head())
print(df[df["total"] == df["total"].mean()])
df[ "percentage"] = (df["total"] /200)* 100
print(df.head())
print(df[df["percentage"] >70])

print(df.sort_values("percentage", ascending=False).head())
top = df .loc[df["percentage"].idxmax()]
print(top)
print(df[df["Math "] > 60])
print(df[df["Statistics "] > 60])

import matplotlib.pyplot as plt

# Math marks graph
# plt.bar(df["Name "], df["Math "])

# plt.title("Math Marks of Students")
# plt.xlabel("Students")
# plt.ylabel("Math Marks")

# plt.show()
# import matplotlib.pyplot as plt

#  Math आणि Statistics चे एकूण marks
# math_total = df["Math "].sum()
# stats_total = df["Statistics "].sum()

# labels = ["Math", "Statistics"]
# marks = [math_total, stats_total]

# plt.pie(marks, labels=labels, autopct="%1.1f%%")
# plt.title("Math vs Statistics Total Marks")
# plt.show()

