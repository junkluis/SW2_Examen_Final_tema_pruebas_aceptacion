# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngresoCA1
  Escenario:
      Dado que mi horario puede ser 'diurno'
      Cuando ingrese mi hora de entrada: '07:10:00' el dia: 'lunes' y código: '20131'
      Entonces aparecerá el mensaje: 'Inicio de Jornada a tiempo, Bienvenido Luis Zuniga.' y mi jornada laboral 'Diurno A'

 @jornadasDeIngresoCA2
  Escenario:
      Dado que mi horario puede ser 'nocturno'
      Cuando ingrese mi hora de entrada: '07:10:00' el dia: 'martes' y código: '20150'
      Entonces aparecerá el mensaje: 'EL día martes no tiene jornada laboral programada.' y mi jornada laboral 'Nocturno A'

 @jornadasDeIngresoCA2
  Escenario:
      Dado que mi horario puede ser 'diurno'
      Cuando ingrese mi hora de entrada: '13:50:00' el dia: 'martes' y código: '20193'
      Entonces aparecerá el mensaje: 'Inicio de Jornada atrasada por 0:05:00' y mi jornada laboral 'Diurno B'

 @jornadasDeIngresoCA2
  Escenario:
      Dado que mi horario puede ser 'nocturno'
      Cuando ingrese mi hora de entrada: '18:00:00' el dia: 'martes' y código: '20191'
      Entonces aparecerá el mensaje: 'Su turno empieza en 0:10:01.' y mi jornada laboral 'Nocturno B'