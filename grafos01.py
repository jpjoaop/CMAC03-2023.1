#Joao Paulo Vieira da Costa - 2020006050
#CMAC03 - Atv01 - 26/03/23


#Falta:
#Fazer as funções (ter)
import  sys
import numpy as np
#A variável dir indica o caminho padrão do arquivo.
dir = 'C:/Users/JoaoP/OneDrive/Documentos/CMAC03/Atividades/Atividade 01/'

#salva o numero de arquivos informados na entrada. O usuário tem a opção de já informar o nome de todos os arquivos de uma vez, ou pode informar um por vez.
num_instancias = len(sys.argv)
for i in range (1, num_instancias):
  #associa o nome da instância à variável.
  instancia_nome = sys.argv[i]
  with open(dir + instancia_nome + '.txt', 'rb') as f:
    #lê a matriz a partir da biblioteca numpy. Abaixo, é passado o tamnho da matriz para as variáveis, para posteriormente salvar no arquivo
    matrix = np.genfromtxt(f, dtype="int64") 
    esc = matrix.shape
    numlinhas = esc[0]
    numcolunas = esc[1]

    #essa parte é a responsável por salvar a matriz. o nome do arquivo vai ser o nome da instancia + o tamanho da matriz (ex: ponte4x4.txt)
    name_newfile = str(instancia_nome) + '_' +str(numlinhas)+ 'x' +str(numcolunas)+'.txt'
    #irá exibir esses dados como saída.
    print (name_newfile + " É uma matriz com " + str(numlinhas) + " linhas e " + str(numcolunas) + " colunas.\n")
    #função para passar a matrix pro arquivo, os números serão formatados como string.
    numx = ''
    for num in matrix:
      numx += str(num)+ ' '
      numx+= '\n'

  f = open (dir + name_newfile, "a")
  f.writelines(numx)
  f.close()



  #Chamada: python main.py exemplo ponte zachary
