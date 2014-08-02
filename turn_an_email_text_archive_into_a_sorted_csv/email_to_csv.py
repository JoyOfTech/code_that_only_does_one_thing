import csv

#Open the raw text file
filename = "commotion-discuss.txt"
listname = "Commotion-discuss"
with open(filename, "r") as archive_file:
	content = archive_file.readlines()


# Create a list of starting line indexes to use later
# Improved performance so that conditionals for subject etc are not checking more lines than necessary
counter = 0
start_indexes = []
for index, row in enumerate(content):
	if "From " in row[0:5]:
		start_indexes.append(index)

# Assemble the csv by writing id, start_line, username, datetime, subject, full_username
with open(filename+'_sorted'+'.csv', 'wb') as csvfile:
	archivewriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	archivewriter.writerow(["message_number", "subject", "datetime","timezone", "username", "message_content"])
	for index, start_line in enumerate(start_indexes):
		# Find the endline
		try:
			end_line = start_indexes[index+1]-1
		except:
			end_line = len(content)
		# email_is_in = content[start_line]
		### Find the username
		try:
			usernameline = ((content[start_line+1]).split("("))
			username = (usernameline[1].split(")")[0])
		except:
			username = "Unknown user on line", start_line
		# Find the date and time
		try:
			datetime = (content[start_line+2].split("Date: ")[1]).strip('\n')
		except:
			datetime = "Unknown datetime on line", start_line
		# Find the timezone
		timezone = (content[start_line+2])[-6:-1]
		# Find the subject
		try:
			subject= (content[start_line+3].split(listname+"]")[1]).split('\n')[0]
		except:
			subject = "Unknown subject on line", start_line
		# Find the message content (too long right now)
		#####Uncomment###message_content = content[start_line+4:end_line]
		message_content = "Placeholder_content"
		# Write the csv file
		archivewriter.writerow([index, subject, datetime, timezone, username, message_content])
