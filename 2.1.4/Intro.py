 #   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("150x150")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack(padx=50)

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

bt_login = tk.Button(frame_login, text='Login')
bt_login.pack()



root.mainloop()
