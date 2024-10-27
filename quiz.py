# Faça um quiz sobre jogos.
import time

print('Seja Bem-vindo ao Quiz de Jogos.')
print('=' * 40)
try:
    time.sleep(2)
    print('-' * 30)
    print('Vamos então começar!')
    time.sleep(1)

    
    farcry = input('Qual Farcry é considerado o melhor de todos os tempos?: ')
    farcry = farcry.lower().replace(" ", "")
    print('-' * 70)
    
    if farcry.lower() == 'farcry3':
        print('Certa Resposta!')
    elif farcry.lower() == 'farcry2':
        print('Quase você acertou, Far cry 2 é considerado o 6° Melhor.')
    elif farcry.lower() == 'farcry5':
        print('Passou perto, o Farcry 5 é considerando o 2° Melhor.')
    elif farcry.lower() == 'farcry4':
        print('Quase, o Farcry 4 é considerando o 3° Melhor.')
    elif farcry.lower() == 'farcry6':
        print('Errou. o Farcry 6 é considerado o 4° Melhor.')
    elif farcry.lower() == 'farcryprimal':
        print('Passou Longe. o Farcry Primal é considerado o 5° Melhor.')
    elif farcry.lower() == 'farcry1':
        print('Desculpe, o Farcry 1 é considerando o 6° Melhor.')
        time.sleep(2)
    else:
        print('Não entendi.')
        exit()

    time.sleep(2)
    print('-' * 60)
    print('Obrigado por jogar meu Quiz, Até mais!')
    print('=' * 40)
except ValueError:
    print(f"Ocorreu um erro!")

exit()
