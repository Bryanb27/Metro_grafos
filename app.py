#Nome: Bryan Jonathan Melo De Oliveira

from tkinter import *
from matplotlib import pyplot as plt

global x1
global y1
global x2
global y2

def buscar(coordenadas, conexoes):
    x1 = 0
    y1 = 0
    conexoes.strip()
    for coordenada in coordenadas:
                coor = coordenada.split(',')
                #print("Entrou", conexoes)
                if coor[0] == conexoes:
                    print("Entrou", conexoes)
                    x1 = int(coor[1])
                    y1 = int(coor[2])
    return x1, y1

def main():
    #Abrir janela
    app=Tk() 
    app.title("Metro")
    app.geometry("900x720")
    
    #canvas na janela
    canvas=Canvas(app,width=900, height=720)
    canvas.pack()

    #Abrir arquivo com coordenadas
    arq = open("Coordenadas.txt","r")
    coordenadas = arq.readlines()
    arq.close()
    #Para cada coordenada desenhar ponto
    for coordenada in coordenadas:
        data = coordenada.split(',')
        data[1] = int(data[1])
        data[2] = int(data[2])
        canvas.create_oval(data[1], data[2], data[1], data[2], fill="red", width=4)
        canvas.create_text(data[1]+35, data[2], text=data[0])

    #Abrir arquivo com linhas
    b = []
    arq = open("Coordenadas.txt","r")
    coordenadas = arq.readlines()
    for coordenada in coordenadas:
        part = coordenada.split(',')
        b.append(part[0])
    arq.close()

    arq = open("Linhas.txt","r")
    numero_de_linhas = 7
    
    #Enquanto tiver linhas
    while numero_de_linhas > 0:
        linhas = arq.readline()
        data = linhas.split(' ')
        j = int(data[3])
        
        while j > 1:
            conexao = arq.readline() #lendo a linha com os dois pontos
            print(conexao)
            conexoes = conexao.split(',') #p1=Conexoes[1], p2=Conexoes[2] 
            print(conexoes[0])
            print(conexoes[1])
            v = b.index(conexoes[0])
            achado = coordenadas[v].split(',')
            x1 = int(achado[1])
            y1 = int(achado[2])
            conexoes[1] = conexoes[1][:-1]
            v = b.index(conexoes[1])
            achado = coordenadas[v].split(',')
            x2 = int(achado[1])
            y2 = int(achado[2])
            print(x1,y1,x2,y2)
            canvas.create_line(x1,y1,x2,y2, fill=data[2], width=3)
            j -= 1

        numero_de_linhas -= 1
    arq.close()
    app.mainloop()

main()


