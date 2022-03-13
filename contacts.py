
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact= Contact(name = name, phone = phone, email = email)
        self._contacts.append(contact)

    def show(self):
        lista=[]
        for contact in self._contacts:
            lista.append(contact)
        return lista

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                return True
        return False
    def searchContact(self, name):
        for contact in self._contacts:
            if contact.name.lower()== name.lower():
                return contact
        return False


"""
def run():

    contact_book = ContactBook()

    with open('contacs.csv', 'r') as f:
        rider = csv.writer(f)
        for idx, row in enumerate(rider):
            if idx == 0:
                continue
            contact_book.add(row[0],row[1],row[2])




    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            print('añadir contacto')
            name = str(input('Escribe nombre de contacto'))
            phone = str(input('Escribe telefono de contacto'))
            email = str(input('Escribe email de contacto'))

            contact_book.add(name=name,phone=phone,email=email)

        elif command == 'ac':
            print('actualizar contacto')


        elif command == 'b':
            print('buscar contacto')
            name = str(input('Escribe nombre de contacto a eliminar'))
            contact_book.searchContact(name)
        elif command == 'e':
            print('eliminar contacto')
            name = str(input('Escribe nombre de contacto a eliminar'))
            estado = contact_book.delete(name)
            if estado:
                print('Eliminado')
            else:
                print('No se encontro')

        elif command == 'l':
            print('listar contactos')
            contact_book.show()

        elif command == 's':
            print('Adios, Buen Día')
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
"""

