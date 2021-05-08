#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector


# In[15]:


root=Tk()
root.title('LOGIN AND REGISTRATION')




text=Label(root,text='LOGIN AND REGISTRATION',font='verdana 20 bold')
text.grid(row=0,column=0)


def registration():
    window=Tk()
    window.title('register')

    con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
    cursor=con.cursor()
    
    text=Label(window,text='registration',font='verdana 20 bold')
    text.grid(row=0,column=0)
    
    name = Label(window,text='name')
    name.grid(row=1,column=0)

    email = Label(window,text='email')
    email.grid(row=2,column=0)
    
    password = Label(window,text='password')
    password.grid(row=3,column=0)
    
    re_password = Label(window,text='re_password')
    re_password.grid(row=4,column=0)
    
    
    e1=Entry(window,width=18)
    e1.grid(row=1,column=1)
    
    e2=Entry(window,width=18)
    e2.grid(row=2,column=1)
    
    e3=Entry(window,width=18)
    e3.grid(row=3,column=1)
    e3.config(show='*')
    
    e4=Entry(window,width=18)
    e4.grid(row=4,column=1)
    e4.config(show='*')
    
    
    def clear():
        e1.delete(first=0,last=100)
        e2.delete(first=0,last=100)
        e3.delete(first=0,last=100)
        e4.delete(first=0,last=100)
        
    def error():
        Messagebox.showerror(title='error',message='password not same')
        
    def insert():
        insert=('insert into register (name,email,password,re_password) values(%s,%s,%s,%s)')
        values=[e1.get(),e2.get(),e3.get(),e4.get()]
        cursor.execute(insert,values)
        if e3.get()==e4.get():
            con.commit()
            clear()
            Messagebox.showinfo(title='done',message='account created')
        else:
            error()
            
    register=Button(window,text='register',fg='green',command=insert)
    register.grid(row=5,column=0)   
    exit=Button(window,text='exit',command=window.destroy)
    exit.grid(row=6,column=0)
    



