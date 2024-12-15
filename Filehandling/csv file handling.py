import csv
with open(r'D:\Saylani\Cloud-Data-Engg\Filehandling\file 1.csv') as file:  # default mode is read # we can also use 'r' mode
    content = csv.reader(file)
    for row in content:
        print(row)


row = [
    ['name', 'date', 'event'],
    ['washington', 1776, 'american revolution'],
    ['waterloo', 1815, 'napoleanic wars'],
    ['pearl harbor', 1941, 'world war II'],
    ['berlin', 1945, 'world war II'],
    ['hiroshima', 1945, 'world war II']
]

with open(r'D:\Saylani\Cloud-Data-Engg\Filehandling\file 1.csv', 'w') as file:  # 'w' mode is write mode
    writer_content = csv.writer(file)
    writer_content.writerows(row)