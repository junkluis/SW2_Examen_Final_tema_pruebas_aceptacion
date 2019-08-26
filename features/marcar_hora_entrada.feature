# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: 
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'resultado_variable'
      Y tambien ocurre lo siguiente (si es necesario)

 @jornadasDeIngresoConRetraso
  Escenario: Ingreso laboral con retraso aceptado
      Dado que mi horario de trabajo puede ser diurno
      Cuando ingrese mi hora de entrada 12:13:55
      Entonces se buscara mi nombre en la lista de trabajadores y aparecera el mensaje: 'Inicio de Jornada a tiempo, Bienvenido Wellington'
      Y la jornada es vespertina

 @jornadasDeIngresoConDiaSinJornada
  Escenario: Dia de trabajo no laborable
      Dado que mi horario de trabajo puede ser diurno
      Cuando ingrese mi hora de entrada que no esta registrada
      Entonces se buscara mi nombre en la lista de trabajadores y aparecera el mensaje: 'el dia domingo no tiene jornada laboral'
      Y la jornada es vespertina

 @jornadasDeIngresoConExcesoDeRetraso
  Escenario: Ingreso laboral con exceso de retraso
      Dado que mi horario de trabajo puede ser diurno
      Cuando ingrese mi hora de entrada 15:13:55
      Entonces se buscara mi nombre en la lista de trabajadores y aparecera el mensaje: 'Inicio de jornada atrasada por 20 minutos'
      Y la jornada es vespertina