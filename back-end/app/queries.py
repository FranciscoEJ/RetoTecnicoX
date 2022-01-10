# This should be as enviroment varialbles defined in a .env file included in the .gitignore
config = {
    'user': 'root',
    'password': 'root',
    'unix_socket': '/var/run/mysqld/mysqld.sock',
    'port': '3306',
    'database': 'MisVuelos'
}

test = 'SELECT * FROM Vuelos'

diasMayVuelo = """
SELECT
   Aerolinea.NOMBRE_AEROLINEA,
   COUNT(Vuelos.dia) AS `DiasMayVuelo`
FROM
   Vuelos
LEFT JOIN
   Aerolinea
ON
   Vuelos.ID_AEROLINEA= Aerolinea.ID_AEROLINEA
GROUP BY
   Aerolinea.NOMBRE_AEROLINEA
HAVING DiasMayVuelo >= 2;
"""


mayorAeropu = """
SELECT
   Aeropuerto.NOMBRE_AEROLINEA,
   COUNT(Vuelos.ID_AEROPUERTO) AS `value_occurrence`
FROM
   Vuelos
INNER JOIN
   Aeropuerto
ON
   Vuelos.ID_ AEROPUERTO = Aeropuerto.ID_ AEROPUERTO
GROUP BY
   Vuelos.ID_ AEROPUERTO
ORDER BY
   `value_occurrence` DESC
LIMIT 1;
"""


mayorAeroli = """
SELECT
   Aerolinea.NOMBRE_AEROLINEA,
   COUNT(Vuelos.ID_AEROLINEA) AS `value_occurrence`
FROM
   Vuelos
INNER JOIN
   Aerolinea
ON
   Vuelos.ID_AEROLINEA= Aerolinea.ID_AEROLINEA
GROUP BY
   Vuelos.ID_AEROLINEA
ORDER BY
   `value_occurrence` DESC
LIMIT 1;
"""

mayorDia = """
SELECT
   dia,
   COUNT(Vuelos.ID_MOVIMIENTO) AS `value_occurrence`
FROM
   Vuelos
GROUP BY
   dia
ORDER BY
   value_occurrence DESC
LIMIT 1;
"""
