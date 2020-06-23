
import tkinter as tk
import datetime
admin={"sathya":"sathya","tarun":"tarun",'admin':'admin'}
supervis={"sathya1":"sathya1","tarun1":"tarun1",'supervis':'supervis'}
standard={"sathya2":"sathya2","tarun2":"tarun2",'standard':'standard'}
scheduled={'MH370':["10:10",'Delhi',"Delayed"],'KI784':['1:20','Pune','Delayed'],'PH169':['12:20','Seattle','Scheduled'],'BH234':['15:20','Bangalore','Scheduled'],'PH234':['15:00','Prayagraj','Delayed'],'BT452':['18:30','Malaysia','Scheduled'],'KR234':['15:20','Cuba','Scheduled']}
cancelled={'AI169':["11:30","Bombay","Cancelled"]}
def reminder():    #This is the reminder function, takes current time from the system and compares it to the list of flights, if the time is greater it creates a pop up with the flight number
    now=datetime.datetime.now()    
    for i in scheduled:
        l=scheduled[i][0].split(":")
        time=now.replace(hour=int(l[0]),minute=int(l[1]),second=0,microsecond=0)        
        if now>time:
            remindersc=tk.Tk()
            remindersc.title("Reminder!")
            tk.Label(master=remindersc,text="Flight Number "+i+" Not Updated").grid(row=0,column=0)
            remindersc.mainloop()
            
def deluser(): #This function is responsible for deleting users
    def deluserback():
        u=uname.get()        
        if not(u in admin or u in supervis or u in cancelled):
            popup=tk.Tk()
            popup.title("Username Not Found!")
            tk.Label(master=popup,text="Username not found! Please try again!").grid(row=1,column=1)
            
        else:
            if uname.get()=='admin':
                    re=tk.Tk()
                    re.title("Can't Delete Superuser!")
                    tk.Label(master=re,text="Cannot Delete Superuser!").grid(row=1,column=1)
                    re.mainloop()
            elif u in admin:
                if u!='admin':
                    del admin[u]
                    r1=tk.Tk()
                    r1.title("Success!")
                    tk.Label(master=r1,text="Admin User Successfully Deleted!").grid(row=1,column=1)
                    
            elif u in supervis:
                del supervis[u]
                r1=tk.Tk()
                r1.title("Success!")
                tk.Label(master=r1,text=" Supervisor Successfully Deleted!").grid(row=1,column=1)
            if u in standard:
                del standard[u]
                r1=tk.Tk()
                r1.title("Success!")
                tk.Label(master=r1,text="Standard User Successfully Deleted!").grid(row=1,column=1)                
    delusersc=tk.Tk()
    delusersc.title("Delete A User")
    tk.Label(master=delusersc,text="Enter the Username").grid(row=1,column=0)
    uname=tk.Entry(master=delusersc)
    unamne.grid(row=1,column=1)
    r2=tk.Button(master=delusersc,text="Confirm Deletion",width=25,command=deluserback).grid(row=1,column=2)
    
