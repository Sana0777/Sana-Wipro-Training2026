import pandas as pd
import numpy as np


students = [
    {"name": "Amit", "score": 85},
    {"name": "Priya", "score": 92},
    {"name": "Rahul", "score": 78},
    {"name": "Neha", "score": 90},
    {"name": "Suresh", "score": 88}
]

df = pd.DataFrame(students)

scores = df["score"].values

mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev_score = np.std(scores)

print("Mean:", mean_score)
print("Median:", median_score)
print("Standard Deviation:", std_dev_score)


df["above_average"] = df["score"] > mean_score

print(df)
