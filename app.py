#Nome: Bryan Jonathan Melo De Oliveira

from asyncio.windows_events import NULL
from cmath import sqrt
import tkinter as tk
#import numpy as np
import math
import time
import sys

sub = []
#Linhas separadas devido a problema para criar matriz
linha_1 = []
linha_2 = []
linha_3 = []
linha_4 = []
linha_5 = []
linha_6 = []
linha_7 = []
#Reserva
outrosub = []

#Vetor com todos os objetos nós
lines = []

#Classe dos nós
class node:
    def __init__(self, nome, cox, coy, color):
        self.nome = nome
        self.cox = cox
        self.coy = coy
        self.color = color    

#Calcular a distancia entre dois pontos
def dist(x1, y1, x2, y2):
    distancia = 0
    distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return distancia 

#Funcao para pegar distancia das duas estacoes
def calculating(linha, estaco, nome2, cont, distancia):
    #Retornar se ja estiver na estacao destino
    if(linha[cont] == nome2):
        return distancia, estaco
    #Senao
    else:
        for p in lines:
            if p.nome == linha[cont]:
                x1 = p.cox
                y1 = p.coy
        #Aumentar cont
        cont += 1
        for p in lines:
            if p.nome == linha[cont]:
                x2 = p.cox
                y2 = p.coy
        
        #Chamar funcao pra calculo entre dois pontos
        distancia = dist(x1, y1, x2, y2)
        #Adicionar linha a string mostrando as estacoes estre os dois pontos
        estaco += " " + linha[cont]
        return calculating(linha, estaco, nome2, cont, distancia)

#Tive que separar para encontrar erros
#achar menor distancia
def achar_em(linhat, ent1, ent2):
    distancia = 9999999
    estaco = ""
    #Testar se possui ambas as estacoes
    if (ent1 in linhat):
        if (ent2 in linhat):
            print("Entrou")
            #Fazer caso a primeira estacao esteja antes da segunda
            if (linhat.index(ent1) < linhat.index(ent2)):
                estaco = "[ " + ent1
                ind1 = linhat.index(ent1)
                distancia, estaco = calculating(linhat, estaco, ent2, ind1, distancia)
                estaco += " ] Distancia = " + str(distancia)  
 
            #Ou fazer caso a segunda esteja antes da primeira
            else:
                estaco = "[ " + ent2
                ind2 = linhat.index(ent2)
                distancia, estaco = calculating(linhat, estaco, ent1, ind2, distancia)
                estaco += " ] Distancia = " + str(distancia) 
 

    #print(esta + " ")   teste
    return distancia, estaco

#Opcao 1, encontrar menor distancia entre duas linhas com x e y das estacoes
def opcao1(linha_1, linha_2, linha_3, linha_4, linha_5, linha_6, linha_7):
    #Abrir janela e configurar
    top_win = tk.Tk()
    top_win.geometry("300x150")
    top_win.configure(bg = 'cyan')
    detalhes = tk.Label(top_win, text = "Entrar com as duas estações desejadas", background='cyan')
    detalhes.place(x = 20, y = 20)
    
    #Escrever estacao 1
    estacao1 = tk.Label(top_win, text = "Estação 1", background='cyan')
    estacao1.place(x = 20, y = 40)
    entry_station1 =  tk.Entry(top_win)
    entry_station1.place(x = 80, y = 40)
    
    #Escrever estacao 2
    estacao2 = tk.Label(top_win, text = "Estação 2", background='cyan')
    estacao2.place(x = 20, y = 60)
    entry_station2 =  tk.Entry(top_win)
    entry_station2.place(x = 80, y = 60)

    def nodes_connected():
        #Timer (começando a calcular apos receber as entradas do usuario)
        start_time = time.time()

        #Janela
        top_win2 = tk.Tk()
        top_win2.geometry("700x100")
        top_win2.configure(bg = 'cyan')
        ent1 = str(entry_station1.get())
        ent2 = str(entry_station2.get())
        distancia = []
        esta = []
        longe = 7
        #Testar com cada linha as entradas
        for j in range(longe):
            if (j == 0):
                x, v = achar_em(linha_1, ent1, ent2)
                distancia.append(x)
                esta.append(v)
                
            elif(j == 1):
                x, v = achar_em(linha_2, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 2):
                x, v = achar_em(linha_3, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 3):
                x, v = achar_em(linha_4, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 4):
                x, v = achar_em(linha_5, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 5):
                x, v = achar_em(linha_6, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 6):
                x, v = achar_em(linha_7, ent1, ent2)
                distancia.append(x)
                esta.append(v)
                    
        #achar menor 
        tmp = min(distancia)
        index = distancia.index(tmp)
        #Se nao achar ambos os nós em nenhuma linha
        if tmp == 0 :
           outros_detalhes = tk.Label(top_win2, text = "Não ha grafos com tais estações", background='cyan') 
           outros_detalhes.place(x = 20, y = 20)
           print("%s seconds " % (time.time() - start_time))
        #Senao
        else:
           outros_detalhes = tk.Label(top_win2, text = "A rota mais curta é " + esta[index], background='cyan')
           outros_detalhes.place(x = 20, y = 20)
           print("%s seconds " % (time.time() - start_time))
    
    #Botao de confirmar as estações
    submit_button = tk.Button(top_win, text = "Confirmar", command= nodes_connected)
    submit_button.place(x = 20, y = 90)

    #Loop pela opcao 1
    top_win.mainloop()

