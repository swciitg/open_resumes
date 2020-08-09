def experience(f,companyName="None",location="None",X="None",Y="None",work="None",startDate="None",endDate="None",workDone="None"):
	f.write("    \\resumeSubheading")
	f.write("\n      {" + companyName + "}{" + location + "}")
	f.write("\n      {" + X + " \& " + Y + " " + work + "}{" + startDate + " - " + endDate + "}")
	f.write("\n      \\resumeItemListStart")
	f.write("\n    \item {" + workDone + "}")
	f.write("\n    \\resumeItemListEnd\n\n")
	
def projects(f,projectName="None",profOrClubName="None",startDate="None",endDate="None",githubLink="None",workDone="None"):
	f.write("\n    \\resumeProject")
	f.write("\n      {" + projectName + "} %Project Name")
	f.write("\n      {" + profOrClubName + "} %Professors Name/Event Name/Club Name")
	f.write("\n      {" + startDate + " - " + endDate +"} %Event Dates")
	f.write("\n      {\href{Link to github}{" + githubLink + "}} %Website")
	f.write("\n      \\resumeItemListStart")
	f.write("\n        \item {" + workDone + "}")
	f.write("\n    \\resumeItemListEnd\n")
	
def technicalSkills(f,subHeadings=[],itemsArrays=[]):
	f.write("\n%-------------Technical Skills--------------------")
	f.write("\n\section{Technical Skills}")
	f.write("\n \\resumeHeadingSkillStart")
	for i in range(0,len(subHeadings)):
		f.write("\n  \\resumeSubItem{" + subHeadings[i] + "} %Category")
		f.write("\n    {")
		for item in itemsArrays[i]:
			f.write(item + ", ")
		f.write("} %Skills")
	f.write("\n\hfill \\textit{\\footnotesize{* Elementary proficiency}} \hspace{3mm}")	
	f.write("\n \\resumeHeadingSkillEnd")
	
def keyCourses(f,subHeadings=[],itemsArrays=[]):
	f.write("\n%-------------Key Courses--------------------")
	f.write("\n\section{Key Courses}")
	f.write("\n \\resumeHeadingSkillStart")
	for i in range(0,len(subHeadings)):
		f.write("\n  \\resumeSubItem{" + subHeadings[i] + "} %Category")
		f.write("\n    {")
		for item in itemsArrays[i]:
			f.write(item + ", ")
		f.write("} %Skills")
	#f.write("\n\hfill \\textit{\\footnotesize{* Elementary proficiency}} \hspace{3mm}")	
	f.write("\n \\resumeHeadingSkillEnd")
	
def PORs(f,itemsArrays=[]):
	f.write("\n%-------------Positions of Responsibility--------------------")
	f.write("\n\section{Positions of responsibility}")
	f.write("\n\\vspace{-0.4mm}")
	f.write("\n\\resumeSubHeadingListStart")
	for i in range(0,len(itemsArrays)):
		f.write("\n  \\resumePOR")
		for item in itemsArrays[i]:
			f.write("{" + item + "}\n")	
	f.write("\n\\resumeSubHeadingListEnd")
	f.write("\n\\vspace{-4mm}")
	
def Achievements(f,itemsArrays=[]):
	f.write("\n%-------------Achievements--------------------")
	f.write("\n\section{Achievements}")
	f.write("\n\\vspace{-0.2mm}")
	f.write("\n\\resumeSubHeadingListStart")
	for i in range(0,len(itemsArrays)):
		f.write("\n  \\resumePOR")
		for item in itemsArrays[i]:
			f.write("{" + item + "}\n")	
	f.write("\n\\resumeSubHeadingListEnd")
	#f.write("\n\\vspace{4mm}")
