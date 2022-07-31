<!DOCTYPE html>
<html>
    <head>
        <title>Hello</title>
        <style>
            .leftimg{
                top:15%;
                left:0;
                float:left;
                width:49%;
                position:absolute;
                height:85%;
            }
            .rightimg{
                top:15%;
                right:0;
                float:right;
                width:49%;
                position:absolute;
                height:85%;
            }
        </style>
    </head>
    
    <body>
        <h1>Visualiser</h1>
        
        <?php 
            $sno=0;
            $imageLft = 'imgs/flow/'.$sno.'.png'; 
            $imageRgt = 'imgs/level/'.$sno.'.png'; 

            $target_dir = "imgs/flow/";
            $nlines = count(glob($target_dir . "*"));
            $numLines = intval($nlines);
        ?>

        <script >

        var sno=parseInt('<?php echo $sno;?>');
        var imageLft = '<?php echo $imageLft;?>';
        var imageRgt = '<?php echo $imageRgt;?>';

        var numLines=parseInt('<?php echo $numLines;?>');
        function next(){
            // document.getElementById("testing").innerHTML=numLines;
            if(sno+1<numLines)
            {
                sno=sno+1;
            }
            
            
            imageLft='imgs/flow/'+(sno)+'.png'; 
            imageRgt='imgs/level/'+(sno)+'.png'; 

            // document.getElementById("testing").innerHTML=imageLft;
            // document.getElementById("testing1").innerHTML=imageRgt;
            document.getElementById('lftimgfrm').src=imageLft;
            document.getElementById('rgttimgfrm').src=imageRgt;
        }
        function prev(){
            if(sno-1>-1)
            {
                sno=sno-1;
            }
            
            imageLft='imgs/flow/'+(sno)+'.png'; 
            imageRgt='imgs/level/'+(sno)+'.png'; 

            // document.getElementById("testing").innerHTML=imageLft;
            // document.getElementById("testing1").innerHTML=imageRgt;
            document.getElementById('lftimgfrm').src=imageLft;
            document.getElementById('rgttimgfrm').src=imageRgt;
        }
        </script>

        <button id="C1" onclick="prev()"> << </button>
        <button id="C2" onclick="next()"> >> </button>
        <!-- <p id="testing"></p>
        <p id="testing1"></p> -->
        <iframe id="lftimgfrm" class="leftimg" src="<?php echo $imageLft; ?>"> </iframe>
        <iframe id="rgttimgfrm" class="rightimg" src="<?php echo $imageRgt; ?>"> </iframe>

</body>
</html>
