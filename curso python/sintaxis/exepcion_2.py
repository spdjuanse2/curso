def divide():

    try:
        val1=float(input("ingrese el primer numero: "))
        val2=float(input("ingrese el segundo numero: "))
        print("la divicion es: " + str(val1/val2))

    except ZeroDivisionError:
        print("no se puede dividir netre  intente de nuevo.")

    except ValueError:
        print("ingrese un valor numerico. ")

    finally:
        print("calculo finalizado")


divide()
