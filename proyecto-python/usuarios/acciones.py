import usuarios.usuario as modelo


class Acciones:

    def registro(self):
        print("\n Ok vamos a registrate en el sistema..")
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"\nPerfecto {registro[1].nombre} te haz registrado con el email {usuario[1].email}")
        else:
            print("\nNo te haz registrado correctamente!!!")

    def login(self):
        print("\n Ok!!! identificate en el sistema..")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu password: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(
                    f'\nBienvenido{login[1]} te haz registrado el {login[5]}')
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f'Login incorrecto!! Intentalo mas tarde')

    def proximasAcciones(self, usuario):
        print("""
            Acciones disponibles:
            - Crear nota(crear)
            - Mostrar tus notas(mostrar)
            - Eliminar notas(eliminar)
            - Salir(salir)
       """)

        accion = input("¿Que quieres hacer?: ")

        if accion == "crear":
            print("Vamos a crear")
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("Vamos a mostrar")
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("Vamos a eliminar")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f'Ok {usuario[1]} Hasta pronto!!!')
            exit()
