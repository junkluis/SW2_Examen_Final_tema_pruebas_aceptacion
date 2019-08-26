"""Funciones necesarias para busqueda de peliculas."""
from datetime import time, timedelta, datetime

empleados = {"20131": ("Luis Zuniga", 		"Diurno A"),
             "20111": ("Tyrion Lannister", 	"Diurno A"),
             "20150": ("Daenerys Targaryen","Nocturno A"),
             "20193": ("Arya Stark", 		"Diurno B"),
             "20153": ("Jon Snow", 			"Diurno B"),
             "20191": ("Eddard Stark", 		"Nocturno B"),
             }

horarios = { "Diurno A": [("lunes", time(7,0,0)), ("viernes", time(7,0,0))],
             "Diurno B": [("martes", time(13,30,0)), ("jueves", time(13,30,0))],
             "Nocturno A": [("lunes", time(18,30,0)), ("miercoles", time(17,00,0))],
             "Nocturno B": [("martes", time(18,30,0)), ("jueves", time(17,00,0))]
			}



def marcar_hora_entrada(cod_trabajador, dia, hora, minutos, segundos):
	mensaje = ""
	

	hora_marcada = datetime.now()
	hora_marcada = hora_marcada.replace(hour=hora, minute=minutos, second=segundos)
	empleado = empleados[cod_trabajador]
	horario = horarios[empleado[1]]

	for jornada in horario:
		if(jornada[0] == dia):
			tmp = jornada[1]
			hora_max_marcado = datetime.now()
			hora_max_marcado = hora_max_marcado.replace(hour=tmp.hour, minute=tmp.minute, second=tmp.second)
			hora_max_marcado_tarde = hora_max_marcado + timedelta(minutes=14, seconds=59)
			hora_max_marcado_temprano = hora_max_marcado - timedelta(minutes=19, seconds=59)

			if(hora_max_marcado_temprano <= hora_marcada <= hora_max_marcado_tarde):
				mensaje = "Inicio de Jornada a tiempo, Bienvenido "+empleado[0]+"."
			else:
				if(hora_marcada > hora_max_marcado_tarde):
					diferencia = hora_marcada - hora_max_marcado_tarde
					mensaje = "Inicio de Jornada atrasada por"+str(diferencia)+"."
				elif( hora_marcada < hora_max_marcado_temprano):
					diferencia = hora_max_marcado_temprano - hora_marcada
					mensaje = "Su turno empieza en "+str(diferencia)+"."

		if(mensaje == ""):
			mensaje = "EL día "+dia+" no tiene jornada laboral programada."

	return mensaje, empleado[1]

if __name__ == "__main__":
	marcar_hora_entrada("20153", "martes", 13, 50, 1)