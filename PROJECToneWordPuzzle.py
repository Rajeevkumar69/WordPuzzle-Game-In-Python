l1=["Father","Mother","Mango","Coding","Computer","Data","Market","Internet","Enjoy","Party","College","Music","Technology","Light","Traffic","Road","Police","Girl","Apple","Water","Orange","River","Valley","Pen","Job","Sky","Software","Chess","Mobile","Game","Black"]


print('''\n\n\t\t"--Welome To Word Puzzle Game--"\n\t''')
a=input("Enter Your Name:- ")
#print("\nRule To Play The Game")
print("\nRule1. You have to Solve all the Incorrect Word!")
print("Rule2. Evert First Letter Should be Capital")
print("\n\n\t  ~Now It's Your Turn Let's Play and Enjoy~ ")
input("\n\t Press any key to Continue..")
#system("clear")
count=0
for e in l1:
    print("\n")
    print("\n\t\t -----------------")
    print("\t\t   "  ,e[::-1])
    print("\t\t -----------------")
    
    if(e==input("\nEnter The Correct Word:- ")):
        print("\tCorrect!!")
        count=+1
    else:
        print("\tWrong!!")
        count=-1
    

       
            

print("\n",a," Your Score Is: ",count)
