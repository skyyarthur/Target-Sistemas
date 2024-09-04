def reverter_texto(palavra):
    return palavra[::-1]

entrada = input("Digite um texto: ")
resultado_reverso = reverter_texto(entrada)
print(f"string invertida: {resultado_reverso}")
