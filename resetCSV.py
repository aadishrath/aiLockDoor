import os
import csv

cwd = os.getcwd()
path = cwd + '\\user_data\\users.csv'
users = {0:"Ariana", 1:"Eddie"} # Assign Name

with open(path, mode='w') as csvfile:
    fieldnames = ['key', 'value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for key in sorted(users.keys()) :
        writer.writerow({'key': key, 'value': users[key]})