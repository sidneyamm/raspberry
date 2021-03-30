# -*- coding: utf-8 -*-

#!/usr/bin/env python # Comando bash do Linux para uso do Python

# Importação da Biblioteca para uso dos pinos do Raspberry
import RPi.GPIO as GPIO

# Importação da Biblioteca para uso de alguns comandos do sistema
import sys

# Importação da Biblioteca para uso de comandos de tempo
import time

GPIO.setwarnings(False) # Elimina mensagens de erro
GPIO.setmode(GPIO.BOARD) # Definição de uso e estado dos pinos GPIO
GPIO.setup(11,GPIO.OUT) # Acende/Apaga a Lâmpada da Frente de Casa
GPIO.setup(12,GPIO.OUT) # Acende/Apaga as Lâmpadas da Garagem
GPIO.setup(13,GPIO.OUT) # Acende/Apaga a Lâmpada do Jardim Principal
GPIO.setup(15,GPIO.OUT) # Acende/Apaga as Lâmpadas do Jardim de Inverno
GPIO.setup(16,GPIO.OUT) # Abre/Fecha o Portão Automático da Garagem
GPIO.setup(19,GPIO.OUT) # Liga/Desliga o Sistema de Alarme
GPIO.setup(22,GPIO.OUT) # Liga/Desliga a Automação Automática/Manual de Portões e Lâmpadas
GPIO.setup(23,GPIO.OUT) # Liga/Desliga a Sirene
GPIO.setup(24,GPIO.IN) # Sensor do Portão da Garagem
GPIO.setup(26,GPIO.IN) # Sensor do Portão do Jardim de Inverno

# Enquanto não for recebido o comando de saída system.ext(0), continua no looping
while (True):

    # num - variável que recebe uma das opções dos subMenus
    num = int(input("\nMenu Principal (digite um dos números nas opções abaixo): \n\n1 - Acender/Apagar a Lâmpada da Frente da Casa \n2 - Acender/Apagar as Lâmpadas da Garagem \n3 - Acender/Apagar a Lâmpada do Jardim Principal \n4 - Acender/Apagar as Lâmpadas do Jardim de Inverno \n5 - Abrir/Fechar Portão Automático da Garagem \n6 - Ligar/Desligar o Sistema de Alarme \n7 - Ligar/Desligar a Automação Automática/Manual dos Portões e Lâmpadas \n0 - Para Sair \n\n"))

    # Se a opção digitada for 1, entra no subMenu Acencer/Apagar a Lâmpada da Frente de Casa
    if(num == 1):

        # Enquanto não for digitada a opção de saída break, continua no looping
        while (True):

            # Informa o subMenu atual
            print("\nVocê está no subMenu Acender/Apagar a Lâmpada da Frente de Casa")

            # Verifica o estado atual do pino 11
            state = GPIO.input(11)

            # Se variável state for 1
            if(state == 1):

                # Informa que o dispositivo está ligado
                print("\nO estado atual da Lâmpada é LIGADA")

            # Se variável state não for 1 (será 0)
            else:

                # Informa que o dispositivo está desligado
                print("\nO estado atual da Lâmpada é DESLIGADA")

            # opcao - variável que recebe uma das ações a serem executadas
            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Acender a Lâmpada da Frente de Casa \n2 - Para Apagar a Lâmpada da Frente de Casa \n3 - Voltar para o Menu Principal \n\n"))

            # Se variável opcao for 1
            if(opcao == 1):

                # Liga o relé e imprime a mensagem
                GPIO.output(11,1)
                print("\nLâmpada Acesa")

            # Se variável opcao for 2
            elif(opcao == 2):

                # Desliga o relé e imprime a mensagem
                GPIO.output(11,0)
                print("\nLâmpada Apagada")

            # Se variável opcao for 3
            elif(opcao == 3):

                # Sai do looping do subMenu
                break

            # Se variável opcao receber um número diferente
            else:

                # Imprime a mensagem, não sai do looping e exibe novamente o subMenu
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

            # Pino 24 informa o estado do Sensor do Portão Automático da Garagem
            state = GPIO.input(24)

            if(state == 1):

                print("\nO estado atual do Portão Automático da Garagem é ABERTO")

            else:

                print("\nO estado atual do Portão Automático da Garagem é FECHADO")

            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Abrir/Fechar o Portão Automático da Garagem \n2 - Para verificar o estado do Portão Automático da Garagem (ABERTO ou FECHADO) \n3 - Voltar para o Menu Principal \n\n"))

            if(opcao == 1):

                # Pino 16 aciona o Relé que liga o Controle Remoto do Portão Automático da Garagem
                GPIO.output(16,1)
                # Tempo de 1 segundo de acionamento
                time.sleep(1)
                GPIO.output(16,0)
                print("\nPortão Automático da Garagem Abriu/Fechou")

            # Opção para a verificar o estado do portão (ABERTO ou FECHADO)
            elif(opcao == 2):

                time.sleep(0.25)

            elif(opcao == 3):

                break

            else:

                print("\nOpção Inválida, digite um número válido")

    elif(num == 6):

        while (True):

            print("\nVocê está no subMenu Ligar/Desligar o Sistema de Alarme")

            # O Pino 19 liga/desliga o Sistema de Alarme, é de controle e usado para verificar seu estado (0 - Desligado ou 1 - Ligado)
            state = GPIO.input(19)

            if(state == 1):

                print("\nO estado atual do Sistema de Alarme é LIGADO")

            else:

                print("\nO estado atual do Sistema de Alarme é DESLIGADO")

            opcao = int(input("\nDigite um dos números para uma das ações abaixo: \n\n1 - Para Ligar o Sistema de Alarme \n2 - Para Desligar o Sistema de Alarme \n3 - Voltar para o Menu Principal \n\n"))

            # A Sirene toca 2 vezes informando que o Sistema de Alarme foi ligado
            if(opcao == 1):

                GPIO.output(19,1)
                print("\nSistema de Alarme Ligado")
                # Aciona a Sirene por 0,25 segundos, o Pino 23 aciona o Relé 
                GPIO.output(23,1)
                time.sleep(0.25)
                # Desliga a Sirene e aguarda 0,25 segundos
                GPIO.output(23,0)
                time.sleep(0.25)
                # Aciona a Sirene por 0,25 segundos pela 2a vez
                GPIO.output(23,1)
                time.sleep(0.25)
                GPIO.output(23,0)

            # A Sirene toca 1 vez informando que o Sistema de Alarme foi desligado
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

            # O Pino 22 é apenas de estado para verificar a opção Automática/Manual dos Portões e Lâmpadas
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

    # Se a variável num for 0, sai do script
    elif(num == 0):

        # Comando que encerra um script python
        sys.exit()

    # Se a variável num for diferente das opções, imprime a mensagem abaixo
    else:

        print("\nOpção Inválida, digite um número válido")
