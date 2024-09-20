def ler_sensor(sensor):
    sensores = {
        "TEMP_INT": 150,  
        "TEMP_EXT": 20,
        "UMIDADE": 45,   
        "BOTAOPRONTO": "OFF"  
    }
    return sensores[sensor]

def acionar_exaustor(estado):
    print(f"Exaustor {estado}")

def ajustar_aquecimento(temperatura):
    if temperatura == "OFF":
        print("Desligando aquecimento")
    else:
        print(f"Aquecendo para {temperatura}°C")

def ajustar_timer(estado, tempo=None):
    if estado == "SET":
        print(f"Contador de tempo definido para {tempo} minutos")
    elif estado == "RESET":
        print("Contador de tempo resetado")

def desumidificacao(temp_int, umidade):
    if temp_int >= 15 and umidade > 40:
        print("Iniciando desumidificação...")
        acionar_exaustor("ON")
    elif temp_int < 15 or umidade <= 40:
        acionar_exaustor("OFF")
        print("Desumidificação concluída")

def controle_temperatura(temp_int, umidade):
    if temp_int < 200:
        ajustar_aquecimento(380)  
    elif umidade <= 5 and temp_int == 380:
        ajustar_aquecimento("OFF")
        print("Aquecimento concluído, forno pronto para uso")
        ajustar_timer("SET", 180)  

def verificar_botao_pronto(botao_pronto):
    if botao_pronto == "ON":
        print("Processo de cocção iniciado")
    else:
        print("Processo de cocção ainda não iniciado")

def controle_forno():
    temp_int = ler_sensor("TEMP_INT")
    umidade = ler_sensor("UMIDADE")
    botao_pronto = ler_sensor("BOTAOPRONTO")

    desumidificacao(temp_int, umidade)
    controle_temperatura(temp_int, umidade)
    verificar_botao_pronto(botao_pronto)

controle_forno()

