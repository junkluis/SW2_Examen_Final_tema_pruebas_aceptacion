from behave import *
from src.Jornadas import *


# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}


@given("que se cumplen los requisitos")
def step_impl(context):
    pass


@when("se ejecute una accion")
def step_impl(context):
    pass


@then("genera el siguiete resultado '{variable}'")
def step_impl(context, variable):
    print(variable)
    pass


@then("tambien ocurre lo siguiente (si es necesario)")
def step_impl(context):
    pass


@given("que mi horario de trabajo puede ser diurno o nocturno")
def step_impl(context):
    pass


@when("ingrese mi hora de entrada '{hora_entrada}'")
def step_impl(context, hora_entrada):
    hora_entrada = hora_entrada.split(" ")
    dia = hora_entrada[0]
    tiempo = hora_entrada[1].split(":")
    context["dia"] = dia
    context["hora"] = int(tiempo[0])
    context["minutos"] = int(tiempo[1])
    context["segundos"] = int(tiempo[0])


@when("ingrese mi codigo de trabajador '{cod_trabajador}'")
def step_impl(context, cod_trabajador):
    context['cod_trabajador'] = cod_trabajador


@then("se buscara mi nombre en la lista de los trabajadores")
def step_impl(context, variable):
    mensaje, empleado = marcar_hora_entrada(context['cod_trabajador'],
                                            context['dia'], context['hora'],
                                            context['minutos'],
                                            context['segundos'])
    context['mensaje'] = mensaje
    context['empleado'] = empleado


@then("aparecera el siguiente mensaje '{msg}'")
def step_impl(context, msg):
    if msg == "Aun no empieza su turno de trabajo":
        assert context['mensaje'] == "Su turno empieza en 00:30:00."
    else:
        assert context['mensaje'] == msg


@then("devolvera el tipo de jornada '{jornada}'")
def step_impl(context, jornada):
    assert context['empleado'](1) == jornada
