<?php
$con = mysqli_connect('localhost','root');

if($con){
	echo "Connection successful";
}
else{
	echo "No Connection";

}

mysqli_select_db($con, 'edu');
$id = $_POST['id'];
$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$email = $_POST['email'];
$password = $_POST['password'];

$query = "insert into student(id, firstname, lastname, email, password)
values('$id','$firstname','$lastname','$email','$password')";

echo "$query";

mysqli_query($con,$query);

?>