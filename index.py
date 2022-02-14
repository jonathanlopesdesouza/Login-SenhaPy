#Importar as bibliotecas
from ast import Pass
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Databaser
#Criar Janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.config(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")

#===== Carregando Imagens ========

logo = PhotoImage(file="icons/logo.png")

# ======= Widgets ===============

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame= Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=3, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=145, y=115)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=154)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=145, y=164)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    Databaser.cursor.execute("""
    SELECT * FROM Users 
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print ("Selected")
    VerifyLogin = Databaser.cursor.fetchone()
    try:
         if ( User in VerifyLogin and Pass in VerifyLogin):
           messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acess Denied!")

#Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    #Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHT BLUE", fg="white")
    NomeLabel.place(x=5, y = 5)

    NomeEntry = ttk.Entry(RightFrame, width=38)
    NomeEntry.place(x=100, y=17)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHT BLUE", fg="white")
    EmailLabel.place(x=5, y= 55)

    EmailEntry = ttk.Entry (RightFrame, width=38)
    EmailEntry.place(x=100, y=67)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User  = UserEntry.get()
        Pass = PassEntry.get()
        
        if (Name == "" and Email == "" and User == "" and Pass == ""):
             messagebox.showerror(tittle="Register Error", message="Preencha Todos os Campos")
        else:
             Databaser.cursor.execute("""
                INSERT INTO Users (Name, Email, User, Password) VALUES (?, ?, ?, ?)
                """, (Name, Email, User, Pass))
             Databaser.conn.commit()
             messagebox.showinfo(title="Register Info", message="Account Created Sucess")

    Register = ttk.Button(RightFrame, text="Register", width=20, command=RegisterToDataBase)
    Register.place(x=125, y=225)  

    def BackToLogin():
        #Removendo Widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo de volta os Widgets de Login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)


    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

          
RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()
