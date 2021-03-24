# -*- coding: utf-8 -*- # Codificação mais comum da www (World Wide Web)

# Comando bash do linux para uso do Python
#!/usr/bin/env python

import RPi.GPIO as GPIO # Importação da Biblioteca para uso dos pinos do Raspberry

import sys # Importação da Biblioteca para uso de alguns comandos do sistema

import time # Importação da Biblioteca para uso de comandos de tempo

# from datetime import datetime # Importação da Biblioteca para uso de comandos de datas e horas

GPIO.setwarnings(False) # Remove mensagens de alerta
GPIO.setmode(GPIO.BOARD) # Definição do uso e estado dos pinos GPIO
GPIO.setup(11,GPIO.OUT) # Acende/Apaga a Lampada da Frente de Casa
GPIO.setup(12,GPIO.OUT) # Acende/Apaga a Lampada da Garagem
GPIO.setup(15,GPIO.OUT) # Acende/Apaga a Lampada do Jardim de Inverno
GPIO.setup(19,GPIO.OUT) # Liga/Desliga o Sistema de Alarme
GPIO.setup(22,GPIO.OUT) # Liga/Desliga Automação Manual/Automática
GPIO.setup(23,GPIO.OUT) # Aciona/Desaciona a Sirene
GPIO.setup(24,GPIO.IN) # Sensor do Portao Automatico da Garagem
GPIO.setup(26,GPIO.IN) # Sensor do Portao do Jardim de Inverno

# Loop infinito
while (1):

#    data_e_hora_atuais = datetime.now()
#    hora = data_e_hora_atuais.strftime('%H')

    stata = GPIO.input(19)

    if(stata == 1):

        time.sleep(1) # Aguarda 1 segundo até soar o Alarme de Ligado

        state = GPIO.input(24) # Verifica se Portão Automático da Garagem está Aberto (1) ou Fechado (0)
        stati = GPIO.input(26) # Verifica se Portão do Jardim de Inverno está Aberto (1) ou Fechado (0)

        if((state == 1) or (stati == 1)):

            GPIO.output(23,1) # Se Portão Aotomático da Garagem Abrir, Aciona o Sistema de Alarme

        else:

            GPIO.output(23,0) # Se o Portão Automático da Garagem Fechar, Desaciona o Sistema de Alarme

    stato = GPIO.input(22)

    if(stato == 0):

        state = GPIO.input(24)

        if(state == 1):

            GPIO.output(12,1)

        else:

            GPIO.output(12,0)

        stati = GPIO.input(26)

        if(stati == 1):

            GPIO.output(11,1)
            GPIO.output(15,1)

        else:

            GPIO.output(11,0)
            GPIO.output(15,0)

#@reboot python /home/pi/Desktop/inicializar/plgji.py &
