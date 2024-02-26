import csv

with open('students.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

    sum_class = {}
    count_class = {}

    for row in reader:
        if 'Хадаров Владимир' in row[1]:
            print(f'Ты получил: {row[4]} за {row[2]}')

    for elem in reader:
        if elem[-1] == 'None':
            sum_class[elem[-2]] = sum_class.get(elem[-2], 0) + int(elem[-1])
        count_class[elem[-2]] = count_class.get(elem[-2], 0) + 1

    for elem in reader:
        if elem[-1] == 'None':
            elem[-1] = round(sum_class[elem[-2]] / count_class[elem[-2]], 3)

with open('students.csv', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['id','Name','titleProject_id','level','score'])
    writer.writerows(reader)