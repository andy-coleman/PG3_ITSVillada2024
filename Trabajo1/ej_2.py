def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"tu año {anio} es bisiesto")
        return True
        
    else:
        print(f"tu anio {anio} no es bisiesto")
        return False
    

anio = int(input("que año desa investigar"))

es_bisiesto(anio)