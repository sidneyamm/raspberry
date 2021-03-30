# -*- coding: utf-8 -*- # Codificação mais comum da www (World Wide Web)

# Comando bash do linux para uso do Python
#!/usr/bin/env python

# Importação da Biblioteca para uso dos pinos do Raspberry
import RPi.GPIO as GPIO

# Importação da Biblioteca para uso de alguns comandos do sistema
import sys

# Importação da Biblioteca para uso de comandos de tempo
import time

GPIO.setwarnings(False) # Remove mensagens de alerta
GPIO.setmode(GPIO.BOARD) # Definição do uso e estado dos pinos GPIO
GPIO.setup(11,GPIO.OUT) # Acende/Apaga a Lampada da Frente de Casa
GPIO.setup(12,GPIO.OUT) # Acende/Apaga a Lampada da Garagem
GPIO.setup(15,GPIO.OUT) # Acende/Apaga a Lampada do Jardim de Inverno
GPIO.setup(19,GPIO.OUT) # Liga/Desliga o Sistema de Alarme
GPIO.setup(22,GPIO.OUT) # Liga/Desliga a Automação Automática/Manual dos Portões e Lâmpadas
GPIO.setup(23,GPIO.OUT) # Aciona/Desaciona a Sirene
GPIO.setup(24,GPIO.IN) # Sensor do Portao Automatico da Garagem
GPIO.setup(26,GPIO.IN) # Sensor do Portao do Jardim de Inverno

# Contador utilizado para acionar a Sirene apenas 1 vez ao entrar na programação de horário da Automação Automática do Sistema de Alarme
cont = 0

# Contador utilizado para não acionar a Sirene ao entrar na programação de horário da Automação Automática do Sistema de Alarme, mas que irá acionar a Sirene toda vez que sair do horário programado da Automação Automática do Sistema de Alarme
cont2 = 1

# Loop Infinito
while (1):

    # stata recebe estado do Alarme: 1 - Ligado ou 0 - Desligado
    stata = GPIO.input(19)

    if(stata == 1):

        # Aguarda 1 segundo até soar a Sirene do Sistema de Alarme
        time.sleep(1)

        # Pega o estado do Sensor do Portão Automático da Garagem: 0 - Fechado, 1 - Aberto
        state = GPIO.input(24)
        # Pega o estado do Sensor do Portão do Jardim de Inverno: 0 - Fechado, 1 - Aberto        
        stati = GPIO.input(26)
        
        if((state == 1) or (stati == 1)):

            GPIO.output(23,1) # Aciona a Sirene

        else:

            GPIO.output(23,0) # Desliga a Sirene

    # Pega o estado da Automação Automática/Manual dos Portões e Lâmpadas: 0 - Automática, 1 - Manual
    stato = GPIO.input(22)

    if(stato == 0):

        # Pega o estado do Sensor do Portão Automático da Garagem: 0 - Fechado, 1 - Aberto
        state = GPIO.input(24)

        if(state == 1):

            GPIO.output(12,1) # Liga as Lâmpadas da Garagem

        else:

            GPIO.output(12,0) # Desliga as Lâmpadas da Garagem

        # Pega o estado do Sensor do Portão do Jardim de Inverno: 0 - Fechado, 1 - Aberto
        stati = GPIO.input(26)

        if(stati == 1):

            GPIO.output(11,1) # Liga a Lâmpada da Frente da Casa
            GPIO.output(15,1) # Liga as Lâmpadas do Jardim de Inverno

        else:

            GPIO.output(11,0) # Desliga a Lâmpada da Frente da Casa
            GPIO.output(15,0) # Desliga as Lâmpadas do Jardim de Inverno

# sudo crontab -eu root # para crontab como root e na raiz
# crontab -e # para usar crontab como usuário
# @reboot python /home/pi/Desktop/inicializar/plgji.py &
