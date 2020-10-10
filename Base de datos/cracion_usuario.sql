--creacion de usuario
--drop user c##portafolio cascade;
create user c##mi_prueba3 IDENTIFIED by oracle;
grant connect, resource to c##mi_prueba3;
alter user c##mi_prueba3 default tablespace users quota unlimited on users;