from tkinter import *
import tkinter.font as font

# col = ["black", "white", "violet", "purple", "blue", "powderblue", "light grey", "dark grey"]
col = ["black", "white", "#A5DEF2", "#1E80C1", "#5BAEB7", "#A5DEF2", "#414C6B", "#414C6B"]
calc = ""

root = Tk()
root.title("Calculator by ZP")
root.geometry("532x512+880+350")
root.resizable(False, False)
root.configure(bg=col[6])  # 2

myFont = font.Font(family='Calibra',
                   size=15,
                   weight="bold")

cFont = ("Calibra",
         30,
         "bold")


# SHOW VALUES
def show(value):
    global calc
    calc += value
    input_result.config(text=calc)


# CLEAR VALUES
def clear():
    global calc
    calc = ""
    input_result.config(text=calc)


# CALCULATE VALUES
def calculate():
    global calc
    result = ""
    if calc != "":
        try:
            result = eval(calc)
        except ZeroDivisionError:
            result = "Error - Division by zero"
            calc = ""
        except SyntaxError:
            result = "Error - Invalid Input"
            calc = ""
    input_result.config(text=result)


# MAIN INPUT
input_result = Label(root, width=23, height=2, fg=col[1], bg=col[7], text="", font=("Calibra", 36))
input_result.place(x=0, y=50)
input_result.pack()


# BUTTONS
btn_c = Button(root, text="Clear", width=5, height=1,
               font=cFont, bd=1, fg=col[1], bg=col[4],
               command=lambda: clear())
btn_c.place(x=265, y=100)

btn_d = Button(root, text="/", width=5, height=1,
               font=cFont, bd=1, fg=col[1], bg=col[3],
               command=lambda: show("/"))
btn_d.place(x=399, y=346)

btn_per = Button(root, text="%", width=5, height=1,
                 font=cFont, bd=1, fg=col[1], bg=col[3],
                 command=lambda: show("%"))
btn_per.place(x=135, y=100)

btn_m = Button(root, text="x", width=5, height=1,
               font=cFont, bd=1, fg=col[1], bg=col[3],
               command=lambda: show("*"))
btn_m.place(x=399, y=100)

btn7 = Button(root, text="7", width=5, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("7"))
btn7.place(x=5, y=182)

btn8 = Button(root, text="8", width=5, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("8"))
btn8.place(x=135, y=182)

btn9 = Button(root, text="9", width=5, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("9"))
btn9.place(x=265, y=182)

btn_s = Button(root, text="-", width=5, height=1,
               font=cFont, bd=1, fg=col[1], bg=col[3],
               command=lambda: show("-"))
btn_s.place(x=399, y=182)

btn4 = Button(root, text="4", width=5, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("4"))
btn4.place(x=5, y=264)

btn5 = Button(root, text="5", width=5, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("5"))
btn5.place(x=135, y=264)

btn6 = Button(root, text="6", width=5, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("6"))
btn6.place(x=265, y=264)

btn_a = Button(root, text="+", width=5, height=1,
               font=cFont, bd=1, fg=col[1], bg=col[3],
               command=lambda: show("+"))
btn_a.place(x=399, y=264)

btn1 = Button(root, text="1", width=5, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("1"))
btn1.place(x=5, y=346)

btn2 = Button(root, text="2", width=5, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("2"))
btn2.place(x=135, y=346)

btn3 = Button(root, text="3", width=5, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("3"))
btn3.place(x=265, y=346)

btnDot = Button(root, text=".", width=5, height=1,
                font=cFont, bd=1, fg=col[1], bg=col[3],
                command=lambda: show("."))
btnDot.place(x=5, y=100)

btn0 = Button(root, text="0", width=9, height=1,
              font=cFont, bd=1, fg=col[1], bg=col[2],
              command=lambda: show("0"))
btn0.place(x=5, y=428)

btn_e = Button(root, text="=", width=12, height=1,
               font=cFont, bd=1, fg=col[1], bg=col[4],
               command=lambda: calculate())
btn_e.place(x=231, y=428)

mainloop()

# Created by ZP
