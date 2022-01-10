# This should be as enviroment varialbles defined in a .env file included in the .gitignore
config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
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
   Vuelos.ID_AEROLINEA= XAerolinea.ID_AEROLINEA
GROUP BY
   Aerolinea.NOMBRE_AEROLINEA
HAVING DiasMayVuelo >= 2;
"""
