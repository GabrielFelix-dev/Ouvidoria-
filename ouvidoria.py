from operacoesbd import *

conn = criarConexao("127.0.0.1","root","310107","ouvidoria")


# Lista todas as manifestações:

def listarManifestacoes(conn):
    listarManifestacoes = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conn, listarManifestacoes)

    if len(manifestacoes) < 1:
        print("Sem manifestações no momento.")
    else:
        print("\nLista de manifestações: ")
        for item in manifestacoes:
            print(f" - Código({item[0]}) {item[1]}: {item[2]} ; ")


# Lista as manifestações pelo seu tipo: Reclamação, elogio ou sugestão:

def listarManifestacaoPorTipo(conn, tipo):
   
    listagemPorTipo = listarBancoDados(conn, tipo)

    if len(listagemPorTipo) < 1:
        print("Não possui manifestações do tipo escolhido.")
    else:
        print("\nLista de manifestações: ")
        for item in listagemPorTipo:
            print(f" - {item[1]}: {item[2]} ; ")
def consultarTipo(conn):
    try:
        print("\nDigite o tipo de manifestações que deseja listar: ")
        print("\n1) Reclamação; \n2) Elogio; \n3) Sugestão.")
        tipoManifestacao = int(input("Digite sua opção: "))
      
        if tipoManifestacao == 1:

            tipo = "select * from manifestacoes where tipo like 'r%' or tipo like 'R%' " 
            listarManifestacaoPorTipo(conn, tipo)

        elif tipoManifestacao == 2:

            tipo = "select * from manifestacoes where tipo like 'e%' or tipo like 'E%' " 
            listarManifestacaoPorTipo(conn, tipo)        

        elif tipoManifestacao == 3:
            
            tipo = "select * from manifestacoes where tipo like 's%' or tipo like 'S%' " 
            listarManifestacaoPorTipo(conn, tipo)

    except ValueError:
        print("Insira um número de acordo com as opções acima!")


# Criar nova manifestação:

def addManifestacao(conn):   
    try:
        while True:
            nome = input("\nDigite seu nome: ")
            if nome:
                break
            print("Entrada inválida!")

        while True:
            tipo = input("Digite o tipo da manifestação (Elogio, Reclamação, Sugestão): ").strip().upper()
            if tipo:
                break
            print("O tipo não pode estar vazia!")

        while True:
            try:
                descricao = input("O que deseja informar: ")
                break
            except ValueError:
                print("Insira uma descrição!")

        add = "INSERT INTO manifestacoes (nome, tipo, descricao) VALUES (%s, %s, %s)"
        dados = (nome, tipo, descricao)

        linhasAfetadas = insertNoBancoDados(conn, add, dados)

        if linhasAfetadas > 0:
            print("Manifestação adicionada com sucesso!")
        else:
            print("Erro ao adicionar a manifestação. Tente novamente.")

    except Exception as e:
        print(f"Erro inesperado: {e}")


# Exibir quantidade de manifestações:

def exibirManifestacoes(conn):
        consultaContagem = "select tipo, count(*) from manifestacoes group by tipo"
        resultados = listarBancoDados(conn, consultaContagem)

        if resultados:
            print("\nContagem de manifestações por tipo:")
            for item in resultados:
                print(f"{item[0]}: {item[1]}")
        else:
            print("Nenhuma manifestação cadastrada no sistema.")


# Pesquisar uma manifestação por código:

def pesquisarManifestacao(conn):
    try:
        codigoManifestacao = int(input("\nDigite o código da manifestação: "))
        consultaPesquisaManifestacao = 'SELECT * FROM manifestacoes WHERE codigo = %s'
        registros = listarBancoDados(conn, consultaPesquisaManifestacao, (codigoManifestacao,))

        if registros:
            registro = registros[0]
            tipo, descricao = registro[1], registro[2]
            print(f"Manifestação encontrada: {tipo}")
            print(f"Descrição: {descricao}")
        else:
            print("Nenhuma manifestação encontrada para o código informado.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")


# Excluir uma Manifestação pelo Código:

def excluirManifestacao(conn):
    try:
        codigoManifestacao = int(input("\nDigite o código da manifestação a remover: "))
        consultaPesquisaManifestacao = 'SELECT * FROM manifestacoes WHERE codigo = %s'
        registros = listarBancoDados(conn, consultaPesquisaManifestacao, (codigoManifestacao,))

        if registros:
            confirmacao = input(f"Tem certeza que deseja remover a manifestação '{registros[0][1]}'? (s/n): ").strip().lower()
            
            if confirmacao == 's':
                consultaRemover = "DELETE FROM manifestacoes WHERE codigo = %s"
                linhasAlteradas = excluirBancoDados(conn, consultaRemover, (codigoManifestacao,))

                if linhasAlteradas > 0:
                    print("Manifestação removida com sucesso!")
                else:
                    print("Erro ao remover a manifestação.")
            else:
                print("Operação cancelada.")
        else:
            print("Nenhuma manifestação encontrada para o código informado.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")


encerrarConexao(conn)