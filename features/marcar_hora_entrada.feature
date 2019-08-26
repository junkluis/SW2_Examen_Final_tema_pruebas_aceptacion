# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: 
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'resultado_variable'
      Y tambien ocurre lo siguiente (si es necesario)

  @jornadasDeIngresoC1
  Escenario: llega a tiempo
      Dado que mi horario de trabajo es 'Diurno B y es 'martes'
      Cuando ingrese mi hora de entrada como '13:54:59'
      Y ingrese mi codigo de trabajador '20131'
      Entonces se buscara mi nombre en la lista de trabajadores y aparecerá el siguiente mensaje 'INICIO DE JORNADA A TIEMPO BIENVENIDO LUIS ZUÑIGA.'
      Y cuya jornada laboral es 'Diurno B'

   @jornadasDeIngresoC2
  Escenario: no tiene jornada laboral ese dia
      Dado que mi horario de trabajo es 'Diurno B' y es 'lunes'
      Cuando ingrese mi hora de entrada como '13:54:59'
      Y ingrese mi codigo de trabajador '20131'
      Entonces se buscara mi nombre en la lista de trabajadores y aparecerá el siguiente mensaje 'EL DIA LUNES NO TIENE JORNADA LABORAL PROGRAMADA.'
      Y cuya jornada laboral es 'Diurno B'
      

   @jornadasDeIngresoC3
  Escenario: llega atrasado
      Dado que mi horario de trabajo es 'Nocturno A' y es 'miercoles'
      Cuando ingrese mi hora de entrada como '17:15:00'
      Y ingrese mi codigo de trabajador '20111'
      Entonces aparecerá el siguiente mensaje 'Inicio de Jornada atrasada por 0:00:00.'
      Y cuya jornada laboral es 'Nocturno A'

   @jornadasDeIngresoC4
  Escenario: llega muy temprano
      Dado que mi horario de trabajo es 'Nocturno B' y es 'jueves'
      Cuando ingrese mi hora de entrada como '16:40:00'
      Y ingrese mi codigo de trabajador '20193'
      Entonces aparecerá el mensaje 'Aún no empieza su turno de trabajo.'
      Y cuya jornada laboral es 'Nocturno B'