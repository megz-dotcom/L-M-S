#This LMS project store the data in database, this Project created a MySQL database with name "lms"
#This Database has 3 tables to store and retrieve the data about the LMS system,i.e. book, member, transaction
#MySql Connector : This module is used to connect mysql database to fetch/add data into database.
#DateTime : To set date and get current date and update the details on the tables.

import mysql.connector as a

from datetime import date 

def clear():
  for _ in range(1):
     print


# FIRST PAGE : REGISRE MENU TO ENTER TO THE MAIN MENU   
def register_menu():
    while True:

      print('\n====================== W E L L  C O M E =====================')
      print('\n===== L I B R E R Y   M A N A G E M E N T   S Y S T E M =====')
      print('\n===================== L O G I N   M E N U ===================')
      print("\nNote : If you are member of this application then choose Login if not choose Register option")
      print('\n1.  Login')
      print('\n2.  Register')     
      print('\n3.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
          login()
      if choice == 2:
          register()
      if choice == 3:
          break

#STAFF AUTHENTICATION MENU
#TO ADD MEMBER TO TABLE- STAFF :WE HAVE TO ADD STAFF'S BASIC DETAILS         
def register():
    #MYDB : FUNCTION TO CONNECT TO THE MYSQL SERVER
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )

    #MYCURSOR : COMMUNICATE WITH MYSQL DATABASE 
    mycursor=mydb.cursor()   
    print("\n\n===== R E G I S T E R   H E R E =====")
    print("\nNOTE : Staff use only")
    #EACH NON FORMAT ENTRY MAKE YOU TO CAME OUT OF LOOP AND EXIT FROM SYSTEM
    name=input("Enter your name: ")     
    stid=input("Enter your staff id(like-LMSXXX): ")    
    dob=input("Enter Date of Birth(yyyy-mm-dd): ")   
    address=input("Enter your address: ")    
    pno=input("Enter your phone number: ")  
    steid=input("Enter your email address: ")  
   # sql="create table staff(name varchar(40) not null, stid varchar(6) not null,dob date, address varchar(60), pno varchar(10), steid varchar(40),primary key(stid));"
    sql="Insert into staff values('{}','{}','{}','{}','{}','{}');".format(name,stid,dob,address,pno,steid)
    #EXICUTE THIS MODULE
    mycursor.execute(sql)

   #CALL METHOD TO SEND COMMIT STATEMENT TO MYSQL SERVER, COMMETTING THE CURRENT TRANSACTION
    mydb.commit()

    print("Member Added Successfully...:)\n\n")

    #CLOSE THE SQL-CONNECTION TO REUSE THE SAME CONNECTION FOR OTHER MODULES
    mydb.close()

# LOGIN : MEMBER ENTERS IF AND ONLY IF HIS/HER USERNAME AND PASSWORD MATCHES IN STAFF TABLE
# USER NAME=EMAIL ADDRESS OF MEMBER, PASSWORD=staff ID
def login():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )    
    mycursor=mydb.cursor()    
    print("\n\n===== L O G I N   H E R E =====")
    
    username=input("Enter your username: ")   
    password=input("Enter your password: ")   

    flag=0
    
    sql = "select * from staff"    
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(sql)
    #STORED FETCHED DATA
    records = mycursor.fetchall()    
    #Fetching each row using column name
    for row in records:       
        stid = row["stid"]
        steid = row["steid"]
  
        if username == steid and password == stid:
          print('Login Successful...:)\n')
          flag=1  
          break
        
    mydb.close()
    
    if flag==1:        
        main_menu()
    else:
        print("Invalid username and password...:(\n\n")
        #RETURN TO FIRST PAGE
        register_menu()
        

