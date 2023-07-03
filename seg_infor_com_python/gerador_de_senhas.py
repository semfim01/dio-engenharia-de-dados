import random 
import string
# ou posso colocar uma vírgula e colocar string ....

tamanho = 16

chars = string.ascii_letters + string.digits + '!@#$%&*()_+-.='
# gera senhas maiuscúlas e minuscúlas usando o ascii_letters
#se usar ascii_lowercase vai ter so minuscula e upper só maiúsculas 

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
#a cada digito adicionarar um caracter
