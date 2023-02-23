
#f=open('alumnos.txt','r')
# alumnos=f.read()
# print(alumnos)
# f.seek(0)
# alumnos2=f.read()
# print(alumnos2)

# alumnos=f.readlines()
# print(alumnos)
# for item in alumnos:
#     print(item, end='')

# alumnos=f.readline()
# print(alumnos)
# f.close()

#Escribir en el archivo
f=open('alumnos2.txt','a')
f.write('\n'+'Hola Mundo')
f.write('\n'+'Nuevo Hola Mundo')


