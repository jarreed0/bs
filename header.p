<?php 
echo "<link rel='stylesheet' type='text/css' href='beach.css'>";
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
  echo "<a href='index.p'><img src='res/bslogo.jpg' style='width:45%; height:200px;'>
  </a>
 </center>
</div>";

?>











