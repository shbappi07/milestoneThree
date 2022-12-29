import csv

# with open('students.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

blank_list = []
with open('studentDict.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        blank_list.append(row)

print(blank_list)