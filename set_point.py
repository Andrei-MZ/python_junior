import math

dados = [
    [20, 19.5], [20, 19.7], [20, 20.2], [20, 20.1], 
    [21, 19.9], [21, 20.7], [21, 21.2], [21, 21.5], 
    [25, 25.5], [25, 24.7], [25, 25.2], [25, 24.1]
]

sp_values = [dado[0] for dado in dados]
pv_values = [dado[1] for dado in dados]

def calcular_media(valores):
    return sum(valores) / len(valores)

def calcular_desvio_padrao(valores, media):
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return math.sqrt(variancia)

media_sp = calcular_media(sp_values)
desvio_padrao_sp = calcular_desvio_padrao(sp_values, media_sp)

media_pv = calcular_media(pv_values)
desvio_padrao_pv = calcular_desvio_padrao(pv_values, media_pv)

print(f"Média de SP: {media_sp:.2f}")
print(f"Desvio Padrão de SP: {desvio_padrao_sp:.2f}")

print(f"Média de PV: {media_pv:.2f}")
print(f"Desvio Padrão de PV: {desvio_padrao_pv:.2f}")
