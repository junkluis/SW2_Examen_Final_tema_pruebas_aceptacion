# language: es

Característica: Registrar hora de entrada

 @jornadasDeIngreso
  Escenario: aceptacion 1
      Dado que mi horario de trabajo puede ser diurno o nocturno
      Cuando ingrese {dia} {hora}:{min}:{segundos}
      Entonces genera el siguiete resultado 'resultado_variable'
      Y tambien ocurre lo siguiente (si es necesario)
