from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que mi horario de trabajo es '{horario}'")
def step_impl(context, horario):
	assert horario in ["diurno", "nocturno"]

@when("ingrese mi hora de entrada siendo las '{hora_entrada}' el dia '{dia}' con codigo '{codigo}'")
def step_impl(context, hora_entrada, dia, codigo):
	mensaje, jornada = marcar_hora_entrada(codigo, dia, int(hora_entrada.split(":")[0]), int(hora_entrada.split(":")[1]), int(hora_entrada.split(":")[2]))
	context.mensaje = mensaje
	context.jornada = jornada

@then("aparecera el mensaje '{mensaje}' con mi jornada '{jornada}'")
def step_impl(context, mensaje, jornada):
	print(context.mensaje)
	print(context.jornada)
	assert context.mensaje.split(".")[0] == mensaje
	assert context.jornada == jornada