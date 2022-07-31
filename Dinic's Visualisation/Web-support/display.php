<!DOCTYPE html>
<html>
    <head>
        <title>Hello</title>
        <style>
            .leftimg{
                top:15%;
                left:0;
                float:left;
                width:49.5%;
                position:absolute;
                height:75%;
            }
            .leftlbl{
                /* background-color: #110011; */
                bottom:0;
                left:0;
                float:left;
                width:100%;
                position:absolute;
                height:8%;
            }
            .rightimg{
                top:15%;
                right:0;
                float:right;
                width:49.5%;
                position:absolute;
                height:75%;
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

            $labelLft = 'imgs/labels/'.($sno).'.txt';
        ?>

        <script >

        var sno=parseInt('<?php echo $sno;?>');
        var imageLft = '<?php echo $imageLft;?>';
        var imageRgt = '<?php echo $imageRgt;?>';
        var labelLft = '<?php echo $labelLft;?>';
        var numLines=parseInt('<?php echo $numLines;?>');
        function next(){
            // document.getElementById("testing").innerHTML=numLines;
            if(sno+1<numLines)
            {
                sno=sno+1;
            }
            
            // document.getElementById("testing").innerHTML=labelLft;
            // document.getElementById("testing1").innerHTML=imageLft;
            imageLft='imgs/flow/'+(sno)+'.png'; 
            imageRgt='imgs/level/'+(sno)+'.png'; 
            labelLft='imgs/labels/'+(sno)+'.txt';

            document.getElementById('lftimgfrm').src=imageLft;
            document.getElementById('rgttimgfrm').src=imageRgt;
            document.getElementById('lftlbl').src=labelLft;
        }
        function prev(){
            if(sno-1>-1)
            {
                sno=sno-1;
            }
            
            // document.getElementById("testing").innerHTML=labelLft;
            // document.getElementById("testing1").innerHTML=imageLft;
            imageLft='imgs/flow/'+(sno)+'.png'; 
            imageRgt='imgs/level/'+(sno)+'.png'; 
            labelLft='imgs/labels/'+(sno)+'.txt';

            document.getElementById('lftimgfrm').src=imageLft;
            document.getElementById('rgttimgfrm').src=imageRgt;
            document.getElementById('lftlbl').src=labelLft;
        }
        </script>

        <button id="C1" onclick="prev()"> << </button>
        <button id="C2" onclick="next()"> >> </button>
        <p id="testing"></p>
        <p id="testing1"></p>
        <iframe id="lftimgfrm" class="leftimg" src="<?php echo $imageLft; ?>"> </iframe>
        <iframe id="rgttimgfrm" class="rightimg" src="<?php echo $imageRgt; ?>"> </iframe>
        <iframe id="lftlbl" class="leftlbl" src="<?php echo $labelLft; ?>"> </iframe>

</body>
</html>
