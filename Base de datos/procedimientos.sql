--cursor que rescata el tipo de afiliacion para la vista de formulario_afiliacion
CREATE OR REPLACE PROCEDURE sp_listar_tipo_afiliacion(tipo_afiliacion out SYS_REFCURSOR)
IS
BEGIN
    open tipo_afiliacion for select * from tipo_afiliacion;
END;

--retorna las solicitudes de afiliacion pendiente
CREATE OR REPLACE PROCEDURE SP_LISTAR_SOLICITUDES_PENDIENTES(SOLICITUD_AFILIACION out SYS_REFCURSOR)
IS
BEGIN
    -- id_estado_solicitud = 1 equivale a estado PENDIENTE
    open SOLICITUD_AFILIACION 
    for select * from
        solicitud_afiliacion S 
        join tipo_afiliacion t on s.id_tipo_afiliacion = t.id_tipo_afiliacion 
        where s.id_estado_solicitud = 1;
END;

--retorna las solicitudes de afiliacion aprobadas
CREATE OR REPLACE PROCEDURE SP_LISTAR_SOLICITUDES_APROBADAS(SOLICITUD_AFILIACION out SYS_REFCURSOR)
IS
BEGIN
    -- id_estado_solicitud = 2 equivale a estado APROBADA
    open SOLICITUD_AFILIACION 
        for select * from
        solicitud_afiliacion S 
        join tipo_afiliacion t on s.id_tipo_afiliacion = t.id_tipo_afiliacion 
        where s.id_estado_solicitud = 2;
END;

--retorna las solicitudes de afiliacion Rechazadas
CREATE OR REPLACE PROCEDURE SP_LISTAR_SOLICITUDES_RECHAZADAS(SOLICITUD_AFILIACION out SYS_REFCURSOR)
IS
BEGIN
    -- id_estado_solicitud = 3 equivale a estado RECHAZADA
    open SOLICITUD_AFILIACION 
        for select * from
        solicitud_afiliacion S 
        join tipo_afiliacion t on s.id_tipo_afiliacion = t.id_tipo_afiliacion 
        where s.id_estado_solicitud = 3;
END;

--buscar una solicitud pro su ID
CREATE OR REPLACE PROCEDURE SP_BUSCAR_SOLICITUD(SOLICITUD_AFILIACION out SYS_REFCURSOR, P_ID IN solicitud_afiliacion.ID_SOLICITUD%TYPE)
IS
BEGIN
    open SOLICITUD_AFILIACION 
        for select * from
        solicitud_afiliacion S 
        join tipo_afiliacion t on s.id_tipo_afiliacion = t.id_tipo_afiliacion 
        where s.id_solicitud = P_ID
        AND rownum < 1;
END;

--buscar una solicitud pro su ID
CREATE OR REPLACE PROCEDURE SP_BUSCAR_SOLICITUD(SOLICITUD_AFILIACION out SYS_REFCURSOR, P_ID IN solicitud_afiliacion.ID_SOLICITUD%TYPE)
IS
BEGIN
    open SOLICITUD_AFILIACION 
        for select * from
        solicitud_afiliacion S 
        join tipo_afiliacion t on s.id_tipo_afiliacion = t.id_tipo_afiliacion 
        where s.id_solicitud = P_ID
        AND rownum < 1;
END;

--prosedimeinto que update un registro
CREATE OR REPLACE PROCEDURE SP_APROBAR_SOLICITUD_AFILIACION(
    P_ID IN solicitud_afiliacion.ID_SOLICITUD%TYPE,
    P_SALIDA OUT NUMBER)
IS
BEGIN
    
    UPDATE solicitud_afiliacion SET ID_ESTADO_SOLICITUD=2 WHERE ID_SOLICITUD=P_ID;
    COMMIT;
    P_SALIDA := 1;

    EXCEPTION
    WHEN others then
        P_SALIDA := 0;
    
END;

CREATE OR REPLACE PROCEDURE SP_RECHAZAR_SOLICITUD_AFILIACION(
    P_ID IN solicitud_afiliacion.ID_SOLICITUD%TYPE,
    P_SALIDA OUT NUMBER)
IS
BEGIN
    
    UPDATE solicitud_afiliacion SET ID_ESTADO_SOLICITUD=3 WHERE ID_SOLICITUD=P_ID;
    COMMIT;
    P_SALIDA := 1;

    EXCEPTION
    WHEN others then
        P_SALIDA := 0;
    
END;


--insertar formulario afiliacon, con procedimiento recibiendo parametros opcionales
CREATE OR REPLACE PROCEDURE SP_CREATE_SOLICITUD_AFILIACION(
    P_NOMBRE_COMPLETO IN SOLICITUD_AFILIACION.NOMBRE_COMPLETO%TYPE,
    P_MAIL IN SOLICITUD_AFILIACION.MAIL%TYPE,
    P_ID_TIPO_AFILIACION IN SOLICITUD_AFILIACION.ID_TIPO_AFILIACION%TYPE,
    P_NOMBRE_EMPRESA IN SOLICITUD_AFILIACION.NOMBRE_EMPRESA%TYPE DEFAULT NULL,
    P_TELEFONO_CONTACTO IN SOLICITUD_AFILIACION.TELEFONO_CONTACTO%TYPE DEFAULT NULL,
    P_COMENTARIO IN SOLICITUD_AFILIACION.COMENTARIO%TYPE DEFAULT NULL
    )

IS
BEGIN
    INSERT INTO SOLICITUD_AFILIACION ("NOMBRE_COMPLETO","NOMBRE_EMPRESA","TELEFONO_CONTACTO","MAIL","COMENTARIO","FECHA_SOLICITUD","ID_ESTADO_SOLICITUD","ID_TIPO_AFILIACION","USER_ID")
    VALUES (P_NOMBRE_COMPLETO, P_NOMBRE_EMPRESA,P_TELEFONO_CONTACTO,P_MAIL,P_COMENTARIO,SYSDATE,1,P_ID_TIPO_AFILIACION,NULL);
    
    COMMIT;
END;
    
