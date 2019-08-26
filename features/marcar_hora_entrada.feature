# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: 
      Dado que mi horario de trabajo puede ser diurno o nocturno
      Cuando llegue el dia 'lunes' e ingrese mi hora de entrada '7':'14':'59' e ingrese mi codigo de trabajador '20131'
      Entonces se buscara mi nombre en la lista de trabajadores
      Y aparecera el siguiente mensaje: 'Inicio de Jornada a tiempo, Bienvenido Luis Zuniga.'
      Y devolvera el tipo de jornada laboral: 'Diurno A'

 @jornadasDeIngreso
  Escenario: 
      Dado que mi horario de trabajo puede ser diurno o nocturno
      Cuando llegue el dia 'martes' e ingrese mi hora de entrada '7':'14':'59' e ingrese mi codigo de trabajador '20131'
      Entonces se buscara mi nombre en la lista de trabajadores
      Y aparecera el siguiente mensaje: 'EL día martes no tiene jornada laboral programada.'
      Y devolvera el tipo de jornada laboral: 'Diurno A'

 @jornadasDeIngreso
  Escenario: 
      Dado que mi horario de trabajo puede ser diurno o nocturno
      Cuando llegue el dia 'lunes' e ingrese mi hora de entrada '7':'30':'00' e ingrese mi codigo de trabajador '20131'
      Entonces se buscara mi nombre en la lista de trabajadores
      Y aparecera el siguiente mensaje: 'Inicio de Jornada atrasada por 0:15:00.999990.'
      Y devolvera el tipo de jornada laboral: 'Diurno A'

 @jornadasDeIngreso
  Escenario: 
      Dado que mi horario de trabajo puede ser diurno o nocturno
      Cuando llegue el dia 'lunes' e ingrese mi hora de entrada '6':'40':'00' e ingrese mi codigo de trabajador '20131'
      Entonces se buscara mi nombre en la lista de trabajadores
      Y aparecera el siguiente mensaje: 'Su turno empieza en 0:00:00.999990.'
      Y devolvera el tipo de jornada laboral: 'Diurno A'