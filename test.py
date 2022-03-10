import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "10 Hours of Dark Souls Relaxation", "views": 100000},
        {"likes": 10000, "name": "Gwyn's Theme played in Stormy Anor Londo", "views": 80000},
        {"likes": 35, "name": "Pasha", "views": 2000}]

for i in range(len(data)):
    res = requests.put(BASE + "video/" + str(i), data[i])
    print(res.json())

input()
res = requests.get(BASE + "video/2")
print(res.json())