paginas = int(input())
porcentagem = float(input())
paginasTotais = (paginas*100)/porcentagem
paginasRestantes = paginasTotais-paginas
print(f"O documento possui {paginasTotais:.0f} paginas")
print(f"J� foram impressas {paginas} paginas")
print(f"Faltam {paginasRestantes:.0f} paginas")
