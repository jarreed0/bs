#!/usr/pkg/bin/php

<?php
parse_str($_SERVER['QUERY_STRING'], $_GET);

echo "<style>a.link{font-color:black !important;}</style>";
echo "<link rel='stylesheet' type='text/css' href='beach.css'>";
echo "
<html>
 <title>SHOP - Beach Street</title>
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
</div>

</header>

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

     <a  href='shop.cgi?rand=true"; echo "&gen=";echo $_GET['gen']; echo "&tag=";echo $_GET['tag']; echo "'>
      RANDOM
     </a><p>
    </ul>
   </div>
  </div>
  <div style='display:inline-block;'>";
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
 </a>";
/* <span class='menu' style='float:left; margin-top:25px; margin-left:18px;'>
  ABOUT
 </span>*/
echo "<span class='menu' style='float:right; margin-right:30px; margin-top:20px;'>
  <a href=' https://www.paypal.com/cgi-bin/webscr?cmd=_cart&business=sales@thebeachstreet.com&display=1' class='fas fa-shopping-bag fa-2x' style='color:white;'>
  </a>
 </span>
</div>";
echo "
 <style>";
  /*div.it:hover {
   background-color:lightgrey;
  }
  div.it:active {
   background-color:grey;
  }*/ echo "
 </style>

 <div style='width: 100%; display: table-cell; display: table;'>
  <div style='display: table-row;'>
   <div style='padding-left:42px; position:sticky;position:-webkit-sticky; font-size: 18px;'><br>
    <ul>
     <a class='link' href='?gen=a"; echo "&price=";echo $_GET['price']; echo "&tag=";echo $_GET['tag']; echo "'>"; if($_GET['gen']==a){echo "
      <u>";} echo "
       ALL"; if($_GET['gen']==a){echo "
      </u>";} echo "
     </a><br>
     <a class='link' href='?gen=m"; echo "&price=";echo $_GET['price']; echo "&tag=";echo $_GET['tag']; echo "'>"; if($_GET['gen']==m){echo "
      <u>";} echo "
       MEN"; if($_GET['gen']==m){echo "
      </u>";} echo "
     </a><br>
     <a class='link' href='?gen=w"; echo "&price=";echo $_GET['price']; echo "&tag=";echo $_GET['tag']; echo "'>"; if($_GET['gen']==w){echo "
      <u>";} echo "
       WOMEN"; if($_GET['gen']==w){echo "
      </u>";} echo "
     </a><p>

     <a class='link' href='?tag=a"; echo "&price=";echo $_GET['price']; echo "&gen=";echo $_GET['gen']; echo "'>"; if($_GET['tag']==a){echo "<u>";} echo "ALL"; if($_GET['tag']==a){echo "</u>";} echo "</a><br>
     <a class='link' href='?tag=shirt"; echo "&price=";echo $_GET['price']; echo "&gen=";echo $_GET['gen']; echo "'>"; if($_GET['tag']==shirt){echo "<u>";} echo "SHIRTS"; if($_GET['tag']==shirt){echo "</u>";} echo "</a><br>
     <a class='link' href='?tag=jacket"; echo "&price=";echo $_GET['price']; echo "&gen=";echo $_GET['gen']; echo "'>"; if($_GET['tag']==jacket){echo "<u>";} echo "JACKETS"; if($_GET['tag']==jacket){echo "</u>";} echo "</a><br>
     <a class='link' href='?tag=hat"; echo "&price=";echo $_GET['price']; echo "&gen=";echo $_GET['gen']; echo "'>"; if($_GET['tag']==hat){echo "<u>";} echo "HATS"; if($_GET['tag']==hat){echo "</u>";} echo "</a><p>

     <a class='link' href='?rand=true"; echo "&gen=";echo $_GET['gen']; echo "&tag=";echo $_GET['tag']; echo "'>"; if($_GET['rand']){echo "<u>";} echo "RANDOM"; if($_GET['rand']){echo "</u>";} echo "</a><p>

     <a class='link' href='?price="; if(!$_GET['price'] || $_GET['price']=='low'){echo "high";}else{echo "";} echo ""; echo "&gen=";echo $_GET['gen']; echo "&tag=";echo $_GET['tag'];echo "'>"; if($_GET['price']==high){echo "<u>";} echo "PRICE &uarr;"; if($_GET['price']==high){echo "</u>";} echo "</a><br>
     <a class='link' href='?price="; if(!$_GET['price'] || $_GET['price']=='high'){echo "low";}else{echo "";} echo ""; echo "&gen=";echo $_GET['gen']; echo "&tag=";echo $_GET['tag'];echo "'>"; if($_GET['price']==low){echo "<u>";} echo "PRICE &darr;"; if($_GET['price']==low){echo "</u>";} echo "</a><p>
    </ul>
   </div>
   <div style='display:table-cell;width:84%;padding:10px;'><br>";
    // PDO + SQLite
    $pdo = new PDO('sqlite:/home/t/thebeachstreet.com/database/bs.db');
    //$statement = $pdo->query('SELECT * FROM items ORDER BY RANDOM()');
    //$statement = $pdo->query('SELECT * FROM items ORDER BY CASE tag WHEN 'shirt' THEN 0 WHEN 'jacket' THEN 1 WHEN 'hat' THEN 2 END');
    $statement = $pdo->query('SELECT * FROM items ORDER BY id DESC');
    if($_GET['price'] == 'high') {$statement = $pdo->query('SELECT * FROM items ORDER BY price DESC');}
    if($_GET['price'] == 'low') {$statement = $pdo->query('SELECT * FROM items ORDER BY price ASC');}
    if($_GET['rand']) {$statement = $pdo->query('SELECT * FROM items ORDER BY RANDOM()');}
    //echo "<br><span style='font-weight:510;'>ALL ;)</span><br>";
    while($row = $statement->fetch(PDO::FETCH_ASSOC)) {
     if($row['gen'] == $_GET['gen'] || $_GET['gen'] == 'a' || !$_GET['gen'] || $row['gen'] == 'a') {
      if($_GET['tag'] && $_GET['tag'] == $row['tag'] && $row['tag'] != a) {
       include('item.p');
      } elseif(!$_GET['tag'] || $_GET['tag'] == a) {
       $_GET['img'] = $row['img'];
       $_GET['name'] = $row['name'];
       $_GET['price'] = $row['price'];
       $_GET['id'] = $row['id'];
       $_GET['shop'] = $row['shop'];
       $_GET['check'] = $row['check'];
       include('item.p');
      }
     }
    } echo "
   </div>
  </div>
 </div>
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

$db = new PDO('sqlite:/home/t/thebeachstreet.com/database/bs.db');
$email = $_GET['sub'];
$db->exec('INSERT INTO elist (email) VALUES ($email)');

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

