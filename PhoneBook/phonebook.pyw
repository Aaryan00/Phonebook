from Tkinter import *
from tkMessageBox import *
from datetime import datetime
import sqlite3
import re

con=sqlite3.Connection("Phone_Record")
cur=con.cursor()
cur.execute("create table if not exists record(id INTEGER PRIMARY KEY ,f_name VARCHAR(50),m_name VARCHAR(50),l_name VARCHAR(50),c_name VARCHAR(50),add_n VARCHAR(50),city VARCHAR(20),pincode VARCHAR(20) ,web VARCHAR(100),birth DATE,p_no VARCHAR(20),email VARCHAR(40),type1 VARCHAR(20),type2 VARCHAR(10))")
first=Tk()
first.geometry("800x600")
first.config(bg="light yellow")
Label(first,text="Project Title : PhoneBook",font='times 20 bold ',bg="light yellow").grid(stick=NW,row=0,column=0,columnspan=3)
Label(first,text="Project of Python and Database",font='times 20 bold ',bg="light yellow").grid(row=1,column=4)
Label(first,text="Developed By: Aryan Agrawal",font="times 17 bold",fg="blue",bg="light yellow").grid(row=2,column=4)
Label(first,text="         Enrollment no: 181B050",font="times 17 bold",fg="blue",bg="light yellow").grid(row=3,column=4)
Label(first,text="         Batch: B2",font="times 17 bold",fg="blue",bg="light yellow").grid(row=4,column=4)
Label(first,text=" Under Guidance of Dr. Mahesh Kumar",font="times 18 bold",fg='green',bg='Light yellow').grid(row=5,column=3,columnspan=2)
Label(first,text="Move the mouse over the screen to move on the project",font="times 13 bold",fg="red",bg="light yellow").grid(row=6,column=4)
    
def close(e=1):
    first.destroy()
    main=Tk()
    main.geometry("500x590")
    main.title("Phonebook")
    photo=PhotoImage(file='phone.gif')
    photo=photo.subsample(7,7)
    a=StringVar()
    b=StringVar()
    c=StringVar()
    d=StringVar()
    e=StringVar()
    f=StringVar()
    g=StringVar()
    h=StringVar()
    i=StringVar()
    j=IntVar()
    k=StringVar()
    l=IntVar()
    m=StringVar()
    Label(main,image=photo).grid(row=0,column=2)
    Label(main,text="Phone Book",font="times 17 bold underline",fg="blue").grid(row=3,column=2)
    Label(main,text="First Name",font="times 13").grid(row=4,column=1)
    a=Entry(main,bd=3)
    a.grid(row=4,column=2)
    Label(main,text="Middle Name",font="times 13").grid(row=5,column=1)
    b=Entry(main,bd=3)
    b.grid(row=5,column=2)
    Label(main,text="Last Name",font="times 13").grid(row=6,column=1)
    c=Entry(main,bd=3)
    c.grid(row=6,column=2)
    Label(main,text="Company Name",font="times 13").grid(row=7,column=1)
    d=Entry(main,bd=3)
    d.grid(row=7,column=2)
    Label(main,text="Address",font="times 13").grid(row=8,column=1)
    e=Entry(main,bd=3)
    e.grid(row=8,column=2)
    Label(main,text="City",font="times 13").grid(row=9,column=1)
    f=Entry(main,bd=3)
    f.grid(row=9,column=2)
    Label(main,text="Pin Code",font="times 13").grid(row=10,column=1)
    g=Entry(main,bd=3)
    g.grid(row=10,column=2)
    Label(main,text="Website URL",font="times 13").grid(row=11,column=1)
    h=Entry(main,bd=3)
    h.grid(row=11,column=2)
    Label(main,text="Date of Birth",font="times 13").grid(row=12,column=1)
    i=Entry(main,bd=3)
    i.grid(row=12,column=2)
    Label(main,text='DD-MM-YYYY').grid(row=12,column=3)
    Label(main,text="Select Phone Type : ",font="times 15",fg='blue').grid(row=13,column=1)
    r1=Radiobutton(main,text="office",variable=j,value=0)
    r1.grid(row=13,column=2)
    r1.select()
    r2=Radiobutton(main,text="home",variable=j,value=1).grid(row=13,column=3)
    r3=Radiobutton(main,text="mobile",variable=j,value=2).grid(row=13,column=4)    
    Label(main,text="Phone Number",font="times 13").grid(row=14,column=1)
    k=Entry(main,bd=3)
    k.grid(row=14,column=2)
    Label(main,text="Select Email Type : ",font="times 15",fg="blue").grid(row=15,column=1)    
    r4=Radiobutton(main,text="office",variable=l,value=0)
    r4.grid(row=15,column=2)
    r4.select()
    r5=Radiobutton(main,text="personal",variable=l,value=1).grid(row=15,column=3)
    Label(main,text="Email Id",font="times 13").grid(row=16,column=1)
    m=Entry(main,bd=3)
    m.grid(row=16,column=2)
    Label(main,text=" ").grid(row=17,column=1)
    def type1():
        k.delete(0,END)

    Button(main,text="+",command=type1).grid(row=14,column=3)
    def type2():
        m.delete(0,END)
        
    Button(main,text="+",command=type2).grid(row=16,column=3)
    
    regex= '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    global form
    form=i.get()
    
    def save():
       form=i.get()
       def check_email(em):
           if(re.search(regex,em)):
               return 0
           else:
               return 1

       if((len(form)>10 or len(form)<10) and form!=''):
           showerror('error','Check the format of date')

       em=m.get()
       pin=g.get()
       conn=check_email(em)
