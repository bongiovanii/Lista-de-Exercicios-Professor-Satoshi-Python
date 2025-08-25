   #  Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%. 

salario =  float(input("Insira o salario bruto do funcionario: "))

reajuste =  float (salario * 0.15)

salario += reajuste
print("Salario reajustado: ", salario)