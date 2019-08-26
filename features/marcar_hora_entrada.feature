# language: es

Característica: Registrar hora de entrada

  @jornadasDeIngreso
  Escenario: 
      Dado que mi horario es Diurno B
      Cuando ingrese mi entrada con retraso de 00:14:59 a mi hora de marcado 13:00 el dia martes
      Y ingrese mi codigo de trabajador: 20153
      Entonces se buscara mi nombre
      Y aparecera el mensaje: Inicio de Jornada a tiempo, Bienvenido Jon Snow.

  @jornadasDeIngreso
  Escenario: 
      Dado que mi horario es Diurno B
      Cuando ingrese entrada en un dia (miercoles) con hora 7:00 que no este mi horario
      Y ingrese mi codigo de trabajador: 20153
      Entonces aparecera el mensaje: EL día miercoles no tiene jornada laboral programada.

  @jornadasDeIngreso
  Escenario: 
      Dado que mi horario es Diurno B
      Cuando ingrese mi entrada con retraso de 00:59:59 a mi hora de marcado 13:00 el dia martes
      Y ingrese mi codigo de trabajador: 20153
      Entonces se buscara mi nombre
      Y aparecera el mensaje: Inicio de Jornada atrasada por 0:14:59.