def manageuser():#this function is responsible for adding users
    def adduser():
        def addadmin():
            def adminusname():
                def adminuserback():
                    p=passw.get()                                                             
                    admin[u]=p
                    popup=tk.Tk()
                    popup.title("Success")
                    tk.Label(master=popup,text="Admin Successfully Added!").grid(row=1,column=1)
                u=usname.get()
                if u in admin or u in supervis or u in standard:
                        popup=tk.Tk()
                        popup.title("Username Already Exists!")
                        tk.Label(master=popup,text="Username Already Exists! Please Try Again").grid(row=1,column=1)
                        manageusersc.destroy()
                        aa.destroy()
                else:        
                    tk.Label(master=aa,text="Enter the Password").grid(row=2,column=0)
                    passw=tk.Entry(master=aa,show='*')
                    passw.grid(row=2,column=1)
                    tk.Button(master=aa,text="Confirm Password",command=adminuserback,width=25).grid(row=2,column=3)
            aa=tk.Tk()
            aa.title("Add An Admin")
            tk.Label(master=aa,text="Enter the Username").grid(row=1,column=0)
            usname=tk.Entry(master=aa)
            usname.grid(row=1,column=1)
            a3=tk.Button(master=aa,text="Confirm Username",width=25,command=adminusname).grid(row=1,column=3)
        def addsuper():
            def superusname():
                def superuserback():
                    p=passw.get()                                                             
                    supervis[u]=p
                    popup=tk.Tk()
                    popup.title("Success")
                    tk.Label(master=popup,text="Supervisor Successfully Added!").grid(row=1,column=1)
                u=usname.get()
                if u in admin or u in supervis or u in standard:
                        popup=tk.Tk()
                        popup.title("Username Already Exists!")
                        tk.Label(master=popup,text="Username Already Exists! Please Try Again").grid(row=1,column=1)
                        manageusersc.destroy()
                        aa.destroy()
                else:        
                    tk.Label(master=aa,text="Enter the Password").grid(row=2,column=0)
                    passw=tk.Entry(master=aa,show='*')
                    passw.grid(row=2,column=1)
                    tk.Button(master=aa,text="Confirm Password",command=superuserback,width=25).grid(row=2,column=3)
            aa=tk.Tk()
            aa.title("Add A Supervisor")
            tk.Label(master=aa,text="Enter the Username").grid(row=1,column=0)
            usname=tk.Entry(master=aa)
            usname.grid(row=1,column=1)
            a3=tk.Button(master=aa,text="Confirm Username",width=25,command=superusname).grid(row=1,column=3)
        def addstand():
            def standusname():
                def standuserback():
                    p=passw.get()                                                             
                    standard[u]=p                    
                    popup=tk.Tk()
                    popup.title("Success")
                    tk.Label(master=popup,text="Standard User Successfully Added!").grid(row=1,column=1)
                u=usname.get()
                if u in admin or u in supervis or u in standard:
                        popup=tk.Tk()
                        popup.title("Username Already Exists!")
                        tk.Label(master=popup,text="Username Already Exists! Please Try Again").grid(row=1,column=1)
                        
                        aa.destroy()
                else:        
                    tk.Label(master=aa,text="Enter the Password").grid(row=2,column=0)
                    passw=tk.Entry(master=aa,show='*')
                    passw.grid(row=2,column=1)
                    tk.Button(master=aa,text="Confirm Password",command=standuserback,width=25).grid(row=2,column=3)
            aa=tk.Tk()
            aa.title("Add A Standard User")
            tk.Label(master=aa,text="Enter the Username").grid(row=1,column=0)
            usname=tk.Entry(master=aa)
            usname.grid(row=1,column=1)
            a3=tk.Button(master=aa,text="Confirm Username",width=25,command=standusname).grid(row=1,column=3)
        addusersc=tk.Tk()
        addusersc.title("Add A User")
        tk.Button(master=addusersc,width=25,text="Add An Admin",command=addadmin).grid(row=1,column=1)
        tk.Button(master=addusersc,width=25,text="Add A Supervisor",command=addsuper).grid(row=2,column=1)
        tk.Button(master=addusersc,width=25,text="Add A Standard User",command=addstand).grid(row=3,column=1)
    def viewuser():
        viewsc=tk.Tk()
        viewsc.title("View Users")
        tk.Label(master=viewsc,text="Admins Are:").grid(row=0,column=0)
        c=0
        for i in admin:
            c+=1
            tk.Label(master=viewsc,text=("------",i)).grid(row=c,column=0)
        c+=1
        tk.Label(master=viewsc,text="Supervisors Are:").grid(row=c,column=0)        
        for i in supervis:
            c+=1
            tk.Label(master=viewsc,text=("-----",i)).grid(row=c,column=0)
        c+=1
        tk.Label(master=viewsc,text="Standard Users Are:").grid(row=c,column=0)        
        for i in standard:
            c+=1
            tk.Label(master=viewsc,text=("-----",i)).grid(row=c,column=0)
    def deluser():
        def deluserback():
            u=uname.get()
            if not(u in admin or u in supervis or u in standard):
                popup=tk.Tk()
                popup.title("Username Not Found!")
                tk.Label(master=popup,text="Username not found! Please try again!").grid(row=1,column=1)
            else:
                if u in admin:
                    del admin[u]
                    r1=tk.Tk()
                    r1.title("Success!")
                    tk.Label(master=r1,text="Admin User Successfully Deleted!").grid(row=1,column=1)
                    delusersc.destroy()
                elif u in supervis:
                    del supervis[u]
                    r1=tk.Tk()
                    r1.title("Success!")
                    tk.Label(master=r1,text=" Supervisor Successfully Deleted!").grid(row=1,column=1)
                    delusersc.destroy()
                if u in standard:
                    del standard[u]
                    r1=tk.Tk()
                    r1.title("Success!")
                    tk.Label(master=r1,text="Standard User Successfully Deleted!").grid(row=1,column=1)
                    delusersc.destroy()
        delusersc=tk.Tk()
        delusersc.title("Delete A User")
        tk.Label(master=delusersc,text="Enter the Username").grid(row=1,column=0)
        uname=tk.Entry(master=delusersc)
        uname.grid(row=1,column=1)
        r2=tk.Button(master=delusersc,text="Confirm Deletion",width=25,command=deluserback).grid(row=1,column=2)                
    manageusersc=tk.Tk()
    manageusersc.title("Manage Users")
    tk.Button(master=manageusersc,text="Add Users",width=25,command=adduser).grid(row=1,column=0)
    tk.Button(master=manageusersc,text="Delete A User",width=25,command=deluser).grid(row=2,column=0)
    tk.Button(master=manageusersc,text="View Current Users",width=25,command=viewuser).grid(row=3,column=0)

