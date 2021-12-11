# Faça um programa que peça as 4 notas bimestrais e mostre a média.

count = 0
soma  = 0
for nota in range(1,5):
    count += 1
    n = float(input(f'{count}° nota do Bimestre: '))
    soma += n

media = (soma)/count
print(f'A média bimestral é igual a {media}')

if media > 5.0:
    print('Aluno aprovado!!!')
else:
    print('Aluno reprovado.')