# -*- coding: utf-8 -*-

#!/usr/bin/env python # Comando bash do Linux para uso do Python

import RPi.GPIO as GPIO # Importação da Biblioteca para uso dos pinos do Raspberry

import sys # Importação da Biblioteca para uso de alguns comandos do sistema

import time # Importação da Biblioteca para uso de comandos de tempo

GPIO.setwarnings(False) # Elimina mensagens de erro
GPIO.setmode(GPIO.BOARD) # Definição de uso e estado dos pinos GPIO
GPIO.setup(11,GPIO.OUT) # Acende/Apaga a Lâmpada da Frente de Casa
GPIO.setup(12,GPIO.OUT) # Acende/Apaga as Lâmpadas da Garagem
GPIO.setup(13,GPIO.OUT) # Acende/Apaga a Lâmpada do Jardim Principal
GPIO.setup(15,GPIO.OUT) # Acende/Apaga as Lâmpadas do Jardim de Inverno
GPIO.setup(16,GPIO.OUT) # Abre/Fecha o Portão Automático da Garagem
GPIO.setup(18,GPIO.OUT) # Liga/Desliga a Automação Automática/Manual do Sistema de Alarme
GPIO.setup(19,GPIO.OUT) # Liga/Desliga o Sistema de Alarme
GPIO.setup(22,GPIO.OUT) # Liga/Desliga a Automação Automática/Manual de Portões e Lâmpadas
GPIO.setup(23,GPIO.OUT) # Liga/Desliga a Sirene
GPIO.setup(24,GPIO.IN) # Sensor do Portão da Garagem
GPIO.setup(26,GPIO.IN) # Sensor do Portão do Jardim de Inverno

