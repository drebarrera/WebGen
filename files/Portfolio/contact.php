if($_POST["submit"]) {
	$recipient="drebarrera@yahoo.com";
	$name=$_POST["name"];
	$email=$_POST["email"];
	$phone=$_POST["phone"];
	$subject="Website message from ".$name;
	$message=$_POST["message"];
	$visitInfo = 'Contact,';
	$visitInfo .= $_SERVER['REMOTE_ADDR'];
        date_default_timezone_set("America/New_York");
        $visitInfo .= ','.date("Y-m-d;h:i:sA").','.$email.PHP_EOL;
	
	if (strstr($message,'drebarrera.com') or strstr($message,'.xyz') or strstr($message,'bit.ly')) {
        	file_put_contents('../data/scamInfo.txt', $visitInfo, FILE_APPEND);
    	} else {
        	$mailBody="Name: $name\nEmail: $email\nPhone: $phone\n\n$message\n\n$visitInfo";
		mail($recipient, $subject, $mailBody, "From: $name <$email>");
		$thankYou="<p>Thank you! Your message has been sent.</p>";
    	}
}

