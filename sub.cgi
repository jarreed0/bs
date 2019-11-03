#!/usr/pkg/bin/php

<?php
echo "<html>";
echo "<link rel='stylesheet' type='text/css' href='beach.css'>";

parse_str($_SERVER['QUERY_STRING'], $_GET);


echo "
<style>
div.menu {
 width:45%;
 height:45%;
 margin-top:15%;
 margin-left:25%;
 position:relative;
 font-family: Arial, Helvetica, sans-serif;
 display:inline-block;
}
img {
 width: 100px;
 height: 100px;
 padding: 5px;
}
img:hover {
 background-color: lightgrey;
 opacity:.8;
}
a {
 text-decoration: none;
 color: black;
 font-family: Arial, Helvetica, sans-serif;

}
a:visited {
 color: black;
}
</style>
<head>
<title>Thanks For Signing Up!</title>
<link rel='shortcut icon' type='image/png' href='res/favicon.ico'/>
</head>
<body>
<div class='menu'><center>
<i style='font-size:2em;'>Thanks For Signing Up "; echo $_GET['sub'];echo"</i><p>
<i style='font-size:1.5em;'>Return To The Beach Street&copy;</i><p>
<div><a href='index.cgi'><img src='res/monkey.png'><br>Site</a></div>
<div><a href='shop.cgi'><img src='res/favicon.ico'><br>Shop</a></div>
</center></div>
</body>
<footer>

<script src='https://kit.fontawesome.com/21c9216300.js' crossorigin='anonymous'></script>
<style>
div.ft {
 padding: 0px;
 height: 80px;
 width: 100%;
 bottom: 0px;
}
div.ft-disp {

 bottom: 0px;
 width: 90%;
 position: absolute;
 margin-left: 5%;
}
div.social {    

}
.fa-twitter, .fa-instagram, .fa-credit-card, .fa-cc-paypal {
 color: grey !important;
}
.fa-twitter:hover, .fa-instagram:hover, .fa-credit-card:hover, .fa-cc-paypal:hover {
 color: darkgrey !important;
}
</style>

<div class='ft'>
        <div class='ft-disp'>
&nbsp&nbsp&nbsp                                <a class='fab fa-twitter fa-3x' href='https://twitter.com/thebeachstreet'></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                <a class='fab fa-instagram fa-3x' href='https://www.instagram.com/thebeachstreetofficial/'></a>
                <br><a href='mailto:sales@thebeachstreet.com'>Get In Contact With Us!</a>
                <span style='float:right'>Beach Street &copy;2019</span>

        </div>

</div>

</footer>";

try {
 $db = new PDO('sqlite:/home/t/thebeachstreet.com/database/bs.db');
 $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
 echo 'Connection failed: ' . $e->getMessage();
 echo $e->getTraceAsString();
}

$em = $_GET['sub'];
#echo "email is $em";
try {
 $db->exec("INSERT INTO elist (email) VALUES ('$em')");
 $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
 echo 'Connection failed: ' . $e->getMessage();
}

try {
 $statement = $db->query("SELECT * FROM elist");
 $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
 echo 'Connection failed: ' . $e->getMessage();
}


echo '</html>';

?>
