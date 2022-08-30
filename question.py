"""
Este programa é mais para treinar meu conhecimento com dicionario e fazer
um sistema simples de perguntas e respostas para brincar

o intuito é fazer perguntas para gincanas na igreja e demais modalidade

29/08/2022

"""
import time
print()
questions = {  # dicionario de perguntas e respostas
    'Pergunta 01': {  
        'pergunta': 'A quem Paulo chamou de meu companheiro de lutas: ',
        'alternativas':{'A':'Apolo','B':'Arquipo','C':'Àfia',},
        'resp_certa':'B',
    },  
    'Pergunta 02': {
        'pergunta': 'Quais discípulos perguntaram a Jesus se podiam fazer descer fogo do céu? ',
        'alternativas': {'A': 'João e Tiago', 'B': 'Pedro e João', 'C':'Tiago e Pedro', },
        'resp_certa': 'A',
    },
    'Pergunta 03': {
        'pergunta': 'Qual era o nome da serpente de bronze que Moisés tinha feito? ',
        'alternativas': {'A': 'Aserá', 'B': 'Leviatã', 'C': 'Neustã', },
        'resp_certa': 'C',
    },
    'Pergunta 04': {
        'pergunta': 'Qual era o nome babilônico de Daniel?',
        'alternativas': {'A': 'Aspenaz', 'B': 'Beltessazar', 'C': 'Abede-Nego', },
        'resp_certa': 'B',
    },
    'Pergunta 05': {
        'pergunta': 'Qual o nome que Jacó deu ao lugar onde sonhou com Deus? ',
        'alternativas': {'A': 'Betuel', 'B': 'Luz', 'C': 'Betel', },
        'resp_certa': 'C',
    },
    'Pergunta 06': {
        'pergunta': 'Qual o livro da Bíblia que termina com um ponto de interrogação? ',
        'alternativas': {'A': 'Jonas', 'B': 'Joel', 'C': 'Judas', },
        'resp_certa': 'A',
    },
    'Pergunta 07': {
        'pergunta': 'Qual o menor livro da Bíblia? ',
        'alternativas': {'A': 'Judas', 'B': 'II João', 'C': 'III João', },
        'resp_certa': 'B',
    },
    'Pergunta 08': {
        'pergunta': 'Qual livro se encontra no Novo Testamento? ',
        'alternativas': {'A': 'Sofonias', 'B': 'Filemon', 'C': 'Habacuque', },
        'resp_certa': 'B',
    },
    'Pergunta 09': {
        'pergunta': 'Quem teve seu corpo disputado pelo arcanjo Miguel e o Diabo? ',
        'alternativas': {'A': 'Jesus', 'B': 'Eliseu', 'C': 'Moisés', },
        'resp_certa': 'C',
    },
    'Pergunta 10': {
        'pergunta': 'Quem foi a única mulher citada na Bíblia a ter o status de juíza e líder de Israel? ',
        'alternativas': {'A': 'Jael', 'B': 'Débora', 'C': 'Ester', },
        'resp_certa': 'C',
    },
}
ponto = 0
erro = 0
for p, r in questions.items():
    print(f'{p}: {r["pergunta"]}')
    for i, n in r["alternativas"].items():
        print(f'{i}) {n}')
    resp = input('Escolha a alternativa correta: ')
    if resp.upper() == r['resp_certa']:
        print('Wow! Você Acertou!!')
        print()
        ponto += 1
    else:
        print('Que pena! Você Errou!')
        print()
        erro += 1
    time.sleep(3)
   
    print()
print('Calculando os Pontos... ')
time.sleep(6)
print(f'Seu acertos foram {ponto}!')
print(f'Seu erros foram {erro}!')

enter = input('Aperte Enter para Finalizar....')
