# Include the Dropbox SDK libraries
from dropbox import client, rest, session
#Used to store fetched data and process them
import csv
import os
import commands

# Get your app key and secret from the Dropbox developer website
# You need to create an app with option Full Dropbox Folder
APP_KEY = 'APP_KEY'
APP_SECRET = 'APP_SECRET'

# ACCESS_TYPE should be 'dropbox' since we are interested in the log of a file
ACCESS_TYPE = 'dropbox'

sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

request_token = sess.obtain_request_token()

url = sess.build_authorize_url(request_token)

# Make the user sign in and authorize this token
print "url:", url
print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)

client = client.DropboxClient(sess)
#For debug, you can use following to display account info
#print "linked account:", client.account_info()

# To store time stamps of each revision
dictTimeStamps={}

# To Get All Files in a Folder you can use:
#folder_metadata = client.metadata('/Research/ThesisOzanSener/')#name of the folder we are interested
#for i in range(1,len(folder_metadata['contents'])):
#	if folder_metadata['contents'][i]['is_dir']==False:

#Full path of the files we are interested in their stories
filel = ['file1','file2']
for fN in filel:
	dictFS = {} #Processed value of a single file
	dictFSStr = {} #Yet another value
	revs = client.revisions(fN)
	for i in range(len(revs)): #Maximum number of revision is 1000 in default case
		f, metadata = client.get_file_and_metadata( revs[i]['path'],revs[i]['rev']) Fetch data
		# Write revision of the file
		out = open("/home/ozan/thesisLog" + revs[i]['path'] + str(revs[i]['revision']), 'w')
		out.write(f.read())
		out.close()
		dictTimeStamps[revs[i]['revision']]=revs[i]['modified']
		# Process your files to get necessary data
		wcBeforeStrip=int(commands.getstatusoutput('wc -w '+"/home/ozan/thesisLog" + revs[i]['path'] + str(revs[i]['revision'])+' |cut -f1 -d" "')[1])
		os.system("/home/ozan/thesisLog/a.pr "+"/home/ozan/thesisLog" + revs[i]['path'] + str(revs[i]['revision'])+" >tmp.txt")
		wcAfterStrip=int(commands.getstatusoutput('wc -w '+"tmp.txt"+' |cut -f1 -d" "')[1])
		# Store the data
		dictFS[revs[i]['revision']]=wcBeforeStrip
		dictFSStr[revs[i]['revision']]=wcAfterStrip
	# Save the story of a single file to a CSV file
	w2 = csv.writer(open( "/home/ozan/thesisLog" + revs[i]['path']+".csv", "w"),delimiter=';')
	for key, val in dictFS.items():
		w2.writerow([key,dictTimeStamps[key],val,dictFSStr[key]])
#Save the timestamps for further usage
w = csv.writer(open("timeStamps.csv", "w"),delimiter=';')
for key, val in dictTimeStamps.items():
    w.writerow([key, val])
