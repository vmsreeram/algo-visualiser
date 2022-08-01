<!DOCTYPE html>
<html>
    <head>
        <title>Dinic's visualization</title>
        <style>
/*             
            .leftimg{
                top:10%;
                left:52.5%;
                float:right;
                position:absolute;
                height:80%;
                max-width:45vw;
            }
*/
            .leftimg{
                top:10%;
                right:51%;
                float:right;
                position:absolute;
                height:80%;
                max-width:45vw;
            }
            .rightimg{
                top:10%;
                left:51%;
                float:left;
                position:absolute;
                height:80%;
                max-width:45vw;
            }
            .leftlbl{
                /* background-color: #110011; */
                bottom:0;
                left:2.5%;
                float:left;
                width:100%;
                position:absolute;
                height:11%;
                border: none;
            }

            .anotherlbl{
                top:5%;
                left:25%;
                /* float:right; */
                /* width:45%; */
                position:absolute;
                /* height:11%; */
                border: none;
            }

            .albl{
                top:5%;
                left:65%;
                /* float:left; */
                /* width:45%; */
                position:absolute;
                /* height:11%; */
                border: none;
            }
/* 
            .rightimg{
                top:10%;
                right:52.5%;
                float:left;
                position:absolute;
                height:80%;
                max-width:45vw;
            }
             */
            .buttonl {
                /* width: 100%; */
                font-weight: bolder;
                /* font-family: 'Times New Roman', Times, serif; */
                background-color: #4CAF50;
                color: white;
                margin-right: 50.5%;
                position:relative;
                /* padding: 8px 20px; */
                padding: 0.55% 1.5%;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                float: right;
                
            }

            .buttonl:hover {
                background-color: #45a049;
            }

            .buttonr {
                /* width: 100%; */
                font-weight: bolder;
                /* font-family: 'Times New Roman', Times, serif; */
                background-color: #4CAF50;
                color: white;
                margin-left: 50.5%;
                position:absolute;
                /* padding: 8px 20px; */
                padding: 0.55% 1.5%;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                float: left;
                }

            .buttonr:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    
    <body>
        <!-- <h1>Dinic's Visualiser</h1> -->
        
        <?php 
            $sno=0;
            $imageLft = 'imgs/flow/'.$sno.'.png'; 
            $imageRgt = 'imgs/level/'.$sno.'.png'; 
            $flow = 'imgs/labels/flo.txt';
            $resi = 'imgs/labels/'.$sno.'.txt'; 
            $target_dir = "imgs/flow/";
            $nlines = count(glob($target_dir . "*"));
            $numLines = intval($nlines);

            $labelLft= 'imgs/labels/lb.txt';
        ?>

        <script >

        var sno=parseInt('<?php echo $sno;?>');
        var imageLft = '<?php echo $imageLft;?>';
        var imageRgt = '<?php echo $imageRgt;?>';
        var labelLft = '<?php echo $labelLft;?>';
        var numLines=parseInt('<?php echo $numLines;?>');
        var flow = '<?php echo $flow;?>';
        var resi = '<?php echo $resi;?>';
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
            flow ='imgs/labels/flo.txt'; 
            resi = 'imgs/labels/'+(sno)+'.txt'; 
            if(sno!=numLines-1)
            {
                labelLft= 'imgs/labels/lb.txt'; //Try lb.png instead
            }
            else
            {
                labelLft= 'imgs/labels/final.txt';
            }
            document.getElementById('lftimgfrm').src=imageLft;
            document.getElementById('rgttimgfrm').src=imageRgt;
            document.getElementById('lftlbl').src=labelLft;
            document.getElementById('flow').src=flow;
            document.getElementById('resi').src=resi;
        }
        function prev(){
            if(sno>0)
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
            labelLft= 'imgs/labels/lb.txt';
            flow ='imgs/labels/flo.txt'; 
            resi = 'imgs/labels/'+(sno)+'.txt'; 
            document.getElementById('lftimgfrm').src=imageLft;
            document.getElementById('rgttimgfrm').src=imageRgt;
            document.getElementById('lftlbl').src=labelLft;
            document.getElementById('flow').src=flow;
            document.getElementById('resi').src=resi;
        }
        </script>
        <!-- <div> -->
        <button class="buttonl" id="C1" onclick="prev()" hidden accesskey="a"> Prev </button>
        <button class="buttonr" id="C2" onclick="next()" accesskey="s"> Next </button>
        <!-- </div> -->
        <!-- <p id="testing"></p>leftlbl
        <p id="testing1"></p> -->
        <img id="lftimgfrm" class="leftimg" src="<?php echo $imageLft; ?>">
        <img id="rgttimgfrm" class="rightimg" src="<?php echo $imageRgt; ?>">
        <iframe id="lftlbl" class="leftlbl" src="<?php echo $labelLft; ?>"> </iframe>
        <iframe id="flow" class="anotherlbl" src="<?php echo $flow; ?>"> </iframe>
        <iframe id="resi" class="albl" src="<?php echo $resi; ?>"> </iframe>

</body>
</html>
