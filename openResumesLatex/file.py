from file1 import *

f1 = open("latexFile1.txt","rt")
f = open("latexFile.txt","w")

#f.write(f1.read())
lines = f1.readlines()
f.write(lines[0])
f.close()
f = open("latexFile.txt","a")

for i in range(1,127):
	f.write(lines[i])

#initialCode(f)

f.write("\\newcommand{\\name}{" + "StudentsName" + "} % Your Name")
f.write("\n\\newcommand{\course}{" + "B.Tech" + " - " + "XXXXXXX" + " and " + "YYYYYYY" " Engineering} % Your Course")
f.write("\n\\newcommand{\\roll}{" + "XXXXXXXXX" + "} % Your Roll No.")
f.write("\n\\newcommand{\phone}{" + "XXXXXXXXX" + "} % Your Phone Number")
f.write("\n\\newcommand{\emaila}{" + "something@example.com" + "} %Email 1")
f.write("\n\\newcommand{\emailb}{" + "somethingelse@example.com" + "} %Email 2")
f.write("\n\\newcommand{\github}{" + "USERID" + "} %Github")
f.write("\n\\newcommand{\website}{" + "https://example.com" + "} %Website")
f.write("\n\\newcommand{\linkedin}{" + "LINKEDINUSERID" + "} %linkedin")
f.write("\n\n\n\n")

for i  in range(130,167):
	f.write(lines[i])

f.write("  B.Tech" + ". Major & Indian Institute of Technology, Guwahati & " + "0.00" + " (Current) & " + "2016" + "-Present\\\\")
f.write("\n  \hline")
f.write("\n  B.Tech" + ". Minor & Indian Institute of Technology, Guwahati & " + "0.0" + " (Current) & " + "2017" + "-Present\\\\ %Optional")
f.write("\n  \hline")
f.write("\n  Senior Secondary & " + "CBSE Board" + " & " + "00.0" + "\% & " + "2015" + " \\\\")
f.write("\n  \hline")
f.write("\n  Secondary & " + "ICSE Board" + " & " + "00.0" + "\% & " + "2013" + " \\\\")
f.write("\n  \hline\n")

for i in range(168,175):
	f.write(lines[i])

noOfExperience = 1 
noOfProjects = 1

subHeadingsTech = ["Programming","Category XYZ"]
itemsArraysTech = [["C","C++","Python"],["Skill A","Skill B","Skill C","Skill D"]]

subHeadingsKeyCourses = ["Mathematics","Course Category,XYZ"]
itemsArraysKeyCourses = [["Linear Algebra", "Basic Calculus", "Discrete Maths", "Probability \& Random Processes" ],
			 ["Course Name 1", "Course Name 2", "Course Name 3", "Course Name 4"]]

itemsArraysPORs = [["City Representative","Technothlon, IIT Guwahati","Apr. 2018 - Apr. 2019"],
		   ["Position","Club,Event","Tenure period"]]

itemsArraysAchievements = [["Bronze Medal","XYZ Challenge, ABC Company, FGH City","2018"],
		   ["Institute Merit Scholarhip","(given to branch toppers)","July. 2019 - May 2020"]]

for i in range(0,noOfExperience):
	experience(f)
	
for i in range(185,197):
	f.write(lines[i])
	
for i in range(0,noOfProjects):
	projects(f)

f.write("\n\n")
for i in range(198,208):
	f.write(lines[i])

if len(subHeadingsTech) :
	technicalSkills(f,subHeadingsTech,itemsArraysTech)
	
f.write("\n\n")	

if len(subHeadingsKeyCourses) :
	keyCourses(f,subHeadingsKeyCourses,itemsArraysKeyCourses)
	
f.write("\n\n")	

if len(itemsArraysPORs) :
	PORs(f,itemsArraysPORs)
	
f.write("\n\n")	

if len(itemsArraysAchievements) :
	Achievements(f,itemsArraysAchievements)
	
f.write("\n\n")

for i in range(209,214):
	f.write(lines[i])

f.close()











