import csv

students = {'name': 'Salimul', 'email': 'shbappi@gmail.com', 'fb': 'https://fb.com/salimul.7'}

with open('studentDict.csv', 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames= students.keys())
    header = writer.writeheader()
    i = 0
    while i <100:
        writer.writerow(students)
        i += 1
