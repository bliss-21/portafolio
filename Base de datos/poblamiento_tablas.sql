Insert into AUTH_GROUP (ID,NAME) values ('1','ADMINISTRADOR');
Insert into AUTH_GROUP (ID,NAME) values ('2','PRODUCTOR');

Insert into AUTH_USER (ID,PASSWORD,LAST_LOGIN,IS_SUPERUSER,USERNAME,FIRST_NAME,LAST_NAME,EMAIL,IS_STAFF,IS_ACTIVE,DATE_JOINED) values ('2','pbkdf2_sha256$216000$h0h3aWwa64C7$IFhF9EXyPMeZXdvfv3I8PUEKwgS8RK/PsI9yFZtpeYI=',to_timestamp('20/09/20 05:10:22,557045000','DD/MM/RR HH24:MI:SSXFF'),'0','eliasolate','Elias Deeividt','Olate Rivera','eli.olate@alumnos.duoc.cl','0','1',to_timestamp('13/09/20 20:36:44,000000000','DD/MM/RR HH24:MI:SSXFF'));
Insert into AUTH_USER (ID,PASSWORD,LAST_LOGIN,IS_SUPERUSER,USERNAME,FIRST_NAME,LAST_NAME,EMAIL,IS_STAFF,IS_ACTIVE,DATE_JOINED) values ('1','pbkdf2_sha256$216000$AQHx1ldA5P9T$7rbaVZtM7sRRoF5G2WyGro1nUzlTsOiefrBJtROkwy0=',to_timestamp('13/09/20 20:38:30,957314000','DD/MM/RR HH24:MI:SSXFF'),'1','admin',null,null,'admin@admin.com','1','1',to_timestamp('13/09/20 20:34:18,397885000','DD/MM/RR HH24:MI:SSXFF'));

Insert into AUTH_USER_GROUPS (ID,USER_ID,GROUP_ID) values ('1','2','2');

