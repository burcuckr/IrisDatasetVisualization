import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("myproject/Iris.csv") #veri yükleme
print(df.head()) #ilk 5 satırı okur

#Grafik çizme
#Line graph
'''
x = df.index
y = df["SepalWidthCm"]

plt.plot(x, y)
plt.xlabel("index")
plt.ylabel("Width")
plt.title("Index - SepalWidth")
plt.show()
print(df.describe())

#Line graph-2

x = df.index
y = df["PetalLengthCm"]

plt.plot(x, y, linestyle = "--")
plt.xlabel("index")
plt.ylabel("Petal Length")
plt.show()

#bar graph

avg = df.groupby("Species")["SepalLengthCm"].mean()

plt.bar(avg.index, avg.values)

plt.xlabel("Species")
plt.ylabel("Petal Length")
plt.show()

#scatter plot
x = df["SepalLengthCm"]
y = df["PetalLengthCm"]

plt.scatter(x, y)
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal Length vs Petal Length")
plt.show()

#Histogram
plt.hist(df["PetalLengthCm"], bins = 20)
plt.show()

#Box Plot
plt.boxplot(df["SepalLengthCm"])
plt.show()
'''
#Correlation Heat Map
sns.heatmap(df.corr(numeric_only = True), annot = True)
plt.show()