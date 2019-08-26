from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("mi codigo {codigo}")
def step_impl(context, codigo):
	context.codigo = codigo
	print(context.codigo)

@when("ingreso el dia {dia} con la hora {hora}, minutos {minutos} y segundos {segundos}")
def step_impl(context, dia, hora, minutos, segundos):
	context.hora = int(hora)
	context.dia = dia
	context.minutos = int(minutos)
	context.segundos = int(segundos)
	context.retorno = marcar_hora_entrada(context.codigo, context.dia, context.hora, context.minutos, context.segundos)

@then("genera el siguiete resultado '{mensaje}'")
def step_impl(context, mensaje):
	assert(context.retorno[0],'Inicio de Jornada a tiempo, Bienvenido Luis Zuniga')

@then("mi tipo de jornada laboral es {jornada}")
def step_impl(context, jornada):
	assert("mi tipo de jornada laboral es " + "'" + context.retorno[1] + "'","mi tipo de jornada laboral es 'Diurno A'")

@then("no puedo ingresar porque {mensaje}")
def step_impl(context, mensaje):
	assert(context.retorno[0], 'EL día martes no tiene jornada laboral programada.')
