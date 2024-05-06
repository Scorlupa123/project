from tkinter import *
class Example:
    def __init__(self, a, b, c, d, e):
        self.master = Tk()
        self.label = Label(self.master, text=a)
        self.label.grid(row=0, column=1)
        self.button = Button(self.master, text=b, command=self.change_button_color)
        self.button.grid(row=1, column=0)
        self.button.config(bg='white')
        self.button1 = Button(self.master, text=c, command=self.change_button_color1)
        self.button1.grid(row=1, column=2)
        self.button1.config(bg='white')
        self.button2 = Button(self.master, text=d, command=self.change_button_color2)
        self.button2.grid(row=3, column=0)
        self.button2.config(bg='white')
        self.button3 = Button(self.master, text=e, command=self.change_button_color3)
        self.button3.grid(row=3, column=2)
        self.button3.config(bg='white')
        self.button4 = Button(self.master, text='Next', command=self.next_quastion)
        self.button4.grid(row=2, column=1)
        self.button4.config(bg='white')
        self.master.mainloop()

    def change_button_color(self):
        self.button.config(bg='red')
    def change_button_color1(self):
        self.button1.config(bg='red')
    def change_button_color2(self):
        self.button2.config(bg='red')
    def change_button_color3(self):
        self.button3.config(bg='green')
    def next_quastion(self):
        self.master.destroy()
        Example('123', '123', '123', '123','asdasd')

Example('asdasd','asdasd','asdasd','asdasd','esadasd')