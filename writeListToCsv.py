import csv

students = ['sal','messi','mbappe','neymar']

with open('students.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(students)
