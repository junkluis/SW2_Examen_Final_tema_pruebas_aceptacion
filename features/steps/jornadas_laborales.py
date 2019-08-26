from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

@given("que mi horario sea: '{jornada}'")
def step_impl(context, jornada):
    context.dia = jornada

@when("ingrese mi hora de entrada en hora: '{hora}', minutos: '{minutos}', segundos: '{segundos}' y mi codigo: '{codigo}'")
def step_impl(context, hora, minutos, segundos, codigo):
    context.hora = int(hora)
    context.minutos = int(minutos)
    context.segundos = int(segundos)
    context.codigo = codigo

    mensaje, jornada = marcar_hora_entrada(context.codigo,context.dia,context.hora,context.minutos, context.segundos)
    print(resultado)
    context.mensaje = mensaje
    context.jornada = jornada

@then("se buscara mi nombre en la lista de empleados")
def step_impl(context):
    pass
@then("aparecera el mensaje: '{mensaje}'")
def step_impl(context, mensaje):
    print(mensaje)
    print(context.mensaje)
    assert context.mensaje == mensaje
@then("devolvera mi jornada laboral: '{jornada}'")
def step_impl(context, jornada):
    print(jornada)
    print(context.jornada)
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
