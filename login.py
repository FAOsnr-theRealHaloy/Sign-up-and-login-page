from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

root= Tk()
root.title('login page')
root.geometry('800x700')
root.config(bg='white')
root.resizable(False,False)



def forget_password():
    def change_password():
        if usernameentry.get()=='' or passwordentry.get()==''or confirmpasswordentry.get()=='':
            messagebox.showerror('Error','All fields are required',parent= window)

        elif passwordentry.get()!=confirmpasswordentry.get():
            messagebox.showerror('Error','Password and confirming password are not matching',parent= window)
        else:
            con=pymysql.connect(host='localhost', user='Faith', password='@Faith4real', database='userdetails')
            mycursor=con.cursor()
            query='select * from data where username =%s'
            mycursor.execute(query,(usernameentry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect username',parent= window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(passwordentry.get(),usernameentry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, please login with new password',parent= window)
                window.destroy()

    window= Toplevel()
    window.title('Change password')

    window.resizable(False,False)

    img = Image.open('images/Tabletlogin.jpg')
    #print(img.width,img.height)
    #img.show()
    imge= img.resize((int(img.width/4),int(img.height/4)))
    #print(imge.width,imge.height)
    #imge.show()
    newpic= ImageTk.PhotoImage(imge)
    mylabel= Label(window, image=newpic,bd=0)
    mylabel.grid()

    heading= Label(window, text='RESET PASSWORD',bg='white',fg='black',font=('Times New Roman',16,'bold'))
    heading.place(x=273,y=50)

    usernameLabel= Label(window, text='Username',bg='white',fg='green',font=('Times New Roman',14,))
    usernameLabel.place(x=265,y=100)
    usernameentry= Entry(window,bg='white',width=25,bd=0,fg='white',font=('Times New Roman',12,))
    usernameentry.place(x=265,y=130)
    frame6=Frame(window,bg='green',width=200,)
    frame6.place(x=265,y=155)

    passwordLabel= Label(window, text='New Password',bg='white',fg='green',font=('Times New Roman',14,))
    passwordLabel.place(x=265,y=170)
    passwordentry= Entry(window,bg='white',width=25,bd=0,fg='white',font=('Times New Roman',12,))
    passwordentry.place(x=265,y=200)
    frame7=Frame(window,bg='green',width=200,)
    frame7.place(x=265,y=225)
    
    confirmpasswordLabel= Label(window, text='Confirm Password',bg='white',fg='green',font=('Times New Roman',14,))
    confirmpasswordLabel.place(x=265,y=240)
    confirmpasswordentry= Entry(window,bg='white',width=25,bd=0,fg='white',font=('Times New Roman',12,))
    confirmpasswordentry.place(x=265,y=270)
    frame8=Frame(window,bg='green',width=200,)
    frame8.place(x=265,y=295)
    #Login button
    Submit_button= Button(window,text='Submit',bd=0,width=15,bg='green',activebackground='white',command=change_password,cursor='hand2',font=('Times New Roman',14, 'bold'),fg='white',activeforeground='green',)
    Submit_button.place(x=280,y=350)

    window.mainloop()


def login_user():
    if usernameentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror('Error', 'All fields are requird')
    else:
        try:
            con=pymysql.connect(host='localhost',user='Faith',password='@Faith4real')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established, try again')
            return
        query='use user data'
        mycursor.execute(query)
        query='select * from data where username =%s and password=%s'
        mycursor.execute(query, (usernameentry.get(),passwordentry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error', 'invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'login is successul')
#def hide():
    #openeye.config(file='images/unsightedeyes.png')
    #passwordentry.config(show='*')
    #eye_Button.config(command=show)
#def show():
    #openeye.config(file='images/seenn.png')
    #passwordentry.config(show='')
    #eye_Button.config(command=hide)
def user_enter(event):
    if (usernameentry.get()=='Username'):
        usernameentry.delete(0,END)
def user_password(event):
    if (passwordentry.get()=='Password'):
        passwordentry.delete(0,END)
def signup_page():
    root.destroy()
    import signup


img = Image.open('images/Tabletlogin.jpg')
#print(img.width,img.height)
#img.show()
imge= img.resize((int(img.width/4),int(img.height/4)))
#print(imge.width,imge.height)
#imge.show()
newpic= ImageTk.PhotoImage(imge)
mylabel= Label(root, image=newpic,bd=0)
mylabel.place(x=50,y=70)
heading= Label(root, text='USER LOGIN',bg='white',fg='black',font=('Times New Roman',16,'bold'))
heading.place(x=480,y=50)
frame1=Frame(root,bg='white',)
frame1.place(x=375,y=100)
#usernameentry= Entry(root,bg='blue',width=30,fg='green',font=('Times New Roman',16,'bold'))
#usernameentry.place(x=400,y=120)
usernameentry= Entry(frame1,bg='white',width=40,bd=0,fg='green',font=('Times New Roman',12,))
usernameentry.grid(row=0,column=0)

usernameentry.insert(0,'Username')
usernameentry.bind('<FocusIn>',user_enter)
frame2=Frame(frame1,bg='green',width=330,)
frame2.grid(row=1,column=0, pady=10)

passwordentry= Entry(frame1,bg='white',bd=0,width=40,fg='green',font=('Times New Roman',12,))
passwordentry.grid(row=2,column=0,pady=(10,0))

passwordentry.insert(0,'Password')
passwordentry.bind('<FocusIn>',user_password)
frame3=Frame(frame1,bg='green',width=330,)
frame3.grid(row=3,column=0,pady=(10,0) )

#password eye button
see = Image.open('images/seenn.png')
print(see.width,see.height)
openeye= ImageTk.PhotoImage(see)

eye_Button=Button(root,image=openeye,bg='white',bd=0, fg='green')
eye_Button.place(x=689,y=159)

#Forget password
forgetpasswordbutton= Button(root,text='Forget Password?',bd=0,command=forget_password, bg='white',activebackground='white',cursor='hand2',fg='green',activeforeground='green')
forgetpasswordbutton.place(x=610,y=200)
#Login button
Loginbutton= Button(root,text='Login',bd=0,bg='green',command=login_user, activebackground='white',cursor='hand2',font=('Times New Roman',13, 'bold'),fg='white',activeforeground='green')
Loginbutton.place(x=375,y=230)



OrLabel= Label(root, text='--------------------------OR------------------------',bg='white',fg='grey',font=('Times New Roman',14,))
OrLabel.place(x=374,y=280)
#fb,twitter and google logo
facebook_logo=PhotoImage(file='images/logo fb.png')
fbLabel=Label(root,image=facebook_logo,bg='white')
fbLabel.place(x=448,y=315)

instagram_logo=PhotoImage(file='images/logo linkedin.png')
instaLabel=Label(root,image=instagram_logo,bg='white')
instaLabel.place(x=580,y=312)

twitter_logo=PhotoImage(file='images/twitter.png')
xLabel=Label(root,image=twitter_logo,bg='white')
xLabel.place(x=515,y=316)

#Dont have an acc.
signupLabel= Label(root, text='Dont Have An Account?',bg='white',fg='black',font=('Times New Roman',13,))
signupLabel.place(x=374,y=401)
#signup button
newaccountButton=Button(root,text='Create New One',command=signup_page,bd=0,bg='white',activebackground='white',cursor='hand2',font=('Times New Roman',13, 'bold'),fg='green',activeforeground='green')
newaccountButton.place(x=580,y=400)


root.mainloop()