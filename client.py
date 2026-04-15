from socket import *
from constCS import *
import json

def enviar_requisicao(s, requisicao):
    """Envia uma requisicao ao servidor e retorna a resposta."""
    msg = json.dumps(requisicao)
    s.send(msg.encode())
    data = s.recv(4096)
    return json.loads(data.decode())

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
print(f"Conectado ao servidor {HOST}:{PORT}\n")

# 1. Calculadora: adicao
resp = enviar_requisicao(s, {"operacao": "calculadora", "a": 15, "b": 7, "op": "add"})
print(f"15 + 7 = {resp['resultado']}")

# 2. Calculadora: multiplicacao
resp = enviar_requisicao(s, {"operacao": "calculadora", "a": 6, "b": 8, "op": "mul"})
print(f"6 * 8 = {resp['resultado']}")

# 3. Calculadora: divisao
resp = enviar_requisicao(s, {"operacao": "calculadora", "a": 100, "b": 3, "op": "div"})
print(f"100 / 3 = {resp['resultado']}")

# 4. Fatorial
resp = enviar_requisicao(s, {"operacao": "fatorial", "parametro": 10})
print(f"Fatorial de 10 = {resp['resultado']}")

# 5. Contar primos ate 100
resp = enviar_requisicao(s, {"operacao": "contar_primos", "parametro": 100})
print(f"Primos ate 100 = {resp['resultado']}")

# 6. Verificar primo
resp = enviar_requisicao(s, {"operacao": "is_primo", "parametro": 97})
print(f"97 eh primo? {resp['resultado']}")

# 7. Reverter texto
resp = enviar_requisicao(s, {"operacao": "reverter", "parametro": "Sistemas Distribuidos"})
print(f"Texto revertido = {resp['resultado']}")

s.close()
print("\nConexao encerrada.")
