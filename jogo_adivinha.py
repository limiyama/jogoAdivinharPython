import random

def menu():
    r = int(input('Selecione: \n 1 - Adivinhar um número \n 2 - Fazer o computador adivinhar \n 3 - Sair \n'))
    if r == 1:
        adivinhar(10)
    elif r == 2:
        computadorAdivinha(10)
    else:
        exit()

def adivinhar(x):
    aleatorio = random.randint(1, x)
    palpite = 0
    while palpite != aleatorio:
        palpite = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if palpite < aleatorio:
            print('Tente novamente! Tentou baixo.')
        elif palpite > aleatorio:
            print('Tente novamente! Tentou alto.')

    print(f'Parabéns!!! Você adivinhou o número {aleatorio}!!')
    menu()
    
def computadorAdivinha(x):
    baixo = 1
    alto = x
    feedback = ''
    while feedback != 'c':
        if baixo != alto:
            tentativa = random.randint(baixo, alto)
        else:
            tentativa = baixo  
        feedback = input(f'O meu chute foi {tentativa}. Ele foi alto (digite A), baixo (digite B), ou correto (digite C)?? ').lower()
        if feedback == 'a':
            alto = tentativa - 1
        elif feedback == 'b':
            baixo = tentativa + 1

    print(f'O computador adivinhou seu número {tentativa} !!!')
    menu()

menu()
