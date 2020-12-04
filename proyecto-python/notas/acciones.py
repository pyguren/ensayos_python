import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f'Ok {usuario[1]}!! Vamos a crear una nueva nota')
        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Mete el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(
                f'\nPerfecto haz guardado correctamente la nota: {nota.titulo}')
        else:
            print(f'\nLo siento {usuario[1]} no se ha podido guardar la nota')

    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}!! Aqui tienes tus notas: ")

        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        for nota in notas:
            print(*********************************************)
            print(nota[2])
            print(nota[3])
            print(*********************************************)

    def borrar(self, usuario):
        print(f"\nOk {usuario[1]}!!! Vamos a borrar notas: ")

        titulo = input("Introduce la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"\nHemos borrado la nota: {nota.titulo}")

        else:
            print("\nNo se ha borrado la nota")
