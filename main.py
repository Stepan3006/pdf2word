from tkinter import Tk, Label, Frame, Entry, Button
from tkinter import filedialog as fd
from pdf2docx import parse
import pathlib


def callback():
    name = fd.askopenfilename()
    ePath.config(state='normal')
    ePath.delete('1', 'end')
    ePath.insert('1', name)
    ePath.config(state='readonly')


def convert():
    pdf_file = ePath.get()
    word_file = pathlib.Path(pdf_file)
    word_file = word_file.stem + '.docx'
    parse(pdf_file, word_file)
    Label(root, text='Конвертация завершена', font='Arial 15 bold',
          fg='lime', bg='black'
          ).pack(pady=10)


root = Tk()
root.title('Конвертер pdf -> word')
root.geometry('400x300+300+300')
root.resizable(height=False, width=False)
root['bg'] = 'black'
btn_Raise = Button(root, text='Выбрать PDF файл', font='Arial 15 bold',
                   fg='lime', bg='black', command=callback
                   )
btn_Raise.pack(pady=10)
lbPath = Label(root, text='Путь к файлу:',
               font='Arial 15 bold',
               fg='lime', bg='black'
               )
lbPath.pack()
ePath = Entry(root, width=50, state='readonly')
ePath.pack(pady=10)
btnConvert = Button(root, text='PDF->WORD', font='Arial 15 bold',
                    fg='lime', bg='black', command=convert)
btnConvert.pack(pady=10)
root.mainloop()