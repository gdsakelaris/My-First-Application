import tkinter as tk
import sys
import time


root = tk.Tk()

canvas1 = tk.Canvas(root, bg = 'yellow', width = 1920, height = 1080)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(960, 350, window=entry1)


def fobot():

    global value
    value = entry1.get()

    label1 = tk.Label(root, bg = 'yellow',text="HELLO",fg='blue',font=('helvetica',35,'bold'))
    canvas1.create_window(960, 600, window=label1)

    labelname = tk.Label(root, bg = 'yellow',text = value.upper(), fg='purple1',font=('helvetica',35,'bold'))
    canvas1.create_window(960, 670, window = labelname)

    button2 = tk.Button(root, text="GOODBYE",fg='red',font=('Helvetica',25,'bold'),command = root.destroy)
    canvas1.create_window(960, 850, window=button2)

    
label2 = tk.Label(root, bg = 'yellow', text = 'FORMERLY "FOBOT"', fg='red',font=('helvetica',50,'bold'))
canvas1.create_window(960, 100, window = label2)

label3 = tk.Label(root, bg = 'yellow', text = 'ENTER YOUR NAME', fg='dark orange',font=('helvetica',25,'bold'))
canvas1.create_window(960, 250, window = label3)

button1 = tk.Button(text='Enter',fg='green',font=('helvetica',25,'bold'),command=fobot)
canvas1.create_window(960, 450, window=button1)

#button2 = tk.Button(root, bg = 'red', text="GOODBYE",fg='black',font=('Helvetica',12,'bold'),command = root.destroy)
#canvas1.create_window(250, 450, window=button2)


root.mainloop()
