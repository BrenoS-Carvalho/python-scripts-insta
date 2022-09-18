




import datetime
horario = datetime.datetime.now()
ano = horario.year
mes = horario.month
dia = horario.day
hora = horario.hour
minuto = horario.minute
segundo = horario.second
print('='*30)
print(f'Agora são {hora}:{minuto}:{segundo} do dia {dia}/{mes}/{ano}.')