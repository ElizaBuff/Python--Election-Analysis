#the data we need to retrive
#1. the total number of votes cast
#2.a complete list of candidates who recieved votes
#3.the percentage of votes each candidate won
#4.total number of votes each candidate won
#5.the winner of teh election based on popular vote

# #import datetime class from teh datetime module
# import datetime
# #use now() attribute on the datetime class to get the present time 
# now=datetime.datetime.now()
# #print the present time
# print("The time right now is", now)

import csv
import os

#assign a variable for the file to load and the path
file_to_load= os.path.join("Resources" , "election_results.csv")

#create a filename variable to a direct or indirect path to the file
file_to_save= os.path.join("anaylsis", "election_anaylsis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:

#To do: read and analyze the data here 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)



