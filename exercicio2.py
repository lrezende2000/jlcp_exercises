nome = input("Digite seu nome: ")
cargo = input("Digite seu cargo: ")

print(f'Nome: {nome if len(nome) > 0 else "não informado"} - Cargo: {cargo if len(cargo) > 0 else "não informado"}')
