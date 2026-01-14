import csv
with open("data.csv" ,"w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name","ID","Age"])
    writer.writerow(["Sana","101","23"])
    writer.writerow(["Shifa","102","20"])
