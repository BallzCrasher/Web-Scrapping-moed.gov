import json
import csv

"""
if you are using the highSchool version use the first Subjects list.
if you are using the ninthGrade version use the first Subject list.
Make sure to open the right JSON folder.
"""
check = u'\u2713'
minus = u'\u2212'
#Subjects = ['Arabic','English','French',"Who give's a shit ?",'Math','Phyisics','Chimistry','Biography','Total','Sins','Grand Total','Pure Total']
Subjects = ['Arabic','English','French',"Who give's a shit ?",'Math','Science','Sins','Total']
Student_proprities = ['Student Number','City' , 'Name' , "Mother's Name" , 'School','Status'] #size 5

data = open('data2.json','r')
data = json.load(data)

writer = csv.writer(open('result2.csv','w',encoding='utf-8',newline=''))

writer.writerow(Student_proprities + Subjects)
row = []

for stdnum in data :
    row.append(stdnum)
    for prop in data[stdnum]:
        if type(data[stdnum][prop]) != dict :
            row.append(data[stdnum][prop])
        else :
            for mark in data[stdnum][prop] :
                row.append(data[stdnum][prop][mark])
    writer.writerow(row)
    row.clear()