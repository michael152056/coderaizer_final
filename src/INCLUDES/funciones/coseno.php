<?php
    $documento1 = $_POST['documento_1'];
    $documento2 = $_POST['documento_2'];
    $param = 'metodo';
    $keywords = $_POST['keywords'];
    $tmp =  exec("python ../../code/coseno_vectorial.py $documento1 $documento2 $param $keywords");
    echo json_encode($tmp);                            
?>