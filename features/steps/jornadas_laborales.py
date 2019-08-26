from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("mi codigo {codigo}")
def step_impl(context, codigo):
	context.codigo = codigo

@when("ingreso el dia {dia} con la hora {hora}, minutos {minutos} y segundos {segundos}")
def step_impl(context, dia, hora, minutos, segundos):
	context.hora = int(hora)
	context.dia = dia
	context.minutos = int(minutos)
	context.segundos = int(segundos)
	retorno = marcar_hora_entrada(context.codigo, context.dia, context.hora, context.minutos, context.segundos)
	context.mensaje = retorno[0]
	context.jornada = retorno[1]
	print(context.mensaje)

@then("genera el siguiete resultado '{mensaje}'")
def step_impl(context, mensaje):
	print(mensaje)
	print(context.mensaje)
	assert context.mensaje.split(".")[0] + "." == mensaje

@then("mi tipo de jornada laboral es '{jornada}'")
def step_impl(context, jornada):
	assert context.jornada == jornada

@then("no puedo ingresar porque '{mensaje}'")
def step_impl(context, mensaje):
	print(mensaje)
	print(context.mensaje)
	assert context.mensaje == mensaje

@then("estoy atrasado porque aparece el mensaje '{mensaje}'")
def step_impl(context, mensaje):
	print(context.mensaje)
	print(mensaje)
	assert context.mensaje == ""