# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso1
  Escenario: 
      Dado que mi horario de trabajo puede ser diurno o nocturno
	  Cuando se ingrese mi hora de entrada '7' hora '14' minutos '59' el dia 'lunes' hasta con un retraso de 14 minutos con 59 segundos a mi hora de marcado e ingrese mi codigo de trabajador '20111'
      Entonces se buscara mi nombre en la lista
      Y aparecera el siguiente mensaje 'Inicio de Jornada a tiempo, Bienvenido Tyrion Lannister.'
	  Y devolvera el tipo de jornada laboral 'Diurno A'
	  
 @jornadasDeIngreso2
  Escenario: 
      Dado que mi horario de trabajo puede ser diurno o nocturno
	  Cuando se ingrese mi hora de entrada '1' hora '12' minutos '59' segundos un dia que no este 'martes' en mi horario e ingrese mi codigo de trabajador '20111'
      Entonces se buscara mi nombre en la lista
      Y aparecera el siguiente mensaje 'EL día martes no tiene jornada laboral programada.'
	  Y devolvera el tipo de jornada laboral 'Diurno A'
	  
 @jornadasDeIngreso3
  Escenario: 
      Dado que mi horario de trabajo puede ser diurno o nocturno
	  Cuando se ingrese mi hora de entrada '7' hora '16' minutos '15' el dia 'lunes' con un retraso mayor o igual a 15 minutos, pero menor a 1 hora, e ingrese mi codigo de trabajador '20111'
      Entonces se buscara mi nombre en la lista
      Y aparecera el siguiente mensaje 'Inicio de Jornada atrasada por 0:01:16.'
	  Y devolvera el tipo de jornada laboral 'Diurno A'
	  
 @jornadasDeIngreso4
  Escenario: 
      Dado que mi horario de trabajo puede ser diurno o nocturno
	  Cuando se ingrese mi hora de entrada '6' hora '39' minutos '0' el dia 'lunes' antes de lo esperado (20 minutos antes de mi hora de entrada) e ingrese mi codigo de trabajador '20111'
      Entonces se buscara mi nombre en la lista
      Y aparecera el siguiente mensaje 'Su turno empieza en 0:01:01.'
	  Y devolvera el tipo de jornada laboral 'Diurno A'