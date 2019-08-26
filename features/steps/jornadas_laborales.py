from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que se cumplen los requisitos")
def step_impl(context):
	pass

@given("que mi horario de trabajo puede ser diurno o nocturno")
def step_impl(context):
	pass

@when("se ejecute una accion")
def step_impl(context):
	pass

@when("ingrese mi hora de entrada hasta con un retraso de {minutos} minutos con {segundos} segundos a mi hora de marcado")
def step_impl(context):
	pass

@then("se buscara mi nombre en la lista de trabajadores y aparecera el mensaje: '{mensaje}'")
def step_impl(context):
	pass

@then("")
def step_impl(context):
	pass

@then("genera el siguiete resultado '{variable}'")
def step_impl(context, variable):
	print(variable)
	pass

@then("tambien ocurre lo siguiente (si es necesario)")
def step_impl(context):
	pass