import math

#Datos
consumoElectricidadAnual = 12000 #kWh
consumoElectricidadDiaria = 12000 / 365 #kWh
eficienciaPanel = 0.15 #15%
radiacionSolar = 5  #kWh/m²/día
areaPanel = 1.6 #m2

#Formulas
potenciaGeneradaDia = areaPanel * radiacionSolar * eficienciaPanel
potenciaGeneradaAnual = potenciaGeneradaDia * 365
numPanel = consumoElectricidadAnual / potenciaGeneradaAnual
panelExacto = math.ceil(numPanel)

#Resultados
print(f"Potencia generada por panel anualmente es: {potenciaGeneradaAnual} kWh")
print(f"Potencia generada por panel al dia es: {potenciaGeneradaDia} kWh")
print(f"Los paneles necesarios son: {numPanel}")
print(f"Paneles solares necesarios exactos son: {panelExacto}")

print()
print("Extra")

#Extra "Datos"
extraConsumoElectricidadAnual = float(input("Digite la cantidad de energia anual consumida anualmente en kWh: "))
ExtraEficienciaPanel = float(input("Digite el porcentaje de la eficiencia de los paneles solares: "))
extraEficienciaPanel = ExtraEficienciaPanel / 100
extraAreaPanel = float(input("Digite en metros cuadrados el area de los paneles: "))
extraRadiacionSolar = float(input("Digite la cantidad de horas promedio que se encuentra el sol en su localidad: "))

#Extra "Formulas"
extraPotenciaGeneradaDia = extraAreaPanel * extraRadiacionSolar * extraEficienciaPanel
extraPotenciaGeneradaAnual = extraPotenciaGeneradaDia * 365
extraNumPanel = extraConsumoElectricidadAnual / extraPotenciaGeneradaAnual
extraPanelExacto = math.ceil(extraNumPanel)

print()

#Extra "Resultados"
print(f"Potencia generada por panel anualmente es: {extraPotenciaGeneradaAnual} kWh")
print(f"Potencia generada por panel al dia es: {extraPotenciaGeneradaDia} kWh")
print(f"Los paneles necesarios son: {extraNumPanel}")
print(f"Paneles solares necesarios exactos son: {extraPanelExacto}")
