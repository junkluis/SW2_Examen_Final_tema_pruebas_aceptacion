# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: 
      Dado que mi horario de trabajo es 'diurno'
      Cuando ingrese mi hora de entrada siendo las '13:35:00' el dia 'martes' con codigo '20153'
      Entonces aparecera el mensaje 'Inicio de Jornada a tiempo, Bienvenido Jon Snow' con mi jornada 'Diurno B'

 @jornadasDeIngreso
  Escenario:
      Dado que mi horario de trabajo es 'diurno'
      Cuando ingrese mi hora de entrada siendo las '13:35:00' el dia 'lunes' con codigo '20153'
      Entonces aparecera el mensaje 'EL día lunes no tiene jornada laboral programada' con mi jornada 'Diurno B'

 @jornadasDeIngreso
  Escenario:
      Dado que mi horario de trabajo es 'diurno'
      Cuando ingrese mi hora de entrada siendo las '13:50:00' el dia 'martes' con codigo '20153'
      Entonces aparecera el mensaje 'Inicio de Jornada atrasada por 0:05:00' con mi jornada 'Diurno B'

 @jornadasDeIngreso
  Escenario:
      Dado que mi horario de trabajo es 'diurno'
      Cuando ingrese mi hora de entrada siendo las '13:05:00' el dia 'martes' con codigo '20153'
      Entonces aparecera el mensaje 'Su turno empieza en 0:05:01' con mi jornada 'Diurno B'