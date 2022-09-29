import os

Extension = '.jpg'
dataset = False

#IMPORTANTE
# Deben estar en la carpeta solo los objetos que se deseen renombrar
# De lo contrario el resultado sera incorrecto


Carpeta=input('Ingrese ruta ')  #Ingresa la ruta 
Formato=input('Ingrese nombre final ') #ingrese como va a quedar el nombre
Mode=input('Modo Dataset (s)/(n) ')

if Mode=='s' :
    dataset = True


contenido = os.listdir(f'{Carpeta}')
contenido = contenido[1::]
j = 0

#Se usa para que los archivos queden con la misma extension de origen
def extension_inicial(string,formato):
    try:
        #verifica que la extension exita
        existe = string.index(f'{formato}')
    except: 
        existe = False
    return existe

if dataset:
    for i in range(1,(len(contenido)+1),1):

        #se valida extension del archivo
        Texto = extension_inicial(contenido[i-1],'.txt')
        Imagen_jpg = extension_inicial(contenido[i-1],'.jpg')
        Imagen_png = extension_inicial(contenido[i-1],'.png')

        #se coloca la extension correspondiente para no alterar los archivos
        if Texto:
            Extension = '.txt'
        if Imagen_jpg:
            Extension = '.jpg'
        if Imagen_png:
            Extension = '.png' 

        #se usa este if para que si hay un error en la extension no lo cambie de nombre
        if Texto or Imagen_jpg or Imagen_png:
            j = i-1
            #se define el nombre nuevo
            nombre_nuevo = f'{Carpeta}\{Formato}{int(j/2)}{Extension}'
            #se toma la ubicacion del archivo a renombrar
            path=f'{Carpeta}\{contenido[i-1]}'

            try:
                #renombra el archivo
                os.rename(path, nombre_nuevo)
            except:
                print(nombre_nuevo)
                print(f'Error 1: Numero {i} Ha fallado en el cambio de nombre')
                continue
        else:
            print(f'Error 2: Numero {i} Ha fallado en la extension')
            continue
        
        print(f'Dataset, Proceso {i} finalizado.')

else:
    for i in range(1,(len(contenido)+1),1):

        #se valida extension del archivo
        Texto,dataset1 = extension_inicial(contenido[i-1],'.txt')
        Imagen_jpg,dataset2 = extension_inicial(contenido[i-1],'.jpg')
        Imagen_png,dataset3 = extension_inicial(contenido[i-1],'.png')

        #se coloca la extension correspondiente para no alterar los archivos
        if Texto:
            Extension = '.txt'
        if Imagen_jpg:
            Extension = '.jpg'
        if Imagen_png:
            Extension = '.png' 


        #se usa este if para que si hay un error en la extension no lo cambie de nombre
        if Texto or Imagen_jpg or Imagen_png:
            
            #se define el nombre nuevo
            nombre_nuevo = f'{Carpeta}\{Formato}{i}{Extension}'
            #se toma la ubicacion del archivo a renombrar
            path=f'{Carpeta}\{contenido[i-1]}'

            try:
                #renombra el archivo
                os.rename(path, nombre_nuevo)
            except:
                print(f'Error 1: Numero {i} Ha fallado en el cambio de nombre')
                continue
        else:
            print(f'Error 2: Numero {i} Ha fallado en la extension')
            continue
        
        print(f'Proceso {i} finalizado.')

input("Press Enter to continue...")
