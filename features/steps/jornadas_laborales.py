from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que mi horario es {tipo_horario}")
def step_impl(context, tipo_horario):
    es_valido = tipo_horario == "Nocturno A" or tipo_horario == "Nocturno B"\
            or tipo_horario == "Diurno A" or tipo_horario == "Diurno B"
    assert es_valido == True
    context.tipo_horario = tipo_horario


@when("ingrese mi entrada con retraso de {tiempo} a mi hora de marcado {hora} el dia {dia}")
def step_impl(context, tiempo, hora, dia):
    tiempo = tiempo.split(":")
    context.horas = int(tiempo[0])
    context.minutos = int(tiempo[1])
    context.segundos = int(tiempo[2])

    hora = hora.split(":")
    context.hora = int(hora[0])
    context.minuto = int(hora[1])
    context.dia = dia
    

@when("ingrese mi codigo de trabajador: {codigo}")
def step_impl(context, codigo):
    context.codigo = codigo


@then("se buscara mi nombre")
def step_impl(context):
    context.empleado = empleados[context.codigo][0]
    horario = empleados[context.codigo][1]
    assert context.tipo_horario == horario
        

@then("aparecera el mensaje: {mensaje}")
def step_impl(context, mensaje):
    msj, empleado = marcar_hora_entrada(context.codigo, context.dia,
                                    context.hora, context.minutos,
                                    context.segundos)
    print(msj)
    assert msj == mensaje


@when("ingrese entrada en un dia ({dia}) con hora {tiempo} que no este mi horario")
def step_impl(context, dia, tiempo):
    context.dia = dia
    tiempo = tiempo.split(":")
    context.hora = int(tiempo[0])
    context.minuto = int(tiempo[1])
    context.horas = 0
    context.minutos = 0
    context.segundos = 0
