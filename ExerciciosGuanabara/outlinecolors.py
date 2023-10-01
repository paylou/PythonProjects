nome = str(input("Informe seu primeiro nome:     ")).upper().strip()

if nome == "MARLONN":
    print("\033[35mSua cor favorita é roxo!\033[m")
elif nome ==  "PAULO" or nome == "SAVANNA":
    print("\033[32mSua cor favorita é verde!\033[m")
elif nome == "BRUNO":
    print("\033[7;30mSua cor favorita é preto!\033[m")
elif nome == "SERJÃO":
    print("\033[30mSua cor favorita é cinza!\033[m")