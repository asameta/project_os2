<?php
$ini_data = file_get_contents('php://input');
file_put_contents('setup.ini', $ini_data);
echo 'Success';

?>
