<?php
echo "
<div id=popup"; echo $row['id']; echo " class=overlay>
 <div class=popup>
  <h2>";
   echo $row['name']; echo "
  </h2>
  <a class=close href='#q"; echo $row['id']; echo "'>
   &times;
  </a>
  <div class=content style='padding:-20px;'>"; echo "
  <center>
   <img align='center' src='res/items/"; echo $row['img']; echo "'width='400px' height='400px'>
  </center>"; echo "
  <div style='width:40%;height:50%;float:left;'>";
   echo "<br>";
   echo $row['desc'];
   echo "<br>Shipping: ";
   echo $row['ship'];
   echo " days<br>$";
   echo htmlentities($row['price']); echo "
  </div>
  <div style='width:120px;height:50%;float:right;'>"; echo "
   <form target='paypal' action='https://www.paypal.com/cgi-bin/webscr' method='post'>
    <input type='hidden' name='cmd' value='_s-xclick'>
    <input type='hidden' name='hosted_button_id' value='"; echo $row['check']; echo "'>";
     if($row['tag'] == 'jacket' || $row['tag'] == 'shirt') { echo "
      <table>
       <tr>
        <td>
         <input type='hidden' name='on0' value='Sizes'>
        </td>
       </tr>
       <tr>
        <td>
         <select name='os0'>
    	  <option value='S'>
	   Small
	  </option>
	  <option selected='selected' value='M'>
	   Medium
	  </option>
	  <option value='L'>
	   Large
	  </option>
         </select>
        </td>
       </tr>
      </table>";} echo "
      <input type='image' src='https://www.paypalobjects.com/en_US/i/btn/btn_cart_LG.gif' border='0' name='submit' alt='PayPal - The safer, easier way to pay online!'>
      <img alt='' border='0' src='https://www.paypalobjects.com/en_US/i/scr/pixel.gif' width='1' height='1'>
     </form>";
     //style='width:60px;height:60px;' src='res/addtocart.png'
     echo "
    </div>
   </form>"; echo "
  </div>
 </div>
</div>";

echo "
<div style='display:inline-block;'>";echo "
 <div class='it' name='q"; echo $row['id']; echo "align='center'>"; echo "
  <a class=link href='#popup"; echo $row['id']; echo "'>"; echo "
   <img align='center' src='res/items/"; echo $row['img']; echo "' width='200px' height='200px'>";
   echo "<br>";
   echo htmlentities($row['name']);
   echo "<br>&nbsp;$";
   echo htmlentities($row['price']);
   echo "<br>"; echo "
  </a>"; echo "
 </div>
</div>";

echo "
<style>
 .it {
  color: black !important;";
  //background-color: orange;
  //border: solid black;
  echo "cursor: pointer;
  width:76%;
  margin:30px;
 }
 .overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.2);";
  //transition: opacity 500ms;
  echo "visibility: hidden;
  opacity: 0;
  z-index: 2;
}
.overlay:target {
  visibility: visible;
  opacity: 1;
 }
 .popup {
  width: 40%;";
  //height: 20%;
  echo "margin: 70px auto;
  padding: 20px;
  background: #fff;";
  //border-radius: 5px;
  echo "position: relative;
  transition: all 5s ease-in-out;
 }
 .popup h2 {
  color: black;
  margin-top: 0;
 }
 .popup .close {
  position: absolute;
  top: 20px;
  right: 30px;
  transition: all 200ms;
  font-size: 30px;
  font-weight: bold;
  color:#333;
  text-decoration: none;
 }
 .popup .content {
  max-height: 30%;
  overflow: auto;
 }
</style>";

?>