##       now=datetime.now().date()
       ph=k.get()
       an=ph.isdigit()
       if(len(form)==10):
           az=form[0]
           ax=form[1]
           ac=form[3]
           av=form[4]
           ab=form[6]
           am=form[7]
           aq=form[8]
           aw=form[9]
           za=az.isdigit()
           xa=ax.isdigit()
           ca=ac.isdigit()
           va=av.isdigit()
           ba=ab.isdigit()
           ma=am.isdigit()
           qa=aq.isdigit()
           wa=aw.isdigit()
       
       if(a.get()=='' and b.get()=='' and c.get()=='' and d.get()=='' and e.get()=='' and f.get()=='' and g.get()=='' and h.get()=='' and i.get()=='' and k.get()=='' and m.get()==''):
           showerror('error','Please fill the entries')
       elif(an==False):
           showerror('error','Phone number is not valid')
       elif(conn==1 and em!=''):
           showerror('error','Email address is not valid')
       elif(a.get()==b.get()==c.get()):
           showerror('error','First , Middle, Last name cannot be same')
       elif((len(pin)>6 or len(pin)<6) and pin!=''):
           showerror('error','Check the pincode')
       elif((len(form)>10 or len(form)<10) and form!=''):
           showerror('error','Check the format of date')
       elif(form!='' and (za==False or xa==False or ca== False or va==False or ba==False or ma==False or qa==False or wa==False)):
           showerror('error','Check the format of date')
       elif(form!='' and (form[2]!='-' and form[5]!='-')):
           showerror('error','Check the format of date')
       else:
           fname=a.get()
           mname=b.get()
           lname=c.get()
           cname=d.get()
           add=e.get()
           city=f.get()
           pin=g.get()
           web=h.get()
           date=i.get()
           phone=k.get()
           email=m.get()
           if j.get()==0:
               t1='office'
           elif j.get()==1:
               t1='home'
           elif j.get()==2:
               t1='mobile'

           if l.get()==0:
               t2='office'
           elif l.get()==1:
               t2='personal'
           cur.execute('select max(id) from record')
           rr=cur.fetchall()
           aa=rr[0]
           ss=aa[0]
           sss=ss+1
           cur.execute('insert into record values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(sss,fname,mname,lname,cname,add,city,pin,web,date,phone,email,t1,t2))
           con.commit()
           #con.close()
           a.delete(0,END)
           b.delete(0,END)
           c.delete(0,END)
           d.delete(0,END)
           e.delete(0,END)
           f.delete(0,END)
           g.delete(0,END)
           h.delete(0,END)
           i.delete(0,END)
           k.delete(0,END)
           m.delete(0,END)
           showinfo('save','record successfully saved')
        
    Button(main,text="SAVE",command=save).grid(row=18,column=1)

    def search():
            ss=Tk()
            n=StringVar()
            ss.geometry("609x689")
            Label(ss,text="Searching Phone Book",bg="light blue",font="times 20 bold").grid(row=0,column=1)
            Label(ss,text="Enter Name:",font="arial 13").grid(row=1,column=0)
            n=Entry(ss,bd=3,width=30)
            n.grid(row=1,column=1)
            o=Listbox(ss,height=25,width=60,fg="blue",font="times 14 bold")
            o.grid(row=2,column=0,columnspan=10,rowspan=3)
            def clos():
                ss.destroy()
            def ch(e):
                o.delete(0,END)
            def cha(e):
                o.delete(0,END)
                li=[]
                li.append(n.get())
                a=li[0]
                cur.execute('select f_name,m_name,l_name from record where f_name like "%'+str(a)+'%" or m_name like "%'+str(a)+'%" or l_name like "%'+str(a)+'%" order by f_name')
                result=cur.fetchall()
                cur.execute('select * from record where f_name like "%'+str(a)+'%" or m_name like "%'+str(a)+'%" or l_name like "%'+str(a)+'%" order by f_name')
                global resul
                global resu
                resul=cur.fetchall()
                for i in range (len(result)):
                    o.insert(i,result[i])  
            def cursor(*args):
                 a=o.curselection()
                 b=o.get(a)
                 a=a[0]
                 resu=resul[a][0]
    ##             print resu
                 res=(resu,)
    ##             print res
                 details=Tk()
                 details.geometry("400x540")
                 details.title("Details")
                 Label(details,text="Details Of User",fg="indigo",font="Times 20 bold italic").grid(row=0,column=0,columnspan=10)
                 listbox=Listbox(details,height=20,width=40,bg="black",fg="coral",font="times 14 bold")
                 listbox.grid(row=2,column=0,columnspan=10,rowspan=3)
                 o.delete(0,END)
                 cur.execute('select id from record where f_name like (?) and m_name like (?) and l_name like(?)',b)
                 f=cur.fetchall()
    ##             print f[0]
                 cur.execute('select * from record where id =(?)',res)
                 l=cur.fetchall()
                 l=l[0]
                 k=l[1]
                 ss.destroy()
                 listbox.insert(0,'First Name:  '+ k)
                 k=l[2]
                 listbox.insert(1,'Middle Name:  '+k)
                 k=l[3]
                 listbox.insert(2,'Last Name:   '+k)
                 k=l[4]
                 listbox.insert(3,'Company Name:    '+k)
                 k=l[5]
                 listbox.insert(4,'Address:      '+k)
                 k=l[6]
                 listbox.insert(5,'City :        '+k)
                 k=l[7]
                 listbox.insert(6,'Pincode:      '+str(k))
                 k=l[8]
                 listbox.insert(7,'Website:      '+k)
                 k=l[9]
                 listbox.insert(8,'Date Of Birth:    '+k)
                 listbox.insert(9,"PHONE DETAILS.......")
                 k=l[10]
                 listbox.insert(10,l[12]+" :     " + k)
                 listbox.insert(11,'EMAIL DETAILS.......')
                 k=l[11]
                 listbox.insert(12,l[13]+" :      " + k)
                 def delete():
                    cur.execute("delete from record where id=(?)",f[0])
                    con.commit()
                    showinfo('delete','CONTACT DELETED')
                    details.destroy()
                 Button(details,text="DELETE",command=delete).grid(row=5,column=3)
                 def clos():
                     details.destroy()
                 Button(details,text="CLOSE",command=clos).grid(row=5,column=4)
                 
            ss.bind('<Button-3>',cursor)
            ss.bind('<Double-Button-1>',cursor)
            ss.bind('<KeyPress>',ch)
            ss.bind('<KeyRelease>',cha)
            Label(ss,text="Double click to select the contact").grid(row=5,column=1)
            Button(ss,text="CLOSE",command=clos).grid(row=6,column=1)
            ss.mainloop
        
    Button(main,text="SEARCH",command=search).grid(row=18,column=2)

    def close():
        main.destroy()
        
    Button(main,text="CLOSE",command=close).grid(row=18,column=3)

    def edit():
        edit=Tk()
        n=StringVar()
        edit.geometry("609x689")
        Label(edit,text="Searching Phone Book",bg="light blue",font="times 20 bold").grid(row=0,column=1)
        Label(edit,text="Enter Name:",font="arial 13").grid(row=1,column=0)
        n=Entry(edit,bd=3,width=30)
        n.grid(row=1,column=1)
        o=Listbox(edit,height=25,width=60,fg="blue",font="times 14 bold")
        o.grid(row=2,column=0,columnspan=10,rowspan=3)
        def clos():
            edit.destroy()
        def ch(e):
            o.delete(0,END)
        def cha(e):
            o.delete(0,END)
            li=[]
            li.append(n.get())
            a=li[0]
            cur.execute('select f_name,m_name,l_name from record where f_name like "%'+str(a)+'%" or m_name like "%'+str(a)+'%" or l_name like "%'+str(a)+'%" order by f_name')
            result=cur.fetchall()
            cur.execute('select * from record where f_name like "%'+str(a)+'%" or m_name like "%'+str(a)+'%" or l_name like "%'+str(a)+'%" order by f_name')
            global resul
            global resu
            resul=cur.fetchall()
            for i in range(len(result)):
                o.insert(i,result[i])
        def cursor(*args):
            a=o.curselection()
            b=o.get(a)
            a=a[0]
            resu=resul[a][0]
##            print resu
            res=(resu,)
##            print res
            details=Tk()
            details.geometry("500x490")
            details.title("Details")
            cur.execute('select id from record where f_name like (?) and m_name like (?) and l_name like(?)',b)
            f=cur.fetchall()
            cur.execute('select * from record where id =(?)',res)
            cd=res[0]
            var=cur.fetchall()
            var=var[0]
            a=StringVar()
            b=StringVar()
            c=StringVar()
            d=StringVar()
            e=StringVar()
            f=StringVar()
            g=IntVar()
            h=StringVar()
            i=StringVar()
            tt=IntVar()
            k=IntVar()
            jj=IntVar()
            m=StringVar()
            Label(details,text="Edit Contact.....",font="Times 20 bold italic",fg='green').grid(row=0,column=2)
            Label(details,text="Phone Book",font="times 17 bold underline",fg="blue").grid(row=3,column=2)
            Label(details,text="First Name",font="times 13").grid(row=4,column=1)
            a=Entry(details,bd=3)
            a.grid(row=4,column=2)
            a.insert(0,var[1])
            Label(details,text="Middle Name",font="times 13").grid(row=5,column=1)
            b=Entry(details,bd=3)
            b.grid(row=5,column=2)
            b.insert(0,var[2])
            Label(details,text="Last Name",font="times 13").grid(row=6,column=1)
            c=Entry(details,bd=3)
            c.grid(row=6,column=2)
            c.insert(0,var[3])
            Label(details,text="Company Name",font="times 13").grid(row=7,column=1)
            d=Entry(details,bd=3)
            d.grid(row=7,column=2)
            d.insert(0,var[4])
            Label(details,text="Address",font="times 13").grid(row=8,column=1)
            e=Entry(details,bd=3)
            e.grid(row=8,column=2)
            e.insert(0,var[5])
            Label(details,text="City",font="times 13").grid(row=9,column=1)
            f=Entry(details,bd=3)
            f.grid(row=9,column=2)
            f.insert(0,var[6])
            Label(details,text="Pin Code",font="times 13").grid(row=10,column=1)
            g=Entry(details,bd=3)
            g.grid(row=10,column=2)
            g.insert(0,var[7])
            Label(details,text="Website URL",font="times 13").grid(row=11,column=1)
            h=Entry(details,bd=3)
            h.grid(row=11,column=2)
            h.insert(0,var[8])
            Label(details,text="Date of Birth",font="times 13").grid(row=12,column=1)
            i=Entry(details,bd=3)
            i.grid(row=12,column=2)
            i.insert(0,var[9])
            Label(details,text="Select Phone Type : ",font="times 15").grid(row=13,column=1)
            r1=Radiobutton(details,text="office",variable=tt,value=0)
            r1.grid(row=13,column=2)
            r2=Radiobutton(details,text="home",variable=tt,value=1)
            r2.grid(row=13,column=3)
            r3=Radiobutton(details,text="mobile",variable=tt,value=2)
            r3.grid(row=13,column=4)    
            Label(details,text="Phone Number",font="times 13").grid(row=14,column=1)
            k=Entry(details,bd=3)
            k.grid(row=14,column=2)
            k.insert(0,var[10])
            Label(details,text="Select Email Type : ",font="times 15",fg="blue").grid(row=15,column=1)    
            r4=Radiobutton(details,text="office",variable=jj,value=0)
            r4.grid(row=15,column=2)
            r5=Radiobutton(details,text="personal",variable=jj,value=1)
            r5.grid(row=15,column=3)
            Label(details,text="Email Id",font="times 13").grid(row=16,column=1)
            m=Entry(details,bd=3)
            m.grid(row=16,column=2)
            m.insert(0,var[11])
            if (var[12]=='office'):
                r1.select()
            if (var[12]=='home'):
                r2.select()
            if (var[12]=='mobile'):
                r3.select()

            if (var[13]=='office'):
                r4.select()
            if (var[13]=='home'):
                r5.select()
            Label(details,text=" ").grid(row=17,column=1)
            def update():
                if(a.get()=='' and b.get()=='' and c.get()=='' and d.get()=='' and e.get()=='' and f.get()=='' and g.get()=='' and h.get()=='' and i.get()=='' and k.get()=='' and m.get()==''):
                    showerror('error','Please fill the entries')
                else:
                   fname=a.get()
                   mname=b.get()
                   lname=c.get()
                   cname=d.get()
                   add=e.get()
                   city=f.get()
                   pin=g.get()
                   web=h.get()
                   date=i.get()
                   phone=k.get()
                   email=m.get()
                   if tt.get()==0:
                       t1='office'
                   elif tt.get()==1:
                       t1='home'
                   elif tt.get()==2:
                       t1='mobile'

                   if jj.get()==0:
                       t2='office'
                   elif jj.get()==1:
                       t2='personal'
                
                cur.execute('update record set f_name=(?),m_name=(?),l_name=(?),c_name=(?),add_n=(?),city=(?),pincode=(?),web=(?),birth=(?),p_no=(?),email=(?),type1=(?),type2=(?) where id=(?)',(fname,mname,lname,cname,add,city,pin,web,date,phone,email,t1,t2,cd))
                con.commit()
                showinfo('update',"Contact Successfully Updated")
                details.destroy()
                edit.destroy()
            Button(details,text="UPDATE",command=update).grid(row=18,column=2)
            def clos():
                 details.destroy()
            Button(details,text="CLOSE",command=clos).grid(row=18,column=3)
             
        edit.bind('<Double-Button-1>',cursor)
        edit.bind('<KeyPress>',ch)
        edit.bind('<KeyRelease>',cha)
        Label(edit,text="Double click to select the contact").grid(row=5,column=1)
        Button(edit,text="CLOSE",command=clos).grid(row=6,column=1)
        edit.mainloop()
        
    Button(main,text="EDIT",command=edit).grid(row=18,column=4)

    main.mainloop()
    
first.bind("<Motion>",close)
first.mainloop()
