from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}
#Revisar que exista el tipo de jornada

@given("que mi horario puede ser '{jornada}'")
def step_impl(context, jornada):
    jornadas = ['nocturno', 'diurno']
    assert jornada in jornadas
#Formato hh:mm:ss, Error de UTF8 sin tildes
@when("ingrese mi hora de entrada: '{entrada}' el dia: '{dia}' y código: '{codigo}'")
def step_impl(context, entrada, dia, codigo):
    hora, minutos, segundos = entrada.split(':')
    mensaje, jornada = marcar_hora_entrada(codigo, dia, int(hora), int(minutos), int(segundos))
    context.mensaje = mensaje
    context.jornada = jornada

@then("aparecerá el mensaje: '{mensaje}' y mi jornada laboral '{jornada}'")
def step_impl(context, mensaje, jornada):
    print(context.mensaje)
    assert context.mensaje == mensaje
    assert context.jornada == jornada

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
