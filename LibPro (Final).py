#FUNCTIONS
db={}
def add(n):

	l=[]
	an=input("Enter Author Name:")
	bn=input("Enter Book Name:")
	p=int(input("Enter Price:"))
	i=input("Enter Issue Status(y/n):")
	l.append(an)
	l.append(bn)
	l.append(p)
	l.append(i)
	db[n]=l

def delete(n):
	del db[n]

def showall(n):            # N=TOTAL NO. OF RECORDS
	print("S.NO.","\t","AUTHOR NAME","\t","BOOK NAME","\t","PRICE","\t","AVAILIBILTY")
	for i in range(1,n+1):
		print(i,"\t","\t",db[i][0],"\t","\t","\t",db[i][1],"\t","\t",db[i][2],"\t","\t",db[i][3])

def edit(n):             # N= N'TH RECORD (TO BE EDITED)
	rep3=None
	rep1=input("Which value do you want to edit?:")
	rep2=input("What do you want it to be replaced with?:")
	if rep1=="author_name":
		 rep3=0
	elif rep2=="book_name":
		 rep3=1
	elif rep2=="price":
		 rep3=2
	db[n][rep3]=rep2

def check_status(n):             # N= N'TH RECORD (TO BE CHECKED)
	k=db[n][3]
	if k=="yes":
		print("Book is availible")
	elif k=="no":
		print("Book is unavailible")


#INTERFACE
print("\t","\t","LIBRARY MANAGEMENT SYSTEM 101")
un=input("Username:")
pw=input("Password:")

while un=="user" and pw=="1991":
	print("\t","LIBRARY MANAGEMENT SYSTEM 101")
	print("~YOU CAN PERFORM THE FOLLOWING OPERATIONS~")
	print()
	print("\t","1.Add a record")
	print("\t","2.Delete a record")
	print("\t","3.Edit a record")
	print("\t","4.Issue a book")
	print("\t","5.Return a book")
	print("\t","6.Show all the records")
	print("\t","7.Check Availibilty")
	print("\t","8.Exit")
	print()

	c=int(input("Enter your choice:"))

	if c==1:
		n=int(input("Enter the Record No. to be Added:"))
		print(".......")
		print(add(n))
		print("SUCCESS!")

	elif c==2:
		n=int(input("Record No. to be Deleted:"))
		print("......")
		print(delete(n))
		print("SUCCESS!")

	elif c==3:
		n=int(input("Record No. to be Edited:"))
		print(edit(n))
		print("SUCCESS!")

	elif c==4:
		n=int(input("Record No. to be Issued:"))
		print("......")
		db[n][3]="no"
		print("SUCCESS!")


	elif c==5:
		n=int(input("Record No. to be Returned:"))
		print("......")
		db[n][3]="yes"
		print("SUCCESS!")

	elif c==6:
		n=int(input("Total no. of Records:"))
		print("......")
		print(showall(n))
		print("SUCCESS!")

	elif c==7:
		n=int(input("Record No. to be checked:"))
		print("......")
		print(check_status(n))
		print("SUCCESS!")

	elif c==8:
		print("Thank you for using LMS 101")
		break
	elif c==1991:
		print("You just discovered an easter egg!")
		print()
		print("A qoute by Linus Trovalds(creator of Linux)-")
		print("~A computer is like air conditioning, it is useless if you open Windows~")
		print()
		break

else:
	print()
	print("\t","Access Denied")
#DONE
