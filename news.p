<?php echo "<link rel='stylesheet' type='text/css' href='beach.css'>
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

$db = new PDO('sqlite:res/bs.db');
$email = $_GET['sub'];
$db->exec('INSERT INTO elist (email) VALUES ($email)');

echo "
<div class='nw'>
 <center>
  <h1>
   Subscribe To Our Newsletter
  </h1>
  <a name='contact'>
   <form action='sub.p' onsubmit='return myFunction()'>
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

?>
