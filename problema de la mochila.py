
from operator import itemgetter

#Robo de un establecimiento de electrodomesticos, kilo, precio
CAJAS = (
    ("laptop asus", 9, 1500), ("laptop HP", 10, 1600), ("lavadora lg", 153, 2000), ("televisor led", 90, 1600),
    ("licuadora oster", 15, 90), ("microondas", 66, 450), ("televisor 4k", 35, 6000), ("lavadora ultrarapida", 290, 8400),
    ("ollas electricas", 130, 650), ("refrigerador", 320, 6000), ("cocina electrica", 210, 2700), ("otras pequeñas cosas", 120, 3000))

#carga máxima de los autos
PESOMAXIMO = 300

get_peso = itemgetter(1)
get_valor = itemgetter(2)

def total_peso(cajas):
    return sum(get_peso(x) for x in cajas)

def total_valor(cajas):
    return sum(get_valor(x) for x in cajas)

print(total_peso(CAJAS), total_valor(CAJAS))



def combinaciones(cajas, peso_maximo):
    paqs = [ p for p in cajas if get_peso(p) <= peso_maximo ]
    resultado = []
    for p in paqs:
        res = combinaciones([x for x in paqs if x!=p], peso_maximo - get_peso(p))
        if len(res) == 0:
            resultado.append([p])
        else:
            resultado.extend([[p]+x for x in res])
    return resultado


from pprint import pprint
# solución
sol = max(combinaciones(CAJAS, PESOMAXIMO), key=total_valor)

print("Peso {} Valor {}".format(total_peso(sol), total_valor(sol)))
pprint(sol)
