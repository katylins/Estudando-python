#Calcular Médias 

def calcular_medida(notas):
    quantidades = len(notas)
    soma = sum(notas)
    media = soma / quantidades
    print ('Anota referente ao aluno(a):', aluno, 'é: ', media)
    return media

def aprovação(media):
    if media >=6:
        print ("O Aluno foi aprovado")
    else:
        print ('Aluno não foi Aprovado')

aluno = input('Escreva nome do aluno: ')
v = []
while len(v) < 4:
    x = int(input("Escreva as notas do bimestre: "))
    v.append(x)

media = calcular_medida (v)
aprovação(media)

