from my_class.bienvenida import Bienvenida

#bucle para correr el programa (temporal)

instanceBucle = True 
welcome = Bienvenida()

while instanceBucle:
    instanceBucle = welcome.bienvenido()

    if not instanceBucle:
        
        

        instanceBucle = True
