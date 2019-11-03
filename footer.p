<?php 
echo "<link rel='stylesheet' type='text/css' href='style.beach'>";
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
   y.style.display = 'block";
   } else {
    y.style.display = 'none";
   }
 }
</script>";

