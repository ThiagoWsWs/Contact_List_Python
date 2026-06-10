from colorama import init, Fore

from contato import (
    adicionar_contato,
    listar_contatos,
    buscar_contato,
    editar_contato,
    excluir_contato
)
# Inicializa o Colorama
init(autoreset=True)

while True:
    print(Fore.GREEN + """
╔══════════════════════════════╗
║      AGENDA DE CONTATOS      ║
╚══════════════════════════════╝
""")

    print(Fore.CYAN + "1 - Adicionar contato")
    print(Fore.CYAN + "2 - Listar contatos")
    print(Fore.CYAN + "3 - Buscar contato")
    print(Fore.CYAN + "4 - Editar contato")
    print(Fore.CYAN + "5 - Excluir contato")
    print(Fore.RED + "0 - Sair")

    opcao = input(Fore.YELLOW + "\nEscolha uma opção: ")

    if opcao == "1":
        print(Fore.GREEN + "\n=== NOVO CONTATO ===")

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")

        adicionar_contato(nome, telefone, email)

    elif opcao == "2":
        print(Fore.BLUE + "\n=== LISTA DE CONTATOS ===")
        listar_contatos()

    elif opcao == "3":
        print(Fore.BLUE + "\n=== BUSCAR CONTATO ===")

        nome = input("Digite o nome para buscar: ")
        buscar_contato(nome)

    elif opcao == "4":
        print(Fore.MAGENTA + "\n=== EDITAR CONTATO ===")

        listar_contatos()

        try:
            id_contato = int(
                input("\nDigite o ID do contato que deseja editar: ")
            )

            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo e-mail: ")

            editar_contato(
                id_contato,
                nome,
                telefone,
                email
            )

            print(Fore.GREEN + "Contato atualizado com sucesso!")

        except ValueError:
            print(Fore.RED + "ID inválido!")

    elif opcao == "5":
        print(Fore.RED + "\n=== EXCLUIR CONTATO ===")

        listar_contatos()

        try:
            id_contato = int(
                input("\nDigite o ID do contato que deseja excluir: ")
            )

            confirmar = input(
                Fore.YELLOW + "Tem certeza? (S/N): "
            ).upper()

            if confirmar == "S":
                excluir_contato(id_contato)
                print(Fore.GREEN + "Contato excluído com sucesso!")
            else:
                print(Fore.YELLOW + "Operação cancelada.")

        except ValueError:
            print(Fore.RED + "ID inválido!")

    elif opcao == "0":
        print(Fore.GREEN + "\nEncerrando sistema...")
        break

    else:
        print(Fore.RED + "\nOpção inválida!")