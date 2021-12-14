<?php
    $size = $_POST['size'];
    $param = 'csv';
    $keywords = $_POST['keywords'];

    for ($i=0; $i < $size ; $i++) { 
        $matriz[0][$i] = $_POST['array'.$i]; 
    }

    for ($i= 0; $i < $size; $i++) { 
        for ($j=0; $j < $size; $j++) { 
            $tmp =  exec("python ../../code/jaccard.py ".$matriz[0][$i]." " .$matriz[0][$j] . " " . $param . " ". $keywords);   
            $matriz[$i+1][$j] = $tmp;   
        }
    }
    $outputBuffer = fopen('../../code/mapa.csv', 'w');
    foreach($matriz as $n_linea => $linea) {
        fputcsv($outputBuffer, $linea);		
    }
    fclose($outputBuffer);      
  
?>