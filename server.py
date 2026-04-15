from socket import *
from constCS import *
import json
import math

def fatorial(n):
    """Calcula o fatorial de n."""
    if n < 0:
        return "Erro: numero negativo"
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def is_primo(n):
    """Verifica se n eh primo."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(n):
    """Conta quantos primos existem ate n."""
    count = 0
    for i in range(2, n + 1):
        if is_primo(i):
            count += 1
    return count

def calculadora(a, b, op):
    """Calculadora remota: add, sub, mul, div."""
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        if b == 0:
            return "Erro: divisao por zero"
        return a / b
    else:
        return "Erro: operacao desconhecida"

def reverter_texto(texto):
    """Reverte o texto recebido."""
    return texto[::-1]

def processar_requisicao(data):
    """Processa a requisicao do cliente e retorna a resposta."""
    try:
        req = json.loads(data)
        operacao = req.get("operacao")

        if operacao == "fatorial":
            resultado = fatorial(int(req["parametro"]))
        elif operacao == "contar_primos":
            resultado = contar_primos(int(req["parametro"]))
        elif operacao == "is_primo":
            resultado = is_primo(int(req["parametro"]))
        elif operacao == "calculadora":
            resultado = calculadora(float(req["a"]), float(req["b"]), req["op"])
        elif operacao == "reverter":
            resultado = reverter_texto(str(req["parametro"]))
        else:
            resultado = "Erro: operacao desconhecida"

        resposta = {"status": "ok", "operacao": operacao, "resultado": str(resultado)}
    except Exception as e:
        resposta = {"status": "erro", "mensagem": str(e)}

    return json.dumps(resposta)

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
print(f"Servidor escutando em {HOST}:{PORT}")

(conn, addr) = s.accept()
print(f"Conexao de {addr}")
while True:
    data = conn.recv(4096)
    if not data:
        break
    msg = data.decode()
    print(f"Requisicao: {msg}")
    resposta = processar_requisicao(msg)
    print(f"Resposta: {resposta}")
    conn.send(resposta.encode())
conn.close()
print("Conexao encerrada")
