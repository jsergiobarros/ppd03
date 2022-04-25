import threading
from tkinter import messagebox

import instancia
from tkinter import *

sensores=Tk()  # tela inicial, de selecionar peça e definir nome de usuário
sensores.geometry("400x200")
sensores.resizable(False, False)
sensores.title("Sensor")
canvas0=Canvas(sensores, width=400, height=200)
label = Label(canvas0, width=20, text="digite o Nome do sensor")
nome = Entry(canvas0, width=20)
nome.insert(0,"Digite")
foto0 = PhotoImage(file="temperatura.png")
foto1 = PhotoImage(file="umidade.png")
foto2 = PhotoImage(file="velocidade.png")
button1 = Button(canvas0, image=foto0, borderwidth=0, command = lambda: getNome("Temperatura",foto0))
button2 = Button(canvas0, image=foto1, borderwidth=0, command = lambda: getNome("Umidade",foto1))
button3 = Button(canvas0, image=foto2, borderwidth=0, command = lambda: getNome("Velocidade",foto2))



def inst(topico,nome,linf,lsup):
    try:
        if float(linf) > float(lsup):
            float("as")
        sensor = threading.Thread(target=instancia.instancia, args=(topico, nome, linf, lsup))
        sensor.start()
    except:
        messagebox.showerror(title="valor incorreto", message="valor nao aceito, \ntente novamente")




def getNome(txt,foto):
    canvas0.create_line(0, 180, 400, 180, fill="black", width=1)
    sensores.geometry("400x400")
    limiteInf.delete(0, END)
    limiteSup.delete(0, END)
    label1["text"]="Sensor de "+txt+"\n\nLimite Inferior"
    button4["image"]=foto
    limiteInf.grid( row=1)
    label2.grid(row=2)
    limiteSup.grid(row=3)
    button4.grid(pady=20,row=4)

    if txt=="Temperatura":
        limiteInf.insert(0, 0)
        limiteSup.insert(0,35)
        button4["command"] = lambda: inst("Temperatura",nome.get(),limiteInf.get(),limiteSup.get())
    elif txt=="Umidade":
        limiteInf.insert(0, 30)
        limiteSup.insert(0,70)
        button4["command"] = lambda: inst("Umidade",nome.get(),limiteInf.get(),limiteSup.get())
    elif txt=="Velocidade":
        limiteInf.insert(0, 20)
        limiteSup.insert(0,100)
        button4["command"] = lambda: inst("Velocidade",nome.get(),limiteInf.get(),limiteSup.get())


label.grid(pady=20,row=0,column=1)
nome.grid(pady=10,row=1,column=1)
button1.grid(pady=20,row=2, column=0)
button2.grid(pady=20,padx=10,row=2, column=1)
button3.grid(pady=20,row=2, column=2)
canvas1=Canvas(sensores,width=400, height=100)
button4 = Button(canvas1, image=foto2, borderwidth=0)
label1 = Label(canvas1,text="")
limiteInf = Entry(canvas1, width=20)
label2 = Label(canvas1,text="limite Superior")
limiteSup = Entry(canvas1, width=20)
label1.grid(row=0)


canvas0.pack()
canvas1.pack()
sensores.mainloop()