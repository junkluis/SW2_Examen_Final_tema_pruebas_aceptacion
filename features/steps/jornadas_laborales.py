from behave import *
from src.Jornadas import *



#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que se cumplen los requisitos")
def step_impl(context):
	dict_horarios = horarios
	context.horarios = dict_horarios
	print(dict_horarios)
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