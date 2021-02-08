from tkinter import *
from tkinter import ttk
from dictionary import DictionaryPtBr as dic


def ok():
    name_var.set(name.get())
    frases = name.get().split(".")
    text_var.set("")
    text = ""
    count = 0
    for frase in frases:
        if not frase:
            continue

        count += 1
        palavras = frase.split(" ")
        text += str(count) + ") "

        for palavra in palavras:
            if word_type.get() == 1 and palavra.lower() in dic.verbs:
                text += "___________ "
                print("achou o verbo - " + palavra)
                continue
            elif word_type.get() == 2 and palavra.lower() in dic.subs:
                text += "___________ "
                print("achou o substantivo - " + palavra)
                continue
            elif word_type.get() == 3 and palavra.lower() in dic.names:
                text += "___________ "
                print("achou o nome - " + palavra)
                continue
            else:
                text += palavra.strip() + " "
        text += "\n"

    text_var.set(text)


def limpar():
    name_var.set("Nome")
    onevar.set(False)
    twovar.set(False)
    threevar.set(False)


def select_word_type():
    name_var.set(name_var.get() + " | " + str(word_type.get()))


root = Tk(screenName="D&D", baseName="RPG")

content = ttk.Frame(root, style="Fun.TButton")
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100, style="Fun.TButton")
text_var = StringVar()
text_var.set("Hoje eu comprei frutas para comer.")

textlbl = ttk.Label(frame, textvariable=text_var, style="Fun.TButton")

name_var = StringVar()
name_var.set("Frase")

namelbl = ttk.Label(content, textvariable=name_var, style="Fun.TButton")
name = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

word_type = IntVar()

# one = ttk.Checkbutton(content, text="Guerreiro", variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text="Mago", variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text="Ladino", variable=threevar, onvalue=True)

verb_radio = ttk.Radiobutton(content, text="Verbos", variable=word_type, value=1, command=select_word_type)
subs_radio = ttk.Radiobutton(content, text="Substantivos", variable=word_type, value=2, command=select_word_type)
names_radio = ttk.Radiobutton(content, text="Nomes", variable=word_type, value=3, command=select_word_type)

ok = ttk.Button(content, text="Ok", command=ok, style="Fun.TButton")
cancel = ttk.Button(content, text="Limpar", command=limpar, style="Fun.TButton")

content.grid(column=0, row=0)

frame.grid(column=0, row=0, columnspan=3, rowspan=2)

textlbl.grid(column=0, row=0)

namelbl.grid(column=3, row=0, columnspan=2)

name.grid(column=3, row=1, columnspan=4)

# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)

verb_radio.grid(column=0, row=3)
subs_radio.grid(column=1, row=3)
names_radio.grid(column=2, row=3)

ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.mainloop()

# Zé vai sair. Gosto da colher azul. Vou te falar pra pegar essa vassoura e sair voando.
