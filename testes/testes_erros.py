try:
    numero = int(input("Digite um número: "))
    print("Você digitou:", numero)

except ValueError:
    print("Erro! Você precisa digitar um número inteiro.")

else:
    print("Conversão realizada com sucesso!")

finally: 
    print("Programa finalizado!")