Algoritmo sin_titulo
	consumoElectricidadAnual = 12000
	eficienciaPanel = 0.15
	radiacionSolar = 5
	areaPanel = 1.6
	potenciaGeneradaDia = areaPanel * radiacionSolar * eficienciaPanel
	potenciaGeneradaAnual = potenciaGeneradaDia * 365
	numPanel = consumoElectricidadAnual / potenciaGeneradaAnual
	Escribir "Potencia generada por panel anualmente es: " potenciaGeneradaAnual "kWh"
	Escribir "Potencia generada por panelal dia es: " potenciaGeneradaDia "kWh"
	Escribir "Los paneles necesarios son: " numPanel
FinAlgoritmo