while (True):

    num = 0


    num = int(input("\nMenu Principal (digite um dos números nas opções abaixo): \n\n1 - Acender/Apagar a Lâmpada da Frente da Casa \n2 - Acender/Apagar as Lâmpadas da Garagem \n3 - Acender/Apagar a Lâmpada do Jardim Principal \n4 - Acender/Apagar as Lâmpadas do Jardim de Inverno \n5 - Abrir/Fechar Portão Automático da Garagem \n6 - Ligar/Desligar o Sistema de Alarme \n7 - Ligar/Desligar a Automação Automática/Manual dos Portões e Lâmpadas \n8 - Liga/Desliga a Automação Automática/Manual do Sistema de Alarme \n0 - Sair do Script \n\n"))

    if(num == 1):


        while (True):


            print("\nVocê está no subMenu Acender/Apagar a Lâmpada da Frente de Casa")


	    state = GPIO.input(11)


	    if(state == 1):


		print("\nO estado atual da Lâmpada é LIGADA")


	    else:


		print("\nO estado atual da Lâmpada é DESLIGADA")


            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Acender a Lâmpada da Frente de Casa \n2 - Para Apagar a Lâmpada da Frente de Casa \n3 - Voltar para o Menu Principal \n\n"))


            if(opcao == 1):


                GPIO.output(11,1)
                print("\nLâmpada Acesa")


            elif(opcao == 2):


                GPIO.output(11,0)
                print("\nLâmpada Apagada")


            elif(opcao == 3):


                break


            else:


                print("\nOpção Inválida, digite um número válido")

    elif(num == 2):

        while (True):

            print("\nVocê está no subMenu Acender/Apagar as Lâmpadas da Garagem")

            state = GPIO.input(12)

            if(state == 1):

                print("\nO estado atual das Lâmpadas é LIGADAS")

            else:

                print("\nO estado atual das Lâmpadas é DESLIGADAS")

            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Acender as Lâmpadas da Garagem \n2 - Para Apagar as Lâmpadas da Garagem \n3 - Voltar para o Menu Principal \n\n"))

            if(opcao == 1):

                GPIO.output(12,1)
                print("\nLâmpadas Acesas")

            elif(opcao == 2):

                GPIO.output(12,0)
                print("\nLâmpadas Apagadas")

            elif(opcao == 3):

                break

            else:

                print("\nOpção Inválida, digite um número válido")

    elif(num == 3):

        while (True):

            print("\nVocê está no subMenu Acender/Apagar a Lâmpada do Jardim Principal")

            state = GPIO.input(13)

            if(state == 1):

                print("\nO estado atual da Lâmpada é LIGADA")

            else:

                print("\nO estado atual da Lâmpada é DESLIGADA")

            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Acender a Lâmpada do Jardim Principal \n2 - Para Apagar a Lâmpada do Jardim Principal \n3 - Voltar para o Menu Principal \n\n"))

            if(opcao == 1):

                GPIO.output(13,1)
                print("\nLâmpada Acesa")

            elif(opcao == 2):

                GPIO.output(13,0)
                print("\nLâmpada Apagada")

            elif(opcao == 3):

                break

            else:

                print("\nOpção Inválida, digite um número válido")

    elif(num == 4):

        while (True):

            print("\nVocê está no subMenu Acender/Apagar as Lâmpadas do Jardim de Inverno")

            state = GPIO.input(15)

            if(state == 1):

                print("\nO estado atual das Lâmpadas é LIGADAS")

            else:

                print("\nO estado atual das Lâmpadas é DESLIGADAS")

            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Acender as Lâmpadas do Jardim de Inverno \n2 - Para Apagar as Lâmpadas do Jardim de Inverno \n3 - Voltar para o Menu Principal \n\n"))

            if(opcao == 1):

                GPIO.output(15,1)
                print("\nLâmpadas Acesas")

            elif(opcao == 2):

                GPIO.output(15,0)
                print("\nLâmpadas Apagadas")

            elif(opcao == 3):

                break

            else:

                print("\nOpção Inválida, digite um número válido")

    elif(num == 5):

        while (True):

            print("\nVocê está no subMenu Abrir/Fechar o Portão Automático da Garagem")

            state = GPIO.input(24)

            if(state == 1):

                print("\nO estado atual do Portão Automático da Garagem é ABERTO")

            else:

                print("\nO estado atual do Portão Automático da Garagem é FECHADO")

            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Abrir/Fechar o Portão Automático da Garagem \n2 - Voltar para o Menu Principal \n\n"))

            if(opcao == 1):

                GPIO.output(16,1)
                time.sleep(1)
                GPIO.output(16,0)
                print("\nPortão Automático da Garagem Abriu/Fechou")

            elif(opcao == 2):

                break

            else:

                print("\nOpção Inválida, digite um número válido")

    elif(num == 6):

        while (True):

            print("\nVocê está no subMenu Ligar/Desligar o Sistema de Alarme")

            state = GPIO.input(19)

            if(state == 1):

                print("\nO estado atual do Sistema de Alarme é LIGADO")

            else:

                print("\nO estado atual do Sistema de Alarme é DESLIGADO")

            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Ligar o Sistema de Alarme \n2 - Para Desligar o Sistema de Alarme \n3 - Voltar para o Menu Principal \n\n"))

            if(opcao == 1):

                GPIO.output(19,1)
                print("\nSistema de Alarme Ligado")
                GPIO.output(23,1)
                time.sleep(0.5)
                GPIO.output(23,0)

            elif(opcao == 2):

                GPIO.output(19,0)
                print("\nSistema de Alarme Desligado")
                GPIO.output(23,1)
                time.sleep(0.25)
                GPIO.output(23,0)

            elif(opcao == 3):

                break

            else:

                print("\nOpção Inválida, digite um número válido")

    elif(num == 7):

        while (True):

            print("\nVocê está no subMenu Ligar/Desligar a Automação Automática/Manual dos Portões e Lâmpadas")

            state = GPIO.input(22)

            if(state == 0):

                print("\nO estado atual da Automação dos Portões e Lâmpadas é AUTOMÁTICA")

            else:

                print("\nO estado atual da Automação dos Portões e Lâmpadas é MANUAL")

            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Ligar a Automação Automática dos Portões e Lâmpadas \n2 - Para Ligar a Automação Manual dos Portões e Lâmpadas \n3 - Voltar para o Menu Principal \n\n"))

            if(opcao == 1):

                GPIO.output(22,0)
                print("\nAutomação dos Portões e Lâmpadas está Automática")

            elif(opcao == 2):

                GPIO.output(22,1)
                print("\nAutomação dos Portões e Lâmpadas está Manual")

            elif(opcao == 3):

                break

            else:

                print("\nOpção Inválida, digite um número válido")

    elif(num == 0): # Se a variável num for 0, sia do script

        break

    else:

        print("\nOpção Inválida, digite um número válido")
