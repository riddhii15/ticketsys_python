

#Ticket booking system
from tkinter import *
import mysql.connector
from functools import partial
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="ticket")
cursor = db.cursor()
root = Tk()
frame=Frame(root,width=400,height=400,bg="azure2").pack()
root.configure(background="azure2")
root.title("Essel World")
def ins_dblogin(name,pas,con):
    query = "INSERT INTO login(name,contact,password) VALUES ('%s','%s','%s')"%(name,con,pas)
    cursor.execute(query)
    db.commit()
def insdb_empty(uid):
    query = "UPDATE usr_detail SET type='',gender='',rides='',weight='' WHERE (user_id='%s')"%(uid)
    cursor.execute(query)
    db.commit()
def insdb_type(uid):
    val = ew1.get()
    val2 = ew.get()
    query = "UPDATE usr_detail SET type='%s',gender='%s' WHERE (user_id='%s')"%(val,val2,uid)
    cursor.execute(query)
    db.commit()
def insdb_rides(uid):
    val = ew5.get()
    val2 = ew6.get()
    query = "UPDATE usr_detail SET rides='%s',weight='%s' WHERE (user_id='%s')"%(val,val2,uid)
    cursor.execute(query)
    db.commit()
#Function for submitting new user data
def submit_new():
    newus=Tk()
    newuswin=Frame(newus,width=200,height=200,bg="azure2").pack()
    newus.configure(background="azure2",width=400,height=400)
    global new_pas
    newus.title("Essel World")
    global new_name
    new_name=t1.get()
    global new_contact_no
    new_contact_no=t2.get()
    new_pas=t3.get()
    ins_dblogin(new_name,new_pas,new_contact_no)
    l8=Label(newus,text="Account created successfully...click the 'Next' button to continue",font=("Calibri",10),bg="azure2").place(x=20,y=20)
#Function for logging in after creating new user
def submit_and_continue():
    get_name=t1.get()
    get_pass=t3.get()
    query = "SELECT * FROM login WHERE ((name='%s') AND (password='%s'))"%(get_name,get_pass)
    cursor.execute(query)
    res = cursor.fetchone()
    if(res==None):
        l5["text"]="User Not Found"
    get_id=str(res[0])
    if res[3]==get_pass:
        root=Tk()
        root.destroy()
        rot=Tk()
        rot.configure(background="azure2",width=400,height=400)
        rot.title("Essel world")
        insdb_empty(get_id)

        def de(tod):
            tod.destroy()
           
        def cus():
            cu=Toplevel()
            cu.title("Customers")
            cu.configure(background="azure2",width=400,height=400)
            am = Label(cu,text="Your ticket details are as follows:",font=("Britannic Bold",18),bg="azure2").place(x=30,y=20)
            query = "SELECT * FROM usr_detail WHERE user_id='%s'"%(get_id)
            cursor.execute(query)
            cures = cursor.fetchone()
            cs = Label(cu,text="User Id: "+str(cures[0]),font=("Calibri",12),bg="azure2").place(x=60,y=70)
            cs1 = Label(cu,text="Gender: "+str(cures[1]),font=("Calibri",12),bg="azure2").place(x=60,y=90)
            cs2 = Label(cu,text="Type of Ticket: "+str(cures[2]),font=("Calibri",12),bg="azure2").place(x=60,y=110)
            cs3 = Label(cu,text="Selected Rides: "+str(cures[3]),font=("Calibri",12),bg="azure2").place(x=60,y=130)
            cs4 = Label(cu,text="Weight: "+str(cures[4]),font=("Calibri",12),bg="azure2").place(x=60,y=150)

        def resl():
            re=Toplevel()
            re.title("Reservation")
            re.configure(background="azure2",width=400,height=400)
            ls = Label(re, text="Select One Type:",font=("Britannic Bold",18),bg="azure2").place(x=30,y=20)
            ls2 = Label(re, text="1) Normal",font=("Calibri",12),bg="azure2").place(x=50, y=70)
            ls3 = Label(re, text="2) VIP",font=("Calibri",12),bg="azure2").place(x=50, y=90)
            ls4 = Label(re, text="3) Student",font=("Calibri",12),bg="azure2").place(x=50, y=110)
            ls5 = Label(re,text="Enter Type here:",font=("Calibri",12),bg="azure2").place(x=50, y=130)
            global ew1
            ew1 = Entry(re)
            ew1.place(x=50,y=160)
            lo = Label(re, text="Enter your Gender (M/F/Others):",font=("Calibri",12),bg="azure2").place(x=50, y=180)
            global ew 
            ew = Entry(re)
            ew.place(x=50, y=210)
            b1=Button(re,text="  Submit  ",command=lambda:insdb_type(get_id)).place(x=145,y=245)

        def ri():
            ride=Toplevel()
            ride.title("Rides")
            ride.configure(background="azure2",width=400,height=400)
            la = Label(ride, text="Select the rides which you want",font=("Britannic Bold",18),bg="azure2").place(x=30,y=20)
            lr1 = Label(ride, text="1) Boomerang",font=("Calibri",12),bg="azure2").place(x=50,y=70)
            lr2 = Label(ride, text="2) Floats",font=("Calibri",12),bg="azure2").place(x=50,y=90)
            lr3 = Label(ride, text="3) Loopy Woopy",font=("Calibri",12),bg="azure2").place(x=50,y=110)
            lr4 = Label(ride, text="4) Splash",font=("Calibri",12),bg="azure2").place(x=50,y=130)
            lr5 = Label(ride, text="Enter your rides:",font=("Calibri",12),bg="azure2").place(x=50,y=150)
            global ew5
            ew5 = Entry(ride)
            ew5.place(x=50,y=180)
            lo = Label(ride, text="Enter your weight:",font=("Calibri",12),bg="azure2").place(x=50, y=200)
            global ew6
            ew6 = Entry(ride)
            ew6.place(x=50, y=220)
            bri=Button(ride,text="  Submit  ",command=lambda:insdb_rides(get_id)).place(x=120,y=260)

        ls1 = Label(rot, text="Welcome to Essel World!!",font=("Britannic Bold",20),fg="orange",bg="azure2").place(x=40,y=20)
        std= "Name:-" + get_name + " ID:-" + get_id
        ls2=Label(rot,font=("Arial Bold",10),bg="azure2")
        ls2["text"]=std
        ls2.place(x=100,y=50)
        ls3 = Label(rot, text="Select an option:",font=("Britannic Bold",12),bg="azure2").place(x=110,y=90)
        bs1=Button(rot,text="  Your Ticket  ",command=cus).place(x=70,y=130)
        bs2=Button(rot,text="  Reservation  ",command=resl).place(x=200,y=130)
        bs3=Button(rot,text="       Rides      ",command=ri).place(x=140,y=180)
        bs5=Button(rot,text="     Exit     ",command=lambda:de(rot)).place(x=145,y=245)
    else:
        l5["text"]="Wrong Password or Incorrect user"
