from tkinter import *
window= Tk()
window.title("윈도우창 연습입니다")

label1 = Label(window, text="첫번째 텍스트")
label2 = Label(window,text="공부중",bg="magenta", width=20,height=5,anchor=SE)
window.resizable(width=False, height=False)



label1.pack()
label2.pack()

window.mainloop()