#START OF MAIN MENU
def main_menu():
    while True:
        print('\n====================== W E L L   C O M E ====================')
        print('\n===== L I B R E R Y   M A N A G E M E N T   S Y S T E M =====')
        print('\n====================== M A I N   M E N U ====================')
        print('\n\n1.  Add Member')  
        print('\n2.  Modify Member Information')     
        print('\n3.  Add Books')
        print('\n4.  Modify Book Informtion')  
        print('\n5.  Issue Book ')     
        print('\n6.  Return Book ')    
        print('\n7.  Search Menu')
        print('\n8.  Report Menu')
        print('\n9.  Delete Menu')
        print('\n0.  Exit From Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))

        if choice == 1:
            add_member()
        if choice == 2:
            modify_member() 
        if choice == 3:
            add_book()
        if choice == 4:
            modify_book()           
        if choice == 5:
            issue_book()
        if choice == 6:
            return_book()
        if choice == 7:
            search_menu()
        if choice == 8:
            report_menu()
        if choice == 9:            
            delete_menu()        
        if choice == 0:
            break


def add_member():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()
      
    print("\n\n===== R E G I S T E R   H E R E =====")
    name=input("Enter your name: ")     
    mid=input("Enter your member id: ")    
    dob=input("Enter Date of Birth(yyyy-mm-dd): ")   
    address=input("Enter your address: ")    
    pno=input("Enter your phone number: ")  
    eid=input("Enter your email address: ")  

   # sql="create table member(name varchar(40) not null, mid varchar(10) not null,dob date, address varchar(60), pno varchar(10), eid varchar(40),primary key(mid));"
    sql="Insert into member values('{}','{}','{}','{}','{}','{}');".format(name,mid,dob,address,pno,eid)
    mycursor.execute(sql)
    mydb.commit()
    print('\n\n')

    print("Member Added Successfully...:)\n\n")
    mydb.close()
  

#TO ADD BASIC BOOK DETAILS TO TABLE        
def add_book():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()
    
    print("\n\n========== A D D  B O O K   H E R E ==========")
    book_id = int(input('Enter Book ID : '))
    title = input('Enter Book Title : ')
    author = input('Enter Book Author : ')
    publisher = input('Enter Book Publisher : ')
    price = float(input('Enter Book Price : '))
    edition = int(input('Enter Book Edition : '))
    #sql="create table book(book_id int,title varchar(40),author varchar(40),publisher varchar(40),price float(6,2),edition int,status char(10),primary key(book_id));"    
    sql="Insert into book values({},'{}','{}','{}',{},{},'available')".format(book_id,title,author,publisher,price,edition)
    mycursor.execute(sql)
    mydb.commit()


    print('\n\n')
    print("\n\nNew Book Added Successfully...:)\n\n")  
    mydb.close()    
#end of add book

#MADIFY MEMEBER INFORMATION  
def modify_member():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )    
    mycursor=mydb.cursor()
    print('='*50)
    print('\n Modify Member Information Screen \n')
    print('='*50)
    print('\n1. Name')
    print('\n2. Date of Birth')
    print('\n3. address')
    print('\n4. Phone Number')
    print('\n5. Email Address')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'dob'
    if choice ==3:
        field ='address'
    if choice == 4:
        field = 'pno'
    if choice == 5:
        field = 'eid'
        
    #get new values to be change for particular member
    mem_id = input('Enter member ID : ')
    value = input('Enter new value : ')
    sql = 'update member set '+ field +' = "'+value+'" where mid = "'+mem_id+'";'    
    mycursor.execute(sql)
    mydb.commit()
    print('\n\n')
    print('Member details Updated Successfully...\n')
    mydb.close()
# end of modify member

# MODIFY BOOK DETAILS
def modify_book():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )    
    mycursor=mydb.cursor()
    print('='*50)
    print('\nModify BOOK Details Screen \n')
    print('='*50)
    print('\n1. Book ID')
    print('\n2. Book Title')
    print('\n3. Book Author')
    print('\n4. Book Publisher')    
    print('\n5. Book Price')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'book_id'
    if choice == 2:
        field = 'title'
    if choice == 3:
        field = 'author'
    if choice == 4:
        field = 'publisher'
    if choice == 5:
        field = 'price'

    bookid = input('Enter Book ID : ')
    value = input('Enter new value : ')    
    sql = 'update book set ' + field + ' = "'+value+'" where book_id = "'+bookid+'";'
    #print(sql)
    mycursor.execute(sql)
    mydb.commit()
    print('\n\n')
    print('\n\nBook details Updated Successfully...\n')
    mydb.close()
