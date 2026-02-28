1.¿Es seguro usar variable global?
R/ No, no es realmente seguro usar variables globales, ya que si varios usuarios hacen peticiones simultáneamente, pueden intentar modificar la misma variable al mismo tiempo, lo que puede generar errores como datos duplicados o contadores incorrectos.

2.¿Dónde aparece el recurso compartido?
R/ en la lista de clientes y en el contador de clientes, ya que todos los usuarios o peticiones tendrian acceso a su modificacion.

3.¿Se debería usar lock en producción?
R/ No, porque puede generar condiciones de carrera, deberia usarse bases de datos que manejan automaticamente concurrencia para garantoxar la consistencia de los datos.