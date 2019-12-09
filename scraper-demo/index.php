<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Scraper Demo</title>
    <link type="text/css" rel="stylesheet" href="/main.css">
    <link type="text/css" rel="stylesheet" href="/scraper-demo/styles.css">
  </head>
  <body>
    <h1>Scraper Demo</h1>
    <form action="." method="post">
      <input type="text" name="url" placeholder="Enter Wayfair URL">
      <input type="submit" value="Submit">
    </form>
  </body>
</html>

<?php 
if (isset($_POST['url'])) {
  $url = $_POST['url'];
  $command = "python3 ./mine-scraper/scraper.py " . $url;
  $product_json = shell_exec($command); // response from the scraper

  if (preg_match("/ConnectionError/", $product_json)) {
      echo $product_json;
      die();
  }

  $product_portfolio = json_decode($product_json);

  echo('<br><h2>' . $product_portfolio->{'title'} . '</h2>');
  echo('<img src="' . $product_portfolio->{'image'} . '">');
  echo('<div class="center">');
  echo('<p><b>' . $product_portfolio->{'price'} . '</b></p>');
  echo('<p>' . $product_portfolio->{'desc'} . '</p>');
  echo("</div>");
}
?>
