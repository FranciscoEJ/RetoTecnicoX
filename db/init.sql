CREATE DATABASE MisVuelos;
use MisVuelos;

create table Aeropuerto (ID_AEROPUERTO integer, NOMBRE_AEROLINEA varchar(20), PRIMARY KEY (ID_AEROPUERTO));
		insert into Aeropuerto (ID_AEROPUERTO, NOMBRE_AEROLINEA) values (1,"Benito Juares");
      insert into Aeropuerto (ID_AEROPUERTO, NOMBRE_AEROLINEA) values (2,"Guanajuato");
		insert into Aeropuerto (ID_AEROPUERTO, NOMBRE_AEROLINEA) values (3,"La paz");
		insert into Aeropuerto (ID_AEROPUERTO, NOMBRE_AEROLINEA) values (4,"Oaxaca");

create table Aerolinea (ID_AEROLINEA integer, NOMBRE_AEROLINEA varchar(2), PRIMARY KEY (ID_AEROLINEA));
		insert into Aerolinea (ID_AEROLINEA, NOMBRE_AEROLINEA) values (1,"Volaris");
        insert into Aerolinea (ID_AEROLINEA, NOMBRE_AEROLINEA) values (2,"Aeromar");
		insert into Aerolinea (ID_AEROLINEA, NOMBRE_AEROLINEA) values (3,"Interjet");
		insert into Aerolinea (ID_AEROLINEA, NOMBRE_AEROLINEA) values (4,"Aeromexico");

create table Movimiento (ID_MOVIMIENTO integer, DESCRIPCION varchar(10), PRIMARY KEY (ID_MOVIMIENTO));
		insert into Movimiento (ID_MOVIMIENTO, DESCRIPCION) values (1,"SALIDA");
        insert into Movimiento (ID_MOVIMIENTO, DESCRIPCION) values (2,"LLEGADA");

create table Vuelos (ID_AEROLINEA integer, ID_AEROPUERTO integer, ID_MOVIMIENTO integer, dia date,
                     FOREIGN KEY (ID_AEROLINEA) REFERENCES Aerolinea(ID_AEROLINEA),
                     FOREIGN KEY (ID_AEROPUERTO) REFERENCES Aeropuerto(ID_AEROPUERTO),
                     FOREIGN KEY (ID_MOVIMIENTO) REFERENCES Movimiento(ID_MOVIMIENTO));
		insert into Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, dia) values (1, 1, 1, "2021-05-02");
		insert into Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, dia) values (2, 1, 1, "2021-05-02");
      insert into Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, dia) values (3, 2, 2, "2021-05-02");
		insert into Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, dia) values (4, 3, 2, "2021-05-02");
      insert into Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, dia) values (1, 3, 2, "2021-05-02");
      insert into Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, dia) values (2, 1, 1, "2021-05-02");
      insert into Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, dia) values (2, 3, 1, "2021-05-04");
      insert into Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, dia) values (3, 4, 1, "2021-05-04");
      insert into Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, dia) values (3, 4, 1, "2021-05-04");




