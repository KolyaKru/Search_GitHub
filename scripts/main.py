from sqlparse import sql
from classes import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton  
from tkinter import scrolledtext

def userradbtnlick():
    list.delete(0, END)
    reposradbtn['value'] = 0
    userradbtn['value'] = 1
    namelabel ['text'] ='Введите имя пользователя:'
    nametextbox.grid(column=2, row=3)
    searchbtn.grid(column=3, row=3)
    
def reposradbtnclick():
    list.delete(0, END)
    infobox.delete(1.0,END)
    userradbtn['value'] = 0
    reposradbtn['value'] = 1
    namelabel ['text'] ='Введите название репозитория:'
    nametextbox.grid(column=2, row=3)
    searchbtn.grid(column=3, row=3)
    
def searchbtnclick():
    try:
        list.delete(0, END)
        if userradbtn['value'] == 1:
            repos = git.getrepos(nametextbox.get())

        if reposradbtn['value'] == 1:
            repos = git.getnamerepos(nametextbox.get())

        for repo in repos:
            list.insert(END, repo.name)
        infobox.grid(column=2, row=4)
        list.grid(column=1, row=4)
        infobtn.grid(column=1, row=5)
        
    except:
        messagebox.showinfo("Внимание","Такого нет!")

def infobtnclick():
    try:
        if userradbtn['value'] == 1:
           info = git.getinforepos(git.getrepos(nametextbox.get())[int(list.curselection()[0])])
           
        if reposradbtn['value'] == 1:
            info = git.getinforepos(git.getnamerepos(nametextbox.get())[int(list.curselection()[0])])

        infobox.delete(1.0,END)
        switchbtn.grid(column=2, row=5)
        downloadbtn.grid(column=3, row=5)
        savebtn.grid(column=3,row=4)
        infobox.insert(INSERT, 'Name: ' + info['name']
                                +'\nDescription: ' + info['description']
                                +'\nOwner: ' + info['owner']
                                +'\nDate created: ' + info['date_created']
                                +'\nDate of last push: ' + info['date_push']
                                + '\nHomepage: ' + info['homepage']
                                + '\nLanguage: ' + info['language']
                                + '\nURL: ' + info['url'])
        
    except:
        messagebox.showinfo("Внимание", "Ошибка!")

def switchbtnclick():
    try:
        if userradbtn['value'] == 1:
            git.switch(git.getrepos(nametextbox.get())[int(list.curselection()[0])])

        if reposradbtn['value'] == 1:
            git.switch(git.getnamerepos(nametextbox.get())[int(list.curselection()[0])])
    except:
        messagebox.showinfo("Внимание","Проблема с соединением!")

def downloadbtnclick():
    try:
        if userradbtn['value'] == 1:
            git.downloadrepo(git.getrepos(nametextbox.get())[int(list.curselection()[0])])

        if reposradbtn['value'] == 1:
            git.downloadrepo(git.getnamerepos(nametextbox.get())[int(list.curselection()[0])])
        messagebox.showinfo("Выполнено","Скачаны все ветки репозитория в папку <<Downloads>> на компьютере!")
    except:
        messagebox.showinfo("Внимание","Не удалось скачать!")

def savebtnclick():
    try:
        if userradbtn['value'] == 1:
            sql.insertdb(git.getrepos(nametextbox.get())[int(list.curselection()[0])])

        if reposradbtn['value'] == 1:
            sql.insertdb(git.getnamerepos(nametextbox.get())[int(list.curselection()[0])])
        messagebox.showinfo("Выполнено","Выбранный репозиторий добавлен в БД!")
    except:
        messagebox.showinfo("Внимание","Не удалось добавить!")

window = Tk()

git = Git()

sql = Sql()

window.title("Search GitHub")

window.geometry('1050x300')

lang = IntVar()

label = Label(window, text='Выберите способ поиска', font= ("Arial Bold", 20))
label.focus()
namelabel = Label(window, font= ("Arial Bold", 20))
list = Listbox(width=50, selectmode=SINGLE)
userradbtn= Radiobutton(window, text='Поиск по имени пользователя', variable=lang, command=userradbtnlick)  
reposradbtn = Radiobutton(window, text='Поиск по названию репозитория', variable=lang, command=reposradbtnclick)
nametextbox = Entry(window, width= 50)
infobtn = Button(window, text="Посмотреть информацию", command = infobtnclick)
searchbtn = Button(window, text="Поиск", command= searchbtnclick) 
switchbtn = Button(window, text="Перейти к репозиторию", command= switchbtnclick) 
downloadbtn = Button(window, text="Скачать репозиториий", command= downloadbtnclick) 
savebtn = Button(window, text="Сохранить в БД", command= savebtnclick) 
infobox = scrolledtext.ScrolledText(window, width=60,height=10)

label.grid(column=1, row=1)
userradbtn.grid(column=1, row=2)
reposradbtn.grid(column= 2, row=2)
namelabel.grid(column=1,row=3)

window.mainloop()





