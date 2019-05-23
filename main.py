"""
5/23/2018

se desea crear un sw el cual lea una imagen.gif (96x65) B&W
dicha imagen debe ser leida pixel a pixel y transformada a 1 y 0
1 : esta oscuro
0 : esta blanco

la informacion sera guardada en resultado.txt

python -m pip install Pillow
"""

# Se importa os para saber en que carpeta esta el proyecto
import os
# Se importa el lector de imagenes
from PIL import Image as convertidorImagen
# Se importa lo de la interfaz grafica
from tkinter import *


class SW:
    def __init__(self):
        # la ruta del proyecto
        self.ruta_proyecto = str(os.path.dirname(os.path.abspath(__file__)))
        self.pantalla = Tk()
        self.tela = Canvas(self.pantalla, width=500, height=500)
        self.lblNameImg = Label(self.tela, text="Nombre Imagen: ")
        self.txtImg = Entry(self.tela)
        self.btnConvet = Button(self.tela, text="Convertir", command=self.loadImg)
        self.img = None
        # Se pinta
        self.pantalla.title("Conver IMG to 10 by loko")
        self.pantalla.geometry("500x500")
        self.tela.place(x=0, y=0)
        self.lblNameImg.place(x=10, y=10)
        self.txtImg.place(x=120, y=10)
        self.btnConvet.place(x=300, y=8)
        self.pantalla.mainloop()

    def loadImg(self):
        if len(str(self.txtImg.get().strip())) > 0:
            try:
                # Se carga un visualizador de img
                self.img = PhotoImage(file=self.ruta_proyecto+"\\"+str(self.txtImg.get().strip()))
                # Se carga en pantalla
                self.tela.create_image(200, 100, image=self.img, anchor=NW)
                self.convertir()
                self.btnConvet['bg'] = 'green' 
            except:
                self.btnConvet['bg'] = 'black'     
        else:
            self.btnConvet['bg'] = 'red'

    def convertir(self):
        imagen = convertidorImagen.open(self.ruta_proyecto+"\\"+str(self.txtImg.get().strip()))
        pix = imagen.load()
        datos = "None"
        if imagen.size == (96, 65):
            datos = list(imagen.getdata())
            try:
                resultado = open(self.ruta_proyecto+"\\resultado.txt", "w")
                # Procedo a intercambiar por 1 y 0
                temp = str(datos)
                # Quito el primer [ 
                temp = temp.replace("[", "")
                # Quito el ultimo ]
                temp = temp.replace("]", "")

                aux = ""
                # Procedo a analisar dato a dato
                contador_salto = 0
                for i in temp.split(","):
                    if int(i) > 50:
                        aux = aux + "0"
                    else:
                        aux = aux + "1"
                    
                    contador_salto = contador_salto + 1

                    if contador_salto == 96:
                        aux = aux + "\n"
                        contador_salto = 0
                    

                resultado.write(aux)
                resultado.close()
            except:
                self.btnConvet['bg'] = 'gray25'
            
        else:
            self.btnConvet['bg'] = 'red2'

        imagen.close()


sw = SW()