def update():
    updatesc=tk.Tk()     
    updatesc.title("Update/Add A Flight")    
    tk.Label(master=updatesc,text="Enter The Flight Number").grid(row=1,column=0)
    flightnum=tk.Entry(master=updatesc)
    flightnum.grid(row=1,column=1)   
    def updatebutton1():
        if flightnum.get() not in scheduled:
            scheduled[flightnum.get()]=["","",""]
        tk.Label(master=updatesc,text="Enter Departure Time").grid(row=3,column=0)
        deptime=tk.Entry(master=updatesc)
        deptime.grid(row=3,column=1)
        tk.Label(master=updatesc,text="Enter Status").grid(row=4,column=0)
        status=tk.Entry(master=updatesc)
        status.grid(row=4,column=1)
        tk.Label(master=updatesc,text="Enter Destination").grid(row=5,column=0)
        dest=tk.Entry(master=updatesc)
        dest.grid(row=5,column=1)
        def updatebutton2():       
            if deptime.get()!="":
                scheduled[flightnum.get()][0]=deptime.get()
            if status.get()!="":
                scheduled[flightnum.get()][2]=status.get()
            if dest.get()!="":
                scheduled[flightnum.get()][1]=dest.get()
            updatepopup=tk.Tk()
            updatepopup.title("Successfully Updated!")
            tk.Label(master=updatepopup,text="Successfully Updated!!").grid(row=0,column=0)
            updatesc.destroy()           
        tk.Button(master=updatesc,text="Confirm",command=updatebutton2).grid(row=6,column=1)   
    tk.Button(master=updatesc,text="Confirm",command=updatebutton1).grid(row=2,column=1)
    updatesc.mainloop()

def cancel(): #this function cancels flights
    def cancelback():
        t=flightnum.get()
        cancelsc.destroy()        
        if t in cancelled:
            re=tk.Tk()
            re.title("Already Cancelled!")
            tk.Label(master=re,text="Flight Already Cancelled. Please try again!").grid(row=1,column=1)
            cancel()
        elif not(t in scheduled):
            re=tk.Tk()
            re.title("Flight Not Found!")
            tk.Label(master=re,text="Flight Not Found. Please try again!").grid(row=1,column=1)
            cancel()
        else:
            t1=scheduled.pop(t)
            del t1[2]
            t1.append("Cancelled")
            cancelled[t]=t1
            re=tk.Tk()
            re.title("Success!")
            tk.Label(master=re,text="Flight Successfully Cancelled!").grid(row=1,column=1)           
    cancelsc=tk.Tk()
    cancelsc.title("Cancel a Flight")
    tk.Label(master=cancelsc,text="Enter the flight number").grid(row=1,column=0)
    flightnum=tk.Entry(master=cancelsc)
    flightnum.grid(row=1,column=1)
    t7=tk.Button(master=cancelsc,width=25,text="Confirm",command=cancelback).grid(row=2,column=1)
    
def admain():#admin control panel
    def switchuserad():
        admainsc.destroy()
        login()
    admainsc=tk.Tk()
    admainsc.title("Admin Control Panel")    
    tk.Button(master=admainsc,text="View The Details Of Flights",command=view).grid(row=1,column=1)
    tk.Button(master=admainsc,text="Switch User",command=switchuserad).grid(row=2,column=1)
    tk.Button(master=admainsc,text="Cancel A Flight",command=cancel).grid(row=4,column=1)
    tk.Button(master=admainsc,text="Manage Users",command=manageuser).grid(row=5,column=1)
    tk.Button(master=admainsc,text="Exit The Program",command=exit).grid(row=6,column=1)
    tk.Button(master=admainsc,text="Update/Add A Flight",command=update).grid(row=3,column=1)
    
