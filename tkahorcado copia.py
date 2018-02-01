import random
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

images = ["icon/ahorcado_0.gif", "icon/ahorcado_1.gif", "icon/ahorcado_2.gif", "icon/ahorcado_3.gif",
          "icon/ahorcado_4.gif", "icon/ahorcado_5.gif", "icon/ahorcado_6.gif"]
errors = ["icon/emo6.gif", "icon/emo5.gif", "icon/emo4.gif", "icon/emo3.gif", "icon/emo2.gif",
          "icon/emo1.gif", "icon/emo0.gif"]
words = ''''hormiga babuino tejon murcielago oso castor
           camello gato almeja cobra pantera coyote cuervo
           ciervo perro burro pato aguila huron zorro rana
           cabra ganso halcon leon lagarto llama topo mono
           alce raton mula salamandra nutria buho panda loro
           paloma piton conejo carnero rata cuervo rinoceronte
           salmon foca tiburon oveja mofeta perezoso serpiente
           araña cigüeña cisne tigre sapo trucha pavo tortuga
           comadreja ballena lobo wombat cebra'''.split()
keys = [["A", "B", "C", "D", "E", "F"],
        ["G", "H", "I", "J", "K", "L"],
        ["M", "N", "Ñ", "O", "P", "Q"],
        ["R", "S", "T", "U", "V", "W"],
        ["X", "Y", "Z"], ]


def obtain_word(words_list):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    words_index = random.randint(0, len(words_list)-1)
    return words_list[words_index]


def push_button(rowx, coly, images, lf, result, letras_incorrectas, letras_correctas, palabra_secreta):
    btn_matrix[rowx][coly].config(state='disabled')
    intento = keys[rowx][coly]

    if intento in palabra_secreta:
        letras_correctas = letras_correctas + intento

        # Verifica si el jugador ha ganado
        encontradas_todas_letras = True
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letras_correctas:
                encontradas_todas_letras = False
                break
        if encontradas_todas_letras:
            print("¡Si! ¡La palabra secreta es {}! ¡Has ganado!".format(palabra_secreta))
    else:
        letras_incorrectas = letras_incorrectas + intento
        error = len(letras_incorrectas)
        print(letras_incorrectas)
        print(error)
    #    theimage = tkinter.PhotoImage(file=images[error])
    #    images.config(image=theimage)
    #     thelife = tkinter.PhotoImage(file=errors[error])
    #     lf.config(image=thelife)




letras_incorrectas = ''
correct_letters = ''
secret_word = obtain_word(words)
mainWindowPadding = 10
mainWindow = tkinter.Tk()
mainWindow.title("Ahorcado")
mainWindow.geometry("540x540-200-200")
# mainWindow.configure(background='grey')
mainWindow['padx'] = mainWindowPadding
mainWindow['pady'] = mainWindowPadding
mainWindow.minsize(540, 540)
mainWindow.maxsize(540, 540)


# Frame
life_frame = tkinter.Frame(mainWindow)
life_frame.grid(row=0, column=0, sticky='nsew')
# Label con el resultado
result = tkinter.Label(life_frame, text='_ ' * len(secret_word))
result.grid(row=0, column=0, sticky='nsew')
# Label indicando el texto Vidas restantes
label_life = tkinter.Label(life_frame, text="Vidas restantes")
label_life.grid(row=1, column=0, sticky='sw')
# Imagen con las vidas restantes
life = tkinter.PhotoImage(file=errors[0])
label_life = tkinter.Label(life_frame, image=life)
label_life.grid(row=2, column=0, sticky='new')
# Imágen del ahorcado
image = tkinter.PhotoImage(file=images[0])
label_image = tkinter.Label(mainWindow, image=image)
label_image.grid(row=0, column=1, sticky='nsew')
# Frame con los botones del alfabeto
keyPad = tkinter.Frame(life_frame)
keyPad.grid(row=3, column=0, sticky='nsew')
row = 0
btn_matrix = []
for keyRow in keys:
    col = 0
    row_matrix = []
    for key in keyRow:
        btn = tkinter.Button(keyPad, text=key[0], state="normal",
                             command=lambda x=row, y=col, img=label_image, lf=label_life,
                                            re=result, in_let=letras_incorrectas,
                                            co_let=correct_letters, se_wo=secret_word:
                             push_button(x, y, img, lf, re, in_let, co_let, se_wo))
        btn.grid(row=row, column=col, sticky=tkinter.E + tkinter.W)
        row_matrix.append(btn)
        col += 1
    btn_matrix.append(row_matrix)
    row += 1
# Botón de salir
exitButton = tkinter.Button(life_frame, text="Salir", command=mainWindow.destroy)
exitButton.grid(row=4, column=0, sticky='sw')

life_frame.rowconfigure(0, weight=2)
life_frame.rowconfigure(1, weight=1)
life_frame.rowconfigure(2, weight=1)
life_frame.rowconfigure(3, weight=5)
life_frame.rowconfigure(4, weight=2)

# Actualizar
mainWindow.update()
mainWindow.mainloop()
