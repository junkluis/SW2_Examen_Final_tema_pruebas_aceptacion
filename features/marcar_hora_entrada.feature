# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: 
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'resultado_variable'
      Y tambien ocurre lo siguiente (si es necesario)

  @jornadasDeIngreso1
  Escenario:
      Dado que mi horario puede ser 'diurno'
      Cuando ingrese mi hora de entrada: '13:30:00' el dia: 'martes' y código: '20193'
      Entonces aparecerá el mensaje: 'Inicio de Jornada a tiempo, Bienvenido Arya Stark' y mi jornada laboral 'Diurno B'

 @jornadasDeIngreso2
  Escenario:
      Dado que mi horario puede ser 'nocturno'
      Cuando ingrese mi hora de entrada: '07:10:00' el dia: 'jueves' y código: '20131'
      Entonces aparecerá el mensaje: 'EL día jueves no tiene jornada laboral programada.' y mi jornada laboral 'Diurno A'

 @jornadasDeIngreso3
  Escenario:
      Dado que mi horario puede ser 'diurno'
      Cuando ingrese mi hora de entrada: '13:50:00' el dia: 'martes' y código: '20193'
      Entonces aparecerá el mensaje: 'Inicio de Jornada atrasada por 0:05:00.999984 ' y mi jornada laboral 'Diurno B'

 @jornadasDeIngreso4
  Escenario:
      Dado que mi horario puede ser 'diurno'
      Cuando ingrese mi hora de entrada: '13:10:00' el dia: 'martes' y código: '20193'
      Entonces aparecerá el mensaje: 'Aun no empieza su turno de trabajo' y mi jornada laboral 'Diurno B'