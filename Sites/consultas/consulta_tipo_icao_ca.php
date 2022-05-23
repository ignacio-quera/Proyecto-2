<?php include('../templates/header.html'); ?>

<body>
<h1 align="center">Vuelos Aceptados</h1>
<?php
    require("../config/conexion.php");
    // $iaco = $_POST("codigoiaco")
    // $compania = $_POST("compania")

    // $query = "SELECT *
    $query = "SELECT vuelos.fechasalida , vuelos.codigovuelo, vuelos.codigoca
                FROM vuelos
                LEFT JOIN aerodromo
                ON aerodromo.codigoicao = vuelos.llegadaicao
                LEFT JOIN companiaaerea
                ON companiaaerea.codigoca = vuelos.codigoca
                WHERE estado LIKE '%aceptado%'
                AND aerodromo.codigoicao LIKE '%$iaco%'
                AND companiaaerea.codigoca LIKE '%$compania%'"; // Crear la consulta
    $result = $db -> prepare($query);
    $result -> execute();    
    $vuelos = $result -> fetchAll();

    // print_r($vuelos)
    ?>

    <table align="center" class="table table-bordered">
        <thead class="thead-dark">
        <tr>
            <th scope="col">Fecha Salida</th>
            <th scope="col">Codigo Vuelo</th>
            <th scope="col">Codigo Compañia Aerea</th>
        </tr>
        </thead>
        <tbody>
        <?php
        foreach($vuelos as $vuelo){
            echo "<tr><td>$vuelo[0]</td><td>$vuelo[1]</td><td>$vuelo[2]</td></tr>";
        }
        ?>
        </tbody>
    </table>
    <!--  -->
    

    <?php include('../templates/footer.html'); ?>
