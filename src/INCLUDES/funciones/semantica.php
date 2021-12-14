<?php
    $documento1 = $_POST['documento_1'];
    $documento2 = $_POST['documento_2'];
    $param = 'metodo';
    $keywords = $_POST['keywords'];
    $ejec =  exec("python ../../code/semantica.py $documento1 $documento2 $param $keywords");
    echo json_encode($ejec);                         
?>