from tkinter import *
import tkinter.scrolledtext as scrolltext
from tkinter import filedialog , END,  messagebox
import re
import variable as var
import time

main_window = Tk()
frame = Frame(main_window)
textArea = scrolltext.ScrolledText(frame,height = 40)
canvas = Canvas(frame)
listvar = []
root = None

def quit(self):
    self.root.destroy()

def save_file():
    file = filedialog.asksaveasfile(mode='w')
    if file!=None:
        data = textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()

def compile():
    data = textArea.get('1.0',END+'-1c')
    file = open("temp.txt","w")
    file.write(data)
    file.close()
    listvar1= []
    root1 = None
    file = open("temp.txt","r")
    for i in file:
        if(i!=None):
            try:
                i = i.lstrip()
                canvas.delete("all")
                print(i)
                listvar,root = var.matcher(listvar1,i,root1)
                listvar1 = listvar
                root1 = root
                printer(root1)
                main_window.update()
                main_window.after(2000)
            except:
                print('Match not found')
    list_unused = []
    print(listvar)
    print(root.name)
    for x in listvar:
        if var.search(root, x.value) == False:
            list_unused.append(x)
    if len(list_unused) == 0:
        print(len(list_unused))
        messagebox.showinfo("Variable used", "All Variable Used")
    else:
        print(len(list_unused))
        str = ""
        for i in list_unused:
            str = str + i.name + " "
        messagebox.showwarning("Warning", "Variables "+str+" unused")
    file.close()

def printer(root):
    if root == None :
        rec1 = canvas.create_rectangle(200, 2, 230, 30)
        canvas.create_text(215, 16, fill="darkblue", font="Times 20 italic bold",text="-")
    else :
        rec1 = canvas.create_rectangle(200, 2, 230, 30)
        canvas.create_text(215, 16, fill="red", font="Times 20 italic bold", text=root.name)
        if root.left == None :
            rec2 = canvas.create_rectangle(140, 42, 170, 80)
            line1 = canvas.create_line(215, 30, 170, 42)
            canvas.create_text(155, 61, fill="darkblue", font="Times 20 italic bold", text="-")
        else :
            rec2 = canvas.create_rectangle(140, 42, 170, 80)
            line1 = canvas.create_line(215, 30, 170, 42)
            canvas.create_text(155, 61, fill="red", font="Times 20 italic bold", text=root.left.name)
            if root.left.left == None:
                line1 = canvas.create_line(155, 80, 135, 118)
                rec2 = canvas.create_rectangle(105, 118, 135, 156)
                canvas.create_text(120, 137, fill="darkblue", font="Times 20 italic bold", text="-")
            else:
                line1 = canvas.create_line(155, 80, 135, 118)
                rec2 = canvas.create_rectangle(105, 118, 135, 156)
                canvas.create_text(120, 137, fill="red", font="Times 20 italic bold", text=root.left.left.name)
            if root.left.right == None:
                line1 = canvas.create_line(155, 80, 175, 118)
                rec2 = canvas.create_rectangle(175, 118, 205, 156)
                canvas.create_text(190, 137, fill="darkblue", font="Times 20 italic bold", text="-")
            else:
                line1 = canvas.create_line(155, 80, 175, 118)
                rec2 = canvas.create_rectangle(175, 118, 205, 156)
                canvas.create_text(190, 137, fill="red", font="Times 20 italic bold", text=root.left.right.name)

        if root.right == None :
            line1 = canvas.create_line(215, 30, 260, 42)
            rec2 = canvas.create_rectangle(260, 42, 290, 80)
            canvas.create_text(275, 61, fill="darkblue", font="Times 20 italic bold", text="-")
        else :
            line1 = canvas.create_line(215, 30, 260, 42)
            rec2 = canvas.create_rectangle(260, 42, 290, 80)
            canvas.create_text(275, 61, fill="red", font="Times 20 italic bold", text=root.right.name)
            if root.right.left == None :
                line1 = canvas.create_line(275, 80, 255, 118)
                rec2 = canvas.create_rectangle(225, 118, 255, 156)
                canvas.create_text(240, 137, fill="darkblue", font="Times 20 italic bold", text="-")
            else :
                line1 = canvas.create_line(275, 80, 255, 118)
                rec2 = canvas.create_rectangle(225, 118, 255, 156)
                canvas.create_text(240, 137, fill="red", font="Times 20 italic bold", text=root.right.left.name)
            if root.right.right == None :
                line1 = canvas.create_line(275, 80, 295, 118)
                rec2 = canvas.create_rectangle(295, 118, 325, 156)
                canvas.create_text(310, 137, fill="darkblue", font="Times 20 italic bold", text="-")
            else :
                line1 = canvas.create_line(275, 80, 295, 118)
                rec2 = canvas.create_rectangle(295, 118, 325, 156)
                canvas.create_text(310, 137, fill="red", font="Times 20 italic bold", text=root.right.right.name)
def clearScreen():
    textArea.delete('1.0', END)

main_window.title("C Editor")

""""this is  my main menu"""
menu = Menu(main_window)
main_window.config(menu = menu)

'''Added my frame for simplicity'''
frame.pack()

'''This is text editor'''

textArea.pack(side = LEFT)

"""This is a submenu for file (clear screen and compile)"""
FileMenu = Menu(menu)
menu.add_cascade(label = "File",menu=FileMenu)
FileMenu.add_command(label="Clear Screen...",command=clearScreen)
FileMenu.add_command(label="Compile...",command=compile)
FileMenu.add_command(label="Save...",command=save_file)
FileMenu.add_separator()
FileMenu.add_command(label="Exit...", command=main_window.destroy)

'''adding a canvas'''
canvas.pack(side=LEFT)

'''adding a label to define errors in the code'''
label = Label(main_window,text="Error at line :")
label.pack(side=BOTTOM)
main_window.mainloop()
