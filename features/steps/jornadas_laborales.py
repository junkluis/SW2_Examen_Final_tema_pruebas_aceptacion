from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que mi horario de trabajo puede ser diurno o nocturno")
def step_impl(context):
	context.empleados = empleados
	context.horarios = horarios

@when("llegue el dia '{dia}' e ingrese mi hora de entrada '{hora}':'{minu}':'{seg}' e ingrese mi codigo de trabajador '{codigo}'")
def step_impl(context, dia, hora, minu, seg, codigo):
	context.dia = dia
	context.hora = int(hora)
	context.minutos = int(minu)
	context.segundos = int(seg)
	context.codigo = codigo

@then("se buscara mi nombre en la lista de trabajadores")
def step_impl(context):
	mensaje, jornada = marcar_hora_entrada(context.codigo, context.dia, context.hora, context.minutos, context.segundos)
	context.mensaje = mensaje
	context.jornada = jornada

@then("aparecera el siguiente mensaje: '{mensaje}'")
def step_impl(context, mensaje):
	assert context.mensaje == mensaje

@then("devolvera el tipo de jornada laboral: '{jornada}'")
def step_impl(context, jornada):
	assert context.jornada == jornada