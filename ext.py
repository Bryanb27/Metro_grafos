from asyncio.windows_events import NULL
import tkinter as tk
from turtle import left, right
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()
sub = [7]

def main():
    #Adicionar os nós
    b = []
    arq = open("Coordenadas.txt","r")
    coordenadas = arq.readlines()
    for coordenada in coordenadas:
        part = coordenada.split(',')
        G.add_node(part[0], pos= (int(part[1]), int(part[2])))
        b.append(part[0])
    nx.draw(G, with_labels=True)
    arq.close()
    
    #Adicionar as arestas
    c = []
    pr = []

    arq = open("Linhas.txt","r")
    numero_de_linhas = 7
    #Enquanto tiver linhas
    while numero_de_linhas > 0:
        trecho = 0
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
            G.add_edge(conexoes[0], conexoes[1][:-1])
            v = b.index(conexoes[0])
            achado = coordenadas[v].split(',')
            
            j -= 1
            cont +=1
        numero_de_linhas -= 1
        sub[trecho] = G.subgraph(pr)
        print(sub[trecho])
        list(sub[trecho].edges())
        pr.clear()
        trecho += 1
    arq.close()
    
    plt.show()
main()