from tkinter import *

class Question:
    def __init__(self, que, arr_ans, arr_col):
        self.question = que
        self.answers = arr_ans
        self.colors = arr_col

    def get_question(self):
        return self.question

    def get_answer(self, id):
        return self.answers[id]

    def get_color(self, id):
        return self.colors[id]
        
class QuestionsManager:
    def __init__(self):
        self.data = []
        self.cursor = -1

    def next(self):
        self.cursor += 1

    def add_data(self, que, arr_ans, arr_col):
        if self.cursor == -1:
            self.cursor = 0
        self.data.append(Question(que, arr_ans, arr_col))

    def get_data(self):
        return self.data[self.cursor]

    def set_cursor(self, ind):
        self.cursor = ind

    def get_cursor(self):
        return self.cursor

QM = QuestionsManager()

QM.add_data('умный?', ['да', 'нет', 'не уверен', 'точно нет'], ['red', 'red', 'red', 'green'])
QM.add_data('умный?', ['да', 'нет', 'не уверен', 'точно нет'], ['red', 'green', 'red', 'red'])
QM.add_data('умный?', ['да', 'нет', 'не уверен', 'точно нет'], ['red', 'red', 'red', 'green'])
QM.add_data('умный?', ['да', 'нет', 'не уверен', 'точно нет'], ['red', 'red', 'red', 'green'])

master = Tk()

class Example:
    def __init__(self):
        self.data = QM.get_data()
        self.label = Label(master, text=f'{QM.get_cursor() + 1}: {self.data.get_question()}')
        self.label.grid(row=0, column=1)
        self.button = Button(master, text=self.data.get_answer(0), command=self.change_button_color)
        self.button.grid(row=1, column=0)
        self.button.config(bg='white')
        self.button1 = Button(master, text=self.data.get_answer(1), command=self.change_button_color1)
        self.button1.grid(row=1, column=2)
        self.button1.config(bg='white')
        self.button2 = Button(master, text=self.data.get_answer(2), command=self.change_button_color2)
        self.button2.grid(row=3, column=0)
        self.button2.config(bg='white')
        self.button3 = Button(master, text=self.data.get_answer(3), command=self.change_button_color3)
        self.button3.grid(row=3, column=2)
        self.button3.config(bg='white')
        self.button4 = Button(master, text='Next', command=self.next_quastion)
        self.button4.grid(row=2, column=1)
        self.button4.config(bg='white')
        master.mainloop()

    def change_button_color(self):
        self.button.config(bg=self.data.get_color(0))

    def change_button_color1(self):
        self.button1.config(bg=self.data.get_color(1))

    def change_button_color2(self):
        self.button2.config(bg=self.data.get_color(2))

    def change_button_color3(self):
        self.button3.config(bg=self.data.get_color(3))

    def next_quastion(self):
        destroy_object = [self.label, self.button, self.button1, self.button2, self.button3, self.button4]
        for object_name in destroy_object:
            object_name.destroy()
        QM.next()
        self.__init__()

Example()
