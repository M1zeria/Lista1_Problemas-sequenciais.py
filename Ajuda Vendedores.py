valorPro = int(input())
aVista = valorPro*0.9
parcelado = valorPro/3
comissaoVista = aVista*0.05
comissaoParcela = valorPro*0.05
print(f"A vista com desconto de 10%: {aVista:.2f}")
print(f"Valor da parcela em 3x sem juros: {parcelado:.2f}")
print(f"Comissao do vendedor a vista: {comissaoVista:.2f}")
print(f"Comissao do vendedor a prazo: {comissaoParcela:.2f}")
