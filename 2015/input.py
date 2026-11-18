import os

import requests

fname = "in.txt"
if os.path.isfile(fname):
    os.remove(fname)
    print(f"Found an old {fname}. Deleted!")
else:
    print(f"Old {fname} not found. Clear!")

year = input("year: ")
day = input("day: ")
session = input("session: ")

headers = {"Cookie":"session=" + session}
payload = f"https://adventofcode.com/{year}/day/{day}/input"

r = requests.get(payload, headers=headers)
if r.status_code == 200:
    data = r.text

    with open(fname,"w") as f:
        print(data, file=f)
        print(f"{fname} created!")

    boiler = """# Strips whitespace ignores empty lines, i have to change this if puzzle input requires those to remain
with open('in.txt','r') as f:
        lines = [line.strip() for line in f if line.strip()]
for line in lines:
    print(line)
"""
    with open(f"day{day}.py","w") as k:
        print(boiler, file=k)
        print("Boilerplate generated!")
else:
    print("double check session cookie")
