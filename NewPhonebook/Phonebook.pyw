try:
    from Tkinter import *
except:
    from tkinter import *
from tkMessageBox import *
import sqlite3
from datetime import date
#from function import *
con=sqlite3.Connection('phonebook-database.db')
cur=con.cursor()
cur.execute("create table if not exists phone1(c_id integer primary key AutoIncrement ,first_name varchar(20),middle_name varchar(20),last_name varchar(20),company varchar(40),address varchar(40),cityname varchar(30),pin varchar(30),website varchar(30),birth date,c_type varchar(30),contact_num vacrhar(30),etype varchar(30),emailid varchar(30))")
start=Tk()
start.geometry('2000x1500')
start.config(bg='black')
a=" "*20
b=" "*35
c=" "*30
d=" "*70
new1=[1]
val_del=5
#fake=Tk()
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=0,column=0,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=0,column=1,columnspan=2,ipadx=50)
Label(start,text='  Project Title : PHONEBOOK ',font='fixedsys 20 bold ',bg='black',fg='#b1ff32').grid(row=0,column=2,columnspan=2,ipadx=50)
#Label(start,text='               ',bg='black',fg='#b1ff32').grid(row=2,column=2,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=1,column=0,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=1,column=1,columnspan=2,ipadx=50)
Label(start,text='  Project of Python and Database ',font='fixedsys 20 bold',bg='black',fg='#b1ff32').grid(row=1,column=2,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=2,column=0,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=2,column=1,columnspan=2,ipadx=50)
Label(start,text='---------------------------------------------------',font='fixedsys 12 bold',bg='black',fg='#b1ff32').grid(row=2,column=2,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=3,column=0,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=3,column=1,columnspan=2,ipadx=50)
Label(start,text='Developed By : Ashutosh Shrimal',font='fixedsys 18 bold',bg='white',fg='#b1ff32').grid(row=3,column=2,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=4,column=0,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=4,column=1,columnspan=2,ipadx=50)
Label(start,text='---------------------------------------------------',font='fixedsys 12 bold',bg='black',fg='#b1ff32').grid(row=4,column=2,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=5,column=0,columnspan=2,ipadx=50)
Label(start,text=b,font='fixedsys 15 bold',bg='black',fg='#b1ff32').grid(row=5,column=1,columnspan=2,ipadx=50)
Label(start,text='Move your mouse to close this window',font='fixedsys 10 bold',bg='black',fg='#b1ff32').grid(row=5,column=2,columnspan=2,ipadx=50)                                                                              
photo=PhotoImage(file='pypyf.gif')
photo=photo.subsample(2,2)
bb=Label(start,image=photo,bg='black',bd=1)
bb.place(x=600,y=250)
Label(start,text='-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X',font='fixedsys 12 bold',bg='black',fg='#b1ff32').place(x=0,y=600)
def func1():
    home=Tk()
    home.geometry('2000x1500')
    home.config(bg='plum')
    #pic(home)
    Label(home,text='                                                                               ',font='times 20 bold',bg='plum',fg='white').grid(row=0,column=0)
    Label(home,text='                                                                               ',font='times 30 bold',bg='plum',fg='white').grid(row=1,column=0)
    Label(home,text='                                                                               ',font='times 30 bold',bg='plum',fg='white').grid(row=2,column=0)
    Label(home,text='                                                                               ',font='times 30 bold',bg='plum',fg='white').grid(row=3,column=0)
    Label(home,text='                                                                               ',font='times 20 bold',bg='plum',fg='white').grid(row=4,column=0)
    Label(home,text='PHONEBOOK',font='fixedsys 20 bold',bg='black',fg='plum').place(x=695,y=200)
    photo=PhotoImage(file='abc.gif')
    photo=photo.subsample(1,1)
    bb=Label(home,image=photo,bg='plum',bd=1)
    bb.place(x=670,y=0)
    Label(home,text=a+'First Name',font='fixedsys 18',bg='plum').grid(row=6,column=0)
    fname=Entry(home)
    fname.grid(row=6,column=2)
    Label(home,text=a+'Middle Name',font='fixedsys 18',bg='plum').grid(row=7,column=0)
    mname=Entry(home)
    mname.grid(row=7,column=2)
    Label(home,text=a+'Last Name',font='fixedsys 18',bg='plum').grid(row=8,column=0)
    lname=Entry(home)
    lname.grid(row=8,column=2)
    Label(home,text=a+'Company Name',font='fixedsys 18',bg='plum').grid(row=9,column=0)
    comp=Entry(home)
    comp.grid(row=9,column=2)
    Label(home,text=a+'Address',font='fixedsys 18',bg='plum').grid(row=10,column=0)
    add=Entry(home)
    add.grid(row=10,column=2)
    Label(home,text=a+'City',font='fixedsys 18',bg='plum').grid(row=11,column=0)
    city=Entry(home)
    city.grid(row=11,column=2)
    Label(home,text=a+'Pin Code',font='fixedsys 18',bg='plum').grid(row=12,column=0)
    pin=Entry(home)
    pin.grid(row=12,column=2)
    Label(home,text=a+'Website URL',font='fixedsys 18',bg='plum').grid(row=13,column=0)
    url=Entry(home)
    url.grid(row=13,column=2)
    Label(home,text=a+'Date Of Birth',font='fixedsys 18',bg='plum').grid(row=14,column=0)
    dob=Entry(home)
    dob.grid(row=14,column=2)
    Label(home,text=a+'Select Phone Type : ',font='fixedsys 20',bg='plum',fg='white').grid(row=15,column=0)
    phone=IntVar()
    Radiobutton(home,text='Office',bg='plum',font='fixedsys 15',variable=phone,value=1).grid(row=15,column=1)
    Radiobutton(home,text='Home',bg='plum',font='fixedsys 15',variable=phone,value=2).grid(row=15,column=2)
    Radiobutton(home,text='Mobile',bg='plum',font='fixedsys 15',variable=phone,value=3).grid(row=15,column=3)
    Label(home,text=a+'Phone Number',font='fixedsys 18',bg='plum').grid(row=16,column=0)
    contact=Entry(home)
    contact.grid(row=16,column=1)
    Label(home,text=a+'Select Email Type: ',font='fixedsys 20',bg='plum',fg='white').grid(row=17,column=0)
    eid=IntVar()
    Radiobutton(home,text='Office',bg='plum',font='fixedsys 15',variable=eid,value=1).grid(row=17,column=1)
    Radiobutton(home,text='Personal',bg='plum',font='fixedsys 15',variable=eid,value=2).grid(row=17,column=2)
    Label(home,text=a+"Email Id",font='fixedsys 18' ,bg='plum').grid(row=18,column=0)
    email=Entry(home)
    email.grid(row=18,column=1)
    def save():
        if fname.get()=="" and mname.get()=="" and lname.get()=="" and comp.get()=="" and add.get()=="" and city.get()=="" and pin.get()=="" and url.get()=="" and dob.get()=="" and contact.get()=="" and email.get()=="":
            showinfo("Error","No data inserted")
        else:
            if fname.get()=="" and mname.get()=="" and lname.get()=="":
                showinfo("Error","Enter atleast one name")
            else:
                if fname.get()==mname.get()==lname.get():
                    showinfo("Error","You can not insert same first name,middle name,and last name")
                else:
                    def pin_check(pincode):
                        for i in pincode:
                            if ord(i)<48 or ord(i)>57:
                                return 1
                        return 0
                    if pin.get()!="" and pin_check(pin.get()):
                        showinfo("Error","Invalid pincode")
                    else:
                        def birth_check(birthdate):
    ##                        cur.execute('select extract(year from sysdate) from dual')
    ##                        abc123=cur.fetchall()
                            empty=""
                            flag=0
                            count=0
                            for i in birthdate:
                                if ord(i)>=48 and ord(i)<=57:
                                    count=count+1
                                    empty=empty+i
                                else:
                                    count=0
                                    empty=""
                                if count==4:
                                    flag=1
                                    break
                            #print d1
                            if flag==1:
                                print count,empty,flag
                                empty=int(empty)
                                today = date.today()
                                d1 = today.strftime("%Y")
                                d1=int(d1)
                                if empty<=(d1-18):
                                    return 0
                                else:
                                    return 1
                            else:
                                return 1
                        if dob.get()!="" and birth_check(dob.get()) :
                            showinfo("Error"," One with such date of birth can \n not have personal contact\n Write in dd/mm/yyyy format")
                        else:
                            def url_check(url):
                                count_dot=0
                                for i in url:
                                    if ord(i)==46:
                                        count_dot=count_dot+1
                                if count_dot>0 and count_dot<3:
                                    return 0
                                else:
                                    return 1
                            if url.get()!="" and url_check(url.get()):
                                showinfo("Error","Invalid Url")
                            else:
                                def contact_check(con):
                                    length=len(con)
                                    count0=0
                                    for i in con:
                                        if ord(i)>=48 and ord(i)<=57:
                                            if ord(i)==48:
                                                count0=count0+1
                                        else:
                                            return 1
                                    if count0==length or length>14:
                                        return 1
                                    else:
                                        return 0
                                if contact.get()!="" and contact_check(contact.get()):
                                    showinfo("Error","No such Contact Number exist")
                                else:
                                    def email_check(emailid):
                                        count_1=0
                                        count_dot=0
                                        flagpoint=0
                                        count_at=0
                                        emp=""
                                        emp1=""
                                        flag1=0
                                        for i in emailid:
                                            if flagpoint==1:
                                                emp=emp+i
                                            if flag1==1:
                                                emp1=emp1+i
                                            if ord(i)==46:
                                                flag1=0
                                                flagpoint=1
                                                count_dot=count_dot+1
                                            if flagpoint==1 and ord(i)==64:
                                                return 1
                                            if ord(i)==64:
                                                flag1=1
                                                count_at=count_at+1
                                        emp=emp.upper()
                                        emp1=emp1.upper()
                                        if emp1=="YAHOO." or emp1=="GMAIL." or emp1=="OUTLOOK." or emp1=="MSN." or emp1=="REDDIFFMAIL.":
                                            if emp=="COM" or emp=="IN":
                                                if count_dot>0 and count_dot<=2:
                                                    if count_at==1:
                                                        return 0
                                        return 1
                                    if email.get()!="" and email_check(email.get()):
                                        showinfo("Error","Invalid email address")
                                    else:
                                        if fname.get()=="":
                                            v1=""
                                        else:
                                            v1=fname.get()
                                        if mname.get()=="":
                                            v2=""
                                        else:
                                            v2=mname.get()
                                        if lname.get()=="":
                                            v3=""
                                        else:
                                            v3=lname.get()
                                        if comp.get()=="":
                                            v4=""
                                        else:
                                            v4=comp.get()
                                        if add.get()=="":
                                            v5=""
                                        else:
                                            v5=add.get()
                                        if city.get()=="":
                                            v6=""
                                        else:
                                            v6=city.get()
                                        if pin.get()=="":
                                            v7=""
                                        else:
                                            v7=pin.get()
                                        if url.get()=="":
                                            v8=""
                                        else:
                                            v8=url.get()
                                        if dob.get()=="":
                                            v9=""
                                        else:
                                            v9=dob.get()
                                        if contact.get()=="":
                                            v10=""
                                        else:
                                            v10=contact.get()
                                        if email.get()=="":
                                            v11=""
                                        else:
                                            v11=email.get()
                                        if phone.get()==1:
                                            contact_type="Office"
                                        elif phone.get()==2:
                                            contact_type="Home"
                                        else:
                                            contact_type="Mobile"
                                        if eid.get()==1:
                                            email_type="Office"
                                        else:
                                            email_type="Personal"
                                        a=[1]
                                        a[0]=[v1,v2,v3,v4,v5,v6,v7,v8,v9,contact_type,v10,email_type,v11]
                                        cur.execute("insert into phone1(first_name,middle_name,last_name,company,address,cityname,pin,website,birth,c_type,contact_num,etype,emailid) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",a[0])
                                        con.commit()
                                        fname.delete(0,END)
                                        mname.delete(0,END)
                                        lname.delete(0,END)
                                        comp.delete(0,END)
                                        add.delete(0,END)
                                        city.delete(0,END)
                                        pin.delete(0,END)
                                        url.delete(0,END)
                                        dob.delete(0,END)
                                        contact.delete(0,END)
                                        email.delete(0,END)
                                        showinfo("SAVED!","Contact added successfully")
    def search():
        home.destroy()
        sear=Tk()
        sear.geometry('2000x1000')
        sear.config(bg='green')
        #Label(sear,text='font='times 20 bold').grid(row=0,column=0)
        Label(sear,text='Searching Phone Book',font='fixedsys 20 bold',bg='skyblue').grid(row=0,column=0)
        search1=Entry(sear,width='40',bg='grey',fg='black',font='arial 10 bold')
        search1.grid(row=1,column=0)
        lb=Listbox(sear,height='25',width='130',font='times 16 bold')
        lb.config(bg='lightgreen')
        lb.grid(row=2,column=0)
        def key(event):
            try:
                lb.delete(0,END)
                if (ord(event.char)>=32 and ord(event.char)<=126) or ord(event.char)==8:
                    if ord(event.char)==8:
                        abc=len(search1.get())-1
                        search1.delete(abc,END)
                    else:
                        search1.insert(END,event.char)
                    b=[1]
                    b[0]=['%'+search1.get()+'%']
                    a=[1]
                    a[0]=b[0]*13
                    cur.execute("select * from phone1 where first_name like ? or middle_name like ? or last_name like ? or company like ? or cityname like ? or address like ? or pin like ? or website like ? or birth like ? or contact_num like ? or c_type like ? or etype like ? or  emailid like ? order by first_name,middle_name,last_name",a[0])
                    xyz=cur.fetchall()
                    new1=[1]
                    for i in xyz:
                        new1.append(i)
                    for i in xyz:
                        x=i[1]+" "+i[2]+" "+i[3]
                        lb.insert(END,x)
                   # for i in new1:
                    #    print i
                   # print new1[0]
                    def click_button(event):
                        w=event.widget
                        index=int(w.curselection()[0])
                        #index
                        aftersear=Tk()
                        aftersear.geometry('2000x1500')
                        #print new1[index+1][0]
                        aftersear.config(bg='#F8DE7E')
                        Label(aftersear,text='                                                                              ',bg='#F8DE7E',font='times 20 bold').grid(row=0,column=0)
                        Label(aftersear,text='                                                                              ',bg='#F8DE7E',font='times 20 bold').grid(row=1,column=0)
                        Label(aftersear,text='CONTACT DETAILS',font='fixedsys 25 bold underline',bg='#F8DE7E',fg='#C70039').grid(row=4,column=1)
                        Label(aftersear,text='                                                                              ',bg='#F8DE7E',font='times 20 bold').grid(row=5,column=0)
                        Label(aftersear,text='                                                                              ',bg='#F8DE7E',font='times 20 bold').grid(row=6,column=0)
                        Label(aftersear,text='First Name : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=11,column=0,rowspan=1)
                        Label(aftersear,text='Middle Name : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=12,column=0,rowspan=1)
                        Label(aftersear,text='Last Name : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=13,column=0,rowspan=1)
                        Label(aftersear,text='Company : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=14,column=0,rowspan=1)
                        Label(aftersear,text='City : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=15,column=0,rowspan=1)
                        Label(aftersear,text='Address : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=16,column=0,rowspan=1)
                        Label(aftersear,text='Pin : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=17,column=0,rowspan=1)
                        Label(aftersear,text='Website Url : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=18,column=0,rowspan=1)
                        Label(aftersear,text='Date Of Birth : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=19,column=0,rowspan=1)
                        Label(aftersear,text='Contact Type : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=20,column=0,rowspan=1)
                        Label(aftersear,text='Contact Number : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=21,column=0,rowspan=1)
                        Label(aftersear,text='Email Type : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=22,column=0,rowspan=1)
                        Label(aftersear,text='Email ID : ',font='fixedsys 17  bold',bg='#F8DE7E',fg='black').grid(row=23,column=0,rowspan=1)
                        var1=new1[index+1][1]
                        var2=new1[index+1][2]
                        var3=new1[index+1][3]
                        var4=new1[index+1][4]
                        var5=new1[index+1][5]
                        var6=new1[index+1][6]
                        var7=new1[index+1][7]
                        var8=new1[index+1][8]
                        var9=new1[index+1][9]
                        var10=new1[index+1][10]
                        var11=new1[index+1][11]
                        var12=new1[index+1][12]
                        var13=new1[index+1][13]
                        val_del=new1[index+1][0]
                        #print new1[index+1][0]
                        def close2():
                            aftersear.destroy()
                        #showinfo("ERROR","ERROR WINDOW")
                        #print new1[index+1][0],val_del
                        def del1():
                    ##        temp=0
                    ##        print temp
                    #aftersear.destroy()
                            new2=[1]
                            new2[0]=[val_del]
                            cur.execute('delete from phone1 where c_id = ?',new2[0])
                            showinfo("DELETED","CONTACT DELETED SUCCESSFULLY")
                            con.commit()
                            aftersear.destroy()
                            #print val_del
                            #print '0'
                        Label(aftersear,text=var1,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=11,column=2,rowspan=1)
                        Label(aftersear,text=var2,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=12,column=2,rowspan=1)
                        Label(aftersear,text=var3,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=13,column=2,rowspan=1)
                        Label(aftersear,text=var4,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=14,column=2,rowspan=1)
                        Label(aftersear,text=var5,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=15,column=2,rowspan=1)
                        Label(aftersear,text=var6,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=16,column=2,rowspan=1)
                        Label(aftersear,text=var7,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=17,column=2,rowspan=1)
                        Label(aftersear,text=var8,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=18,column=2,rowspan=1)
                        Label(aftersear,text=var9,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=19,column=2,rowspan=1)
                        Label(aftersear,text=var10,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=20,column=2,rowspan=1)
                        Label(aftersear,text=var11,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=21,column=2,rowspan=1)
                        Label(aftersear,text=var12,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=22,column=2,rowspan=1)
                        Label(aftersear,text=var13,font='fixedsys 17  bold',bg='#F8DE7E',fg='blue').grid(row=23,column=2,rowspan=1)
                        #fake=aftersear
                        Button(aftersear,text='Delete',command=del1,font='times 10 bold',bg='gray',fg='black').grid(row=24,column=1)
                        Button(aftersear,text='Close',font='times 10 bold',bg='gray',fg='black',command=close2).grid(row=24,column=2)
                    ind=lb.bind('<Double-Button-1>',click_button)
                else:
                    showinfo("Error","Invalid Character")
            except TypeError:
                aaa=0
                #sear.bind_all('<Key>',key)
        sear.bind_all('<Key>',key)
        def close5():
            sear.destroy()
            func1()
        Button(sear,text='Close',command=close5,bg='grey',fg='black',font='times 10 bold').grid(row=3,column=0)
        sear.mainloop()
    def close1():
        home.destroy()
        final=Tk()
        final.geometry('2000x1500')
        final.config(bg='pink')
        Label(final,text='THANKS FOR USING THE PHONEBOOK',font='fixedsys 25 bold underline',fg='#808000',bg='pink').place(x=375,y=100)
        Label(final,text='          -------------        ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=150)
        Label(final,text='         |   --- ---   |       ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=180)
        Label(final,text='         |    +   +    |       ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=210)
        Label(final,text='         |             |       ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=240)
        Label(final,text='         |      ?      |       ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=270)
        Label(final,text='         |             |       ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=300)
        Label(final,text='         |   -------   |       ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=330)
        Label(final,text='         |-------------|       ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=380)
        Label(final,text='        \       ||       /     ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=410)
        Label(final,text='         \      ||      /    ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=450)
        Label(final,text='          ------||------       ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=480)
        Label(final,text='                ||             ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=510)
        Label(final,text='                ||             ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=540)
        Label(final,text='               /  \            ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=570)
        Label(final,text='            __/    \__         ',font='fixedsys 25 bold',fg='white',bg='pink').place(x=355,y=600)
##        photo=PhotoImage(file='thanksicon.gif')
##        photo=photo.subsample(1,1)
##        bb=Label(final,image=photo,bg='grey',bd=3)
##        bb.place(x=450,y=60)
        def close6(e=1):
            final.destroy()
        final.bind('<Motion>',close6)
        final.mainloop()
    def edit():
        home.destroy()
        edi=Tk()
        edi.geometry('2000x1500')
        edi.config(bg='blue')
        Label(edi,text='Edit Phone Book',font='fixedsys 20 bold',bg='skyblue').grid(row=0,column=0)
        search2=Entry(edi,width='40',bg='grey',fg='black',font='bold')
        search2.grid(row=1,column=0)
        lb1=Listbox(edi,height='25',width='130',font='times 16 bold')
        lb1.config(bg='skyblue')
        lb1.grid(row=2,column=0)
        def close3():
            edi.destroy()
            func1()
        Button(edi,text='Close',command=close3,bg='grey',font='times 10 bold',fg='black').grid(row=3,column=0)
        def key1(event):
            try:
                lb1.delete(0,END)
                if (ord(event.char)>=32 and ord(event.char)<=126) or ord(event.char)==8:
                    if ord(event.char)==8:
                        abc=len(search2.get())-1
                        search2.delete(abc,END)
                    else:
                        search2.insert(END,event.char)
                    b=[1]
                    b[0]=['%'+search2.get()+'%']
                    a=[1]
                    a[0]=b[0]*13
                    cur.execute("select * from phone1 where first_name like ? or middle_name like ? or last_name like ? or company like ? or cityname like ? or address like ? or pin like ? or website like ? or birth like ? or contact_num like ? or c_type like ? or etype like ? or  emailid like ? order by first_name,middle_name,last_name",a[0])
                    xyz1=cur.fetchall()
                    new1=[1]
                    for i in xyz1:
                        new1.append(i)
                    for i in xyz1:
                        x=i[1]+" "+i[2]+" "+i[3]
                        lb1.insert(END,x)
                    def click_button1(event):
                        w=event.widget
                        index=int(w.curselection()[0])
                        #print index
                        edi.destroy()
                        afteredi=Tk()
                        afteredi.geometry('2000x1500')
                        afteredi.config(bg='#C70039')
                        Label(afteredi,text='                                                                               ',font='times 20 bold',bg='#C70039').grid(row=0,column=0)
                        Label(afteredi,text='                                                                               ',font='times 20 bold',bg='#C70039').grid(row=1,column=0)
                        Label(afteredi,text='                                                                               ',font='times 20 bold',bg='#C70039').grid(row=2,column=0)
                        Label(afteredi,text='                                                                               ',font='times 20 bold',bg='#C70039').grid(row=3,column=0)
                        Label(afteredi,text='                                                                               ',font='times 20 bold',bg='#C70039').grid(row=4,column=0)
                        Label(afteredi,text='EDITING CONTACT',font='fixedsys 25 bold',fg='#C70039',bg='white',justify='left').place(x=530,y=80)
                        Label(afteredi,text='                   First Name            ',font='fixedsys 17 bold ',bg='#C70039').grid(row=7,column=0)
                        fname=Entry(afteredi)
                        fname.grid(row=7,column=2)
                        Label(afteredi,text='                  Middle Name          ',font='fixedsys 17 bold ',bg='#C70039').grid(row=8,column=0)
                        mname=Entry(afteredi)
                        mname.grid(row=8,column=2)
                        Label(afteredi,text='                   Last Name              ',font='fixedsys 17 bold ',bg='#C70039').grid(row=9,column=0)
                        lname=Entry(afteredi)
                        lname.grid(row=9,column=2)
                        Label(afteredi,text='                 Company Name        ',font='fixedsys 17 bold ',bg='#C70039').grid(row=10,column=0)
                        comp=Entry(afteredi)
                        comp.grid(row=10,column=2)
                        Label(afteredi,text='                   Address             ',font='fixedsys 17 bold ',bg='#C70039').grid(row=11,column=0)
                        add=Entry(afteredi)
                        add.grid(row=11,column=2)
                        Label(afteredi,text='                   City                ',font='fixedsys 17 bold ',bg='#C70039').grid(row=12,column=0)
                        city=Entry(afteredi)
                        city.grid(row=12,column=2)
                        Label(afteredi,text='                 Pin Code            ',font='fixedsys 17 bold ',bg='#C70039').grid(row=13,column=0)
                        pin=Entry(afteredi)
                        pin.grid(row=13,column=2)
                        Label(afteredi,text='                 Website URL         ',font='fixedsys 17 bold ',bg='#C70039').grid(row=14,column=0)
                        url=Entry(afteredi)
                        url.grid(row=14,column=2)
                        Label(afteredi,text='                   Date Of Birth           ',font='fixedsys 17 bold ',bg='#C70039').grid(row=15,column=0)
                        dob=Entry(afteredi)
                        dob.grid(row=15,column=2)
                        Label(afteredi,text='          Select Phone Type :',font='fixedsys 20 bold ',bg='#C70039',fg='blue').grid(row=16,column=0)
                        phone=IntVar()
                        Radiobutton(afteredi,text='Office',bg='#C70039',font='fixedsys 10 bold',variable=phone,value=1).grid(row=16,column=1)
                        Radiobutton(afteredi,text='Home',bg='#C70039',font='fixedsys 10 bold',variable=phone,value=2).grid(row=16,column=2)
                        Radiobutton(afteredi,text='Mobile',bg='#C70039',font='fixedsys 10 bold',variable=phone,value=3).grid(row=16,column=3)
                        Label(afteredi,text='                 Phone Number        ',font='fixedsys 17 bold',bg='#C70039').grid(row=17,column=0)
                        contact=Entry(afteredi)
                        contact.grid(row=17,column=2)
                        Label(afteredi,text='          Select Email Type:',font='fixedsys 20 bold ',bg='#C70039',fg='blue').grid(row=18,column=0)
                        eid=IntVar()
                        Radiobutton(afteredi,text='Office',bg='#C70039',font='fixedsys 10 bold',variable=eid,value=1).grid(row=18,column=1)
                        Radiobutton(afteredi,text='Personal',bg='#C70039',font='fixedsys 10 bold',variable=eid,value=2).grid(row=18,column=2)
                        Label(afteredi,text="                Email Id:        ",font='fixedsys 17 bold' ,bg='#C70039').grid(row=19,column=0)
                        email=Entry(afteredi)
                        email.grid(row=19,column=2)
                        var1=new1[index+1][1]
                        var2=new1[index+1][2]
                        var3=new1[index+1][3]
                        var4=new1[index+1][4]
                        var5=new1[index+1][5]
                        var6=new1[index+1][6]
                        var7=new1[index+1][7]
                        var8=new1[index+1][8]
                        var9=new1[index+1][9]
                        var10=new1[index+1][10]
                        var11=new1[index+1][11]
                        var12=new1[index+1][12]
                        var13=new1[index+1][13]
                        var_del=new1[index+1][0]
                        if var1!="":
                            fname.insert(END,var1)
                        if var2!="":
                            mname.insert(END,var2)
                        if var3!="":
                            lname.insert(END,var3)
                        if var4!="":
                            comp.insert(END,var4)
                        if var5!="":
                            add.insert(END,var5)
                        if var6!="":
                            city.insert(END,var6)
                        if var7!="":
                            pin.insert(END,var7)
                        if var8!="":
                            url.insert(END,var8)
                        if var9!="":
                            dob.insert(END,var9)
                        if var11!="":
                            contact.insert(END,var11)
                        if var13!="":
                            email.insert(END,var13)
                        if var10=="Office":
                            varx=1
                        elif var10=="Home":
                            varx=2
                        else:
                            varx=3
                        if var12=="Office":
                            vary=1
                        else:
                            vary=2
                        def update():
                            if fname.get()=="" and mname.get()=="" and lname.get()=="":
                                showinfo("Error","Enter atleast one name")
                            else:
                                if fname.get()==mname.get()==lname.get() and fname.get()!="":
                                    showinfo("Error","You can not insert same first name,middle name,and last name")
                                else:
                                    def birth_checker1(birthdate):
                                        empty=""
                                        flag=0
                                        count=0
                                        for i in birthdate:
                                            if ord(i)>=48 and ord(i)<=57:
                                                count=count+1
                                                empty=empty+i
                                            else:
                                                count=0
                                                empty=""
                                            if count==4:
                                                flag=1
                                                break
                                        if flag==1:
                                            print count,empty,flag
                                            empty=int(empty)
                                            today = date.today()
                                            d1 = today.strftime("%Y")
                                            d1=int(d1)
                                            if empty<=(d1-18):
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    if  dob.get()!="" and birth_checker1(dob.get()):
                                          showinfo("Error"," One with such date of birth can \n not have personal contact\n Write in dd/mm/yyyy format")
                                    else:
                                        def pin_check1(pincode1):
                                            for i in pincode1:
                                                if ord(i)<48 or ord(i)>57:
                                                    return 1
                                            return 0
                                        if pin.get()!="" and pin_check1(pin.get()):
                                            showinfo("Error","Invalid pincode")
                                        else:
                                            def url_check(url):
                                                count_dot=0
                                                for i in url:
                                                    if ord(i)==46:
                                                        count_dot=count_dot+1
                                                if count_dot>0 and count_dot<3:
                                                    return 0
                                                else:
                                                    return 1
                                            if url.get()!="" and url_check(url.get()):
                                                showinfo("Error","Invalid Url")
                                            else:
                                                def contact_check(con):
                                                    length=len(con)
                                                    count0=0
                                                    for i in con:
                                                        if ord(i)>=48 and ord(i)<=57:
                                                            if ord(i)==48:
                                                                count0=count0+1
                                                        else:
                                                            return 1
                                                    if count0==length or length>14:
                                                        return 1
                                                    else:
                                                        return 0
                                                if contact.get()!="" and contact_check(contact.get()):
                                                    showinfo("Error","No such Contact Number exist")
                                                else:
                                                    def email_check(emailid):
                                                        count_1=0
                                                        count_dot=0
                                                        flagpoint=0
                                                        count_at=0
                                                        emp=""
                                                        emp1=""
                                                        flag1=0
                                                        for i in emailid:
                                                            if flagpoint==1:
                                                                emp=emp+i
                                                            if flag1==1:
                                                                emp1=emp1+i
                                                            if ord(i)==46:
                                                                flag1=0
                                                                flagpoint=1
                                                                count_dot=count_dot+1
                                                            if flagpoint==1 and ord(i)==64:
                                                                return 1
                                                            if ord(i)==64:
                                                                flag1=1
                                                                count_at=count_at+1
                                                        emp=emp.upper()
                                                        emp1=emp1.upper()
                                                        if emp1=="YAHOO." or emp1=="GMAIL." or emp1=="OUTLOOK." or emp1=="MSN." or emp1=="REDDIFFMAIL.":
                                                            if emp=="COM" or emp=="IN":
                                                                if count_dot>0 and count_dot<=2:
                                                                    if count_at==1:
                                                                        return 0
                                                        return 1
                                                    if email.get()!="" and email_check(email.get()):
                                                        showinfo("Error","Invalid email address")
                                                    else:
                                                        if var1!=fname.get():
                                                            a2=[1]
                                                            a2=[fname.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set first_name= ? where c_id = ?',a2)
                                                        if var2!=mname.get():
                                                            a2=[1]
                                                            a2=[mname.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set middle_name=? where c_id = ?',a2)
                                                        if var3!=lname.get():
                                                            a2=[1]
                                                            a2=[lname.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set last_name=? where c_id = ?',a2)
                                                        if var4!=comp.get():
                                                            a2=[1]
                                                            a2=[comp.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set company=? where c_id = ?',a2)
                                                        if var5!=add.get():
                                                            a2=[1]
                                                            a2=[add.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set address=? where c_id = ?',a2) 

                                                        if var6!=city.get():
                                                            a2=[1]
                                                            a2=[city.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set cityname=? where c_id = ?',a2) 

                                                        if var7!=pin.get():
                                                            a2=[1]
                                                            a2=[pin.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set pin=? where c_id = ?',a2) 

                                                        if var8!=url.get():
                                                            a2=[1]
                                                            a2=[url.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set website=? where c_id = ?',a2)

                                                        if var9!=dob.get():
                                                            a2=[1]
                                                            a2=[dob.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set birth=? where c_id = ?',a2)
                                                        if var11!=contact.get():
                                                            a2=[1]
                                                            a2=[contact.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set contact_num=? where c_id = ?',a2)
                                                        if var13!=email.get():
                                                            a2=[1]
                                                            a2=[email.get()]
                                                            a2.append(var_del)
                                                            cur.execute('update phone1 set emailid= ? where c_id = ?',a2)
                                                        showinfo("UPDATED","CONTACT UPDATED SUCESSFULLY")
                                                        con.commit()
                                                        afteredi.destroy()
                                                        func1()
                        def close4():
                            abchsh=0
                            afteredi.destroy()
                            func1()
                        Label(afteredi,text='                                                                               ',font='times 20 bold',bg='#C70039').grid(row=20,column=0)
                        Button(afteredi,text='Close',bg='grey',fg='black',font='times 10 bold',command=close4).grid(row=21,column=1)
                        Button(afteredi,text='Update',bg='grey',fg='black',font='times 10 bold',command=update).grid(row=21,column=2)
                        afteredi.mainloop()
                    ind=lb1.bind('<Double-Button-1>',click_button1)
                else:
                    showinfo("Error","Invalid Character")
            except TypeError:
                aaa=0
                #sear.bind_all('<Key>',key)
        edi.bind_all('<Key>',key1)   
    Button(home,text="Save",command=save,font='SsnsSerif 10 bold',bg='maroon',fg='white').grid(row=19,column=1)
    Button(home,text="Search",command=search,font='SsnsSerif 10 bold',bg='maroon',fg='white').grid(row=19,column=2)
    Button(home,text="Close",command=close1,font='SsnsSerif 10 bold',bg='maroon',fg='white').grid(row=19,column=3)
    Button(home,text="Edit",font='SsnsSerif 10 bold',bg='maroon',fg='white',command=edit).grid(row=19,column=5)
    home.mainloop()
def close(e=1):
    start.destroy()
    func1()
start.bind('<Motion>',close)
start.mainloop()
