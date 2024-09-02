<?php

$district = strtoupper($_GET['district']);
$crop = ucfirst($_GET['crop']);
$area = $_GET['area'];
$soil = $_GET['soil'];

$res = shell_exec("python3 RF_predict.py $district $crop $area $soil 2>&1");

echo $res;


?>