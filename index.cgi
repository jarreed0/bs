#!/usr/pkg/bin/php

<?php

parse_str($_SERVER['QUERY_STRING'], $_GET);

echo "<link rel='stylesheet' type='text/css' href='beach.css'>";
echo "<html>";

echo "<title>Beach Street</title>";

echo "
<header>
 <link rel='shortcut icon' type='image/png' href='res/favicon.ico'/>";
echo "
<style>
 div.hd {
  background-color: black;
  padding: 0px;
  margin: 0px;
  height: 230px;
  width: 100%;
 }
</style>

<div class='hd'>
 <center>";
echo "
<style>
 #myDIV, #myDIV-bottom {
  background-color: white;
  color: black;
  padding: 0;
  margin: 0;
  height: 20px;
  width: 100%;
  font-size: 1em;
  position: sticky;
  position: -webkit-sticky;
  top: 0;
 }
 a.p {
  color: black;
  text-decoration: none;
 }
 a.p:visited {
  color: black !important;
 }
</style>

<div id='myDIV'>
 <center>";
  echo "<a class='p' href='#news'>Free Shipping On All Orders - Sign Up For Our Newsletter</a>"; echo "
  <div class='p' style='float: right; margin-right:13px; cursor: pointer;' onclick='myFunction()'>
   &times;
  </div>
 <center>
</div>

<script>
 function myFunction() {
  var x = document.getElementById('myDIV');
  if (x.style.display === 'none') {
   x.style.display = 'block';
  } else {
   x.style.display = 'none';
  }
 }
</script>";
  echo "<a href='index.cgi'><img src='res/bslogo.jpg' style='width:45%; height:200px;'>
  </a>
 </center>
</div>";

 echo "
</header>";

echo "
<body>";
 echo "<script src='https://kit.fontawesome.com/21c9216300.js' crossorigin='anonymous'></script>
<style>
 div.bar {
  background-color: #348E74;
  padding: 0px;
  height: 70px;
  width: 100%;
  position: sticky;
  position: -webkit-sticky;
  top: 0;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  --logo-w: 38px;
  z-index: 1;
 }
 span.menu, a.menu {
  position: relative;
  color: white;
 }
 a.menu:visited {
  color: white;
 }
 a.menu:hover {
  color:#684388;
 }
 span.menu:hover {
  color:#684388;
 }
 div.dropdown {
  position: absolute;
  display: none;
  width: initial;
  color: white;
 }
 span.shop:hover div.dropdown {
  display: block;
  margin-left: -77px;"; //19 + icon size
  echo "left: 0px;
  overflow-x: hidden;
 }
 .fa-shopping-bag:hover {
  color: #684388 !important;
 }
</style>

