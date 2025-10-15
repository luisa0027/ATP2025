# Cinema = [Sala]
# Sala = [nlugares, Vendidos, filme]
# nlugares = Int
# filme = String 
# Vendidos = [Int]

sala1 = [150, [55,70,66,23,70], "It ends with us"]
sala2 = [200, [55,70,66,23,70], "Top gun"]
sala3 = [250, [55,70,66,23,70], "The fault in our stars"]
cinema = [sala1, sala2 , sala3]


def listar(cinema):
    print("----------------------------------FILMES EM EXIBIÇÃO----------------------------------")
    for sala in cinema:
         print("Nome: ", sala[2], "    |    ", "Nº de lugares: ", sala[0])
    return 


def disponivel(cinema, filme, lugar):
    for sala in cinema:
        if filme == sala[2]:
            if lugar in sala[1]:   
                print(f"O lugar {lugar} para o filme {filme} não está disponível.") 
                return False
            else:
                print(f"O lugar {lugar} para o filme {filme} está disponível.")
                return True
    print("Filme não encontrado.")
    return False


def vendebilhete(cinema, filme, lugar):
    for sala in cinema:
        if filme == sala[2]:
            if lugar not in sala[1]:
                sala[1].append(lugar)
                print(f"O seu bilhete com o lugar {lugar} para o filme {filme} foi comprado.")
                return cinema
            else:
                print("Não pode comprar este bilhete, o lugar já se encontra ocupado.") 
                return cinema
    print("Filme não encontrado.")
    return cinema


def disponibilidade(cinema):   
    print("----------------------------------DISPONIBILIDADE----------------------------------")
    for sala in cinema:
        lugares_disponiveis = int(sala[0]) - len(sala[1])
        print(f"O filme {sala[2]} tem {lugares_disponiveis} lugares disponíveis.")


def existesala(cinema, nome_sala):
    for sala in cinema:
        if sala[2] == nome_sala:
            print("A sala já existe.")
            return True
    print("Pode adicionar esta sala.")
    return False


def inserirsala(cinema, nome_sala, nlugares, filme):
    if not existesala(cinema, nome_sala):
        nova_sala = [nlugares, [], filme]
        cinema.append(nova_sala)
        print(f"Adicionou a sala {nome_sala}, com o filme {filme} e {nlugares} lugares disponíveis.")
    return cinema


print("Bem vindo à aplicação onde pode ver os filmes que estão em exibição, comprar bilhetes e se for gestor do cinema pode adicionar as novidades do grande ecrã.")
print("Opção 1: Veja aqui os filmes que estão em exibição.")
print("Opção 2: Já sabe o filme que quer ver? Veja a disponibilidade de lugares aqui.")
print("Opção 3: Aqui consegue comprar o seu bilhete. ")
print("Opção 4: Aqui consegue ver o filme exibido e o total de lugares disponíveis.")
print("Opção 5: Há um novo filme em cartaz? Pode verificar se a sala existe.")
print("Opção 6: Verificou que a sala não existe, agora sim, pode adicionar aqui essa sala, o filme e o número de lugares disponíveis.")
print("Opção 0: Sair")

opção = input("Introduza a opção a que quer aceder:")

while opção != "0":
    if opção == "1":
        listar(cinema)
        opção = input("Introduza a opção a que quer aceder:")

    elif opção == "2":
        filme = input("Insira o nome do filme para o qual quer ver a disponibilidade de bilhetes: ")
        lugar = int(input("Escolha um lugar:"))
        disponivel(cinema, filme, lugar)
        opção = input("Introduza a opção a que quer aceder:")

    elif opção == "3":
        filme = input("Insira o nome do filme para o qual quer comprar bilhete: ")
        lugar = int(input("Escolha um lugar:"))
        vendebilhete(cinema, filme, lugar)
        opção = input("Introduza a opção a que quer aceder:")

    elif opção == "4":
        disponibilidade(cinema)
        opção = input("Introduza a opção a que quer aceder:")

    elif opção == "5":
        nome_sala = input("Introduza o nome da sala, podendo ser um número ou um nome: ")
        existesala(cinema, nome_sala)
        opção = input("Introduza a opção a que quer aceder:") 

    elif opção == "6":
        nome_sala = input("Introduza o nome da sala, podendo ser um número ou um nome: ")
        nlugares = int(input("Introduza o número de lugares da sala:"))
        filme = input("Insira o nome do filme em exposição na nova sala: ")
        inserirsala(cinema, nome_sala, nlugares, filme)
        opção = input("Introduza a opção a que quer aceder:") 

    elif opção not in ["1","2","3","4","5","6"]:
        print("Escolha uma opção válida.")
        opção = input("Introduza a opção a que quer aceder:") 

print("Muito obrigada por escolher a nossa aplicação. Volte sempre.")
