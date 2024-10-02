# Proyecto Urban Grocers 

Mariana Rubio Jaramillo. Cohorte 14


# **Descripción del proyecto.**

Urban Grocers es una plataforma interactiva que permite al cliente comprar 
artículos comestibles, crear kits y solicitar un servicio de entrega. Por ende,
el cliente debe registrarse para crear un nuevo usuario y asi tener su 
propio carrito de compra. 

La plataforma tiene un menú principal para hacer pedidos, la cual, 
consta de varios kits que ya vienen establecidos y además, el usuario
puede crear su propio kit. Dentro de estos kits, se pueden encontrar 
productos organizados por catalogos, precio y cantidad.

En este caso, se automatizaron las pruebas para la lista de comprobación
del campo 'name' en la solicitud de un kit de productos, es decir, se deberá 
crear un nuevo usuario y crear un kit dentro del nuevo usuario.

## Tecnologías y técnicas utilizadas.

    Documentación de la API de Urban Grocers = URL + /docs/ 
    GitHub
    Pycharm
    Lenguaje python
    Librería requests
    Pytest

## Reglas

### Configuration.py

En este archivo están almacenadas las URL y rutas de solicitud que fueron
obtenidas por la documentación de API de Urban Grocers.

### Data.py
En este archivo están almacenados los cuerpos de la solicitud POST.

### Sender_stand_request.py
En este archivo están almanaceadas las solicitudes para crear un usuario
y para crear un kit dentro del nuevo usuario.

### Create_kit_name_kit_test.py
En este archivo están almacenadas las pruebas de la lista de comprobación
del campo 'name'.


## **Creación de un nuevo usuario**

1. Descargar el paquete requests.
2. Importar configuration, data y requests. 
3. Crear un nuevo usuario con el método POST utilizando las rutas URL_SERVICE y
CREATE_USER_PATH y el body del archivo data.py 
4. Guardar el authToken.

 Resultado
 Esta solicitud generará un nuevo usuario y un token de autenticación 'authToken'.

## **Creación de un kit dentro del usuario nuevo**

1. Realizar todos los pasos de 'Creación de un nuevo usuario'.
2. Crear el kit con el método POST utilizando la rutas URL_SERVICE y KITS_PATH 
y el kit_body de data.py.
3. Llamar el authToken que se generó cuando se creó el nuevo usuario.
4. Llamar el encabezado authorization.

Resultado
Esta solicitud generará un kit dentro del usuario enlazado por medio del 
    authToken

## **Pruebas de la lista de comprobación del campo 'name'**

1. Descargar pytest.
2. Importar data y sender_stand_request. 
3. Escribir una función con el método GET para cambiar valores en el parámetro
'name', utilizando el kit_body de data, además, se debe copiar el diccionario del archivo data para
evitar cambios en los datos del diccionario de origen. 
4. Crear una función de prueba positiva teniendo en cuenta el kit_body, el post
del kit_body y el status code. 
5. Comprobar si el código de estado de la función de prueba positiva es 201 y que el campo 'name'
esté en la respuesta y contiene un valor. 
6. Crear una función de prueba negativa teniendo en cuenta el kit_body, el post
del kit_body y el status code. 
7. Comprobar si el código de estado de la función de prueba negativa es 400 y que el status code
en el cuerpo de respuesta es 400. 
8. Crear cada prueba en una función separada y cada uno debe tener el prefijo 'test' para que pytest
la tenga en cuenta. 

    Resultado
    Las pruebas estarán automatizadas y cada prueba creará un nuevo kit dentro del usuario
    teniendo en cuenta el parámetro de la prueba.










