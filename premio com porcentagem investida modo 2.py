nome1 = input("digite o nome do primeiro investidor:")
nome2 = input("digite o nome do segundo investidor:")
nome3 = input("digite o nome do terceiro investidor:")

Var1 = float(input("digite o valor investido pelo primeiro investidor em reais:"))
Var2 = float(input("digite o valor investido pelo segundo investidor em reais:"))
Var3 = float(input("digite o valor investido pelo segundo investidor em reais: "))
premio = float(input("digite o valor do premio em reais:"))

Var_total = float(Var1 + Var2 + Var3)
print(Var_total)

por1 = (Var1 / Var_total)
por2 = (Var2 / Var_total)
por3 = (Var3 / Var_total)

print(por1, por2, por3)

Valor_var1 = float(por1 * premio)
Valor_var2 = float(por2 * premio)
Valor_var3 = float(por3 * premio)

print(nome1, "ganhou, proporcional ao investimento: R$", Valor_var1)
print(nome2, "ganhou, proporcional ao investimento: R$", Valor_var2)
print(nome3, "ganhou, proporcional ao investimento: R$", Valor_var3)
