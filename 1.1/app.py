#Nome: Bryan Jonathan Melo De Oliveira

from asyncio.windows_events import NULL
from cmath import sqrt
import tkinter as tk
from turtle import left, right
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import math
import copy

G = nx.Graph()
sub = [7]

#Classe dos nós
class node:
    def __init__(self, nome, cox, coy, color):
        self.nome = nome
        self.cox = cox
        self.coy = coy
        self.color = color

lines = []    

def dist(x1, y1, x2, y2):
    distancia = 0
    distancia = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    return distancia 

def opcao1():
    top_win = tk.Tk()
    top_win.geometry("300x150")
    detalhes = tk.Label(top_win, text = "Entrar com as duas estações desejadas")
    detalhes.place(x = 20, y = 20)
    
    estacao1 = tk.Label(top_win, text = "Estação 1")
    estacao1.place(x = 20, y = 40)
    entry_station1 =  tk.Entry(top_win)
    entry_station1.place(x = 80, y = 40)

    estacao2 = tk.Label(top_win, text = "Estação 2")
    estacao2.place(x = 20, y = 60)
    entry_station2 =  tk.Entry(top_win)
    entry_station2.place(x = 80, y = 60)

    def nodes_connected():
        top_win2 = tk.Tk()
        ent1 = str(entry_station1.get())
        ent2 = str(entry_station2.get())
        print(ent1)
        print(ent2)
        i = len(sub)
        cont = 0
        x = 0
        for x in range(len(sub)):
            #print(list(sub[x].nodes))
            if (sub[1].has_node(ent1)):
                print("Entrou")
                if (sub[1].has_node(ent2)):
                    print("Entrou2")
                    detalhes = tk.Label(top_win2, text = nx.shortest_path(sub[x], source = sub[x].nodes(ent1), target = sub[x].nodes(ent2)))    
                    detalhes.place(x = 20, y = 20)
                    cont = 1
        
        if (cont == 0):
            detalhes = tk.Label(top_win2, text = "Grafo nao possui tais nós")
            detalhes.place(x = 20, y = 20)
     
    submit_button = tk.Button(top_win, text = "Confirmar", command= nodes_connected)
    submit_button.place(x = 20, y = 90)

    #Loop pela opcao 1
    top_win.mainloop()
    
    

def opcao2():
    nx.draw(G, with_labels=True)
    plt.show()
    janela = tk.Toplevel()
    janela.title('Opção 2')

def opcao3():
    janela = tk.Toplevel()
    janela.title('Opção 3')

def opcao4():
    janela = tk.Toplevel()
    janela.title('Opção 4')

def opcao5():
    janela = tk.Toplevel()
    janela.title('Opção 5')

def opcao6():
    janela = tk.Toplevel()
    janela.title('Opção 6')

def opcao7():
    janela = tk.Toplevel()
    janela.title('Opção 7')

def funcoes(a, b):
    janela = tk.Toplevel()
    janela.title('Funções')
    janela.geometry("200x200")

    botao1 = tk.Button(janela, text = 'Opção 1', command = opcao1)
    botao1.grid(row = 0, column = 2)
    botao1 = tk.Button(janela, text = 'Opção 2', command = opcao2)
    botao1.grid(row = 1, column = 2)
    botao1 = tk.Button(janela, text = 'Opção 3', command = opcao3)
    botao1.grid(row = 2, column = 2)
    botao1 = tk.Button(janela, text = 'Opção 4', command = opcao4)
    botao1.grid(row = 3, column = 2)
    botao1 = tk.Button(janela, text = 'Opção 5', command = opcao5)
    botao1.grid(row = 4, column = 2)
    botao1 = tk.Button(janela, text = 'Opção 6', command = opcao6)
    botao1.grid(row = 5, column = 2)
    botao1 = tk.Button(janela, text = 'Opção 7', command = opcao7)
    botao1.grid(row = 6, column = 2)

#Cria a minha matriz
def crie_matriz(n_linhas, n_colunas, valor):
    matriz = [] # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(n_colunas):
            linha.append(valor)

        # coloque linha na matriz
        matriz.append(linha)

    return matriz

subs = []
#np.matrix()

def main():
    #Abrir janela
    app=tk.Tk() 
    app.title("Metro")
    app.geometry("900x720")
    
    #canvas na janela
    canvas= tk.Canvas(app,width=900, height=720)
    canvas.pack()
    

    #Abrir arquivo com linhas
    b = []
    arq = open("Coordenadas.txt","r")
    coordenadas = arq.readlines()
    for coordenada in coordenadas:
        part = coordenada.split(',')
        lines.append(node(part[0], int(part[1]), int(part[2]), "white"))
        G.add_node(part[0], pos= (int(part[1]), int(part[2])))
        b.append(part[0])
    arq.close()
    print(G.nodes())

    #Vetor pra usar mais tarde
    c = []
    pr = []
    cont = 0
    #Criar linhas no mapa
    arq = open("Linhas.txt","r")
    numero_de_linhas = 7
    #Enquanto tiver linhas
    while numero_de_linhas > 0:
        
        cont = 0
        linhas = arq.readline()
        data = linhas.split(' ')
        j = int(data[3])
        
        while j > 1:
            conexao = arq.readline() #lendo a linha com os dois pontos
            c.append(conexao)
            conexoes = conexao.split(',') #p1=Conexoes[1], p2=Conexoes[2] 
            pr.append(conexoes[0])
            pr.append(conexoes[1][:-1])
            for i in range(len(lines)):
                if(lines[i].nome == conexoes[0]):
                    f = copy.deepcopy(lines[i])
                    i = len(lines)

            for i in range(len(lines)):
                if(lines[i].nome == conexoes[1][:-1]):
                    j = copy.deepcopy(lines[i])
                    i = len(lines)
            subs[numero_de_linhas] = np.append(f,i)
            G.add_edge(conexoes[0], conexoes[1][:-1])
            v = b.index(conexoes[0])
            achado = coordenadas[v].split(',')
            x1 = int(achado[1])
            y1 = int(achado[2])
            conexoes[1] = conexoes[1][:-1]
            v = b.index(conexoes[1])
            achado = coordenadas[v].split(',')
            x2 = int(achado[1])
            y2 = int(achado[2])
            canvas.create_line(x1,y1,x2,y2, fill=data[2], width=8)
            j -= 1
            cont +=1
        sub.append(G.subgraph(pr))
        numero_de_linhas -= 1
        #Criar subgrafo
        pr.clear()
    arq.close()
    
    for i in range(len(lines)):
        print(lines[i].coy)

    #Para cada coordenada desenhar ponto
    for coordenada in coordenadas:
        data = coordenada.split(',')
        data[1] = int(data[1])
        data[2] = int(data[2])
        canvas.create_oval(data[1], data[2], data[1], data[2], fill="red", width=10)
        canvas.create_text(data[1]+35, data[2], text=data[0])

    #Matriz de adjacencia
    a = crie_matriz(32, 32, 0)
    for i in range(len(c)):   
        conexoes = c[i].split(',')
        conexoes[1] = conexoes[1][:-1]
        n = b.index(conexoes[0])
        m = b.index(conexoes[1])
        a[n][m] = 1
        a[m][n] = 1
        #Criar um grafo com todas as conexoes de acordo com a matriz de adjacencia
        G.add_edge(b[n], b[m])
    j = len(sub)
    print(list(sub[2]))    
    #Abrir janela de funcoes
    row = 7
    for x in range(row):
        for y in x:
            print(subs[x][y].nome)

    funcoes(a, b)
     
    #Loop pelo aplicativo
    app.mainloop()

main()


