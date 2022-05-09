# Analysis of the Election Audit

## Overview of Project
### Purpose of Project
In this project, I demonstrated my proficiency with various features in Python and Visual Studio (VS) Code: create and add lists, create and add keys and values to a dictonary, use decision statements to check a condition, apply membership and logical operators to decision statements, use repetition statements to iterate through a list or dictionary. To accomplish these goals, I was given a fictional situation and data set of approximatelly 370 thousand rows of data. 
### Background of Project
A Colorado Board of Elections employee has given the following tasks below to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of counties that cast votes.
3. Calculate the voter turnout for each county and the percentage of votes from each county out of the total count. 
4. Determine the county with the highest turnout. 
5. Get a complete list of candidates who recieved votes.
6. Calculate the total number of votes each candidate recieved and the percentage of votes each candidate won.
7. Determine the winner of the lection based on popular vote. 
---
## Election-Audit Results 
The analysis of the election results show that: 
1. There were *369,711* votes cast in the election.
2. The counties that cast votes were Jefferson, Denver, and Arapahoe. 
3. The county results were: Jefferson made up *10.5%* of the votes with *38,855* number of votes. Denver made up *82.8%* of the votes with *306,055* number of votes. 
Arapahoe made up *6.7%* of the votes with *24,801* number of votes. 
4. The county with the largest number of votes was Denver. 
5. The candidates were Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane
6. The candidate results were: Casper Stockham received *23%* of the votes with *85,213* number of votes. DeGette reicieved *73.8%* of the votes with *272,892* number of votes. Doane reicieved *3.1%* of the votes with *11,606* number of votes. 
7. The winner of the election was **Diana DeGette**, who recieved 73.8% of the votes and 272,892 number of votes. 

---
## Election-Audit Summary 
This script is currently used to find a winning candidate based on the the popular vote for one race. However, a typical ballot will have more than one race so a script that outputs the winner for multiple races is an important modification. The script extracts the candidate name from each row using *candidate_name = row[2]* then uses a for loop to iterate through the row and store the information into a dictionary. A modified script could repeat this for code for each race or use another loop in order to iterate through each row with a unique race.  

Another modification could be how the winner is determined. In some states, like New York, the winning candidate is chosen based on rank choice voting instead of popular vote. The script currenly determines if the votes is greater than the winning count using the code: 

    if (votes > winning_count) and (vote_percentage > winning_percentage):
             winning_count = votes
             winning_percentage = vote_percentage
             winning_candidate = candidate_name


This script could be modified to using if else statements to assign votes to second, third, fourth, or fifth choice candidates if there is no majority winner after counting first choices. Those code would need to eliminate the candidate with the fewest votes and voters who picked that candidate as ‘number 1’ would have their votes count for their next choice. This process would continue until a majority winner was found. 
