import csv

with open("planets.csv", "r", encoding="utf-8", newline="") as fid:
    reader = csv.reader(fid, delimiter=",")
    for planet in reader:
        print(planet[0])