def login():
    window=Tk()
    window.title('LOGIN')
    
    text=Label(window,text='LOGIN',font='verdana 20 bold')
    text.grid(row=0,column=0)

    email = Label(window,text='email')
    email.grid(row=1,column=0)
    
    password = Label(window,text='password')
    password.grid(row=2,column=0)
    
    
    e1=Entry(window,width=18)
    e1.grid(row=1,column=1)
    
    e2=Entry(window,width=18)
    e2.grid(row=2,column=1)
    
    
    def clear():
        e1.delete(first=0,last=100)
        e2.delete(first=0,last=100)
        
    def error():
        Messagebox.showerror(title='error',message='username and password is incorrect')
        
    def login():
        
        mail=e1.get()
        pas=e2.get()
    
        if mail=="" and pas=="":
            
            Messagebox.showinfo('insert data','please insert email and password')
        else:
            con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
            cursor=con.cursor()
            cursor.execute("select email,password from register" )
            rows=cursor.fetchall()
            user_d = []
            pass_d = []
            for row in rows:
                
                user_d.append(row[0])
                pass_d.append(row[1])
            for row in rows:
                if e1.get() in user_d and e2.get() in pass_d :
                    login = True
                    Messagebox.showinfo(title='done',message='login successful')
                    root= Tk()
                    root.geometry("600x300")
                    root.title("blockchain")
                    bid = Label(root,text='enter coin initail')
                    bid.place(x=20,y=30)
                    typ = Label(root,text='enter coin name')
                    typ.place(x=20,y=60)
                    own = Label(root,text='enter owner name')
                    own.place(x=20,y=90)
                    use= Label(root,text='enter the uses')
                    use.place(x=20,y=120)
                    e_id=Entry(root,width=20)
                    e_id.place(x=150,y=30)
                    e_typ=Entry(root,width=20)
                    e_typ.place(x=150,y=60)
                    e_own=Entry(root,width=20)
                    e_own.place(x=150,y=90)
                    e_use=Entry(root,width=20)
                    e_use.place(x=150,y=120)


                    def insert():
                        bid=e_id.get()
                        typ= e_typ.get()
                        own=e_own.get()
                        use=e_use.get()
                        if(bid=="" or typ==""or own==""or use==""):
                            Messagebox.showinfo("insert Status","all fields are required")
                        else:
                            con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                            cursor=con.cursor()
                            query="insert into blockchain values('%s','%s','%s','%s')" % (bid,typ,own,use)
                            cursor.execute(query)
                            cursor.execute("commit");
                            e_id.delete(0,'end')
                            e_typ.delete(0,'end')
                            e_own.delete(0,'end')
                            e_use.delete(0,'end')
                            Messagebox.showinfo("insert status","inserted successfully");
                            con.close();

                    def delete():
                        if(e_id.get()==""):
                            MessageBox.showinfo("delete status","bid is compulsory for delete")
                        else:
                            con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                            cursor=con.cursor()
                            cursor.execute("delete from blockchain where BCID='" + e_id.get()+ "'")
                            cursor.execute("commit");
                            e_id.delete(0,'end')
                            e_typ.delete(0,'end')
                            e_own.delete(0,'end')
                            e_use.delete(0,'end')
                            Messagebox.showinfo("delete status","deleted successfully");
                            con.close();
        
    
                    def engine():
                        root= Tk()
                        root.geometry("600x300")
                        root.title("engine")
                        bid = Label(root,text='enter coin initial ')
                        bid.place(x=20,y=30)
                        nodes = Label(root,text='enter node name')
                        nodes.place(x=20,y=60)
                        e_bid=Entry(root,width=20)
                        e_bid.place(x=150,y=30)
                        e_nodes=Entry(root,width=20)
                        e_nodes.place(x=150,y=60)


                        def insert():
                            bid=e_bid.get()
                            nodes= e_nodes.get()
                            if(bid=="" or nodes==""):
                                Messagebox.showinfo("insert Status","all fields are required")
                            else:
                                con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                                cursor=con.cursor()
                                query="insert into engine values('%s','%s')" % (bid,nodes)
                                cursor.execute(query)
                                cursor.execute("commit");
                                e_bid.delete(0,'end')
                                e_nodes.delete(0,'end')
                                Messagebox.showinfo("insert status","inserted successfully");
                                con.close();

                        def delete():
                            if(e_bid.get()==""):
                                MessageBox.showinfo("delete status","bid is compulsory for delete")
                            else:
                                con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                                cursor=con.cursor()
                                cursor.execute("delete from engine where BCEID='" + e_bid.get()+ "'")
                                cursor.execute("commit");
                                e_bid.delete(0,'end')
                                e_nodes.delete(0,'end')
                                Messagebox.showinfo("delete status","deleted successfully");
                                con.close();
        
    
    
        
                        insert=Button(root,text="insert",command=insert)
                        insert.place(x=20,y=140)

                        delete=Button(root,text="delete",command=delete)
                        delete.place(x=70,y=140)

                           

        
                    def design():
                        root= Tk()
                        root.geometry("600x300")
                        root.title("design")
                        node = Label(root,text='enter node name')
                        node.place(x=20,y=30)
                        bp = Label(root,text='enter blockchain protocol name')
                        bp.place(x=20,y=60)
                        mp = Label(root,text='enter message protocol name')
                        mp.place(x=20,y=90)
                        e_node=Entry(root,width=20)
                        e_node.place(x=150,y=30)
                        e_bp=Entry(root,width=20)
                        e_bp.place(x=150,y=60)
                        e_mp=Entry(root,width=20)
                        e_mp.place(x=150,y=90)

                        def insert():
                            node=e_node.get()
                            bp= e_bp.get()
                            mp=e_mp.get()
                            if(node=="" or bp==""or mp==""):
                                Messagebox.showinfo("insert Status","all fields are required")
                            else:
                                con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                                cursor=con.cursor()
                                query="insert into design values('%s','%s','%s')" % (node,bp,mp)
                                cursor.execute(query)
                                cursor.execute("commit");
                                e_node.delete(0,'end')
                                e_bp.delete(0,'end')
                                e_mp.delete(0,'end')
                                Messagebox.showinfo("insert status","inserted successfully");
                                con.close();

                        def delete():
                            if(e_node.get()==""):
                                MessageBox.showinfo("delete status","node is compulsory for delete")
                            else:
                                con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                                cursor=con.cursor()
                                cursor.execute("delete from design where node='" + e_node.get()+ "'")
                                cursor.execute("commit");
                                e_node.delete(0,'end')
                                e_bp.delete(0,'end')
                                e_mp.delete(0,'end')
                                Messagebox.showinfo("delete status","deleted successfully");
                                con.close();
                        insert=Button(root,text="insert",command=insert)
                        insert.place(x=20,y=140)

                        delete=Button(root,text="delete",command=delete)
                        delete.place(x=70,y=140)
        
        
        
        
                    def consensus():
                        root= Tk()
                        root.geometry("600x300")
                        root.title("consensus")
                        node = Label(root,text='enter node name')
                        node.place(x=20,y=30)
                        fail = Label(root,text='enter failures')
                        fail.place(x=20,y=60)
                        sys = Label(root,text='enter the system')
                        sys.place(x=20,y=90)
                        con_algo= Label(root,text='enter the consensus algo')
                        con_algo.place(x=20,y=120)
                        e_node=Entry(root,width=20)
                        e_node.place(x=150,y=30)
                        e_fail=Entry(root,width=20)
                        e_fail.place(x=150,y=60)
                        e_sys=Entry(root,width=20)
                        e_sys.place(x=150,y=90)
                        e_con_algo=Entry(root,width=20)
                        e_con_algo.place(x=150,y=120)


                        def insert():
                            node=e_node.get()
                            fail= e_fail.get()
                            sys=e_sys.get()
                            con_algo=e_con_algo.get()
                            if(node=="" or fail==""or sys==""or con_algo==""):
                                Messagebox.showinfo("insert Status","all fields are required")
                            else:
                                con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                                cursor=con.cursor()
                                query="insert into consensus values('%s','%s','%s','%s')" % (node,fail,sys,con_algo)
                                cursor.execute(query)
                                cursor.execute("commit");
                                e_node.delete(0,'end')
                                e_fail.delete(0,'end')
                                e_sys.delete(0,'end')
                                e_con_algo.delete(0,'end')
                                Messagebox.showinfo("insert status","inserted successfully");
                                con.close();

                        def delete():
                            if(e_node.get()==""):
                                MessageBox.showinfo("delete status","node is compulsory for delete")
                            else:
                                con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                                cursor=con.cursor()
                                cursor.execute("delete from consensus where node='" + e_node.get()+ "'")
                                cursor.execute("commit");
                                e_node.delete(0,'end')
                                e_fail.delete(0,'end')
                                e_sys.delete(0,'end')
                                e_con_algo.delete(0,'end')
                                Messagebox.showinfo("delete status","deleted successfully");
                                con.close();
                        insert=Button(root,text="insert",command=insert)
                        insert.place(x=20,y=140)

                        delete=Button(root,text="delete",command=delete)
                        delete.place(x=70,y=140)
        
        
        
                    def fault():
                        root= Tk()
                        root.geometry("600x300")
                        root.title("fault_tolerance_system")
                        node= Label(root,text='enter node name')
                        node.place(x=20,y=30)
                        factor = Label(root,text='enter factor')
                        factor.place(x=20,y=60)
                        cat = Label(root,text='enter category')
                        cat.place(x=20,y=90)
                        red= Label(root,text='enter the redundancy')
                        red.place(x=20,y=120)
                        e_node=Entry(root,width=20)
                        e_node.place(x=150,y=30)
                        e_factor=Entry(root,width=20)
                        e_factor.place(x=150,y=60)
                        e_cat=Entry(root,width=20)
                        e_cat.place(x=150,y=90)
                        e_red=Entry(root,width=20)
                        e_red.place(x=150,y=120)


                        def insert():
                            node=e_node.get()
                            factor= e_factor.get()
                            cat=e_cat.get()
                            red=e_red.get()
                            if(node=="" or factor==""or cat==""or red==""):
                                Messagebox.showinfo("insert Status","all fields are required")
                            else:
                                con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                                cursor=con.cursor()
                                query="insert into fault_tolerance_system values('%s','%s','%s','%s')" % (node,factor,cat,red)
                                cursor.execute(query)
                                cursor.execute("commit");
                                e_node.delete(0,'end')
                                e_factor.delete(0,'end')
                                e_cat.delete(0,'end')
                                e_red.delete(0,'end')
                                Messagebox.showinfo("insert status","inserted successfully");
                                con.close();

                        def delete():
                            if(e_node.get()==""):
                                MessageBox.showinfo("delete status","node is compulsory for delete")
                            else:
                                con= mysql.connector.connect(host='localhost',user='root',passwd='apsjrc',database='blockchain_managesystem')
                                cursor=con.cursor()
                                cursor.execute("delete from fault_tolerance_system where node='" + e_node.get()+ "'")
                                cursor.execute("commit");
                                e_node.delete(0,'end')
                                e_factor.delete(0,'end')
                                e_cat.delete(0,'end')
                                e_red.delete(0,'end')
                                Messagebox.showinfo("delete status","deleted successfully");
                                con.close();
                        insert=Button(root,text="insert",command=insert)
                        insert.place(x=20,y=140)

                        delete=Button(root,text="delete",command=delete)
                        delete.place(x=70,y=140)
        
        
        
        
        
        
        
                    insert=Button(root,text="insert",command=insert)
                    insert.place(x=20,y=140)

                    delete=Button(root,text="delete",command=delete)
                    delete.place(x=70,y=140)

    

                    new=Button(root,text="engine button",command=engine)
                    new.place(x=120,y=140)

                    design=Button(root,text="design",command=design)
                    design.place(x=210,y=140)

                    con=Button(root,text="consensus",command=consensus)
                    con.place(x=300,y=140)


                    fault=Button(root,text="fault",command=fault)
                    fault.place(x=390,y=140)


                             
                    clear()
                    break

                else:
                    login = False
                    Messagebox.showinfo(title='error',message='login was unsuccessful')
                    clear()
                    break
                
                cursor.close();
                con.close();
            
            
    login=Button(window,text='login',fg='green',command=login)
    login.grid(row=5,column=0)   
    exit=Button(window,text='exit',command=window.destroy)
    exit.grid(row=6,column=0)
    
    
    
login=Button(root,text='login',command=login)
login.grid(row=7,column=0)
regis=Button(root,text='regis',command=registration)
regis.grid(row=8,column=0)
exit=Button(root,text='exit',command=root.destroy)
exit.grid(row=9,column=0)


# In[16]:


root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




