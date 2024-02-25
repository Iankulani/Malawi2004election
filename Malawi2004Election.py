
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 02:31:52 2024

@author: IAN CARTER KULANI
"""

print("==============================MALAWI ELECTROL COMMISSION==============================\n") 
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Votes:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null and Void Votes:"))
#Get Total Valid Votes for All candidates
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#
Totalvalidvotesfor_Bingumutharika=int(input("Enter Total Valid Votes For Bingu Wa Mutharika:"))
#
Totalvalidvotesfor_Johntembo=int(input("Enter Total Valid Votes For John Tembo:"))
#
Totalvalidvotesfor_Gwandachakuamba=int(input("Enter Total Valid Votes For Gwanda Chakuamba:"))
#
Totalvalidvotesfor_Brownmpinganjira=int(input("Enter Total Valid Votes For Brown Mpinganjira:"))
#
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

#Calculating Majority
majority_percent=Totalvalidvotesfor_Bingumutharika*percent/Totalvalidvotes;
print("Total Valid Votes For Bingu Wa Mutharika in percentage=",majority_percent)
majority=Totalvalidvotesfor_Johntembo*percent/Totalvalidvotes;
print("Total Valid Votes For John Tembo in percent=",majority_percent)
majority=Totalvalidvotesfor_Gwandachakuamba*percent/Totalvalidvotes;
print("Total Valid Votes For Gwanda Chakuamba=",majority_percent)
majority=Totalvalidvotesfor_Brownmpinganjira*percent/Totalvalidvotes;
print("Total Valid Votes For Brown Mpinganjira=",majority_percent)
majority=Totalvalidvotesfor_Justicemalewezi*percent/Totalvalidvotes;
print("Total Valid Votes For Jusice Malewezi=",majority_percent)
