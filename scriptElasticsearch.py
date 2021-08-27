from subprocess import Popen, PIPE
from os import system
from sys import stdout
from time import sleep

system('clear')

RED = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"


def animate(verifique):
    while verifique == 'false':
        stdout.write('\rloading |')
        sleep(0.1)
        stdout.write('\rloading /')
        sleep(0.1)
        stdout.write('\rloading -')
        sleep(0.1)
        stdout.write('\rloading \\')
        sleep(0.1)
    stdout.write('\rDone!     ')


def CaptureCommand(comando):
    capture = Popen(comando, shell=True, stdout=PIPE)
    return capture.stdout.read().decode('utf-8')


def ExecCommand(comando):
    system(comando)


def CheckCommand(status):
    if 'active (running)' in status:
        ExecCommand('clear')
        print()
        print('O ELASTICSEARCH ESTA ATIVADO E FUNCIONANDO')
    elif 'inactive (dead)' in status:
        ExecCommand('clear')
        print()
        print('O ELASTICSEARCH ESTA PAUSADO/INATIVO')
    else:
        print()
        print('SEU SERVIDOR NAO POSSUI O ELASTICSEARCH')


def ExecACTIVE(command, status):
    global done
    if 'active (running)' in status:
        ExecCommand('clear')
        print()
        print('O ELASTICSEARCH JA ESTA ATIVADO')
    else:
        animate('false')
        ExecCommand(command)
        ExecCommand('clear')
        print(GREEN + 'O ELASTICSEARCH FOI INICIADO' + RESET)


def ExecINACTIVE(command, status):
    global done
    if 'inactive (dead)' in status:
        ExecCommand('clear')
        print()
        print('O ELASTICSEARCH JA ESTA PAUSADO/INATIVO')
    else:
        ExecCommand(command)
        ExecCommand('clear')
        print(RED + 'O ELASTICSEARCH FOI PARADO' + RESET)


option = 0
while option != 9:
    print()
    print('[ 1 ] VERIFICAR STATUS ELASTICSEARCH')
    print('[ 2 ] PARAR ELASTICSEARCH')
    print('[ 3 ] INICIAR ELASTICSEARCH')
    print('[ 4 ] REINICIAR ELASTICSEARCH')
    print('[ 9 ] SAIR DO SCRIPT')
    option = int(input('Digite a opcao desejada: '))

    if option == 1:
        CheckCommand(CaptureCommand('service elasticsearch status'))
    elif option == 2:
        command = 'service elasticsearch stop'
        ExecINACTIVE(command, CaptureCommand(command))
    elif option == 3:
        command = 'service elasticsearch start'
        ExecACTIVE(command, CaptureCommand(command))
    elif option == 4:
        command = 'service elasticsearch restart'
        ExecACTIVE(command, CaptureCommand(command))
    elif option == 5:
        ExecCommand('clear')
    elif option == 9:
        ExecCommand('clear')
    else:
        ExecCommand('clear')
        print()
        print('POR FAVOR DIGITE UMA OPCAO VALIDA')
