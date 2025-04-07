elif opcao == 2:
    tipo = input("Digite o tipo da manifestação (Elogio, Reclamação, Sugestão): ")
    descricao = input("Digite a descrição da manifestação: ").

    if tipo and descricao:
        consultaInserir = "INSERT INTO manifestacao (tipo, descricao) VALUES (%s, %s)"
        linhasAfetadas = inserirBancoDados(conn, consultaInserir, (tipo, descricao))

        if linhasAfetadas > 0:
            print("Manifestação cadastrada com sucesso!")
        else:
            print("Erro ao cadastrar a manifestação.")
    else:
        print("Tipo e descrição não podem estar vazios.")


elif opcao == 4:
    consultaContagem = """
        SELECT tipo, COUNT(*) 
        FROM manifestacao 
        GROUP BY tipo
    """
    resultados = listarBancoDados(conn, consultaContagem)

    if resultados:
        print("\nContagem de manifestações por tipo:")
        for tipo, quantidade in resultados:
            print("{tipo}: {quantidade}")
    else:
        print("Nenhuma manifestação cadastrada no sistema.")
