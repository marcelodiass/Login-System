from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1200x600+350+200")
        self.root.resizable(False, False)

        # Imagem de fundo
        self.bg = ImageTk.PhotoImage(file="images/imagem_fundo.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Form Login
        frame_login = Frame(self.root, bg="#04131e")
        frame_login.place(x=350, y=100, width=500, height=400)

        # Titulo e subtitulo
        title = Label(frame_login, text="Login Here", font=("Inter", 30, "bold"), fg="#05aaeb", bg="#04131e").place(x=65, y=20)
        subtitle = Label(frame_login, text="Members Login Area", font=("Inter", 15, "bold"), fg="#05aaeb", bg="#04131e").place(x=65, y=80)
        
        # Username
        lbl_user = Label(frame_login, text="Username", font=("Inter", 15), fg="#066ba8", bg="#04131e").place(x=65, y=130)
        self.username = Entry(frame_login, font=("Inter", 15), bg="#E7E6E6")
        self.username.place(x=65, y=160, width=300, height=35)

        # Senha
        lbl_password = Label(frame_login, text="Password", font=("Inter", 15), fg="#066ba8", bg="#04131e").place(x=65, y=205)
        self.password = Entry(frame_login, font=("Inter", 15), bg="#E7E6E6")
        self.password.place(x=65, y=235, width=300, height=35)

        # Botão Esqueci a Senha
        btn_forget = Button(frame_login, command=self.check_function, cursor="hand2", text="Forgot password?", bd=0, font=("Inter", 12), fg="#066ba8", bg="#04131e").place(x=65, y=285)

        # Botão Entrar
        btn_login = Button(frame_login, command=self.check_function, cursor="hand2", text="Login", bd=0, font=("Inter", 15), bg="#05aaeb", fg="#04131e").place(x=65, y=335, width=180, height=40)


    # Funções

    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get()!="marcelo" or self.password.get()!="123456":
            messagebox.showerror("Error", "Invalid username or password!", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}!")


root = Tk()
obj = Login(root)
root.mainloop()