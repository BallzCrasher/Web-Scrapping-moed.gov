from os import system
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup
from bs4 import BeautifulSoup as bs
import time

Subjects = ['Arabic','English','French',"Who give's a shit ?",'Math','Phyisics','Chimistry','Biography','Total','Sins','Grand Total','Pure Total']

browser = mechanicalsoup.StatefulBrowser()
n=16513
m=16518

for num in range(n,m+1):
	base_url = "http://moed.gov.sy/scientific/"
	browser.open(base_url)
	browser.select_form()

	#log = browser.get_current_form().print_summary()

	browser['city'] = 10
	browser['stdnum'] = num
	browser.submit_selected()
	page = browser.get_current_page()

	current_subject = 0
	dictSubjects = {}
	for i in page.find_all('span',{'class':'mark'}):
    		dictSubjects[Subjects[current_subject]] = int(i.text)
    		current_subject+=1

	skipper = True
	infoList = page.find_all('div',{'class':'a-table user-info'})
	info = infoList[0].find_all('div',{'class':'a-cell'})
	accepted=info.pop()

	#Output

	for i in info:
			if skipper:
				skipper= not skipper
				continue
			print(i.text)
			skipper = not skipper
	#shit
	for i in dictSubjects:
    		print(i + ' = ' + str(dictSubjects[i]))

	pure = dictSubjects['Total']-max(dictSubjects['French'],dictSubjects['English'])
	print(Subjects[current_subject] + ' = ' + str(pure))

	time.sleep(8)
	#print(log)