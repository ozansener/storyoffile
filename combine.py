#Combine stories (CSV files) of several files into  a single CSV file
import csv
#files to combine
files = ['thesisOzanSener.tex','abs.tex','ack.tex','conc.tex','graph.tex','image.tex','video.tex','intro.tex']
tStamp = 'timeStamps' #time stamp file

#read all file stories into seperate dictionaries
dict = {}
for i in files:
	dict[i]={}
	for key,val in csv.reader(open(i+'.csv'),delimiter=';'):
		dict[i][int(key)] = val
#time stamp dictionary
timeStamp = {}
for items in csv.reader(open(tStamp+'.csv'),delimiter=';'):
	timeStamp[int(items[0])] = items[1]

#Insert proper key values to a time stamps which file does not change
#If X is in time stamps and FileY has no X, value for FileY is selected as the value for the time stamp nearest to X
for items in timeStamp:
	for i in files:
		if items not in dict[i]:
			cTime = items 
			while (cTime not in dict[i]) and (cTime>0):
				cTime=cTime - 1
			if cTime == 0:
				dict[i][items]=0
			else:
				dict[i][items]=dict[i][cTime]


#Write combined value in a single CSV file
w = csv.writer(open("combined.csv", "w"),delimiter=';')
w.writerow(['id','TS']+files)
for key, val in timeStamp.items():
	fV = [key,val]
	for i in files:
		fV = fV + [dict[i][key]]
	w.writerow(fV)
