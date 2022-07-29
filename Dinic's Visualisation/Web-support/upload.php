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
  <br/>
  Enter space separated source and sink vertex indices : <input type=text name="textbox1">
  <br/>
  <input type="submit" value="Proceed" name="proceed">
</form>

<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$txtFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
$target_file = $target_dir . "inputUp.txt";

if(isset($_POST["submit"])) {
      $check = filesize($_FILES["fileToUpload"]["tmp_name"]);
      if($check !== false) {
        $uploadOk = 1;
      } else {
        $uploadOk = 0;
      }

      if ($_FILES["fileToUpload"]["size"] > 500000) {
        echo "Sorry, your file is too large.";
        $uploadOk = 0;
      }

      if($txtFileType != "txt" ) {
        echo "Sorry, only TXT files are allowed.";
        $uploadOk = 0;
      }
      if ($uploadOk == 0) {
        echo "Sorry, your file was not uploaded.";
      } else {
        if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
          echo "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded as uploads/inputUp.txt \n"."<br/>";
          // echo "calling python";
          exec('python start.py');
          // echo "<br/>". is_readable('../imgs/inp_grp.png')."<br/>";
          $srcpath = '../imgs/inp_grp.png';
          if ( !is_readable($srcpath) ) {
              echo "file not found 404";
              echo "<br/>";
              header('file not found', 404);
              die;
          }
          else {
              echo "<img src='imgs/inp_grp.png' width=500 height=500 >"; 
          } 
        } else {
          echo "Sorry, there was an error uploading your file.";
        }
      }
  }
if(isset($_POST["proceed"]))
{
  // echo "Proceed pressed <br/>";
  $tb1=$_POST['textbox1'];
  // echo "got input as".$a ." <br/>";

  $nlines = count(file($target_file));
  $numLines = intval($nlines);
  $delimiter = ' ';
  $words = explode($delimiter, $tb1);
  $cnt = 0;
  // $sourcein = -1;
  $validsrcsnk = true;
  foreach($words as $word)
  {
    $cnt+=1;
    if(intval($word)<0 || intval($word)>=$numLines)
    {
      $validsrcsnk=false;
    }
    if($sourcein==-1)
    {
      $sourcein=intval($word);
    }
    else if(intval($word) == $sourcein)
    {
      $validsrcsnk=false; // src != sink is essential
    }
  }
  if($cnt != 2)
  {
    $validsrcsnk=false;
  }


  if($validsrcsnk)
  {
  $caller='python Dinic.py';
  $caller.=' ';
  $caller.=$tb1;
  echo $caller."<br/>";
  exec($caller);
  }
  else
  {
    
    echo "Invalid input of source/sink.<br/>";
  }
}
?>

</body>
</html>
