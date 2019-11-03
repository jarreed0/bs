<?php
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
 <a href='shop.p?gen=m&tag=a'>
  <div class='men'>
   <div class='text-block' style='bottom:40%!important;right:60%!important'>
    MEN
   </div>
   <img src='res/m.jpg' width=100% height=100%>
  </div>
 </a>
 <a href='shop.p?gen=w&tag=a'>
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
?>
