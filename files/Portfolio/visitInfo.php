$visitInfo = $_SERVER['REQUEST_URI'].',';
$visitInfo .= $_SERVER['REMOTE_ADDR'];
date_default_timezone_set("America/New_York");
$visitInfo .= ','.date("Y-m-d;h:i:sA").','.$email.PHP_EOL;
file_put_contents('../data/visitInfo.txt', $visitInfo, FILE_APPEND);