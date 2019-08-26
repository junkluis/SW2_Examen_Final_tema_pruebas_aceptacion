from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que mi horario de trabajo puede ser '{horario}'")
def step_impl(context, horario):
    #context.jornada = horario
    assert horario in ['diurno','nocturno']
	

@when("ingrese mi horario de entrada: '{entrada}' el dia: '{dia}' , código: '{codigo}'")
def step_impl(context, entrada, dia, codigo):
	hora, minutos, segundos = entrada.split(':')
	mensaje, jornada = marcar_hora_entrada(codigo, dia, int(hora), int(minutos), int(segundos))
	context.mensaje = mensaje
	context.jornada = jornada

@then("aparecerá el mensaje: '{mensaje}' y mi jornada laboral '{jornada}'")
def step_impl(context, mensaje, jornada):
	context.mensaje = context.mensaje[:len(mensaje)]
	assert context.mensaje == mensaje
	assert context.jornada == jornada