#Achar o menor numero de estacoes intermediarias
def achar_em2(linhat, ent1, ent2):
    estaco = ""
    distancia = 9999999
    #Testar se vetor possui ambas as estacoes
    if (ent1 in linhat):
        if (ent2 in linhat):
            print("Entrou")
            for x1 in range(len(linhat)):
                if(linhat[x1] == ent1):
                    x = x1
            #print(x) teste
            for y1 in range(len(linhat)):
                if(linhat[y1] == ent2):
                    y = y1
            #print(y) teste
            #Se a primeira estacao vier antes da segunda no vetor
            if(x < y):
                distancia = y - x
                while x < y:
                    estaco += " " + linhat[x]
                    x += 1
                estaco += " " + linhat[x]
            #Se a segunda estacao vier antes da primeira no vetor
            if(y < x):
                distancia = x - y
                while x > y:
                    estaco += " " + linhat[y]
                    y += 1
                estaco += " " + linhat[y]
            estaco += " ] Distancia = " + str(distancia)

    return distancia, estaco  

#Opcao 2, Encontrar a rota entre duas estacoes com menor numero de estacoes intermediarias
def opcao2(linha_1, linha_2, linha_3, linha_4, linha_5, linha_6, linha_7):
    #Abrir e configurar janela
    top_win = tk.Tk()
    top_win.geometry("300x150")
    top_win.configure(bg = 'cyan')
    detalhes = tk.Label(top_win, text = "Entrar com as duas estações desejadas", background='cyan')
    detalhes.place(x = 20, y = 20)
    
    #Receber primeira estacao
    estacao1 = tk.Label(top_win, text = "Estação 1", background='cyan')
    estacao1.place(x = 20, y = 40)
    entry_station1 =  tk.Entry(top_win)
    entry_station1.place(x = 80, y = 40)
    
    #Receber segunda estacao
    estacao2 = tk.Label(top_win, text = "Estação 2", background='cyan')
    estacao2.place(x = 20, y = 60)
    entry_station2 =  tk.Entry(top_win)
    entry_station2.place(x = 80, y = 60)

    def nodes_connected():
        #Timer - (começando apos o usuario entrar com os dados)
        start_time = time.time()

        #Janela
        top_win2 = tk.Tk()
        top_win2.geometry("700x100")
        top_win2.configure(bg = 'cyan')
        ent1 = str(entry_station1.get())
        ent2 = str(entry_station2.get())
        distancia = []
        esta = []
        longe = 7
        #Checar em cada linha
        for j in range(longe):
            if (j == 0):
                x, v = achar_em2(linha_1, ent1, ent2)
                distancia.append(x)
                esta.append(v)
                
            elif(j == 1):
                x, v = achar_em2(linha_2, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 2):
                x, v = achar_em2(linha_3, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 3):
                x, v = achar_em2(linha_4, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 4):
                x, v = achar_em2(linha_5, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 5):
                x, v = achar_em2(linha_6, ent1, ent2)
                distancia.append(x)
                esta.append(v)

            elif (j == 6):
                x, v = achar_em2(linha_7, ent1, ent2)
                distancia.append(x)
                esta.append(v)
                    
        #achar menor 
        tmp = min(distancia)
        index = distancia.index(tmp)
        #Se nao achar ambos os nós em nenhuma linha
        if tmp == 0 :
           outros_detalhes = tk.Label(top_win2, text = "Não ha grafos com tais estações", background='cyan') 
           outros_detalhes.place(x = 20, y = 20)
           print("%s seconds " % (time.time() - start_time))
        #Senao
        else:
           outros_detalhes = tk.Label(top_win2, text = "A rota mais curta é [ " + esta[index], background='cyan')
           outros_detalhes.place(x = 20, y = 20)
           print("%s seconds " % (time.time() - start_time))

    submit_button = tk.Button(top_win, text = "Confirmar", command= nodes_connected)
    submit_button.place(x = 20, y = 90)

    #Loop pela opcao 1
    top_win.mainloop()

