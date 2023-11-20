import tkinter as tk
from tkinter import *
from tkinter import messagebox

def GUI():
    def newTask():
        task = entry_box.get()
        if task != "":
            lb.insert(END, task)
            entry_box.delete(0, "end")
        else:
            messagebox.showwarning("warning", "Please enter some task.")

    def deleteTask():
        lb.delete(ANCHOR)

    mwindow = tk.Tk()
    mwindow.title("To-Do-List")
    mwindow.geometry('500x450+500+200')
    mwindow.config(bg='#223441')
    mwindow.resizable(width=False, height=False)

    frame = Frame(mwindow)
    frame.pack(pady=6)

    lb = Listbox(
        frame,
        width=25,
        height=8,
        font=('Annai MN', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        #No move when the focus on an item.
        selectbackground='#a6a6a6',
        activestyle="dotbox",
    )
    lb.pack(side=LEFT, fill=BOTH)

    task_list = [
        'GEt up',
        'GO to sleep',
        'Eating ',
        'Thinking'
    ]

    for item in task_list:
        lb.insert(END, item)

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)

    entry_box = Entry(
        mwindow,
        font=('times', 24)
    )

    entry_box.pack(pady=20)

    button_frame = Frame(mwindow)
    button_frame.pack(pady=20)

    addTask_btn = Button(
        button_frame,
        text='Add Task',
        font=('times 14'),
        bg='#c5f776',
        padx=20,
        pady=10,
        command=newTask
    )
    addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    delTask_btn = Button(
        button_frame,
        text='Delete Task',
        font=('times 14'),
        bg='#ff8b61',
        padx=20,
        pady=10,
        command=deleteTask
    )
    delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


    mwindow.mainloop()


if __name__ == '__main__':
    GUI()


