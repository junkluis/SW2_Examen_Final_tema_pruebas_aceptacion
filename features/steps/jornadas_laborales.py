from behave import *
from src.Jornadas import Jornadas


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}


@given("Dado que mi horario de trabajo puede ser diurno o bictyrbi")
def step_impl(context):
    #marcar_hora_entrada(cod_trabajador, dia, hora, minutos, segundos)
    pass

@when("cuando ingrese {dia} {hora}:{min}:{segundos")
def step_impl(context):
    pass

@then("genera el siguiete resultado '{variable}'")
def step_impl(context, variable):
    print(variable)
    pass

@then("tambien ocurre lo siguiente (si es necesario)")
def step_impl(context):
    pass