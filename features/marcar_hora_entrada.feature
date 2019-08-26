# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: 
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'resultado_variable'
      Y tambien ocurre lo siguiente (si es necesario)

 @jornadasDeIngreso1
  Escenario: llego a la hora correcta
      Dado que mi horario de trabajo es 'Diurno B' y es 'martes'
      Cuando ingrese mi hora de entrada como '13:30:00'
      Y ingrese mi codigo de trabajador '20153'
      Entonces se buscara mi nombre en la lista de trabajadores y aparecerá el siguiente mensaje 'Inicio de Jornada a tiempo, Bienvenido Jon Snow.'
      Y cuya jornada laboral es 'Diurno B'

 @jornadasDeIngreso2
  Escenario: no tiene jornada laboral ese dia
      Dado que mi horario de trabajo es 'Nocturno A' y es 'martes'
      Cuando ingrese mi hora de entrada como '9:56:55'
      Y ingrese mi codigo de trabajador '20150'
      Entonces se buscara mi nombre en la lista de trabajadores y aparecerá el siguiente mensaje 'EL día martes no tiene jornada laboral programada.'
      Y cuya jornada laboral es 'Nocturno A'

 @jornadasDeIngreso3
  Escenario: llego atrasado
      Dado que mi horario de trabajo es 'Diurno A' y es 'viernes'
      Cuando ingrese mi hora de entrada como '07:15:00'
      Y ingrese mi codigo de trabajador '20131'
      Entonces aparecerá el siguiente mensaje 'Inicio de Jornada atrasada por 00:00:01.'
      Y cuya jornada laboral es 'Diurno A'

 @jornadasDeIngreso4
  Escenario: llego antes
      Dado que mi horario de trabajo es 'Nocturno A' y es 'lunes'
      Cuando ingrese mi hora de entrada como '18:15:00'
      Y ingrese mi codigo de trabajador '20150'
      Entonces aparecerá el mensaje 'Aún no empieza su turno de trabajo.'
      Y cuya jornada laboral es 'Nocturno A'