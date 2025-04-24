class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def cantidad_nodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def sumar_valores(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

    def primer_valor(self):
        if self.cabeza:
            return self.cabeza.valor
        else:
            return None

    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

if __name__ == "__main__":
    lista = ListaEnlazada()

    print("Ingrese los datos que se insertarán al inicio de la lista.")
    print("Escriba 'fin' para terminar.\n")

    while True:
        entrada = input("Ingrese un número: ")
        if entrada.lower() == "fin":
            break
        try:
            numero = int(entrada)
            lista.insertar_inicio(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Mostrar resultados
    print("\n--- RESULTADOS ---")
    lista.imprimir()
    print("Cantidad de nodos:", lista.cantidad_nodos())
    print("Suma de los valores:", lista.sumar_valores())
    primer = lista.primer_valor()
    if primer is not None:
        print("Primer valor de la lista:", primer)
    else:
        print("La lista está vacía")