def supmain():#supervisor control panel
    def switchusersup():
        supmainsc.destroy()
        login()
    supmainsc=tk.Tk()
    img=tk.PhotoImage(file="ActualLogo.png")
    rp=tk.Label(master=supmainsc,image=img).grid(row=0,column=0)
    supmainsc.title("Supervisor Control Panel")
    tk.Label(master=supmainsc,text="").grid(row=6,column=0)    
    tk.Button(master=supmainsc,text="View The Details Of Flights",command=view).grid(row=1,column=1)
    tk.Button(master=supmainsc,text="Switch User",command=switchusersup).grid(row=2,column=1)
    tk.Button(master=supmainsc,text="Cancel A Flight",command=cancel).grid(row=4,column=1)
    tk.Button(master=supmainsc,text="Exit The Program",command=exit).grid(row=5,column=1)
    tk.Button(master=supmainsc,text="Update/Add A Flight",command=update).grid(row=3,column=1)
    supmainsc.mainloop()
    
def view():#viewing flights
    c=0
    r=1
    view=tk.Tk()
    view.title("View Details Of Flights")
    tk.Label(master=view,text="Flight Number--------ETA--------Destination-------Status").grid(row=1,column=0)
    for i in scheduled:
        c+=1
        r+=1
        tk.Label(master=view,text=(i,"-------",scheduled[i][0],"--------",scheduled[i][1],"--------",scheduled[i][2])).grid(row=r,column=0)
    for i in cancelled:
        c+=1
        r+=1
        tk.Label(master=view,text=(i,"-------",cancelled[i][0],"--------",cancelled[i][1],"--------",cancelled[i][2])).grid(row=r,column=0)
        
def stamain():#standard user control panel
    def switchuserstand():
        stamainsc.destroy()
        login()
    stamainsc=tk.Tk()
    stamainsc.title("Standard User Control Panel")
    tk.Button(master=stamainsc,text="View The Details Of Flights",command=view).grid(row=2,column=0)
    tk.Button(master=stamainsc,text="Switch User",command=switchuserstand).grid(row=3,column=0)
    tk.Button(master=stamainsc,text="Exit The Program",command=exit).grid(row=4,column=0)
    tk.Label(master=stamainsc,text="").grid(row=5,column=0)
    img=tk.PhotoImage(file="ActualLogo.png")
    rp=tk.Label(master=stamainsc,image=img).grid(row=1,column=0)   
    stamainsc.mainloop()        
def login():#login function
    def userver():        
        def passver():
            b=password.get()
            if check==1:
                if admin[a]==b:                    
                    loginsc.destroy()                    
                    admain()
                    reminder()
                else:
                    a3=tk.Tk()
                    a3.title("Wrong Password!")
                    tk.Label(master=a3,text="Wrong Password! Please Try Again!").grid(row=1,column=1)          
                    
            elif check==2:
                if supervis[a]==b:
                    loginsc.destroy()                                        
                    supmain()
                    reminder()
                else:
                    a3=tk.Tk()
                    a3.title("Wrong Password!")
                    tk.Label(master=a3,text="Wrong Password! Please Try Again!").grid(row=1,column=1)
            elif check==3:
                if standard[a]==b:
                    loginsc.destroy()
                    stamain()
                    
                else:
                    a3=tk.Tk()
                    a3.title("Wrong Password!")
                    tk.Label(master=a3,text="Wrong Password! Please Try Again!").grid(row=1,column=1)
        a=username.get()
        
        if not(a in admin or a in supervis or a in standard):
            a1=tk.Tk()
            a1.title("Wrong Username!")
            tk.Label(master=a1,text="Username Not Found. Please Try Again!").grid(row=1,column=1)       
        else:           
            if a in supervis:
                check=2
            elif a in admin:
                check=1
            elif a in standard:
                check=3            
                
            tk.Label(master=loginsc,text="Enter Your Password").grid(row=2,column=0)
            password=tk.Entry(master=loginsc,show='*')            
            password.grid(row=2,column=1)
            a3=tk.Button(master=loginsc,text="Confirm Password",width=25,command=passver).grid(row=2,column=2)   
    loginsc=tk.Tk()
    loginsc.title("Login")
    tk.Label(master=loginsc,text="").grid(row=5,column=1)
    img=tk.PhotoImage(file="download.png")
    rp=tk.Label(master=loginsc,image=img).grid(row=0,column=1)
    tk.Label(master=loginsc,text="Enter Your Username").grid(row=1,column=0)
    username=tk.Entry(master=loginsc)
    username.grid(row=1,column=1)
    a22=tk.Button(master=loginsc,text="Confirm Username",width=25,command=userver).grid(row=1,column=2)
    loginsc.mainloop()
login()



