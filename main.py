
from operacoesbd import *
from ouvidoria import *

conn = criarConexao("127.0.0.1","root","310107","ouvidoria")

print("\nSeja bem vindo a nossa Ouvidoria!")

while True:
    print("\nSelecione uma das opções abaixo: ")
    print('''1) Listar manifestações; \n2) Listar manifestações por tipo; \n3) Criar nova manifestação; 
4) Exibir quantidade de manifestações; \n5) Pesquisar uma manifestação por código; \n6) Excluir uma Manifestação pelo Código; \n7) Sair.''')
    
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        listarManifestacoes(conn)

    elif opcao == 2:
        consultarTipo(conn)

    elif opcao == 3:
        addManifestacao(conn)

    elif opcao == 4:
        exibirManifestacoes(conn) 

    elif opcao == 5:
        pesquisarManifestacao(conn)

    elif opcao == 6:
        excluirManifestacao(conn)    

    elif opcao == 7:
        print("Obrigado")
        break



encerrarConexao(conn)
