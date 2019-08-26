# language: es

Característica: Registrar hora de entrada

    @jornadaDeIngreso1
    Escenario: Hora de ingreso normal
        Dado que mi horario de trabajo puede ser diurno o nocturno
        Cuando ingrese mi hora de entrada: lunes 7:14:59 
        Y ingrese mi codigo de trabajador 20131
        Entonces se buscará mi nombre en la lista de trabajadores
        Y aparecerá el mensaje 'Inicio de Jornada a tiempo, Bienvenido Luis Zuniga.'
        Y devolverá el tipo de jornada 'Diurno A'

    @jornadaDeIngreso2
    Escenario: Hora de ingreso en día no permitido por jornada
        Dado que mi horario de trabajo puede ser diurno o nocturno
        Cuando ingrese mi hora de entrada: martes 7:14:59 
        Y ingrese mi codigo de trabajador 20131
        Entonces se buscará mi nombre en la lista de trabajadores
        Y aparecerá el mensaje 'EL día martes no tiene jornada laboral programada.'
        Y devolverá el tipo de jornada 'Diurno A'

    @jornadaDeIngreso3
    Escenario: Hora de ingreso con atraso
        Dado que mi horario de trabajo puede ser diurno o nocturno
        Cuando ingrese mi hora de entrada: lunes 7:16:00
        Y ingrese mi codigo de trabajador 20131
        Entonces se buscará mi nombre en la lista de trabajadores
        Y aparecerá el mensaje 'Inicio de Jornada atrasada por 0:01:00.'
        Y devolverá el tipo de jornada 'Diurno A'

    @jornadaDeIngreso4
    Escenario: Hora de ingreso temprano
        Dado que mi horario de trabajo puede ser diurno o nocturno
        Cuando ingrese mi hora de entrada: lunes 6:40:00
        Y ingrese mi codigo de trabajador 20131
        Entonces se buscará mi nombre en la lista de trabajadores
        Y aparecerá el mensaje 'Aún no empieza su turno de trabajo.'
        Y devolverá el tipo de jornada 'Diurno A'