#Janela para a opcao 3
def opcao3():
    janela = tk.Toplevel()
    janela.title('Opção 3')

#Janela para a opcao 3
def opcao4():
    janela = tk.Toplevel()
    janela.title('Opção 4')

#Janela para a opcao 3
def opcao5():
    janela = tk.Toplevel()
    janela.title('Opção 5')

#Janela para a opcao 3
def opcao6():
    janela = tk.Toplevel()
    janela.title('Opção 6')

#Janela para a opcao 3
def opcao7():
    janela = tk.Toplevel()
    janela.title('Opção 7')

#Janela para a seleçao da opcao
def funcoes(linha_1, linha_2, linha_3, linha_4, linha_5, linha_6, linha_7):
    #Criar e configurar janela
    janela = tk.Toplevel()
    janela.title('Funções')
    janela.geometry("200x350")
    janela.configure(bg = 'purple')

    #Criar e configurar botoes
    botao1 = tk.Button(janela, text = 'Opção 1', command = lambda: opcao1(linha_1, linha_2, linha_3, linha_4, linha_5, linha_6, linha_7))
    botao1.place(x = 100, y = 50, anchor = 'center')
    botao2 = tk.Button(janela, text = 'Opção 2', command = lambda: opcao2(linha_1, linha_2, linha_3, linha_4, linha_5, linha_6, linha_7))
    botao2.place(x = 100, y = 90, anchor = 'center')
    botao3 = tk.Button(janela, text = 'Opção 3', command = opcao3)
    botao3.place(x = 100, y = 130, anchor = 'center')
    botao4 = tk.Button(janela, text = 'Opção 4', command = opcao4)
    botao4.place(x = 100, y = 170, anchor = 'center')
    botao5 = tk.Button(janela, text = 'Opção 5', command = opcao5)
    botao5.place(x = 100, y = 210, anchor = 'center')
    botao6 = tk.Button(janela, text = 'Opção 6', command = opcao6)
    botao6.place(x = 100, y = 250, anchor = 'center')
    botao7 = tk.Button(janela, text = 'Opção 7', command = opcao7)
    botao7.place(x = 100, y = 290, anchor = 'center')

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
    #Retornar Matriz
    return matriz

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
        b.append(part[0])
    arq.close()

    #Vetor pra usar mais tarde
    c = []
    pr = []

    #Criar linhas no mapa
    arq = open("Linhas.txt","r")
    numero_de_linhas = 7

    #Enquanto tiver linhas
    while numero_de_linhas > 0:
        linhas = arq.readline()
        data = linhas.split(' ')
        j = int(data[3])
        
        while j > 1:
            conexao = arq.readline() #lendo a linha com os dois pontos
            c.append(conexao)
            conexoes = conexao.split(',') #p1=Conexoes[1], p2=Conexoes[2] 
            pr.append(conexoes[0])
            pr.append(conexoes[1][:-1])
            #Salvar os nos da primeira e da segunda linha conectada em um vetor
            for i in range(len(lines)):
                if(lines[i].nome == conexoes[0]):
                    sub.append(lines[i].nome)
                    i = len(lines)
            for i in range(len(lines)):
                if(lines[i].nome == conexoes[1][:-1]):
                    sub.append(lines[i].nome)
                    i = len(lines)
            #Para o canvas
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

        #Armazenar cada elemento do sub a cada um dos vetores
        if(numero_de_linhas == 7):
            for element in sub:
                if element not in linha_1:
                    linha_1.append(element)
        if(numero_de_linhas == 6):
            for element in sub:
                if element not in linha_2:
                    linha_2.append(element)
        if(numero_de_linhas == 5):
            for element in sub:
                if element not in linha_3:
                    linha_3.append(element)
        if(numero_de_linhas == 4):
            for element in sub:
                if element not in linha_4:
                    linha_4.append(element)
        if(numero_de_linhas == 3):
            for element in sub:
                if element not in linha_5:
                    linha_5.append(element)
        if(numero_de_linhas == 2):
            for element in sub:
                if element not in linha_6:
                    linha_6.append(element)
        if(numero_de_linhas == 1):
            for element in sub:
                if element not in linha_7:
                    linha_7.append(element)
        #Limpar sub
        sub.clear()
        numero_de_linhas -= 1

        #Criar subgrafo
        pr.clear()
    arq.close()
    
    """ testar se esta criando os vetores direito
    for i in range(len(linha_2)):
        print("x")
        print(linha_2[i])
    for i in range(len(linha_7)):
        print("x")
        print(linha_7[i])
    """

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
        
    #Chamar a janela para selecionar opcao
    funcoes(linha_1, linha_2, linha_3, linha_4, linha_5, linha_6, linha_7)
     
    #Loop pelo aplicativo
    app.mainloop()

#Chamar metodo principal
main()


