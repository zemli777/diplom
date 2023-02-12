from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

import graph
from graph import graph_build, graph_update
from dir_create import dir_graf
from pars_file import db_pars




root = Tk()
root.title("METANIT.COM")
root.geometry("1500x1500")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

path = 'graph1.png'

# создаем рабочую область
frame1_2 = tk.Frame(root)
frame1_2.pack()


#Добавим изображение
def print_image(path):
    canvas = tk.Canvas(frame1, height=1000, width=1000)
    image = Image.open(path)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw',image=photo)
    canvas.pack()


def load_image(name):
    img = Image.open(name)
    img.thumbnail((1000, 1000), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

canvas = tk.Canvas(frame1, width=1000, height=1000)
canvas.pack()

def set_image(image):
    canvas.delete("all")
    canvas.create_image(500,500, image=image)


# добавим ввод для матрицы смежности
# 2
# и матрицу смежности
image = load_image("graph1.png")

image2 = load_image('graph1.png')
set_image(image)

#frame = tk.Frame(frame1)
imput_str = tk.StringVar()
# 4

# 3
def entry_set_call(name, index, mode):
    text = imput_str.get()
    if int(text) == 0:

        imput_str.set(0)
        return
    elif int(text) == 1:
        imput_str.set(1)
        return
    else:
        imput_str.set(0)
    return 0

imput_str.trace_variable("w", entry_set_call)
# 5
tab1 = []
last = 0

frame1_2.pack()
last = 0
t = tk.Entry(frame1_2)
t.grid()

def do_table(x: int):
    global tab1
    tab1.clear()
    for i in range(x):
        for j in range(x):
            tab = tk.Entry(frame1_2,width=4, font=("Helvetica", 12))
            tab1.append(tab)
            tab.insert(0,"0")
            tab.grid(row=i, column=j)


def clear_table(x: int):
    for i in range(last*last):
        tab1[i].destroy()


def tab():
    global last
    clear_table(last)
    last = int(t.get())
    do_table(last)

def save_table():
    k = []
    for i in range(last):
        buf = []
        for j in range(last):
            buf.append(tab1[i*last+j].get())
        k.append(buf)
    global dir
    dir = dir_graf('create_new_graph')
    graph_build(dir[1], k)
    global image2
    image2 = load_image(f'{dir[1]}.png')
    set_image(image2)


def update_table():
    k = []
    for i in range(last):
        buf = []
        for j in range(last):
            buf.append(tab1[i*last+j].get())
        k.append(buf)
    global dir
    global image2
    graph_update(dir[1], k)
    image2 = load_image(f'{dir[1]}.png')
    set_image(image2)

def view_db():
    db_pars()


b = tk.Button(root, text="Press", command=tab).pack()
c = tk.Button(root, text='Create', command=save_table).pack()
u = tk.Button(root, text='Update', command=update_table).pack()
v = tk.Button(root, text='DATA', command=view_db).pack()

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Калькулятор")
notebook.add(frame2, text="Теория")
notebook.add(frame3, text="Задачи")


root.mainloop()