#Function for logging in for existing user
def sub():
    get_name=te1.get()
    get_pass=te2.get()
    query = "SELECT * FROM login WHERE ((name='%s') AND (password='%s'))"%(get_name,get_pass)
    cursor.execute(query)
    res = cursor.fetchone()
    if(res==None):
        l5["text"]="User Not Found"
    get_id=str(res[0])
    if res[3]==get_pass:
        insdb_empty(get_id)
        rot=Tk()
        rot.configure(background="azure2",width=400,height=400)
        rot.title("Essel world")
        insdb_empty(get_id)
        def de(tod):
            tod.destroy()
        def cus(): #Prints ticket
            cu=Toplevel()
            cu.title("Customers")
            cu.configure(background="azure2",width=400,height=400)
            am = Label(cu,text="Your ticket details are as follows:",font=("Britannic Bold",18),bg="azure2").place(x=30,y=20)
            query = "SELECT * FROM usr_detail WHERE user_id='%s'"%(get_id)
            cursor.execute(query)
            cures = cursor.fetchone()
            cs = Label(cu,text="User Id: "+str(cures[0]),font=("Calibri",12),bg="azure2").place(x=60,y=70)
            cs1 = Label(cu,text="Gender: "+str(cures[1]),font=("Calibri",12),bg="azure2").place(x=60,y=90)
            cs2 = Label(cu,text="Type of Ticket: "+str(cures[2]),font=("Calibri",12),bg="azure2").place(x=60,y=110)
            cs3 = Label(cu,text="Selected Rides: "+str(cures[3]),font=("Calibri",12),bg="azure2").place(x=60,y=130)
            cs4 = Label(cu,text="Weight: "+str(cures[4]),font=("Calibri",12),bg="azure2").place(x=60,y=150)
        def resl(): #Type Function
            re=Toplevel()
            re.title("Reservation")
            re.configure(background="azure2",width=400,height=400)
            ls = Label(re, text="Select One Type:",font=("Britannic Bold",18),bg="azure2").place(x=30,y=20)
            ls2 = Label(re, text="1) Normal",font=("Calibri",12),bg="azure2").place(x=50, y=70)
            ls3 = Label(re, text="2) VIP",font=("Calibri",12),bg="azure2").place(x=50, y=90)
            ls4 = Label(re, text="3) Student",font=("Calibri",12),bg="azure2").place(x=50, y=110)
            ls5 = Label(re,text="Enter Type here:",font=("Calibri",12),bg="azure2").place(x=50, y=130)
            global ew1
            ew1 = Entry(re)
            ew1.place(x=50,y=160)
            lo = Label(re, text="Enter your Gender (M/F/Others):",font=("Calibri",12),bg="azure2").place(x=50, y=180)
            global ew 
            ew = Entry(re)
            ew.place(x=50, y=210)
            b1=Button(re,text="  Submit  ",command=lambda:insdb_type(get_id)).place(x=145,y=245)
        def ri():
            ride=Toplevel()
            ride.title("Rides")
            ride.configure(background="azure2",width=400,height=400)
            la = Label(ride, text="Select the rides which you want",font=("Britannic Bold",18),bg="azure2").place(x=30,y=20)
            lr1 = Label(ride, text="1) Boomerang",font=("Calibri",12),bg="azure2").place(x=50,y=70)
            lr2 = Label(ride, text="2) Floats",font=("Calibri",12),bg="azure2").place(x=50,y=90)
            lr3 = Label(ride, text="3) Loopy Woopy",font=("Calibri",12),bg="azure2").place(x=50,y=110)
            lr4 = Label(ride, text="4) Splash",font=("Calibri",12),bg="azure2").place(x=50,y=130)
            lr5 = Label(ride, text="Enter your rides:",font=("Calibri",12),bg="azure2").place(x=50,y=150)
            global ew5
            ew5 = Entry(ride)
            ew5.place(x=50,y=180)
            lo = Label(ride, text="Enter your weight:",font=("Calibri",12),bg="azure2").place(x=50, y=200)
            global ew6
            ew6 = Entry(ride)
            ew6.place(x=50, y=220)
            bri=Button(ride,text="  Submit  ",command=lambda:insdb_rides(get_id)).place(x=120,y=260)
        ls1 = Label(rot, text="Welcome to Essel World!!",font=("Britannic Bold",20),fg="orange",bg="azure2").place(x=40,y=20)
        std= "Name:-" + get_name + " ID:-" + get_id
        ls2=Label(rot,font=("Arial Bold",10),bg="azure2")
        ls2["text"]=std
        ls2.place(x=100,y=50)
        ls3 = Label(rot, text="Select an option:",font=("Britannic Bold",12),bg="azure2").place(x=110,y=90)
        bs1=Button(rot,text="  Your Ticket  ",command=cus).place(x=70,y=130)
        bs2=Button(rot,text="  Reservation  ",command=resl).place(x=200,y=130)
        bs3=Button(rot,text="       Rides      ",command=ri).place(x=140,y=180)
        bs5=Button(rot,text="     Exit     ",command=lambda:de(rot)).place(x=145,y=245)
    else:
        lsu["text"]="Wrong Password or Incorrect User"