#end of modify_book

#get all details of particular book  
def book_status(b_id):
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()

    sql = 'select * from book where book_id ='+b_id+';'
    
    mycursor.execute(sql)
    result = mycursor.fetchone()
    return result

#get all details of particular member
def mem_status(m_id):
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()

    sql = 'select * from member where mid ="'+m_id+'";'

    
    mycursor.execute(sql)
    result = mycursor.fetchone()
    return result



#issue book to member
def issue_book():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()
    print('='*50)
    print("\n\n I S S U E   B O O K   H E R E\n ")
    print('='*50)
    m_id=input("Enter member Reg No: ")
    #check member details exist in database or not
    meminfo=mem_status(m_id)  
    print(meminfo)    
    title=input("Enter Title: ")    
    b_id=input("Enter Book ID: ")
    
    #check book details exist in database or not
    bookinfo=book_status(b_id)
    print(bookinfo)
    
    #SET DATE WITH CURRENT DATE
    today = date.today()
    wait = input('\n\n\nPress any key to continue.....')
    
    #sql="create table transaction(tid int NOT NULL AUTO_INCREMENT, title varchar(40) not null, m_id varchar(10) not null,b_id int, doi date,primary key(tid));"

    sql="Insert into transaction(title,m_id,b_id,doi) values('"+title+"','"+m_id+"',"+b_id+",'"+str(today)+"');" 
    mycursor.execute(sql)

    #change status of book
    sqlup="update book set status='issued' where book_id="+b_id+";"
    mycursor.execute(sqlup)
    mydb.commit()
    print("\n\n")

    print("Book issued successfully...:)\n\n")
    mydb.close()

#submit the book returned by member    
def return_book():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database=""
       )
    mycursor=mydb.cursor()
    print('='*50)
    print("\n R E T U R N   B O O K   H E R E \n")
    print('='*50)
    m_id=input("Enter member Reg No: ")
    meminfo=mem_status(m_id)
    print(meminfo)    
    title=input("Enter Title: ")
    
    b_id=input("Enter Book ID: ")
    bookinfo=book_status(b_id)
    print(bookinfo)    
    today = date.today()

    wait = input('\n\n\nPress any key to continue.....')
    
    sql="update transaction set dor='"+str(today)+"' where b_id="+b_id+";"
    mycursor.execute(sql)

    #UPDATE STATUS OF BOOK
    sqlup="update book set status='available' where book_id="+b_id+";"
    mycursor.execute(sqlup)
    mydb.commit()
    print("\n\n")

    print("Book returned successfully...:)\n\n")
    mydb.close()

