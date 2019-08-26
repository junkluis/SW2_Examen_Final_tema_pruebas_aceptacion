# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: se llega hasta con un atraso de 14.59
      Dado que mi horario puede ser diurno o nocturno
      Cuando ingrese mi hora de entrada 'lunes', '7', '12', '32' y mi codigo de trabajador '20131'
      Entonces genera el siguiete resultado 'Inicio de Jornada a tiempo, Bienvenido Luis Zuniga'
      y devolvera el tipo de jornada laboral 'Diurno A'

 @jornadasDeIngreso
  Escenario: se ingresa un dia que no este en el horario de trabajo
      Dado que mi horario puede ser diurno o nocturno
      Cuando ingrese mi hora de entrada 'martes', '7', '15', '00' y mi codigo de trabajador '20131'
      Entonces genera el siguiete resultado 'EL día martes no tiene jornada laboral programada.'
      y devolvera el tipo de jornada laboral 'Diurno A'

@jornadasDeIngreso
  Escenario: se llega hasta con un atraso de mayor a 15 pero menor a una hora
      Dado que mi horario puede ser diurno o nocturno
      Cuando ingrese mi hora de entrada 'lunes', '7', '30', '00' y mi codigo de trabajador '20131'
      Entonces genera el siguiete resultado 'Inicio de Jornada atrasada por 15.'
      y devolvera el tipo de jornada laboral 'Diurno A'

@jornadasDeIngreso
  Escenario: se llega antes de lo esperado
      Dado que mi horario puede ser diurno o nocturno
      Cuando ingrese mi hora de entrada 'lunes', '6', '30', '00' y mi codigo de trabajador '20131'
      Entonces genera el siguiete resultado 'Su turno empieza en 10.'
      y devolvera el tipo de jornada laboral 'Diurno A'