<div class='bar' style=' font-size: 18px;'>
 <a href='index.cgi'>
  <img class='icon' src='res/beachstreetprofile.png' style='float:left; margin-left:10px;margin-top:5px;' width=58px height=65px>
 </a> <!--h70-->
 <span class='shop menu' style='float:left; margin-top:25px; margin-left:10px;'>
  <a href='shop.cgi?tag=a&gen=a'>";
   if(basename($_SERVER['PHP_SELF']) == 'shop.cgi'){echo"
    <u>";}
     echo "SHOP"; if(basename($_SERVER['PHP_SELF']) == 'shop.cgi'){echo "
    </u>";} echo "
  </a>
  <div class='dropdown'>";

echo "
<style>
 a, a:visited {
  color:white;
 }
</style>";


echo "
<div style='float:left;background-color:orange;opacity:0;width:50vw;height:26px; position:relative;'>
</div>
<div style='max-width:100%;float:left;background-color:#348E74;width:99vw;   border: solid #684388; border-style: solid hidden hidden hidden; border-width:thin;'>
 <div style='margin-top:0px;'>
  <div style='display:inline-block;'>
   <div style='padding-left:42px;color:white'><br>
    <ul>
     <a href='shop.cgi?gen=a"; echo "&price=";echo $_GET['price']; echo "&tag=";echo $_GET['tag']; echo "'>
      ALL
     </a><br>
     <a href='shop.cgi?gen=m"; echo "&price=";echo $_GET['price']; echo "&tag=";echo $_GET['tag']; echo "'>
      MEN
     </a><br>
     <a href='shop.cgi?gen=w"; echo "&price=";echo $_GET['price']; echo "&tag=";echo $_GET['tag']; echo "'>
      WOMEN
     </a><p>

     <a href='shop.cgi?tag=a"; echo "&price=";echo $_GET['price']; echo "&gen=";echo $_GET['gen']; echo "'>
      ALL
     </a><br>
     <a href='shop.cgi?tag=shirt"; echo "&price=";echo $_GET['price']; echo "&gen=";echo $_GET['gen']; echo "'>
      SHIRTS
     </a><br>
     <a href='shop.cgi?tag=jacket"; echo "&price=";echo $_GET['price']; echo "&gen=";echo $_GET['gen']; echo "'>
      JACKETS
     </a><br>
     <a href='shop.cgi?tag=hat"; echo "&price=";echo $_GET['price']; echo "&gen=";echo $_GET['gen']; echo "'>
      HATS
     </a><p>

     <a href='shop.cgi?rand=true&gen="; echo $_GET['gen']; echo "&tag=";echo $_GET['tag']; echo "'>
      RANDOM
     </a><p>
    </ul>
   </div>
  </div>
  <div style='display:inline-block;'><!-- jcr -->";
// PDO + SQLite
$pdo = new PDO('sqlite:/home/t/thebeachstreet.com/database/bs.db');
$statement = $pdo->query("SELECT * FROM items ORDER BY RANDOM()");

$i=0;

while($row = $statement->fetch(PDO::FETCH_ASSOC)) {
 $i++;
 if($i > 4) {break;}
 //if($_GET["gen"] == 'w') {
 if($row['gen'][$i] == $_GET['gen'] || $_GET['gen'] == 'a' || !$_GET['gen']) {
 echo "<div style='display:inline-block;'>";
  echo "<div style='width:100%;margin:30px;' align='center'>";
   echo "<img align='center' src='res/items/";
    echo $row['img'];
    echo "' width='100px'>";
   echo "<br>";
   echo htmlentities($row['name']);
   echo "<br>";
  echo "</div>
 </div>";}
}

echo "
  </div>
 </div>
</div>";


echo "
  </div>
 </span>
 <a href='#news' class='menu' style='float:left; margin-top:25px; margin-left:18px;'>
  NEWS
 </a>
 <span class='menu' style='float:left; margin-top:25px; margin-left:18px;'>
  ABOUT
 </span>
 <span class='menu' style='float:right; margin-right:30px; margin-top:20px;'>
  <a href=' https://www.paypal.com/cgi-bin/webscr?cmd=_cart&business=sales@thebeachstreet.com&display=1' class='fas fa-shopping-bag fa-2x' style='color:white;'>
  </a>
 </span>
</div>";
 echo "<div style='position:static'>";
echo "
<style>
 div.men {
  width: 30%;
  float: left;
  height: 600px;
  margin-top: 2%;
  margin-left: 2%;
  position: relative;
 }
 div.women {
  margin-top: 2%;
  margin-left: 34%;
  margin-right: 2%;
  height: 600px;
  position: relative;
 }
 div.soon {
  margin-top: 2%;
  width: 60%;
  float: left;
  height: 600px;
  margin-left: 2%;
  position: relative;
 }
 div.month {
  background-color: pink;
  margin-top: 2%;
  margin-bottom: 2%;
  margin-right: 2%;
  margin-left: 64%;
  height: 600px;
  position: relative;
 }
 div.text-block {
  position: absolute;
  font-size: 2em;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  color: #348E74;
  border: solid #348E74;
  border-style: solid hidden solid hidden;
  border-width: 10px;
  font-weight: bold;
  background-color: lightgrey;
  opacity:.8;
 }
 div.text-block:hover {
  border: solid #684389;
  border-style: solid hidden solid hidden;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 2em;
  color: #684389;
  border-width: 10px;
 }
</style>

<div style='width: 100%; overflow: hidden;'>
 <a href='shop.cgi?gen=m&tag=a'>
  <div class='men'>
   <div class='text-block' style='bottom:40%!important;right:60%!important'>
    MEN
   </div>
   <img src='res/m.jpg' width=100% height=100%>
  </div>
 </a>
 <a href='shop.cgi?gen=w&tag=a'>
  <div class='women'>
   <div class='text-block' style='bottom:40%!important;left:20%!important'>
    WOMEN
   </div>
   <img src='https://i.ytimg.com/vi/jAlMr6F1OoE/maxresdefault.jpg' width=100% height=100%>
  </div>
 </a>
</div>

<div style='width: 100%; overflow: hidden;'>
 <div class='soon'>
  <div class='text-block' style='bottom:68%!important;right:30%!important'>
   MORE COMING SOON
  </div>
  <img src='res/sw.jpg' width=100% height=100%>
 </div>
 <div class='month'>
  <div class='text-block' style='bottom:20%!important;right:3%!important'>
   BREAST CANCER AWARENESS
  </div>
  <img src='res/Valentina-Tereshkova.png' width=100% height=100%>
 </div>
</div>";
 echo "</div>";
echo "
<center>
 <h2 class='title'>
  LATEST
 </h1>
 <h1>
  Coming Soon!
 </h1>
</center>";
 echo "
</body>";

echo "<footer>
<a name='news'/>
<style>
 div.nw {
  background-color: lightgrey;
  padding: 0px;
  height: 260px;
  width: 100%;
  padding-top:120px;
 }
 #button, #button {"; /*link, visited*/
  echo "background-color: #348E74;
  color: white;
  padding: 14px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
 }";
 /*#button, active#button { //hover, active
  background-color: #2E564B;
 }*/
 echo "input#sub {
  width: 30%;
 }
 input[type=text] {
  width: 20%;
  padding: 12px 20px;
  margin: 2px 0;
  box-sizing: border-box;
  border: 3px solid #ccc;
  -webkit-transition: 0.5s;
  transition: 0.5s;
  outline: none;
 }
 input[type=text]:focus {
  border: 3px solid #555;
 }
</style>";

#$db = new PDO('sqlite:/home/t/thebeachstreet.com/database/bs.db');
#$email = $_GET['sub'];
#$db->exec('INSERT INTO elist (email) VALUES ($email)');

echo "
<div class='nw'>
 <center>
  <h1>
   Subscribe To Our Newsletter
  </h1>
  <a name='contact'>
   <form action='sub.cgi' onsubmit='return myFunction()'>
    <input type='text' name='sub' id='sub'>
    <input id='button' type='submit' value='Submit'>
    <!--<a id='button' href='?sub='>Submit</a>-->
   </form>
  </a>
 </center>
</div>

<script>
 function myFunction() {
  var at = document.getElementById('sub').value.indexOf('@');
  if(at == -1) {alert('Not a valid e-mail address.');return false;}
 }
</script>";
echo "
<script src='https://kit.fontawesome.com/21c9216300.js' crossorigin='anonymous'>
</script>
<style>
 div.ft {
  background-color: #348E74;
  padding: 0px;
  height: 380px;
  width: 100%;
  bottom: 0px;
  position: relative;
 }
 div.ft-disp {
  bottom: 0px;
  width: 90%;
  position: absolute;
  height: 250px;
  margin-left: 5%;
 }
 div.social {
 }
 a.ft, a.ft:visited {
  color: white;
 }
 a.ft:hover {
  color: #684388;
 }
 .fa-twitter, .fa-instagram, .fa-credit-card, .fa-cc-paypal {
  color: white;
 }
 .fa-twitter:hover, .fa-instagram:hover, .fa-credit-card:hover, .fa-cc-paypal:hover {
  color: #684388 !important;
 }
</style>

<div class='ft'>
 <div class='ft-disp'>
  <div class='social'>
   <center>
    <a class='fab fa-twitter fa-3x' href='https://twitter.com/thebeachstreet'>
    </a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a class='fab fa-instagram fa-3x' href='https://www.instagram.com/thebeachstreetofficial/'>
    </a>
   </center>
  </div>
  FAQ<p>
  <span style='float:right'>
   <i class='far fa-credit-card fa-3x'>
   </i>&nbsp;&nbsp;
   <i class='fab fa-cc-paypal fa-3x'>
   </i>
  </span>
  Terms & Conditions<p>
  Return Policy<p>
  <a class='ft' href='mailto:sales@thebeachstreet.com'>
   Get In Contact With Us!
  </a>
  <span style='float:right'>
   Beach Street &copy;2019
  </span>
 </div>
</div>";
echo "<link rel='stylesheet' type='text/css' href='beach.css'>";
echo "
<div id='myDIV-bottom'>
 <center>"; 
echo "<a class='p' href='#news'>Free Shipping On All Orders - Sign Up For Our Newsletter</a>"; echo "
  <div class='p' style='float: right; margin-right:13px; cursor: pointer;' onclick='bottom()'>
   &times;
  </div>
 <center>
</div>

<script>
 function bottom() {
  var y = document.getElementById('myDIV-bottom');
  if (y.style.display === 'none') {
   y.style.display = 'block';
   } else {
    y.style.display = 'none';
   }
 }
</script>";
echo "</footer>";
?>
