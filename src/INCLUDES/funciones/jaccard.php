<?php
                
    $documento1 = $_POST['documento_1'];
    $documento2 = $_POST['documento_2'];
    $param = 'metodo';
    $tmp =  exec("python ../../code/jaccard.py $documento1 $documento2 $param");
    echo json_encode($tmp);                    
          
?>