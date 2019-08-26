# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngresoC1
  Escenario:
      Dado que mi horario de trabajo puede ser 'diurno'
      Cuando ingrese mi horario de entrada: '07:11:00' el dia: 'lunes' , código: '20132'
      Entonces aparecerá el mensaje: 'Inicio de Jornada a tiempo, Bienvenido Luis Zuniga.' y mi jornada laboral 'Diurno A'

 @jornadasDeIngresoC2
  Escenario:
      Dado que mi horario de trabajo puede ser 'nocturno'
      Cuando ingrese mi horario de entrada: '07:11:00' el dia: 'lunes' , código: '20191'
      Entonces aparecerá el mensaje: 'EL día lunes no tiene jornada laboral programada.' y mi jornada laboral 'Nocturno B'

 @jornadasDeIngresoC3
  Escenario:
      Dado que mi horario de trabajo puede ser 'diurno'
      Cuando ingrese mi horario de entrada: '13:50:00' el dia: 'martes' , código: '20193'
      Entonces aparecerá el mensaje: 'Inicio de Jornada atrasada por 0:05:00' y mi jornada laboral 'Diurno B'

 @jornadasDeIngresoC4
  Escenario:
      Dado que mi horario de trabajo puede ser 'nocturno'
      Cuando ingrese mi horario de entrada: '18:00:00' el dia: 'martes' , código: '20191'
      Entonces aparecerá el mensaje: 'Su turno empieza en 0:30:00.' y mi jornada laboral 'Nocturno B'