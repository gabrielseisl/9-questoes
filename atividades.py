atividade 1
         
nome = input("qual seu nome: ")
idade = int(input("Qual sua idade: "))
cidade = input("Qual sua cidade: ")
print(f"Olá,meu nome é {nome} tenho {idade}anos e moro em {cidade}")

                atividade 2
n1 = float(input("digite um numero: "))
n2 = float(input("digite outro: "))

print(float(n1 + n2))
print(float(n1*n2))
print(float(n1/n2))
print(float(n1-n2))

                atividade 3
n1=int(input("digite um numero: "))

for i  in range (n1,n1*10,n1):
    print(i)
                atividade 4
numero=""

while numero != "23":
    numero=int(input("digite o numero: "))
    if numero>23:
        print("menos")
    elif numero<23:
        print("mais")
    else:
        print("acertou")
        break

            atividade 5
compras = []

c1 = input("Digite uma compra: ")
c2 = input("Digite uma compra: ")
c3 = input("Digite uma compra: ")
c4 = input("Digite uma compra: ")
c5 = input("Digite uma compra: ")


compras = [c1, c2, c3, c4, c5]


print("lista de compras:")
for i, item in enumerate(compras, start=1):
    print(f"{i}. {item}")

c6 = input("Alguma nova compra? ")

compras.append(c6)


print("lista atualizada:")
for i, item in enumerate(compras,start=1):
    print(f"{i}. {item}")


        atividade 7


def par_ou_impar():
    n1=int(input("qual seu numero: "))
    n2=int(input("qual seu numero: "))
    n3=int(input("qual seu numero: "))
    if int (n1)%2==0:
        print("par")
    else:
        print("impar")
    if int (n2)%2==0:
        print("par")
    else:
        print("impar")
    if int (n3)%2==0:
        print("par")
    else:
        print("impar")

par_ou_impar()

            atividade 8 
            def calcular_imc(peso,altura):
    peso=int(input("qual seu peso: "))
    altura=float(input("qual sua altura: "))
    imc=peso/(altura**2)
    
calcular_imc()

            

def calcular_imc():
    peso=int(input("qual seu peso: "))
    altura=float(input("qual sua altura: "))
    imc=peso/(altura**2)
    print(imc)




def calcular_imc():
    peso=float(input("qual seu peso: "))
    altura=float(input("qual sua altura: "))
    imc=int(peso/(altura**2))
    print(imc)



def classificar_imc():
    print("qual seu imc?")
    classificacao=int(input("digite aqui seu imc: "))
    if  (classificacao<18.5 or classificacao>25):
        print("imc ruim")
    else:
        print("imc bom")
        
while True:
    print("                            Menu                               ")
    print("1-Calcular imc")
    print("2-Classificação")
    print("3-Sair")
    escolha=(input("escolha uma das opção acima: "))

    if escolha == "1":
        calcular_imc()
    elif escolha == "2":
        classificar_imc()
    elif escolha == "3":
         break

                atividade 9

tarefas = []

def listar():
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
    else:
        for i, t in enumerate(tarefas, 1):
            print(f'{i}. {t}')

def adicionar():
    print("Adicionar tarefas")
    t1=(input("Tarefa Nova: "))
    t2=(input("Tarefa Nova:  "))
    tarefas.append([t1,t2])
    



def remover(tarefas):
    if tarefas=="":
        print("Nenhuma tarefa para remover.")
        return tarefas

    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"{i+1} - {tarefa}")

    escolha = int(input("Digite o número da tarefa que deseja remover: "))
    indice = escolha - 1

    if 0 <= indice < len(tarefas):
        print(f"Tarefa '{tarefas[indice]}' removida com sucesso!")
        del tarefas[indice]
    else:
        print("Número inválido.")

    return tarefas
        

while True:
    print('\n1 - Adicionar 2 - Remover 3 - Listar 4 - Sair')
    
    opcao = input('Escolha: ')

    if opcao == "3":
        listar()
    elif opcao == "1":
        adicionar()
    elif opcao == "2":
        remover(tarefas)
    elif opcao == "4":
        print("Saindo")
        break
    
