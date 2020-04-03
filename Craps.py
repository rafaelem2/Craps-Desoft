import random
import time  #importando as bibliotecas usadas
jogo=True #O jogo pode continuar ou ser parado (True or False)
resposta=input("Você quer jogar Craps? s/n ")
while jogo==True: #Introduzindo o jogo e aplicando um loop
    if resposta == "s":
        print('Você está na fase Come Out') 
        time.sleep(1) #Time sleep afim de gerar dinâmica ao jogo
        fichas = int(input('Quantas fichas você tem?: '))
        print('Você tem {0} fichas'.format(fichas))
        time.sleep(1)
        aposta= int(input('Quantas fichas você quer apostar?: '))
        time.sleep(1)
        if fichas<aposta:
            print('Insira um valor válido')
            jogo=True #aposta invalida recomeça o jogo
        else:
            tipo_de_aposta= input('Qual aposta você quer fazer? Pass Line Bet, Field, Any Craps ou Twelve?: ')#O jogo pergunta qual aposta a pessoa deseja fazer
            if tipo_de_aposta=="Pass Line Bet":#Aposta Pass Line Bet
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                print("o resultado foi {}" .format(dado))
                if dado == 7 or dado == 11:
                    print('Você ganhou a aposta e {0} fichas'.format(aposta))
                    fichas += aposta
                    time.sleep(1)
                    print('Você tem {0} fichas '.format(fichas))
                    jogo=True
                    
                elif dado == 2 or dado == 3 or dado == 12:
                    print('Você perdeu a aposta e {0} fichas.'.format(aposta))
                    fichas -= aposta
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                    Jogo=True
                    
                if fichas == 0:
                    time.sleep(1)
                    print('Você não tem mais fichas:(')
                    jogo=False #Quando as fichas acabam, o jogo para
                elif dado==1 or dado==4 or dado==5 or dado==6 or dado==8 or dado==9 or dado==10:
                    print("Hora de jogar na fase point") #Fase point
                    time.sleep(1)
                    point = dado
                    print('Você está jogando na Fase Point')
                    time.sleep(1)
                    print('O point para você ganhar é o número {0}'.format(point))
                    input("Pressione Enter para jogar")
                    dado2 = random.randint(1, 6) + random.randint(1, 6)
                    while dado2 != point and dado2 != 7:#loop até o jogador ganhar ou perder
                        print('Você tirou {0}, continue jogando'.format(dado2))
                        input("Pressione Enter para jogar")
                        dado2 = random.randint(1, 6) + random.randint(1, 6)
                        if dado2 == point:                      
                            print('Você acertou o point e ganhou {0} fichas!'.format(aposta))
                            time.sleep(1)
                            fichas += aposta*2
                            print('Você tem {0} fichas '.format(fichas))
                        if dado2 == 7:
                            print('O resultado foi 7 e você perdeu {0} fichas'.format(aposta))
                            time.sleep(1)
                            fichas-=aposta
                            print('Você tem {0} fichas '.format(fichas))
                            if fichas==0:
                                print('Você não tem mais fichas:(') 
                                jogo=False       


            elif tipo_de_aposta== "Field": #Aposta Field
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                print("o resultado foi {}" .format(dado))
                if dado == 5 or dado == 6 or dado == 7 or dado == 8:
                    time.sleep(1)
                    print('Você perdeu a aposta e todas as suas {0} fichas, tchau!.'.format(fichas))
                    fichas -= aposta
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if dado == 3 or dado == 4 or dado == 9 or dado == 10 or dado == 11:
                    time.sleep(1)
                    print('Você ganhou a aposta e {0} fichas'.format(aposta))
                    fichas += aposta
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if dado == 2:
                    time.sleep(1)
                    print('Você ganhou a aposta e {0} fichas'.format(aposta*2))
                    fichas += aposta*2
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if dado==12:
                    time.sleep(1)
                    print('Você ganhou a aposta e {0} fichas'.format(aposta*3))
                    fichas += aposta*3
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if fichas == 0:
                    print('Você não tem mais fichas:(')
                    jogo=False
            elif tipo_de_aposta== "Any Craps": #Aposta Any Craps
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                print("o resultado foi {}" .format(dado))
                if dado == 2 or dado == 3 or dado == 12:
                    time.sleep(1)
                    print('Você ganhou a aposta e {0} fichas'.format(aposta*7))
                    fichas += aposta*7
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                else:
                    time.sleep(1)
                    print('Você não ganhou a aposta e perdeu {0} fichas.'.format(aposta))
                    fichas -= aposta
                    time.sleep(1)
                    print('Suas fichas: {0}'.format(fichas))
                if fichas == 0:
                    print('Você não tem mais fichas:(')
                    jogo=False
            elif tipo_de_aposta == "Twelve": #Aposta Twelve
                input("Pressione Enter para jogar")
                dado = random.randint(1, 6) + random.randint(1, 6)
                print("o resultado foi {}" .format(dado))
                
                if dado == 12:
                    time.sleep(1)
                    print('Você ganhou a aposta e {0} fichas'.format(aposta*30))
                    fichas += (aposta*30)
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                else:
                    time.sleep(1)
                    print('Você não ganhou a aposta e perdeu {0} fichas.'.format(aposta))
                    fichas -= aposta
                    time.sleep(1)
                    print('Você tem {0} fichas'.format(fichas))
                if fichas == 0:
                    print('Você não tem mais fichas:(')
                    jogo=False
    else:
        input("ENTER para sair") #Se a pessoa não quiser jogar, o programa para
        jogo=False
   

    