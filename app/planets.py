import csv 
with open("solar_system.csv", "r", encoding="utf-8", newline="") as fid:
    reader = csv.reader(fid, delimiter=",")

#write a python scrip to read through a csv file and loop through the file 