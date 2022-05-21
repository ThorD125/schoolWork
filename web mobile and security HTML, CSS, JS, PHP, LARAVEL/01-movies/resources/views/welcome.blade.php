<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<p>Battle between movies!</p>
<br>
<?php
$movielist = array("The Matrix",
"Star Wars",
"Star Trek",
"Lord Of The Rings",
"Back to the future",
"Jurassic Park",
"The Terminator",
"The Office",
"Men in Black",
"Stargate",
"The IT crowd",
"DC comics",
"Marvel");

// print $movielist[1];
// print "\n";

// print count($movielist);
// print "\n";

$nom1 = rand(0, count($movielist));
// print $nom1;
// print "\n";

$nom2 = rand(0, count($movielist));

while ($nom1 == $nom2) {
    $nom2 = rand(0, count($movielist));
}
// print $nom2;
?>
<p>
<?php
print $movielist[$nom1];
?>
<br>
<?php
print $movielist[$nom2];
?>
</p>
<br>
<p>Who will win?</p>
</body>
</html>