"""
Esse Software é para auxiliar na programação de culto das igrejas durante o mês
pode ser utilizado tanto para culto gerais como para departamentos de igrejas
No meu caso estou fazendo para os Jovens por senti a necessidade de criar esse software.

02/08/2022 
"""
import random
dia_semana = int(input("Digite quantidade de semana que tem culto: "))
mes = input("Digite o mês da programação: ")
nova_list =[]
jovens = ['Carlos Gustavo',
             'Nicolle',
             'Marta',
             'Gilda',
             'Cecilly',
             'Sophya',
             'Diogo',
             'Debora',
             'Cinthia',
             'Ana Claudia',
             'Ana Vitoria',
             'Saphyra',
             'Jotta Castro',
             'Pr. Cordeiro']

pregadores = ['Jotta Castro', 'Pr. Cordeiro', 'Gilda', 'Marta']

print('\U0001F50A\U0001F50A\U0001F50A==========AVISO IMPORTANTES!==========\U0001F50A\U0001F50A\U0001F50A')
print('')
print('*Olá Mocidade, Graça e a Paz! Tudo bem com vocês?*')
print(f'_Esse é o cronograma do mês do 📅*{mes}*_')
print('_Fiquem atentos pelo do dia da sua participação_\n_Se tiverem em dúvida estou aqui para ajudar_\n_Que Deus abençoe todos vocês🤲_')
print('')
print(20*'=')


dir = random.sample(jovens ,dia_semana)
din = random.sample(jovens, dia_semana)
random.shuffle(pregadores)
pre = pregadores

for i in pre:
    for j in dir:
        if i == j:
            random.shuffle(pre)
            break
for i in din:
    for j in dir:
        if i == j:
                din.remove(i)
                din += random.sample(jovens, 1)
                break

for i in pre:
    for j in din:
        if i == j:
            random.shuffle(pre)
            break
for i in dir:
    for j in din:
        if i == j:
            dir.remove(i)
            dir += random.sample(jovens, 1)
            break



x = 0
while x < dia_semana:
        print(f'📅*{x+1}º Sábado:*')
        print(f'🎤*Dirigente:* _{dir[x]}_')
        print(f'🤾*Dinâmica:* _{din[x]}_')
        print(f'📖*Pregador:* _{pre[x]}_')
        print('='*10)
        x+=1




