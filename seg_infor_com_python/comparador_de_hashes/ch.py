import hashlib
import os

arquivo1 = os.path.join(os.path.dirname(__file__), 'a.txt')
arquivo2 = os.path.join(os.path.dirname(__file__), 'b.txt')

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1,'rb').read())
#rb é o modulo de leitura no binario

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2,'rb').read())

if hash1.digest() != hash2.digest(): 
#resume as informções
    print(f' O arquivo: "{arquivo1}" é diferente do arquivo: "{arquivo2}"')
else:
    print(f'O arquivo: "{arquivo1}" é igual ao arquivo: "{arquivo2}"')