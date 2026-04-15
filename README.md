[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)

Nícolas Santana Kruger - 202200545

## Descricao

Sistema cliente-servidor TCP que oferece 5 operacoes remotas:

### Operacoes disponiveis

1. **Calculadora** (`calculadora`) - Operacoes aritmeticas (add, sub, mul, div) com dois numeros
2. **Fatorial** (`fatorial`) - Calcula o fatorial de um numero
3. **Contar primos** (`contar_primos`) - Conta quantos numeros primos existem ate N
4. **Verificar primo** (`is_primo`) - Verifica se um numero eh primo
5. **Reverter texto** (`reverter`) - Inverte uma string

### Protocolo de comunicacao

As requisicoes e respostas sao enviadas em formato JSON via TCP.

**Requisicao:**
```json
{"operacao": "fatorial", "parametro": 10}
{"operacao": "calculadora", "a": 15, "b": 7, "op": "add"}
```

**Resposta:**
```json
{"status": "ok", "operacao": "fatorial", "resultado": "3628800"}
```

### Como executar

1. Iniciar o servidor:
```
python server.py
```

2. Em outro terminal, executar o cliente:
```
python client.py
```

### Arquivos

- `constCS.py` - Constantes de configuracao (HOST e PORT)
- `server.py` - Servidor TCP com 5 operacoes
- `client.py` - Cliente TCP que chama as operacoes do servidor
