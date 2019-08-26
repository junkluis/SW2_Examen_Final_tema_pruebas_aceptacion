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
		Dado mi codigo 20131
		Cuando ingreso el dia lunes con la hora 07, minutos 16 y segundos 59
		Entonces genera el siguiete resultado 'Inicio de Jornada atrasada por 0:02:00.'

	Escenario:
		Dado mi codigo 20131
		Cuando ingreso el dia lunes con la hora 06, minutos 40 y segundos 00
		Entonces genera el siguiete resultado 'Su turno empieza en 0:00:01.'