#MENU TO SEARCH DESIRED BOOK 
def search_menu():
    while True:
      print('='*50)
      print('\n S E A R C H   M E N U \n')
      print('='*50)
      print("\n1.  Book Title")
      print('\n2.  Book Author')
      print('\n3.  Publisher')
      print('\n4.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field =''
      if choice == 1:
        field='title'
      if choice == 2:
        field = 'author'
      if choice == 3:
        field = 'publisher'
      if choice == 4:
        break
      search_book(field)

#RETRIVE SEARCHED BOOK DETAILS
def search_book(field):
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()
    print('='*50)
    print('\n BOOK SEARCH SCREEN \n')
    print('='*50)
    
    msg ='Enter '+ field +' Name : '
    title = input(msg)
    sql ='select * from book where '+ field + ' like "%'+ title+'%";'
    mycursor.execute(sql)
    records = mycursor.fetchall()
    print('\n\n')

    print('Search Result for :',field,' :' ,title)
    print('='*50)

    for record in records:
      print(record)
    mydb.close()
    
#REPORT MENU TO RETRIVE BRIEF member and book details
def report_menu():
    while True:
      print('='*50)
      print(' R E P O R T    M E N U ')
      print('='*50)      
      print("\n1.  Book List")
      print('\n2.  Member List')
      print('\n3.  Staff List')
      print('\n4.  Issued Books')
      print('\n5.  Available Books')     
      print('\n6.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        reprot_book_list()
      if choice == 2:
        report_member_list()
      if choice == 3:
        reprot_staff_list()
      if choice == 4:
        report_issued_books()
      if choice == 5:
        report_available_books()      
      if choice == 6:
        break
      
#RETRIVE ALL BOOKS DETAILS 
def reprot_book_list():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()
    print('='*50)
    print('\n REPORT - BOOK TITLES ')
    print('='*50)    
    sql ='select * from book;'
    mycursor.execute(sql)
    records = mycursor.fetchall()
    for record in records:
       print(record)
    mydb.close()
    
#RETRIVE ALL STAFF DETAILS 
def reprot_staff_list():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()
    print('='*50)
    print('\n REPORT - staff list ')
    print('='*50)    
    sql ='select * from staff;'
    mycursor.execute(sql)
    records = mycursor.fetchall()
    for record in records:
       print(record)
    mydb.close()

#RETRIVE ALL MEMBER DETAILS 
def report_member_list():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()
    print('='*50)
    print('\n REPORT - Members List ')
    print('='*50)
    sql = 'select * from member;'
    mycursor.execute(sql)
    records = mycursor.fetchall()

    for record in records:
       print(record)
    mydb.close()


#RETRIVE ALL ISSUED BOOKS
def report_issued_books():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()

    print('='*50)
    print('\n REPORT - BOOK TITLES - Issued')
    print('='*50)

    sql = 'select * from book where status = "issued";'
    mycursor.execute(sql)
    records = mycursor.fetchall()

    for record in records:
       print(record)
    mydb.close()



#RETRIVE ALL AVAILABLE BOOK
def report_available_books():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()

    print('='*50)
    print('\n REPORT - BOOK TITLES - Available')
    print('='*50)
    sql = 'select * from book where status = "available";'
    mycursor.execute(sql)
    records = mycursor.fetchall()

    for record in records:
       print(record)
    mydb.close()


#DELETE MEMBER FROM MEMBER TABLE
def del_mem():
    
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()
    
    mem_id=input("Enter member id to delete: ")    
    sqlt = "delete from transaction where m_id ='"+mem_id+"';"
    mycursor.execute(sqlt)
    sql = "delete from member where mid ='"+mem_id+"';"   
    mycursor.execute(sql)
    mydb.commit()
    print('\n\n')
    print("member deleted successfully")
    mydb.close()

    
#DELETE STAFF DETAILS FROM STAFF
def del_staff():
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()
    stf_id=input("Enter member id to delete: ")
    
    sql = "delete from staff where stid = '"+stf_id+"';"    
    mycursor.execute(sql)
    
    mydb.commit()
    print('\n\n')
    print("member deleted successfully")
    mydb.close()

#DELETE BOOK FROM MEMBER TABLE
def del_book():    
    mydb=a.connect(
       host="localhost",
       user="root",
       password="...",
       database="lms"
       )
    mycursor=mydb.cursor()

    bk_id=input("Enter book id to delete: ")
    #DELETE FROM REFERENCED TABLE    
    sqlt = "delete from transaction where b_id ='"+bk_id+"';"
    mycursor.execute(sqlt)
    #DELETE FROM MAIN TABLE
    sql = "delete from book where book_id ='"+bk_id+"';"   
    mycursor.execute(sql)
    mydb.commit()
    print('\n\n')
    print("book deleted successfully...")
    mydb.close()
    
def delete_menu():
    while True:        
      print('='*50)
      print('\n D E L E T E    M E N U \n')
      print('='*50)
      print("\n1.  Delete Member")
      print('\n2.  Delete Staff')
      print('\n3.  Delete Book')         
      print('\n4.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
          del_mem()        
      if choice == 2:
          del_staff()        
      if choice == 3:
          del_book()
      if choice == 4:        
        break

                   
            
#END OF MAIN MENU AND RELATED MODULES

#PATH TO START        
if __name__ == "__main__":
     register_menu()

