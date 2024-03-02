
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 02:31:52 2024

@author: IAN CARTER KULANI
"""
#This software prompts the user to enter total number of published centers,total number of registered votes, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward,it determines the candidate with the majority of votes and displays the results on the screen.
#NOTE:For a candidate to be a majority winner the candidate total valid votes should be greater than majority votes.
print("================================MALAWI ELECTROL COMMISSION================================\n")

Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/turnout:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes:"))
#Get Total Valid Votes for All candidates
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get Total Valid Votes For Bingu Wa Mutharika
Totalvalidvotesfor_Bingumutharika=int(input("Enter Total Valid Votes For Bingu Wa Mutharika:"))
#Get Total Valid Votes For John Tembo
Totalvalidvotesfor_Johntembo=int(input("Enter Total Valid Votes For John Tembo:"))
#Get Total Valid Votes For Gwanda Chakuamba
Totalvalidvotesfor_Gwandachakuamba=int(input("Enter Total Valid Votes For Gwanda Chakuamba:"))
#Get Total Valid Votes For Brown Mpinganjira
Totalvalidvotesfor_Brownmpinganjira=int(input("Enter Total Valid Votes For Brown Mpinganjira:"))
#Get Total Valid Votes For Jusice Malewezi
Totalvalidvotesfor_Justicemalewezi=int(input("Enter Total Valid Votes For Jusice Malewezi:"))
#
percent=100

if Totalvalidvotesfor_Bingumutharika>Totalvalidvotes/2+1:
   print("congratulations Bingu Wa Muthalika You're the winner of 2004 Presiential Election")


elif Totalvalidvotesfor_Johntembo>Totalvalidvotes/2+1:
   print("congratulations John Tembo You're the winner of 2004 Presiential Election")


elif Totalvalidvotesfor_Gwandachakuamba>Totalvalidvotes/2+1:
   print("congratulations Gwanda Chakuamba You're the winner of 2004 Presiential Election")


elif Totalvalidvotesfor_Brownmpinganjira>Totalvalidvotes/2+1:
   print("congratulations Brown Mpinganjira You're the winner of 2004 Presiential Election")

elif Totalvalidvotesfor_Justicemalewezi>Totalvalidvotes/2+1:
   print("congratulations Jusice Malewezi You're the winner of 2004 Presiential Election")

else:
      print("No majority winner was found RUNOF may be required Thank you.\n\n")
      
print("____________________________________ELECTION STATISTICS___________________________________\n")  

#Calculating Majority
#Calculating percentage for total votes cast 
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
#Calculating percentage for total valid votes for all canidates
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)
#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void in percentage=",Percentage)
#Calculating percentage for Total Registered voters/turnout
Percentage=round(Totalvotescast*percent/TotalRegisteredvotes, 2);
print("Total Registered voters/turnout in percentage=",Percentage)
#Calculating percentage for Bingu Wa Mutharika
Percentage=round(Totalvalidvotesfor_Bingumutharika*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Bingu Wa Mutharika in percentage=",Percentage)
#Calculating percentage for John Tembo
Percentage=round(Totalvalidvotesfor_Johntembo*percent/Totalvalidvotes, 2);
print("Total Valid Votes For John Tembo in percentage=",Percentage)
#Calculating percentage for Gwanda Chakuamba
Percentage=round(Totalvalidvotesfor_Gwandachakuamba*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Gwanda Chakuamba in percentage=",Percentage)
#Calculating percentage for Brown Mpinganjira 
Percentage=round(Totalvalidvotesfor_Brownmpinganjira*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Brown Mpinganjira in percentage=",Percentage)
#Calculating percentage for Jusice Malewezi
Percentage=round(Totalvalidvotesfor_Justicemalewezi*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Jusice Malewezi in percentage=",Percentage)
#
print("============================================================================================")
