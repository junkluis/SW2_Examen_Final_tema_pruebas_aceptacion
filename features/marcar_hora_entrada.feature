# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: 
      Dado mi codigo 20131
      Cuando ingreso el dia lunes con la hora 07, minutos 14 y segundos 59
      Entonces genera el siguiete resultado 'Inicio de Jornada a tiempo, Bienvenido Luis Zuniga.'
      Entonces mi tipo de jornada laboral es 'Diurno A'

    Escenario:
    	Dado mi codigo 20131
		Cuando ingreso el dia martes con la hora 07, minutos 14 y segundos 59
		Entonces no puedo ingresar porque 'EL día martes no tiene jornada laboral programada.'

	Escenario:
		
