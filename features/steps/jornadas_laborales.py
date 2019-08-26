from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
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

@given("horario diurno o nocturno")
def step_impl(context):
	context.horario = empleado[horario]
	if context.horarios=="Diurno A" || context.horarios=="Diurno B" context.horarios=="Nocturno A" || context.horario=="Nocturno B"
			mensaje="exito"

@when("el usuario ingresa la hora: '{horario}'")
def step_impl(context, empleado[horario]):
	context.horario = empleado[horario]

@when("el usuario ingresa la hora: '{codigo}'")
def step_impl(context, empleado[cod_trabajador]):
	context.codigo = empleado[cod_trabajador]


@then("genera el siguiete resultado '{variable}'")
def step_impl(context, variable):
	
	