#Creation page for new user
def new_user():
    root.destroy()
    newus = Tk()
    newuswin=Frame(newus,width=400,height=400,bg="azure2").pack()
    newus.configure(background="azure2",width=400,height=400)
    newus.title("Essel World")
    #background_label=Label(newus,image="C:\\Users\\vinu4\\Desktop\\Misc2\\GUI\\rsz_esselworld.gif").place(x=0,y=0,relwidth=1,relheight=1)
    l3=Label(newuswin,text="Welcome to New Account Creation",font=("Eras Demi ITC",14),bg="azure2").place(x=48,y=30)
    l4=Label(newuswin,text="Name:",font=("Calibri",12),bg="azure2").place(x=70,y=70)
    global t1
    t1=Entry(newuswin)
    t1.place(x=150,y=74)
    l5=Label(newuswin,text="Contact No:",font=("Calibri",12),bg="azure2").place(x=70,y=100)
    global t2
    t2=Entry(newuswin)
    t2.place(x=150,y=104)
    l6=Label(newuswin,text="Password:",font=("Calibri",12),bg="azure2").place(x=70,y=130)
    global t3
    t3=Entry(newuswin,show="*")
    t3.place(x=150,y=134)
    b1=Button(newuswin,text="Submit",font=("Calibri",12),command=submit_new).place(x=140,y=220)
    b2=Button(newuswin,text="Next",font=("Calibri",12),command=submit_and_continue).place(x=200,y=220)
#Login Page for Existing User
def exist_user():
    root.destroy()
    exus = Tk()
    exus.configure(background="azure2",width=400,height=400)
    exus.title("Essel World")
    le1=Label(exus,text="Welcome to the Login Page",font=("Eras Demi ITC",14),bg="azure2").place(x=85,y=30)
    le2=Label(exus,text="Name:",font=("Calibri",12),bg="azure2").place(x=70,y=70)
    global te1
    te1=Entry(exus)
    te1.place(x=145,y=74)
    le3=Label(exus,text="Password:",font=("Calibri",12),bg="azure2").place(x=70,y=100)
    global te2
    te2=Entry(exus,show="*")
    te2.place(x=145,y=104)
    be1=Button(exus,text="Submit",font=("Calibri",12),command=sub).place(x=123,y=220)
    be2=Button(exus,text="Exit",font=("Calibri",12),command=lambda:exus.destroy()).place(x=182,y=220)
#Main page/First Page
l1=Label(frame,text="Welcome to the Main Page",font=("Eras Demi ITC",14),bg="azure2")
l1.place(x=78,y=30)
l2=Label(frame,text="Select your Option:",font=("Eras Demi ITC",14),bg="azure2")
l2.place(x=110,y=80)
mb1=Button(frame,text="New User",font=("Calibri",12),command=new_user).place(x=104,y=140)
mb2=Button(frame,text="Existing User",font=("Calibri",12),command=exist_user).place(x=182,y=140)
root.mainloop()