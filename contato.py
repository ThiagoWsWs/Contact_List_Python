from database import conectar

def editar_contato(id_contato, nome, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE contatos
    SET nome = %s,
        telefone = %s,
        email = %s
    WHERE id = %s
    """

    valores = (nome, telefone, email, id_contato)

    cursor.execute(sql, valores)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado.")

    cursor.close()
    conexao.close()

def excluir_contato(id_contato):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM contatos WHERE id = %s"

    cursor.execute(sql, (id_contato,))
    conexao.commit()

    if cursor.rowcount > 0:
        print("Contato excluído com sucesso!")
    else:
        print("Contato não encontrado.")

    cursor.close()
    conexao.close()

def buscar_contato(nome):   
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM contatos
    WHERE nome LIKE %s
    """

    cursor.execute(sql, (f"%{nome}%",))

    resultados = cursor.fetchall()

    if resultados:
        print("\n=== CONTATOS ENCONTRADOS ===")
        for contato in resultados:
            print(
                f"ID: {contato[0]} | "
                f"Nome: {contato[1]} | "
                f"Telefone: {contato[2]} | "
                f"E-mail: {contato[3]}"
            )
    else:
        print("Nenhum contato encontrado.")

    cursor.close()
    conexao.close()

def adicionar_contato(nome, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO contatos (nome, telefone, email)
    VALUES (%s, %s, %s)
    """

    valores = (nome, telefone, email)

    cursor.execute(sql, valores)

    conexao.commit()

    cursor.close()
    conexao.close()

    print("Contato cadastrado com sucesso!")

def listar_contatos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM contatos")

    contatos = cursor.fetchall()

    print("\n=== CONTATOS ===")

    for contato in contatos:
        print(
            f"ID: {contato[0]} | "
            f"Nome: {contato[1]} | "
            f"Telefone: {contato[2]} | "
            f"E-mail: {contato[3]}"
        )

    cursor.close()
    conexao.close()