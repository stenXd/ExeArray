nomes = []
senhas = []
for i in range(5):
    nome = input('Digite seu nome:')
    senha = input('Digite sua senha:')
    nomes.append(nome)
    senhas.append(senha)
for i in range(5):
    print('Nome:', nomes[i])
    print('Senha:', senhas[i])
    print('Posição:', i)
