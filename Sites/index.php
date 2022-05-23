<!DOCTYPE html>
<?php include('../templates/header.html'); ?>
<html lang="en">
<head>
<title>Entrega 2 BBDD</title>

<br>
<h1 align="center">Aquí podras realizar todas las consultas que quieras relacionadas a vuelos.</h1>
<br>
<br>
<h3 align="center">¿Quieres ver todos los vuelos pendientes de ser aprobados por la DGAC?</h3>
<form align="center" action="consultas/consulta_tipo_estado.php">
    <input type="submit" value="Buscar">
</form>

<br>
<br>

<h3 align="center">¿Quieres buscar los vuelos aceptados dado un código ICAO de un aeródromo y una aerolínea?</h3>
<form align="center" action="consultas/consulta_tipo_icao_ca.php" method="post">
    Códgio ICAO:
    <input type="text" name="codigoicao" placeholder="Códgio de 4 letras">
    <br><br>
    Aerolínea:
    <input type="text" name="compania" placeholder="Códgio de compañia">
    <br><br>
    <input type="submit" value="Buscar">
</form>

<br>
<br>

<h3 align="center">¿Quieres buscar los tickets dado un código de reserva, adémas de los pasajeros y costos asociados?</h3>
<form align="center" action="consultas/consulta_tipo_codigo_reserva.php" method="post">
    Códgio de Reserva:
    <input type="text" name="codigoreserva" placeholder="Códgio de letras y números">
    <br><br/>
    <input type="submit" value="Buscar">
</form>

<br>
<br>

<h3 align="center">¿Quieres buscar el cliente que mas tickets ha comprado según cada aerolínea?</h3>
<form align="center" action="consultas/consulta_tipo_cliente_ticket_compania.php">
    <input type="submit" value="Buscar">
</form>

<br>
<br>

<h3 align="center">¿Quieres buscar la cantidad de vuelos por cada estado dado el nombre de una aerolínea?</h3>
<form align="center" action="consultas/consulta_tipo_estado_compania.php">
    <input type="submit" value="Buscar">
</form>

<br>
<br>

<h3 align="center">¿Quieres la aerolínea con el mayor porcentaje de vuelos aceptados?</h3>
<form align="center" action="consultas/consulta_tipo_estado_porcentaje.php">
    <input type="submit" value="Buscar">
</form>

</body>
</html>
<?php include('../templates/footer.html'); ?>
