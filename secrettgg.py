from tkinter import *
from tkinter import messagebox
import base64

code = None  # Define code as a global variable

def decrypt():
    global code  # Access the global variable code

    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        decrypted_message = base64.b64decode(decode_message).decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=300, height=150)

        text2.insert(END, decrypted_message)
    elif password == "":
        messagebox.showerror("Decryption", "Input password")
    else:
        messagebox.showerror("Decryption", "Invalid password")

def encrypt():
    global code  # Access the global variable code

    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encoded_message = message.encode("ascii")
        encrypted_message = base64.b64encode(encoded_message).decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=300, height=150)

        text2.insert(END, encrypted_message)
    elif password == "":
        messagebox.showerror("Encryption", "Input password")
    else:
        messagebox.showerror("Encryption", "Invalid password")

def main_screen():
    global screen
    global code  # Define code as a global variable

    screen = Tk()
    screen.geometry("375x398")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)

    global text1
    text1 = Text(font="Arial 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=10, width=350, height=150)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3839", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=23, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
