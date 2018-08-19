<?php

// single line comment
/* Multi 
line
 comment */

// Variables

//Integer
$var = 1;

echo $var;
;
//String
$var1 = "Test/n";
echo $var1."<br>";

echo gettype($var1);

echo "Concatenate"."Datatype";

if ($var = 1){
print "Executed";
}

else{
print "Else";
}


for ($i=0;$i<5;$i++)

{
print $i;
}

// Funtions

function hello(){
echo "<br> Hello Dinesh!!!";
}

// call function

hello();

function hai($name){
echo "<br> Hello  ".$name;

}

hai("Dinesh");


//Array

$arr = array("aa","bb","cc","dd");
print "<br> print second elem".$arr[1];

print "<br> count" .count($arr);

//for each

foreach($arr as $ar)

{
print "<br> for each".$ar;
}


?>
