from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

def clear():
    Emailentry.delete(0,END)
    USERNAMEentry.delete(0,END)
    PasswordEntry.delete(0,END)
    ConfirmPasswordEntry.delete(0,END)
    Check.set(0)

def connect_database():
    if Emailentry.get()=='' or USERNAMEentry.get=='' or PasswordEntry.get=='' or ConfirmPasswordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif PasswordEntry.get()!=ConfirmPasswordEntry.get():
        messagebox.showerror('Error','Password mismatch')
    elif Check.get()==0:
        messagebox.showerror('Error','Please accept terms and conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='Faith',password='@Faith4real')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue,please try again')
            return
        try:
            query='Create database userdetails'
            mycursor.execute(query)
            query='use userdetails'
            mycursor.execute(query)
            query='Create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdetails')
        query='select * from data where username=%s'
        mycursor.execute(query, (USERNAMEentry.get()))
        
        row= mycursor.fetchone()
        if row!=None:
            messagebox.Showbox('Error','Username already exists')
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(Emailentry.get(),USERNAMEentry.get(),PasswordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration Successful')
            clear()
            root.destroy()
            import login
       
root= Tk()
root.title('signup page')
root.geometry('800x700')
root.config(bg='white')
root.resizable(False,False)

def login_page():
    root.destroy()
    import login

img = Image.open('images/Tabletlogin.jpg')
#print(img.width,img.height)
#img.show()
imge= img.resize((int(img.width/4),int(img.height/4)))
#print(imge.width,imge.height)
#imge.show()
newpic= ImageTk.PhotoImage(imge)
mylabel= Label(root, image=newpic,bd=0)
mylabel.place(x=50,y=70)

heading= Label(root, text='CREATE AN ACCOUNT',bg='white',fg='black',font=('Times New Roman',14,'bold'))
heading.place(x=430,y=50)
frame1=Frame(root,bg='white',)
frame1.place(x=375,y=100)

EmailLabel= Label(frame1, text='Email',bg='white',fg='green',font=('Times New Roman',14,))
EmailLabel.grid(row=0,column=0,sticky='w',pady=(5,0))
Emailentry= Entry(frame1,bg='green',width=40,bd=0,fg='white',font=('Times New Roman',12,))
Emailentry.grid(row=1,column=0,sticky='w',pady=(8,0))

USERNAMELabel= Label(frame1, text='Username',bg='white',fg='green',font=('Times New Roman',14,))
USERNAMELabel.grid(row=2,column=0,sticky='w',pady=(5,0))
USERNAMEentry= Entry(frame1,bg='green',width=40,bd=0,fg='white',font=('Times New Roman',12,))
USERNAMEentry.grid(row=3,column=0,sticky='w',pady=(8,0))

PasswordLabel= Label(frame1, text='Paasword',bg='white',fg='green',font=('Times New Roman',14,))
PasswordLabel.grid(row=4,column=0,sticky='w',pady=(5,0))
PasswordEntry= Entry(frame1,bg='green',width=40,bd=0,fg='white',font=('Times New Roman',12,))
PasswordEntry.grid(row=5,column=0,sticky='w',pady=(8,0))

ConfirmPasswordLabel= Label(frame1, text='Confirm Paasword',bg='white',fg='green',font=('Times New Roman',14,))
ConfirmPasswordLabel.grid(row=6,column=0,sticky='w',pady=(5,0))
ConfirmPasswordEntry= Entry(frame1,bg='green',width=40,bd=0,fg='white',font=('Times New Roman',12,))
ConfirmPasswordEntry.grid(row=7,column=0,sticky='w',pady=(8,0))

Check=IntVar()
term_and_conditions=Checkbutton(root,text='I agree to the terms and conditions',bg='white',fg='green',variable=Check, font=('Times New Roman',12,))
term_and_conditions.place(x=372,y=360)

#Login button
Sign_up_button= Button(root,text='Signup',bd=0,width=29,height=1,bg='green',activebackground='white',command=connect_database,cursor='hand2',font=('Times New Roman',14, 'bold'),fg='white',activeforeground='green',)
Sign_up_button.place(x=375,y=405)

#Already have an acc.
LoginLabel= Label(root, text='Dont Have An Account?',bg='white',fg='black',font=('Times New Roman',12,))
LoginLabel.place(x=372,y=455)
#signup button
LoginButton=Button(root,text='Login',bd=0,bg='white',command=login_page,activebackground='white',cursor='hand2',font=('Times New Roman',12, 'bold'),fg='green',activeforeground='green')
LoginButton.place(x=580,y=456)

root.mainloop()