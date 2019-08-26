# language: es

Característica: Registrar hora de entrada para los contratos

 @jornadasDeIngreso
  Escenario: restraso de hasta 14 min 59 s
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'Inicio de Jornada a tiempo, Bienvenido (nombre)'
      Y tambien ocurre lo siguiente (si es necesario)

 @jornadasDeIngreso
  Escenario: un dia que no este
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'El dia() no tiene jornada laboral programada'
      Y tambien ocurre lo siguiente (si es necesario)

 @jornadasDeIngreso
  Escenario: retraso mayor o igual a 15 min
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'Inicio de Jornada atrasada por HH:mm:ss'
      Y tambien ocurre lo siguiente (si es necesario)

 @jornadasDeIngreso
  Escenario: antes de lo esperado
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'Aun no empieza su turno de trabajo'
      Y tambien ocurre lo siguiente (si es necesario)






