import random
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

imagenes = ["icon/ahorcado_0.gif", "icon/ahorcado_1.gif", "icon/ahorcado_2.gif", "icon/ahorcado_3.gif",
            "icon/ahorcado_4.gif", "icon/ahorcado_5.gif", "icon/ahorcado_6.gif", "icon/ahorcado_7.gif"]
errores = ["icon/emo6.gif", "icon/emo5.gif", "icon/emo4.gif", "icon/emo3.gif", "icon/emo2.gif",
           "icon/emo1.gif", "icon/emo0.gif"]
palabras = ''''hormiga babuino tejon murcielago oso castor
           camello gato almeja cobra pantera coyote cuervo
           ciervo perro burro pato aguila huron zorro rana
           cabra ganso halcon leon lagarto llama topo mono
           alce raton mula salamandra nutria buho panda loro
           paloma piton conejo carnero rata cuervo rinoceronte
           salmon foca tiburon oveja mofeta perezoso serpiente
           araña cigüeña cisne tigre sapo trucha pavo tortuga
           comadreja ballena lobo wombat cebra'''.split()
claves = [["A", "B", "C", "D", "E", "F"],
          ["G", "H", "I", "J", "K", "L"],
          ["M", "N", "Ñ", "O", "P", "Q"],
          ["R", "S", "T", "U", "V", "W"],
          ["X", "Y", "Z"], ]


def obtener_palabra(lista_palabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    indice_palabras = random.randint(0, len(lista_palabras)-1)
    return lista_palabras[indice_palabras]


def mostrar_aciertos():
    resultado = ''
    espacios_vacios = '_' * len(palabra_secreta)

    # completar los espacios vacíos con las letras adivinadas
    for item in range(len(palabra_secreta)):
        if palabra_secreta[item] in letras_correctas:
            espacios_vacios = espacios_vacios[:item] + palabra_secreta[item] + espacios_vacios[item+1:]

    # mostrar la palabra secreta con espacios entre cada letra
    for letra in espacios_vacios:
        resultado += letra + " "

    return resultado


def actualizar_imagenes(numero_errores):
    global life
    global label_life
    global image
    global label_image

    label_image.destroy()
    image = tkinter.PhotoImage(file=imagenes[numero_errores])
    label_image = tkinter.Label(mainWindow, image=image)
    label_image.grid(row=0, column=1, sticky='nsew')

    if numero_errores != 7:
        label_life.destroy()
        life = tkinter.PhotoImage(file=errores[numero_errores])
        label_life = tkinter.Label(life_frame, image=life)
        label_life.grid(row=2, column=0, sticky='new')


def nueva_partida():
    # Mostramos ventana indicando si se quiere jugar una nueva partida
    ventana_nueva_partida = tkinter.Toplevel(mainWindow)
    ventana_nueva_partida.geometry("-300-300")
    ventana_nueva_partida.title("Nueva partida")
    label_nueva_partida = tkinter.Label(ventana_nueva_partida, text="¿Quieres jugar una nueva partida?")
    label_nueva_partida.grid(row=0, column=0, columnspan=2)
    boton_salir = tkinter.Button(ventana_nueva_partida, text="Salir", command=mainWindow.destroy)
    boton_salir.grid(row=1, column=0)
    boton_nueva_partida = tkinter.Button(ventana_nueva_partida, text="Aceptar",
                                         command=lambda ventana=ventana_nueva_partida: inicializar(ventana))
    boton_nueva_partida.grid(row=1, column=1)

    # Para que sólo se pueda hacer cosas con esta ventana
    ventana_nueva_partida.grab_set()
    ventana_nueva_partida.mainloop()


def inicializar(nueva_ventana):
    global palabra_secreta

    nueva_ventana.destroy()

    actualizar_imagenes(0)
    letras_incorrectas.clear()
    letras_correctas.clear()
    palabra_secreta = obtener_palabra(palabras)
    result_text.set(mostrar_aciertos())

    for x in range(len(btn_matrix)):
        for y in range(len(btn_matrix[x])):
            btn_matrix[x][y].config(state='normal')


def pulsar_letra(rowx, coly):
    btn_matrix[rowx][coly].config(state='disabled')
    letra_seleccionada = claves[rowx][coly].lower()

    if letra_seleccionada in palabra_secreta:
        letras_correctas.append(letra_seleccionada)
        result_text.set(mostrar_aciertos())
        # Si todas las letras que pertenecen a la palabra secreta se encuentran en las letras_correctas
        # ya las hemos acertado todas. Hemos ganado y ofrecemos jugar una nueva partida
        acertado = True
        for letra in palabra_secreta:
            if letra not in letras_correctas:
                acertado = False
                break
        if acertado:
            actualizar_imagenes(7)
            nueva_partida()
    else:
        letras_incorrectas.append(letra_seleccionada)
        actualizar_imagenes(len(letras_incorrectas))
        # Si el número de letras incorrectas es igual al de imágenes -2, hemos perdido y ofrecemos jugar
        # una nueva partida
        if len(letras_incorrectas) == len(imagenes) - 2:
            nueva_partida()


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
result_text = tkinter.StringVar()
result = tkinter.Label(life_frame, textvariable=result_text)
result.grid(row=0, column=0, sticky='nsew')
# Label indicando el texto Vidas restantes
label_life = tkinter.Label(life_frame, text="Vidas restantes")
label_life.grid(row=1, column=0, sticky='sw')
# Imagen con las vidas restantes
life = tkinter.PhotoImage(file=errores[0])
label_life = tkinter.Label(life_frame, image=life)
label_life.grid(row=2, column=0, sticky='new')
# Imágen del ahorcado
image = tkinter.PhotoImage(file=imagenes[0])
label_image = tkinter.Label(mainWindow, image=image)
label_image.grid(row=0, column=1, sticky='nsew')
# Frame con los botones del alfabeto
keyPad = tkinter.Frame(life_frame)
keyPad.grid(row=3, column=0, sticky='nsew')
row = 0
btn_matrix = []
for keyRow in claves:
    col = 0
    row_matrix = []
    for key in keyRow:
        btn = tkinter.Button(keyPad, text=key[0], state="normal",
                             command=lambda x=row, y=col:
                             pulsar_letra(x, y))
        btn.grid(row=row, column=col, sticky=tkinter.E + tkinter.W)
        row_matrix.append(btn)
        col += 1
    btn_matrix.append(row_matrix)
    row += 1
# Botón salir
exitButton = tkinter.Button(life_frame, text="Salir", command=mainWindow.destroy)
exitButton.grid(row=4, column=0, sticky='sw')

life_frame.rowconfigure(0, weight=2)
life_frame.rowconfigure(1, weight=1)
life_frame.rowconfigure(2, weight=1)
life_frame.rowconfigure(3, weight=5)
life_frame.rowconfigure(4, weight=2)

letras_incorrectas = []
letras_correctas = []
palabra_secreta = obtener_palabra(palabras)
result_text.set(mostrar_aciertos())

# Actualizar
mainWindow.update()
mainWindow.mainloop()
