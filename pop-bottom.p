<?php 
echo "<link rel='stylesheet' type='text/css' href='beach.css'>";
echo "
<div id='myDIV-bottom'>
 <center>"; echo "<a class='p' href='#news'>Free Shipping On All Orders - Sign Up For Our Newsletter</a>"; echo "
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
?>
