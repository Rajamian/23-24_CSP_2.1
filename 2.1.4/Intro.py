 #   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_botton():
    if(ent_username.get() == "Username" and ent_password.get() == "Password"):
        frame_auth.tkraise()
    else:
        fail_label = tk.Label(frame_login, text="Invalid combination")
        fail_label.pack()
# main window
root = tk.Tk()
root.wm_geometry("175x175")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()

frame_auth =tk.Frame(root)
frame_auth.grid(row=0,column=0,sticky="news")

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack(padx=50)

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

bt_login = tk.Button(frame_login, text='Login',command=test_my_botton)
bt_login.pack()

frame_login.tkraise()

root.mainloop()
