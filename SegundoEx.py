# dias = 1
# horas = 3
# minutos = 46
# segundos = 40

def converteSegundos(dias,horas,minutos,segundos):
    diasPHoras = dias * 24
    horasPMinutos = (horas + diasPHoras)* 60
    minutosPSegundos = (minutos + horasPMinutos) * 60
    segundosTotal = minutosPSegundos + segundos
    return segundosTotal

print(converteSegundos(1,3,46,40))

def convereTudo(segundos):

    min = segundos // 60
    st = segundos % 60 #segundos

    hr = min // 60
    mint = min % 60 #minutos

    hrt = hr % 24 #horas
    d = hr // 24 #dias

    return d,"d",hrt,"h", mint,"m", st,"s"

# th= 3600
# td = 3600 * 24
#
# print(td)
print(convereTudo(100000)) #87426












# a = 10
# a,b = 3 * a, a
# print(a)
# print(b)
# a = 10
# a = 3 * a
# b=a
# print(a)
#  print(b)