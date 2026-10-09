import pandas as po

df = po.read_csv("students.csv")
df2 = po.read_csv("scores.csv")

print(df)
print(df2)

print("missing values:",df.isna().sum().sum())
print("missing values:",df2.isna().sum().sum())

print("fill missing values = 0: ",df.fillna(0))
print("fill missing values = 0: ",df2.fillna(0))

merge = po.merge(df,df2)
print("merge: ",merge)

#average scores for each students
merge['average_scores'] = merge[['math','python','database']].mean(axis=1)
print('average_scores:',merge)

#top 5 scores
top = merge.sort_values(by = "average_scores")
tops = top.head()
print("top 5: ",tops)

#average scores by major
major_average = merge[['math','python','database']].mean()
print("average score by major: ",major_average)