# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: 
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'resultado_variable'
      Y tambien ocurre lo siguiente (si es necesario)

 @jornadaMarcarIngreso
  Escenario:
    Dado que mi horario sea 'martes'
    Cuando ingrese mi hora de entrada en hora '13', minutos '30', segundos '0' y mi codigo '20193'
    Entonces se buscara mi nombre en la lista de empleados
    Y aparecera el mensaje 'Inicio de Jornada a tiempo, Bienvenido Arya Stark'
    Y devolvera mi jornada laboral 'Diurno B'
