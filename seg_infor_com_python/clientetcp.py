import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!!')
        print('erro: {}'.format(e))
        sys.exit()

    print('socket criado com sucesso')

    hostalvo = input('digite o host ou ip a ser conectado:')
    portaalvo = input('digite a porta a ser conectada: ')

    try:
        s.connect((hostalvo, int(portaalvo)))
        print('cliente tcp conectado com sucesso no host: ' + hostalvo + 'e na porta: ' + portaalvo)
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possível conectar no host: ' + hostalvo +'e na porta: ' + portaalvo)
        print('Error: {}'.format(e))
        sys.exit()
if __name__ == '__main__':
    main()