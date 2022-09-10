import random
import tkinter as tk

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

while 1:
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(characters)
            password = password + password_char
        print("パスワードがここだ : ", password)
        
root = tk.Tk()
root.geometry("300x275")

root.mainloop()
