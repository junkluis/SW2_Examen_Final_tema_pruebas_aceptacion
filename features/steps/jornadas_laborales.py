from behave import *
from src.Jornadas import * as jornadas


# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}


@given("Dado que mi horario puede ser diurno o nocturno")
def step_impl(context):
    pass


@when("ingrese mi hora de entrada '{dia}', '{hora}', '{minutos}', '{segundos}' y mi codigo de trabajador '{cod}'")
def step_impl(context, dia, hora, minutos, segundos, cod):
    resultado = marcar_hora_entrada(cod, dia, hora, minutos, segundos)
    context.mensaje = resultado[0]
    context.jornada = resultado[1]


@then("genera el siguiete mensaje '{variable}'")
def step_impl(context, variable):
    assert context.mensaje == variable


@then("y devolvera el tipo de jornada laboral '{jornada}'")
def step_impl(context, jornada):
    assert context.jornada == jornada
