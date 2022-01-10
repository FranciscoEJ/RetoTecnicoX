# Reto técnico

#### Ejecucion local logica:
Ejecutar en terminal con interprete python 3.9 instalado lo siguiente:
`$ pipenv shell`
`$ pipenv install`
Para ejecutar pruebas:
`$ cd src/tests/`
`$ python tests.py`


#### Ejecucion en Docker de los Web servers:

`$ docker-compose up -d`


### Reto 1
Para obtener cada una de los valores dentro del aplicativo, se le asigno un case:

2. Obtener el número de respuestas contestadas y no contestadas -> case 1
3. Obtener la respuesta con menor número de vistas -> case 2
4. Obtener la respuesta más vieja y más actual -> case 3
5. Obtener la respuesta del owner que tenga una mayor reputación -> case 4

### Reto 2
Para contestar cada una de las interrogantes dentro del aplicativo, se le asigno un case:

1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año? -> case 5
2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año? -> case 6
3. ¿En qué día se han tenido mayor número de vuelos? -> case 7
4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día? -> case 8


#### NOTA:
Para el servidor de NGNIX se hace la verificación en busca de cambios en un archivo concreto y volver a cargarlo cuando se actualice o sustituya. Consulte:
`ngnix/uwsgi.ini`
