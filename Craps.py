import random
import time
jogo=True
resposta=input("Você quer jogar Craps? s/n ")
while jogo==True:
    if resposta == "s":
        print('Fase: Come Out')
        time.sleep(1)
        fichas = int(input('Quantas fichas tem?: '))
        print('Suas fichas: {0}'.format(fichas))
        time.sleep(1)
        bet = int(input('Quantas fichas você quer apostar?: '))
        time.sleep(1)
        if fichas<bet:
            print('Insira um valor válido')
            jogo=True
        else:
            aposta = input('Que tipo de aposta você quer fazer?: ')
            if aposta=="Pass Line Bet":
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                print("o resultado foi {}" .format(dado))
                if dado == 7 or dado == 11:
                    print('Você ganhou a aposta e conseguiu {0} fichas!'.format(bet))
                    fichas += bet
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                elif dado == 2 or dado == 3 or dado == 12:
                    print('Você não ganhou a aposta e perdeu {0} fichas.'.format(bet))
                    fichas -= bet
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                else:
                    print("Hora de jogar na fase point")
            elif aposta == "Field":
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                time.sleep(1)
                print("o resultado foi {}" .format(dado))
                if dado == 5 or dado == 6 or dado == 7 or dado == 8:
                    time.sleep(1)
                    print('Você não ganhou a aposta e perdeu todas as suas {0} fichas!.'.format(fichas))
                    fichas -= fichas
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                if dado == 3 or dado == 4 or dado == 9 or dado == 10 or dado == 11:
                    time.sleep(1)
                    print('Você ganhou a aposta e conseguiu {0} fichas!'.format(bet))
                    fichas += bet
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                if dado == 2:
                    time.sleep(1)
                    print('Você ganhou a aposta e conseguiu {0} fichas!'.format(bet*2))
                    fichas += (bet*2)
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                if dado==12:
                    time.sleep(1)
                    print('Você ganhou a aposta e conseguiu {0} fichas!'.format(bet*3))
                    fichas += (bet*3)
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                if fichas == 0:
                    time.sleep(1)
                    print('Suas fichas acabaram!')
            elif aposta == "Any Craps":
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                time.sleep(1)
                print("o resultado foi {}" .format(dado))
                if dado == 2 or dado == 3 or dado == 12:
                    time.sleep(1)
                    print('Você ganhou a aposta e conseguiu {0} fichas!'.format(bet*7))
                    fichas += (bet*7)
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                else:
                    time.sleep(1)
                    print('Você não ganhou a aposta e perdeu {0} fichas.'.format(bet))
                    fichas -= bet
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                    if fichas == 0:
                        time.sleep(1)
                        print('Suas fichas acabaram!')
    
else:
    input("ENTER para sair")
   

    