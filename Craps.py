import random
import time  #importando as bibliotecas usadas
jogo=True
resposta=input("Você quer jogar Craps? s/n ")
while jogo==True: #Introduzindo o jogo e aplicando um loop
    if resposta == "s":
        print('Você está na fase Come Out') 
        time.sleep(1)
        fichas = int(input('Quantas fichas você tem?: '))
        print('Você tem {0} fichas'.format(fichas))
        time.sleep(1)
        bet = int(input('Quantas fichas você quer apostar?: '))
        time.sleep(1)
        if fichas<bet:
            print('Insira um valor válido')
            jogo=True #aposta invalida recomeça o jogo
        else:
            aposta = input('Qual aposta você quer fazer? Pass line Bet, Field, Any Craps ou Twelve?: ')
            if aposta=="Pass Line Bet":#Aposta Pass Line Bet
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                print("o resultado foi {}" .format(dado))
                if dado == 7 or dado == 11:
                    print('Você ganhou a aposta e {0} fichas'.format(bet))
                    fichas += bet
                    time.sleep(1)
                    print('Você tem {0} fichas '.format(fichas))
                elif dado == 2 or dado == 3 or dado == 12:
                    print('Você perdeu a aposta e {0} fichas.'.format(bet))
                    fichas -= bet
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if fichas == 0:
                    time.sleep(1)
                    print('Você não tem mais fichas:(')
                    jogo=False #Quando as fichas acabam, o jogo para
                else:
                    print("Hora de jogar na fase point") #fase point
            elif aposta == "Field": #Aposta Field
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                time.sleep(1)
                print("o resultado foi {}" .format(dado))
                if dado == 5 or dado == 6 or dado == 7 or dado == 8:
                    time.sleep(1)
                    print('Você perdeu a aposta e todas as suas {0} fichas, tchau!.'.format(fichas))
                    fichas -= bet
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if dado == 3 or dado == 4 or dado == 9 or dado == 10 or dado == 11:
                    time.sleep(1)
                    print('Você ganhou a aposta e {0} fichas'.format(bet))
                    fichas += bet
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if dado == 2:
                    time.sleep(1)
                    print('Você ganhou a aposta e {0} fichas'.format(bet*2))
                    fichas += (bet*2)
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if dado==12:
                    time.sleep(1)
                    print('Você ganhou a aposta e {0} fichas'.format(bet*3))
                    fichas += (bet*3)
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if fichas == 0:
                    time.sleep(1)
                    print('Você não tem mais fichas:(')
                    jogo=False
            elif aposta == "Any Craps": #Aposta Any Craps
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
                    print('Você não tem mais fichas:(')
                    jogo=False
            elif aposta == "Twelve": #Aposta Twelve
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                time.sleep(1)
                print("o resultado foi {}" .format(dado))
                
                if dado == 12:
                    time.sleep(1)
                    print('Você ganhou a aposta e conseguiu {0} fichas!'.format(bet*30))
                    fichas += (bet*30)
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                else:
                    time.sleep(1)
                    print('Você não ganhou a aposta e perdeu {0} fichas.'.format(bet))
                    fichas -= bet
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                if fichas == 0:
                    print('Você não tem mais fichas:(')
                    jogo=False
else:
    input("ENTER para sair") #Se a pessoa não quiser jogar, o programa para
   

    