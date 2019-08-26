from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que se cumplen los requisitos")
def step_impl(context):
	pass

@given("que mi horario de trabajo es {horario}")
def step_impl(context, horario):
	context.horario = horario

@when("se ejecute una accion")
def step_impl(context):
	pass

@when("ingrese mi hora de entrada {hora}")
def step_impl(context):
	context.hora = hora

@when("ingrese mi hora de entrada que no esta registrada")
def step_impl(context), minutos, segundos:
	context.minutos = minutos
	context.segundos = segundos

@then("se buscara mi nombre en la lista de trabajadores y aparecera el mensaje: '{mensaje}'")
def step_impl(context):
	assert mensaje == context.mensaje

@then("la jornada es {jornada}")
def step_impl(context, jornada):
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