Insert into CALIDAD (ID_CALIDAD,NOMBRE) values ('4','PREMIUM');
Insert into CALIDAD (ID_CALIDAD,NOMBRE) values ('1','BAJA');
Insert into CALIDAD (ID_CALIDAD,NOMBRE) values ('2','MEDIA');
Insert into CALIDAD (ID_CALIDAD,NOMBRE) values ('3','ALTA');


Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('3',to_timestamp('13/09/20 20:36:44,685686000','DD/MM/RR HH24:MI:SSXFF'),'eliasolate','1','2','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('4',to_timestamp('13/09/20 20:37:43,311401000','DD/MM/RR HH24:MI:SSXFF'),'eliasolate','2','2','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('8',to_timestamp('13/09/20 20:39:38,301910000','DD/MM/RR HH24:MI:SSXFF'),'Calidad object (4)','1','3','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('9',to_timestamp('13/09/20 20:48:41,813315000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (1)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('14',to_timestamp('13/09/20 20:49:39,949365000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (6)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('15',to_timestamp('13/09/20 20:49:45,245134000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (7)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('20',to_timestamp('13/09/20 20:50:41,012631000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (12)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('21',to_timestamp('13/09/20 20:50:45,584522000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (13)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('31',to_timestamp('13/09/20 20:51:38,863049000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (23)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('32',to_timestamp('13/09/20 20:51:44,812810000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (24)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('38',to_timestamp('13/09/20 20:52:38,451179000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (30)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('39',to_timestamp('13/09/20 20:52:46,635627000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (31)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('1',to_timestamp('13/09/20 20:36:00,430190000','DD/MM/RR HH24:MI:SSXFF'),'ADMINISTRADOR','1','1','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('2',to_timestamp('13/09/20 20:36:13,729718000','DD/MM/RR HH24:MI:SSXFF'),'PRODUCTOR','1','1','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('5',to_timestamp('13/09/20 20:39:00,214756000','DD/MM/RR HH24:MI:SSXFF'),'Calidad object (1)','1','3','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('6',to_timestamp('13/09/20 20:39:10,689132000','DD/MM/RR HH24:MI:SSXFF'),'Calidad object (2)','1','3','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('7',to_timestamp('13/09/20 20:39:14,475972000','DD/MM/RR HH24:MI:SSXFF'),'Calidad object (3)','1','3','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('10',to_timestamp('13/09/20 20:49:01,019640000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (2)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('11',to_timestamp('13/09/20 20:49:07,264973000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (3)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('12',to_timestamp('13/09/20 20:49:15,893229000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (4)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('13',to_timestamp('13/09/20 20:49:34,401501000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (5)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('16',to_timestamp('13/09/20 20:49:51,969552000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (8)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('17',to_timestamp('13/09/20 20:49:57,892659000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (9)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('18',to_timestamp('13/09/20 20:50:02,897892000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (10)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('19',to_timestamp('13/09/20 20:50:27,486253000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (11)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('22',to_timestamp('13/09/20 20:50:51,134278000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (14)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('23',to_timestamp('13/09/20 20:50:56,681582000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (15)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('24',to_timestamp('13/09/20 20:51:01,616903000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (16)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('25',to_timestamp('13/09/20 20:51:06,565933000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (17)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('26',to_timestamp('13/09/20 20:51:10,958222000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (18)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('27',to_timestamp('13/09/20 20:51:16,052297000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (19)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('28',to_timestamp('13/09/20 20:51:21,053898000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (20)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('29',to_timestamp('13/09/20 20:51:25,947565000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (21)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('30',to_timestamp('13/09/20 20:51:33,955115000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (22)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('33',to_timestamp('13/09/20 20:52:02,390058000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (25)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('34',to_timestamp('13/09/20 20:52:07,184540000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (26)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('35',to_timestamp('13/09/20 20:52:18,541801000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (27)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('36',to_timestamp('13/09/20 20:52:26,258992000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (28)','1','4','1');
Insert into DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('37',to_timestamp('13/09/20 20:52:32,656005000','DD/MM/RR HH24:MI:SSXFF'),'Fruta object (29)','1','4','1');

Insert into DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('1','auth','group');
Insert into DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('3','core','calidad');
Insert into DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('2','auth','user');
Insert into DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('4','core','fruta');
Insert into DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('21','core','producto');

Insert into DJANGO_SESSION (SESSION_KEY,EXPIRE_DATE) values ('brijg21saem39p9jyvhi6jvufze9ao6i',to_timestamp('03/10/20 23:09:18,368816000','DD/MM/RR HH24:MI:SSXFF'));
Insert into DJANGO_SESSION (SESSION_KEY,EXPIRE_DATE) values ('u5c8sp56zx5o8ipb6rmhx7cjrmmt0908',to_timestamp('04/10/20 05:10:22,562231000','DD/MM/RR HH24:MI:SSXFF'));



Insert into FRUTA (ID_FRUTA,NOMBRE) values ('1','Arándano');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('6','Mandarina');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('7','Naranja');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('12','Chirimoya');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('13','Coco');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('23','Higo');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('24','Manzana');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('30','Nuez');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('31','Pistacho');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('2','Frambuesa');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('3','Fresa');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('4','Moras');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('5','Limón');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('8','Pomelo');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('9','Melón');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('10','Sandía');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('11','Palta');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('14','Maracuyá');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('15','Kiwi');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('16','Mango');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('17','Papaya');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('18','Piña');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('19','Plátano');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('20','Durazno');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('21','Cereza');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('22','Ciruela');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('25','Níspero');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('26','Pera');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('27','Avellana');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('28','Cacahuete');
Insert into FRUTA (ID_FRUTA,NOMBRE) values ('29','Castaña');


Insert into PRODUCTO (ID_PRODUCTO,DESCRIPCION,FECHA_SUBIDA,FECHA_VENCIMIENTO,ID_FRUTA,ID_CALIDAD,CANTIDAD,USER_ID) values ('24','pera de agua verde',to_date('16/09/20','DD/MM/RR'),to_date('16/10/20','DD/MM/RR'),'26','3','200','2');
Insert into PRODUCTO (ID_PRODUCTO,DESCRIPCION,FECHA_SUBIDA,FECHA_VENCIMIENTO,ID_FRUTA,ID_CALIDAD,CANTIDAD,USER_ID) values ('41','Manzana Verde',to_date('16/09/20','DD/MM/RR'),to_date('08/10/20','DD/MM/RR'),'24','1','200','2');
Insert into PRODUCTO (ID_PRODUCTO,DESCRIPCION,FECHA_SUBIDA,FECHA_VENCIMIENTO,ID_FRUTA,ID_CALIDAD,CANTIDAD,USER_ID) values ('81','Piña dulce',to_date('19/11/20','DD/MM/RR'),to_date('21/01/21','DD/MM/RR'),'18','2','500','2');

--tipo afiliacion 
insert into tipo_afiliacion (id_tipo_afiliacion,nombre) values (1, 'PRODUCTOR');
insert into tipo_afiliacion (id_tipo_afiliacion,nombre) values (2, 'TRANSPORTISTA');
insert into tipo_afiliacion (id_tipo_afiliacion,nombre) values (3, 'CLIENTE NACIONAL');
insert into tipo_afiliacion (id_tipo_afiliacion,nombre) values (4, 'CLIENTE INTERNACIONAL');

--estado solicitud afiliacion 
insert into estado_solicitud_afiliacion (nombre) values ('PENDIENTE');
insert into estado_solicitud_afiliacion (nombre) values ('ACEPTADA');
insert into estado_solicitud_afiliacion (nombre) values ('RECHAZADA');
--estado solicitud
insert into estado_solicitud (nombre) values ('PENDIENTE');
insert into estado_solicitud (nombre) values ('ACEPTADA');
insert into estado_solicitud (nombre) values ('RECHAZADA');