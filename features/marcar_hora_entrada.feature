# language: es

Característica: Registrar hora de entrada

    @jornadasDeIngreso
    Escenario: 
        Dado que se cumplen los requisitos
        Cuando se ejecute una accion
        Entonces genera el siguiete resultado 'resultado_variable'
        Y tambien ocurre lo siguiente (si es necesario)


    @jornadasDeIngreso
    Escenario: El trabajador incia su jornada normalmente
        Dado que mi horario de trabajo puede ser diurno o nocturno
        Cuando ingrese mi hora de entrada 'Lunes 7:00:00'
        Y ingrese mi codigo de trabajador '20131'
        Entonces se buscara mi nombre en la lista de los trabajadores
        Y aparecera el siguiente mensaje 'Inicio de jornada a tiempo, Bienvenido Luis Zuniga.'
        Y devolvera el tipo de jornada 'Diurno A'


    @jornadasDeIngreso
    Escenario: El trabajador incia su jornada tarde
        Dado que mi horario de trabajo puede ser diurno o nocturno
        Cuando ingrese mi hora de entrada 'Lunes 7:20:00'
        Y ingrese mi codigo de trabajador '20131'
        Entonces se buscara mi nombre en la lista de los trabajadores
        Y aparecera el siguiente mensaje 'Inicio de Jornada atrasada por 00:20:00.'
        Y devolvera el tipo de jornada 'Diurno A'


    @jornadasDeIngreso
    Escenario: El trabajador intenta iniciar su jornada muy temprano
        Dado que mi horario de trabajo puede ser diurno o nocturno
        Cuando ingrese mi hora de entrada 'Lunes 6:30:00'
        Y ingrese mi codigo de trabajador '20131'
        Entonces se buscara mi nombre en la lista de los trabajadores
        Y aparecera el siguiente mensaje 'Aun no empieza su turno de trabajo'
        Y devolvera el tipo de jornada 'Diurno A'