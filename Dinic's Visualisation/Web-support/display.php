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
            .button {
                /* width: 100%; */
                font-weight: bolder;
                font-family: 'Times New Roman', Times, serif;
                background-color: #4CAF50;
                color: white;
                padding: 8px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                }

            .button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    
    <body>
        <h1>Dinic's Visualiser</h1>
        
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
            if(sno==numLines-1)
            {
                document.getElementById('C2').style.display='none';
            }
            else if(sno<numLines-1)
            {
                document.getElementById('C1').style.display='block';
                document.getElementById('C2').style.display='block';
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
            if(sno==0)
            {
                document.getElementById('C1').style.display='none';
            }
            else if(sno>0)
            {
                document.getElementById('C1').style.display='block';
                document.getElementById('C2').style.display='block';
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

        <button class="button" id="C1" onclick="prev()"> << </button>
        <button class="button" id="C2" onclick="next()"> >> </button>
        <!-- <p id="testing"></p>
        <p id="testing1"></p> -->
        <iframe id="lftimgfrm" class="leftimg" src="<?php echo $imageLft; ?>"> </iframe>
        <iframe id="rgttimgfrm" class="rightimg" src="<?php echo $imageRgt; ?>"> </iframe>
        <iframe id="lftlbl" class="leftlbl" src="<?php echo $labelLft; ?>"> </iframe>

</body>
</html>
