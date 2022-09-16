
var vid, playbtn, seekslider, curtimetext, durtimetext;
var point = 1;
var seconds = 0;
var sec = []

function intializePlayer(){
	// Set object references
	vid = document.getElementById("my_video");
	playbtn = document.getElementById("playpausebtn");
	seekslider = document.getElementById("seekslider");
	curtimetext = document.getElementById("curtimetext");
	durtimetext = document.getElementById("durtimetext");
	// Add event listeners
	playbtn.addEventListener("click",playPause,false);
	seekslider.addEventListener("change",vidSeek,false);
	vid.addEventListener("timeupdate",seektimeupdate,false);
}
window.onload = intializePlayer;
function playPause(e){
	if(vid.paused){
		vid.play();
		startTimer();

        
		playbtn.innerHTML = "Pause";
        // alert("video is play")
	} else {
		// debugger
		vid.pause();
		// alert(point)
		$.ajax({
			method:"POST",
			url:"score/",
			data:{"point":point},
			success: function(data){
				// debugger
				console.log(data);
			},
		});
		clearTimeout(timex);
        // video is stop
		playbtn.innerHTML = "Play";
	}
}
function vidSeek(){
	var seekto = vid.duration * (seekslider.value / 100);
	console.log(seekto,"seekto")
	vid.currentTime = seekto;
	console.log("seekcuurentTime",vid.currentTime)
}
function seektimeupdate(){
	var nt = vid.currentTime * (100 / vid.duration);
	console.log("nettime",nt)
	seekslider.value = nt;
	console.log("seekslider.value",seekslider.value)
	var curmins = Math.floor(vid.currentTime / 60);
	console.log('curmins',curmins)
	var cursecs = Math.floor(vid.currentTime - curmins * 60);
	console.log("cursecs",cursecs)
	var durmins = Math.floor(vid.duration / 60);
	console.log("video durations",vid.duration)
	console.log("durmins",durmins)
	var dursecs = Math.floor(vid.duration - durmins * 60);
	console.log("dursecs",dursecs)
	if(cursecs < 10){ cursecs = "0"+cursecs; }
	if(dursecs < 10){ dursecs = "0"+dursecs; }
	if(curmins < 10){ curmins = "0"+curmins; }
	if(durmins < 10){ durmins = "0"+durmins; }
	curtimetext.innerHTML = curmins+":"+cursecs;
	durtimetext.innerHTML = durmins+":"+dursecs;
}

function startTimer(){
    timex = setTimeout(function(){
        seconds++
		
		console.log(seconds)
        if(seconds>59){seconds=0;point++
		
			if(point<10) {
				console.log(point)
				$("#points").text('0'+point);
			}
			else{
				$("#points").text(point);
		
				}
		}
		startTimer();
    },1000);
}

function count_time(){
	timex = setTimeout(function(){
        seconds++
		console.log(seconds)
		video_duration_time = vid.duration;
		console.log(video_duration_time)
		video_total_sec = [];
		video_total_sec_length = video_total_sec.length;
		if(video_total_sec_length<=video_total_sec){
			video_total_sec.push(seconds)
		}
		else{
			seconds=0
		}
	},1000)


}

$("#score").submit(function(e) {
    e.preventDefault();
});

