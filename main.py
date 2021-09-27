from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup
import time
import json

Subjects = ['Arabic','English','French',"Who give's a shit ?",'Math','Phyisics','Chimistry','Biography','Total','Sins','Grand Total','Pure Total']
Student_proprities = ['City' , 'Name' , 'MotherName' , 'School' , 'Subjects'] #size 5

check = u'\u2713'
minus = u'\u2212'

browser = mechanicalsoup.StatefulBrowser()
n=16250 
m=16300

students = {} #the dict that we are going to be filling in with student dicts

#scrap data between student number n to student number m
for num in range(n,m+1):
	base_url = "http://secondary2021.moed.gov.sy/scientific/"
	browser.open(base_url)
	browser.select_form()

	#log = browser.get_current_form().print_summary()

	browser['city'] = 10
	browser['stdnum'] = num
	browser.submit_selected()
	page = browser.get_current_page()
	try :
		current_subject = 0
		dictSubjects = {}
		#student = {'subjects' : dictSubjects , 'name' : 'rose' , 'school':'shit'}
		student = {}
	

		#fulling dictSubjects with the student marks
		for i in page.find_all('span',{'class':'mark'}):
    			dictSubjects[Subjects[current_subject]] = int(i.text)
    			current_subject+=1

		skipper = True
		infoList = page.find_all('div',{'class':'a-table user-info'})
		info = infoList[0].find_all('div',{'class':'a-cell'})
		accepted=info.pop()
		accepted=accepted.text
		#Get stdnum and fill the student dict with proprities
		stdnum = 0
		current_Student_propritie = 0
		for i in info:
				if skipper:
					skipper= not skipper
					continue
				if i.text.isnumeric() :
					stdnum = int(i.text)
				else :
					student[Student_proprities[current_Student_propritie]] = i.text.strip('\t') #idk why there are tabs in the city section
					current_Student_propritie+=1
				skipper = not skipper
				print(i.text)

		if minus in accepted :
			student['Stateus'] = 'Failed'
		elif check in accepted : 
			student['Stateus'] = 'Succeeded'
		else :
			student['Stateus'] = 'Absent'
	
		for i in dictSubjects:
    			print(i + ' = ' + str(dictSubjects[i]))
		try :
			pure = dictSubjects['Total']-max(dictSubjects['French'],dictSubjects['English'])
			dictSubjects['Pure Total'] = pure
	
			print(Subjects[current_subject] + ' = ' + str(pure))
			student[Student_proprities[current_Student_propritie]] = dictSubjects #filling last Student propritie which is the subject marks
		except KeyError :
			student[Student_proprities[current_Student_propritie]] = "This Student didn't come to the test. i.e. the student is absent"
			print(student[Student_proprities[current_Student_propritie]])

		students[stdnum] = student #pushing the student into the dict base on his stdnum
	
		time.sleep(0.5)

	except IndexError :
		students [num] = 'This student number doesn\'t exist.'
		time.sleep(0.3)
print(students)

for i in students :
	print(i , end=' = ')
	print(students[i])

json.dump(students,open('data.json','w'))
#print(log)
