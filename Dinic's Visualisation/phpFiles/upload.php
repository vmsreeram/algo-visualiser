<!DOCTYPE html>
<html>
  <head>
    <title>
      Dinic's Visualisation
    </title>
  </head>
<body>
 
<h1>Select input </h1>


<form action="upload.php" method="post" enctype="multipart/form-data">
  Select input graph (.txt only):
  <input type="file" name="fileToUpload" id="fileToUpload">
  <br/>
  <input type="submit" value="Upload" name="submit">
</form>

<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
// $target_file = $target_dir . "inputUp.txt";
$uploadOk = 1;
$txtFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
$target_file = $target_dir . "inputUp.txt";

// Check if txtfile file is an actual txtfile or fake txtfile
if(isset($_POST["submit"])) {
  $check = filesize($_FILES["fileToUpload"]["tmp_name"]);
  if($check !== false) {
    // echo "File is a txtfile - " . $check["mime"] . ".";
    $uploadOk = 1;
  } else {
    // echo "File is not a txtfile.";
    $uploadOk = 0;
  }
}

// Check if file already exists
if (file_exists($target_file)) {
  // echo "Sorry, file already exists.";
  $uploadOk = 1;
}

// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000) {
  echo "Sorry, your file is too large.";
  $uploadOk = 0;
}

// Allow certain file formats
echo "file type " . $txtFileType;
echo "<br/>";
if($txtFileType != "txt" ) {
  echo "Sorry, only TXT files are allowed.";
  $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
  echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    echo "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded as ";
  } else {
    echo "Sorry, there was an error uploading your file.";
  }
}

echo basename( $target_file);
echo "<br/>";
?>

</body>
</html>
