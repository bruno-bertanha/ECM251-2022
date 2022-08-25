#Programa que escreve em um arquivo

arquivo = open('data/dados.txt', 'a')
step = True

while step:
    time = input('Digite o time (vazio para sair): ')
    #String vazia é igual a False
    if not time: 
        step = False
        continue
    arquivo.write(time + '\n')

arquivo.close()