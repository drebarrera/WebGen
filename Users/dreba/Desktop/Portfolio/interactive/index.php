<?php $visitInfo = $_SERVER['REQUEST_URI'].',';
$visitInfo .= $_SERVER['REMOTE_ADDR'];
date_default_timezone_set("America/New_York");
$visitInfo .= ','.date("Y-m-d;h:i:sA").','.$email.PHP_EOL;
file_put_contents('../data/visitInfo.txt', $visitInfo, FILE_APPEND); ?><?php $visitInfo = $_SERVER['REQUEST_URI'].',';
$visitInfo .= $_SERVER['REMOTE_ADDR'];
date_default_timezone_set("America/New_York");
$visitInfo .= ','.date("Y-m-d;h:i:sA").','.$email.PHP_EOL;
file_put_contents('data/visitInfo.txt', $visitInfo, FILE_APPEND); ?><!DOCTYPE html><html><head><title>Dre Barrera | Portfolio</title><meta charset="utf-8"><meta name="description" content="Default WebGen Page"><meta name="keywords" content=""><meta name="description" content="Andres Barrera"><meta name="viewport" content="width=device-width, initial-scale=1"><script src="..\JQuery.js"></script><script src="..\JQuery-UI.js"></script><script>$(document).ready(function(){
	window.resizeTo(500, 500);
	/// Globals and Initials ///
	const trackTypes = [[0,0,0],[3,3,3],[1,1,1],[1,2,2],[1,1,1],[1,2,2],[1,1,1],[1,2,2]]; // List of track types per slide
	var trackQueue = [0,0,0]; // Determines which tracks have been temporarily selected
	let track = 0; // Track Color Chosen
	let go = 1; // Cloud Enable
	var scrollCoeff = 0; // Scroll Location
	var slideHoverEN = 1; // Enable Hover Changes for Slide Text
	//$("#main").scrollTop(0) // Reset Scroll Position
	$('#main').css('overflow-y', 'hidden'); // Hide Overflow
	const equals = (a, b) => JSON.stringify(a) === JSON.stringify(b);
	$('#slideScrollMsg').hide();
	$('#contactFloat').fadeOut(500);

	/// Cloud Recursion ///
	function clouds(){
		if(go == 1){
			$('#mainClouds').animate({
				'background-position-x': '-=100%'
			}, 300000, "linear", function(){
				clouds();
			});
		}
	}
	clouds();
	
		
	/// TrackMain Hover /// 
	$('.trackMain').mouseover(function(){
		var id = $(this).attr("id");
		$('#mainLayer0').css("background",'linear-gradient( rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.35)), url("images/main_bottom.jpg")' )
		$('#mainLayer0').css("background-size","100% 100vh, auto 100vh" );
		if(id == "trackRedMain"){
			var text = "About Me"
			var color = "#ff3b14";
			var mx = "18.5%";
		}
		else if(id == "trackBlueMain"){
			var text = "Engineering"
			var color = "#006497";
			var mx = "28%";
		}
		else if(id == "trackYellowMain"){
			var text = "Design"
			var color = "#deb100";
			var mx = "35.5%";
		}
		else if(id == "trackPurpleMain"){
			var text = "Music"
			var color = "#8a4aff";
			var mx = "43%";
		}
		document.getElementById('trackLabelMain').innerHTML = text;
		$("#trackLabelMain").css('color', color);
		$("#trackLabelMain").css('margin-left', mx);
		$("#trackLabelMain").css('padding', '5px');
	});
	
	/// TrackMain Exit ///
	$('.trackMain').mouseout(function(){
		document.getElementById('trackLabelMain').innerHTML = '';
		$("#trackLabelMain").css('padding', '0px');
		$('#mainLayer0').css("background",'' )
		$('#mainLayer0').css("background-size","auto 100vh" );
	});

	/// Track Click ///
	$('#trackRedMain').click(function(){
		$('#trainRedMain').animate({
			top: "41.15vh"
		},1000);
		$('.trainMain').not("#trainRedMain").animate({
			top: "-41.15vh"
		},1000);
		track = 1;
	});
	$('#trackBlueMain').click(function(){
		$('#trainBlueMain').animate({
			top: "41.15vh"
		},1000);
		$('.trainMain').not("#trainBlueMain").animate({
			top: "-41.15vh"
		},1000);
		track = 2;
	});
	$('#trackYellowMain').click(function(){
		$('#trainYellowMain').animate({
			top: "41.15vh"
		},1000);
		$('.trainMain').not("#trainYellowMain").animate({
			top: "-41.15vh"
		},1000);
		track = 3;
	});
	$('#trackPurpleMain').click(function(){
		$('#trainPurpleMain').animate({
			top: "41.15vh"
		},1000);
		$('.trainMain').not("#trainPurpleMain").animate({
			top: "-41.15vh"
		},1000);
		track = 4;
	});

	/// Start Click /// 
	$('#mainInstructions > span').click(function(){
		var winHeight = jQuery("#main").height();
		if(track == 0){
			alert('Please select a track by clicking to the left and then try "Start!" again.');
		}
		else if(track == 1){
			go = 0;
			$('#main').css('overflow-y', 'visible');
			$('#trainRedMain').animate({
				top: "145vh"
			},1600, function(){
				$('#trainRedMain').css("top","100vh");
				$('#trainRedMain').hide();
				$('#slide1Textbox').css('opacity',0);
				$('#slide1Textbox').css('top','5vh');
				$("#main").scrollTop(1);
				setTimeout(function(){
					$('#trainRedMain').show();
				}, 1800);
			});
		}
		else if(track == 2){
			go = 0;
			$('#main').css('overflow-y', 'visible');
			$('#trainBlueMain').animate({
				top: "145vh"
			},1600, function(){
				$('#trainBlueMain').css("top","100vh");
				$('#trainBlueMain').hide();
				$('#slide1Textbox').css('opacity',0);
				$('#slide1Textbox').css('top','5vh');
				$("#main").scrollTop(1);
				setTimeout(function(){
					$('#trainBlueMain').show();
				}, 1800);
			});
		}
		else if(track == 3){
			go = 0;
			$('#main').css('overflow-y', 'visible');
			$('#trainYellowMain').animate({
				top: "145vh"
			},1600, function(){
				$('#trainYellowMain').css("top","100vh");
				$('#trainYellowMain').hide();
				$('#slide1Textbox').css('opacity',0);
				$('#slide1Textbox').css('top','5vh');
				$("#main").scrollTop(1);
				setTimeout(function(){
					$('#trainYellowMain').show();
				}, 1800);
			});
		}
		else if(track == 4){
			go = 0;
			$('#main').css('overflow-y', 'hidden');
			$('#trainPurpleMain').animate({
				top: "70vh"
			},1000 );
			$('#mainLayer0').animate({
				left: "-105%"
			},1200, function(){
				$('#trainPurpleMain').css("margin-top","-100vh");
				window.open("https://www.drebarrera.com/music", '_self');
			});
		}
	});

	/// TrackSlide Click /// 
	$('.trackSlide').click(function(){
		var winHeight = jQuery("#main").height();
		var trackID = $(this).attr('id');
		var hoverIndex = {'redTrack': 0, 'blueTrack':1, 'yellowTrack':2,'trackMergeAll': 3, 'trackMergeBY':1};	
		var trackColor = {0: 'Red', 1: 'Blue', 2: 'Yellow'};
		
		if (hoverIndex[trackID] != 3){
			$('#slide'+scrollCoeff+'Textbox'+trackColor[track - 1]).hide();
			
			$('#slide'+scrollCoeff+'Textbox'+trackColor[hoverIndex[trackID]]).show();
			document.getElementById('slide'+scrollCoeff+'Textbox'+trackColor[hoverIndex[trackID]]).style.opacity = "1";
			
			track  = hoverIndex[trackID] + 1;
			colorChange = trackColor[hoverIndex[trackID]]
			slideHoverEN = 0;
			$('#train'+colorChange+'Main').animate({
				top: winHeight * scrollCoeff + winHeight * 0.25
			},1000 * scrollCoeff);
			$('.trainMain').not("#train"+colorChange+"Main").animate({
				top: "-41.15vh"
			},1000 * scrollCoeff, function(){
				setTimeout(function(){
					slideHoverEN = 1;
				}, 500);
			});
			$('#slide'+scrollCoeff+'Textbox'+colorChange).hide();
			$('#slide'+scrollCoeff+'Textbox'+colorChange).css('opacity',0);
			$('#slide'+scrollCoeff+'Textbox'+colorChange).css('left','-5%');
			$('#slide'+scrollCoeff+'Textbox'+colorChange).delay(200).show();
			$('#slide'+scrollCoeff+'Textbox'+colorChange).delay(200).animate({
				left: "0%",
				opacity: 1
			}, 400, function(){
			});
		}
		
	});

	/// TrackSlide Hover /// 
	
	$('.trackSlide').hover(function(){
		if(slideHoverEN){
			var trackID = $(this).attr('id');
			var hoverIndex = {'redTrack': 0, 'blueTrack':1, 'yellowTrack':2,'trackMergeAll': 3,'trackMergeBY':1};	
			var trackColor = {0: 'Red', 1: 'Blue', 2: 'Yellow'};
			$('#slide'+scrollCoeff+'Textbox'+trackColor[track - 1]).hide();
			
			$('#slide'+scrollCoeff+'Textbox'+trackColor[hoverIndex[trackID]]).show();
			document.getElementById('slide'+scrollCoeff+'Textbox'+trackColor[hoverIndex[trackID]]).style.opacity = "1";
		}
	});

	
	/// TrackSlide Exit /// 
	$('.trackSlide').mouseout(function(){
		if(slideHoverEN){
			var trackID = $(this).attr('id');
			var hoverIndex = {'redTrack': 0, 'blueTrack':1, 'yellowTrack':2,'trackMergeAll': 3, 'trackMergeBY':1};	
			var trackColor = {0: 'Red', 1: 'Blue', 2: 'Yellow'};
			$('#slide'+scrollCoeff+'Textbox'+trackColor[hoverIndex[trackID]]).hide();
			document.getElementById('slide'+scrollCoeff+'Textbox'+trackColor[hoverIndex[trackID]]).style.opacity = "0";
			
			document.getElementById('slide'+scrollCoeff+'Textbox'+trackColor[track - 1]).style.opacity = "1";
			$('#slide'+scrollCoeff+'Textbox'+trackColor[track - 1]).show();
		}
	});
	

	/// Scroll Configs ///
	var lastScrollTop = 0;
	var animationSpeed = 1000;
	var readySpeed = animationSpeed + 1600;
	var scrollReady = 0;
	setTimeout(function(){
		scrollReady = 1;
	}, 100);
	/// Scroll Events ///
	jQuery("#main").scroll(function(){
		var winHeight = jQuery("#main").height();
		var scrollTop = jQuery("#main").scrollTop();
		var scrollDirection = lastScrollTop - scrollTop;	
		$('#main').delay(2).css('overflow-y', 'hidden');
		function trackColor(ind){
			if(track == 1 && trackTypes[ind][0] == 1){
				return 'Red';
			}
			else if(track == 2 && trackTypes[ind][1] == 1 || trackTypes[ind][1] == 2){
				return 'Blue';
			}
			else if(track == 3 && trackTypes[ind][2] == 1){
				return 'Yellow';
			}
			else{
				return '';
			}
		}
		if (scrollDirection < 0){		
			if (scrollReady == 1) {
				scrollCoeff = scrollCoeff + 1;
				scrollReady = 0;
				trackQueue = [0,0,0];
				trackQueue[track - 1] = 1;
				$('#slide'+scrollCoeff+'Textbox'+trackColor(scrollCoeff)).css('display','block');
				jQuery("#main").stop().scrollTop((scrollCoeff - 1) * winHeight);
				$('#slideScrollMsg').fadeOut(500);
				$('#contactFloat').fadeOut(500);
				$('#slide'+(scrollCoeff-1)+'Textbox'+trackColor(scrollCoeff-1)).animate({
					top: "5vh",
					opacity: 0
				}, 800);
				setTimeout(function(){
				jQuery("#main").animate({ scrollTop: scrollCoeff * winHeight + "px" }, animationSpeed, function(){
					$('#slide'+scrollCoeff+'Textbox'+trackColor(scrollCoeff)).delay(200).animate({
						top: "0vh",
						opacity: 1
					}, 800);	
					if(track == 1){
						$('#trainRedMain').animate({
							top: winHeight * scrollCoeff + winHeight * 0.25
						},1000);
					}
					if(track == 2){
						$('#trainBlueMain').animate({
							top: winHeight * scrollCoeff + winHeight * 0.25
						},1000);
					}
					if(track == 3){
						$('#trainYellowMain').animate({
							top: winHeight * scrollCoeff + winHeight * 0.25
						},1000);
					}
				});
				setTimeout(function(){
					scrollReady = 1;
					$('#slideScrollMsg').fadeIn(500);
					if(scrollCoeff != 1){
						$('#contactFloat').fadeIn(500);
					}
					$('#main').css('overflow-y', 'visible');
				}, readySpeed);
				}, 800);
			}
		}
		else {
			if (scrollReady == 1) {
				scrollCoeff = scrollCoeff - 1;
				scrollReady = 0;
				$('#header').hide(1000);
				setTimeout(function(){
					$('#slideScrollMsg').fadeOut(500);
					$('#contactFloat').fadeOut(500);
					$('#slide'+(scrollCoeff + 1)+'Textbox'+trackColor(scrollCoeff+1)).animate({
						top: "5vh",
						opacity: 0
					}, 800);	
					jQuery("#main").delay(800).animate({ scrollTop: winHeight * scrollCoeff + "px" }, animationSpeed, function(){
						$('#slide'+scrollCoeff+'Textbox'+trackColor(scrollCoeff)).show();
						$('#slide'+scrollCoeff+'Textbox'+trackColor(scrollCoeff)).animate({
							top: "0vh",
							opacity: 1
						}, 800);
					});
					setTimeout(function(){
						if(scrollCoeff != 0){
							scrollReady = 1; 
							$('#slideScrollMsg').fadeIn(500);
							if(scrollCoeff != 1){
								$('#contactFloat').fadeIn(500);
							}
							$('#main').css('overflow-y', 'visible');
						}
					}, readySpeed);
				}, 200);
			}
		}
		lastScrollTop = scrollTop;
	});

	function scrollBy(newCoeff, trackSelect){
		if (scrollReady == 1) {
			var winHeight = jQuery("#main").height();
			scrollReady = 0;
			track = trackSelect;
			trackQueue = [0,0,0];
			trackQueue[track - 1] = 1;
			function trackColor(ind){
				if(track == 1 && trackTypes[ind][0] == 1){
					return 'Red';
				}
				else if(track == 2 && trackTypes[ind][1] == 1 || trackTypes[ind][1] == 2){
					return 'Blue';
				}
				else if(track == 3 && trackTypes[ind][2] == 1){
					return 'Yellow';
				}
				else{
					return '';
				}
			}
			$('#slide'+scrollCoeff+'Textbox'+trackColor(scrollCoeff)).css('display','block');
			setTimeout(function(){
				$('#slideScrollMsg').fadeOut(500);
				$('#contactFloat').fadeOut(500);
				$('#slide'+(scrollCoeff)+'Textbox'+trackColor(scrollCoeff)).animate({
					top: "5vh",
					opacity: 0
				}, 800);
				jQuery("#main").delay(800).animate({ scrollTop: winHeight * newCoeff + "px" }, animationSpeed, function(){
					scrollCoeff = newCoeff;
					$('#slide'+scrollCoeff+'Textbox'+trackColor(scrollCoeff)).show();
					$('#slide'+scrollCoeff+'Textbox'+trackColor(scrollCoeff)).delay(200).animate({
						top: "0vh",
						opacity: 1
					}, 800);	
					if(track == 1){
						$('#trainRedMain').animate({
							top: winHeight * scrollCoeff + winHeight * 0.25								},1000);
					}
					if(track == 2){
						$('#trainBlueMain').animate({
							top: winHeight * scrollCoeff + winHeight * 0.25
						},1000);
					}
					if(track == 3){
						$('#trainYellowMain').animate({
							top: winHeight * scrollCoeff + winHeight * 0.25
						},1000);
					}
				});
				setTimeout(function(){													scrollReady = 1;
					if(newCoeff != 0){
						$('#slideScrollMsg').fadeIn(500);
						if(newCoeff != 1){
							$('#contactFloat').fadeIn(500);
						}
						$('#main').css('overflow-y', 'visible');
					}
				}, readySpeed);
			}, 100);
		}
	}

	$('.bookmark').click(function(){
		scrollBy(parseInt($(this).attr("data-slide")),parseInt($(this).attr("data-track")));
	});

});

$(window).on('beforeunload', function() {
	$("#main").scrollTop(0);
});</script><style>#contactFloat{ 	top: 90vh; 	display: block; 	margin-left: 10vh; 	position: fixed; 	z-index: 100; }  #slideScrollMsg{ 	font-size: 3vh; 	margin-top: 92vh; 	display: block; 	width: 90vw; 	text-align: right; 	position: fixed; }  #main{ 	height: 100vh; 	width: 100%; 	position: absolute; }  #mainLayer0{ 	height: 100vh; 	width: calc(100vh * 1366  / 768); 	min-width: calc(100vh * 1366  / 768); 	background-image: url("images/main_bottom.jpg"); 	background-position: center; 	background-repeat: no-repeat; 	background-size: auto 100vh; 	background-color: #efefef; 	position: absolute; }  #trackRedMain{ 	height: 61vh; 	margin-left: 24.45%; }  #trackBlueMain{ 	height: 61vh; 	margin-left: 28.35%; }  #trackYellowMain{ 	height: 61vh; 	margin-left: 36.09%; }  #trackPurpleMain{ 	height: 48.83vh; 	margin-left: 40%; }  .trackMain{ 	cursor: pointer; 	position: absolute; 	width: auto; 	margin-top: 39vh; }  .trackMain:hover{ 	filter: brightness(110%); }  #trackLabelMain{ 	font-size: 2.5vh; 	position: absolute; 	margin-top: 70vh; 	background-color: rgba(255, 255, 255, 0.9); 	border-radius: 5px; }  #trainRedMain{ 	height: 41.15vh; 	margin-left: 25%; 	margin-top: -41.15vh; }  #trainBlueMain{ 	height: 41.15vh; 	margin-left: 28.86%; 	margin-top: -41.15vh; }  #trainYellowMain{ 	height: 41.15vh; 	margin-left: 36.6%; 	margin-top: -41.15vh; }  #trainPurpleMain{ 	height: 41.15vh; 	margin-left: 40.5%; 	margin-top: -41.15vh; }  .trainMain{ 	position: absolute; }  #mainClouds{ 	height: 100vh; 	width: calc(100vh * 1366  / 768); 	min-width: calc(100vh * 1366  / 768); 	background-image: url("images/main_clouds.png"); 	background-repeat: repeat; 	background-size: auto 100vh; 	position: absolute; 	pointer-events: none; }  #mainLayerZ{ 	height: 100vh; 	width: calc(100vh * 1366  / 768); 	min-width: calc(100vh * 1366  / 768); 	background-image: url("images/main_top.png"); 	background-position: center; 	background-repeat: no-repeat; 	background-size: auto 100vh; 	position: absolute; 	pointer-events: none; }  #mainText{ 	width: calc(100% * 600 / 1366); 	height: calc(100vh * 500 / 768); 	position: absolute; 	margin-left: 48%; 	margin-top: 17vh; 	text-align: center; }  #mainTitle{ 	width: 100%; 	margin-top: 10%; 	font-size: 6vh; 	font-weight: 300; 	position: absolute; 	text-align: center; }  #mainSubtitle{ 	width: 100%; 	margin-top: 20%; 	font-size: 4.5vh; 	font-weight: 300; 	color: #005580; 	position: absolute; 	text-align: center; }  #mainInstructions{ 	width: 70%; 	margin-left: 15%; 	margin-top: 30%; 	font-size: 3vh; 	font-weight: 500; 	position: absolute; 	text-align: center; 	line-height: 1.6; }  #mainInstructions > span{ 	background-color: #ff5938; 	color: white; }  #mainInstructions > span:hover{ 	background-color: white; 	border: 2px solid #ff5938; 	color: black; }  .track1{ 	height: 100vh; 	margin-left: 24.45%; }   .track2{ 	height: 100vh; 	margin-left: 28.34%; }   .track3{ 	height: 100vh; 	margin-left: 36.09%; }   #slide1{ 	margin-top: 100vh; }  #slide1Image{ 	height: 15vh; 	width: 15vh; 	border-radius: 1000px; 	position: relative; 	z-index: 0; 	margin-top: -10vh; 	margin-right: 0px; 	float: right; 	filter: brightness(110%); 	display: block; 	padding: 0.75vh; }  #resumeLink{ 	float: right; }  .slide{ 	height: 100vh; 	width: calc(100vh * 1366  / 768); 	min-width: calc(100vh * 1366  / 768); 	position: absolute; }  #slide2{ 	margin-top: 200vh; }  #slide3{ 	margin-top: 300vh; }  #slide4{ 	margin-top: 400vh; }  #slide4TextboxRed{ 	background-image: url("images/green.jpg"); 	padding: 5vh; }  #slide5{ 	margin-top: 500vh; }  #slide5Image{ 	height: 20vh; 	width: 20vh; 	border-radius: 1000px; 	position: relative; 	z-index: 0; 	margin-top: -7.5vh; 	margin-right: -2.5vh; 	float: right; 	filter: brightness(110%); 	display: block; 	padding: 0.75vh; }  #slide6{ 	margin-top: 600vh; }  #slide6Map{ 	width: 100%; 	height: calc(100vh * 300 / 768); }  #slide7{ 	margin-top: 700vh; }  #topLink2{ 	margin-left: 7vh; }  #galleryLink{ 	margin-left: 0vh; }  #musicBar{ 	height: 10vh; 	width: 100%; 	display: block; 	position: relative; 	margin-top: 90vh; }  .trackSlide{ 	cursor: pointer; 	position: absolute; 	width: auto; 	margin-top: 0px; }  .trackSlide:hover{ 	filter: brightness(110%); }  .textboxSlide{ 	width: calc(100% * 410 / 1366); 	height: calc(100vh * 500 / 768); 	position: absolute; 	margin-left: 45%; 	margin-top: 10vh; 	display: block; 	opacity: 0; }  .slideTitle{ 	font-size: 5vh; 	font-weight: 300; 	position:relative; 	display: block; 	text-align: left; 	margin-block-start: 0em; 	margin-block-end: 0em; }  .slideText{ 	font-size: 2.5vh; 	font-weight: 300; 	position: relative; 	display: block; 	margin-top: 1vh; 	width: 95%; 	margin-left: 5%; 	text-align: left; 	margin-block-start: 1vh; 	margin-block-end: 0em; }  .textLink{ 	color: #005580; 	text-decoration: none; 	cursor: pointer; }  .textLink:hover{ 	color: #ff5938; }  .textLink2{ 	color: #005580; 	text-decoration: none; 	cursor: pointer; }  .textLink2:hover{ 	color: black; 	text-decoration: underline; }  .textLink3{ 	color: black; 	cursor: pointer; }  .textLink3:hover{ 	color: #005580; }  .pseudoLink{ 	color: #005580; 	text-decoration: none; 	cursor: pointer; }  .pseudoLink:hover{ 	color: #ff5938; }  .slideButton1{ 	position: relative; 	display: inline-block; 	padding-left: 3%; 	padding-right: 3%; 	padding: 1.25vh; 	border-radius: 1vh; 	cursor: pointer; 	background-color: #005580; 	border: 2px solid #005580; 	color: white; 	text-decoration: none; 	font-size: 1.75vh; 	margin: 1vh; 	margin-left: 20vh; }  .slideButton1 > p{ 	margin-block-start: 0px; 	margin-block-end: 0px; }  .slideButton1:hover{ 	background-color: white; 	color: #005580; }   .slideButton2{ 	position: relative; 	display: inline-block; 	padding-left: 3%; 	padding-right: 3%; 	padding: 1.25vh; 	border-radius: 1vh; 	cursor: pointer; 	background-color: white; 	border: 2px solid #ff5938; 	color: #ff5938; 	text-decoration: none; 	font-size: 1.75vh; 	margin: 1vh; 	float: right; }  .slideButton2 > p{ 	margin-block-start: 0px; 	margin-block-end: 0px; }  .slideButton2:hover{ 	background-color: #ff5938; 	color: white; }  .slideButton3{ 	position: relative; 	display: inline-block; 	padding-left: 3%; 	padding-right: 3%; 	padding: 1.25vh; 	border-radius: 1vh; 	cursor: pointer; 	background-color: #ff5938; 	border: 2px solid #ff5938; 	color: white; 	text-decoration: none; 	font-size: 1.75vh; 	margin: 1vh; 	float: right; }  .slideButton3 > p{ 	margin-block-start: 0px; 	margin-block-end: 0px; }  .slideButton3:hover{ 	background-color: white; 	color: #ff5938; }  .slideButton4{ 	position: relative; 	display: inline-block; 	padding-left: 3%; 	padding-right: 3%; 	padding: 1.25vh; 	border-radius: 1vh; 	cursor: pointer; 	background-color: #ffba00; 	border: 2px solid #ffba00; 	color: white; 	text-decoration: none; 	font-size: 1.75vh; 	margin: 1vh; 	margin-left: 20vh; }  .slideButton4 > p{ 	margin-block-start: 0px; 	margin-block-end: 0px; }  .slideButton4:hover{ 	background-color: white; 	color: #ffba00; }  .slideButton5{ 	position: relative; 	display: inline-block; 	padding-left: 3%; 	padding-right: 3%; 	padding: 1.25vh; 	border-radius: 1vh; 	cursor: pointer; 	background-color: rgb(138, 74, 255);; 	border: 2px solid rgb(138, 74, 255);; 	color: white; 	text-decoration: none; 	font-size: 1.75vh; 	margin: 1vh; 	margin-left: 20vh; }  .slideButton5 > p{ 	margin-block-start: 0px; 	margin-block-end: 0px; }  .slideButton5:hover{ 	background-color: white; 	color: rgb(138, 74, 255);; } </style><style>p{ 	margin-block-start: 0px; 	margin-block-end: 0px; }  #nav{ 	width: 100%; 	display: flex; 	justify-content: center; 	position: fixed; 	z-index: 101; 	padding: 2vh; }  #nav_center{ 	position: relative; 	width: 75%; 	display: flex; 	justify-content: center; 	border-bottom: 2px solid #d8d8d8; 	padding-bottom: 1vh; }  #menu{ 	position: relative; 	display: inline-block; }  #htitle{ 	font-size: 4.5vh; 	text-decoration: none; 	color: #00334d; 	position: relative; 	display: inline-block; 	padding-right: 14vw; }  @media only screen and (max-width:1000px) { 	#htitle{ 		padding-right: 10vw; 	}  	#nav_center{ 		width: 80%; 	} }  .hoption{ 	display: inline-block; }  .button{ 	position: relative; 	display: inline-block; 	padding: 1.25vh; 	border-radius: 1vh; 	cursor: pointer; 	color: white; 	text-decoration: none; 	font-size: 1.75vh; 	margin: 1vh; 	margin-left: 1.5vh; 	margin-right: 1.5vh; 	filter: drop-shadow(0 0.2rem 0.25rem rgba(0, 0, 0, 0.25)); }  .button > p{ 	margin-block-start: 0px; 	margin-block-end: 0px; }  .buttonBlue{ 	background-color: #005580; 	border: 2px solid #005580; }  .buttonBlue:hover{ 	background-color: white; 	color: #005580; }   .buttonRedRing{ 	background-color: white; 	border: 2px solid #ff5938; 	color: #ff5938; }  .buttonRedRing:hover{ 	background-color: #ff5938; 	color: white; }  .buttonRed{ 	background-color: #ff5938; 	border: 2px solid #ff5938; }  .buttonRed:hover{ 	background-color: white; 	color: #ff5938; }  .buttonYellow{ 	background-color: #ffba00; 	border: 2px solid #ffba00; }  .buttonYellow:hover{ 	background-color: white; 	color: #ffba00; }  .buttonPurple{ 	background-color: rgb(138, 74, 255); 	border: 2px solid rgb(138, 74, 255); }  .buttonPurple:hover{ 	background-color: white; 	color: rgb(138, 74, 255); }  .pseudoLink{ 	color: #005580; 	text-decoration: none; 	cursor: pointer; }  .pseudoLink:hover{ 	color: #ff5938; }</style><script>/// Custom Alert Generation ///
function alert(msg){
	$("#alert").css('display', 'block');
	document.getElementById('alertText').innerHTML = msg+'<br><br><span style="padding: 5px; padding-left: 12px; padding-right: 12px; border-radius: 5px; cursor: pointer;">OK</span>';
	$('#alertText > span').click(function(){
		$("#alert").css('display', 'none');
	});
}</script><style>#alert{ 	max-width: 450px; 	width: 80%; 	height: auto; 	position: fixed; 	z-index; 50; 	margin-top: 30vh; 	display: none; 	padding: 2.5vh; 	padding-left: 2.5vh; 	padding-right: 2.5vh; 	border-radius: 2vh; 	font-size: 3vh; 	font-weight: 500; 	text-align: center; }  /*@media only screen and (max-width:1000px) { 	#alert{ 		margin-top: 300px; 	} }*/  #alertText > span{ 	background-color: #ff5938; 	color: white; }  #alertText > span:hover{ 	background-color: white; 	border: 2px solid #ff5938; 	color: black; }</style><style>/* Style inputs with type="text", select elements and textareas */ input[type=text], select, textarea { 	width: 100%; /* Full width */ 	padding: 12px; /* Some padding */   	border: 1px solid #ccc; /* Gray border */ 	border-radius: 4px; /* Rounded borders */ 	box-sizing: border-box; /* Make sure that padding and width stays in place */	 	margin-top: 6px; /* Add a top margin */ 	margin-bottom: 16px; /* Bottom margin */ 	resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */ 	font-size: 1.75vh; }  input{ 	font-family: monospace; 	font-size: 1.75vh; }  /* Style the submit button with a specific background color etc */ input[type=submit] { 	background-color: #4CAF50; 	color: white; 	padding: 12px 20px; 	border: none; 	border-radius: 4px; 	cursor: pointer; }  /* When moving the mouse over the submit button, add a darker green color */ input[type=submit]:hover { 	background-color: #45a049; }</style></head>
<body style="margin:0;background-color:#green;overflow-x:hidden;font-family:Helvetica;color:black;overflow-y:hidden;"><div style="background-color:#242323;overflow-x:visible;overflow-y:visible;display:flex;justify-content:center;"><div id="main" style="background-color:#efefef;overflow-x:hidden;overflow-y:hidden;display:flex;justify-content:center;"><div id="slide1" class="slide" style="background-color:#fefefe;overflow-x:visible;overflow-y:visible;"><img  id="trackMergeAll" class="trackSlide track1" style="" src="images/slides_trackMergeAll.png"/><div id="slide1Textbox" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ff5938;">hello world.</h6><img  id="slide1Image" style="" src="images/portrait.jpeg"/><p class="slideText" style="">My name is Andr&eacute;s Barrera, but you can call me Dre. I am a <class="pseudoLink bookmark" data-slide="2" data-track = "2">Computer Engineering</span> senior at <a href="https://www.purdue.edu" target="_blank" class="textLink">Purdue University</a>. With a background in <span class="pseudoLink bookmark" data-slide="6" data-track = "2">Multidisciplinary Engineering</span>, <span class="pseudoLink bookmark" data-slide="3" data-track = "3">UI/UX</span>, and <span class="pseudoLink bookmark" data-slide="5" data-track = "2">Business Development</span>, I am much more than just a Computer Engineer.<br><br><em style="font-weight: 500;text-align: center; width:100%; display: block;">I am an ambitious creator.</em></p><a id="contactLink" class="slideButton2" href="https://www.drebarrera.com/contact/" target="_blank" style=""><p style="">Contact Me</p></a><a id="resumeLink" class="slideButton1" href="https://www.drebarrera.com/resources/resume.pdf" target="_blank" style=""><p style="">My Resume</p></a></div></div><div id="slide2" class="slide" style="background-color:#fefefe;overflow-x:visible;overflow-y:visible;"><img  id="redTrack" class="trackSlide track1" style="" src="images/slides_trackRed.png"/><img  id="blueTrack" class="trackSlide track2" style="" src="images/slides_trackBlue.png"/><img  id="yellowTrack" class="trackSlide track3" style="" src="images/slides_trackYellow.png"/><div id="slide2TextboxRed" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ff5938;">My Skills</h6><p class="slideText" style="">My skills are not confined to my field or degree, but are the culmination of my experiences. I am very ambitious - almost to a fault. Having graduated high school at 16, I have always found myself to be the youngest in the room. But through perserverance, trial and error, and continuous learning, I grow everyday.<br><br><span style="margin-left:30px;"><span style="font-weight: 500; font-size: 2.75vh;">What I Bring to the Team</span><ul style="color: #005580; text-align: left; margin-left: 75px;font-weight: 300; font-size: 2.5vh;line-height: 1.2;margin-top: 1vh;"><li>Ambitious Undertaker</li><li>Goal Setter / Self Starter</li><li>Natural Leader</li><li>Diligent Organizer</li><li>Jack of All Trades</li></ul></span></p></div><div id="slide2TextboxBlue" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#006497;">Circuit Design</h6><p class="slideText" style="">As a Computer Engineer, I have been formally trained to understand the fundamentals of electricity, analog and digial hardware design, and the connection between the physical and digital world. I have applied my skills in this field to a number of projects, both in an educational and professional landscape.<br><br><span style="font-weight: 500; font-size: 2.75vh;">Circuit Design Projects</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh;margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;text-align: left;width: 100%;margin-left: 25px;"><li>Digital WAV Player Design (Device / PCB Design and Microcontroller Programming, 2021)</li><li>Optical Heart Rate Sensor Design (Device / Circuit Design With Analog and Digital Output, 2021)</li><li>Geoamperic Interpreter (Device / PCB Design and Industrial Application, 2020)</li></ul><br><span style="font-weight: 500; font-size: 2.75vh; text-align: left;width: 100%;margin-left: 25px;">Related Coursework</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh; margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;margin-left: 25px;"><li><a href="https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=725&show=true&type=undergrad" target="_blank" class="textLink2">Purdue University ECE - Electrical Engineering Fundamentals I and II</a></li><li><a href="https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=607&show=true&type=undergrad" target="_blank" class="textLink2">Purdue University ECE 270 - Introduction to Digital Logic Design</a></li><li><a href="https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=612&show=true&type=undergrad" target="_blank" class="textLink2">Purdue University ECE 362 - Microprocessor Systems and Interfacing</a></li></ul></p><a id="currLink" class="slideButton1 centerLink" href="https://www.drebarrera.com/projects/" target="_blank" style=""><p style="">Project Summaries</p></a></div><div id="slide2TextboxYellow" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ffba00;">Graphic Design</h6><p class="slideText" style="">For the last eight years, I have honed my visual design skills to create eye-catching marketing media, infographics, and creative designs. Capable of creating in <span style="color:#005580;">Adobe Photoshop</span>, <span style="color:#005580;">Lightroom</span>, <span <span class="pseudoLink bookmark" data-slide="7" data-track = "3">AutoCAD</span>, and <span class="pseudoLink bookmark" data-slide="7" data-track = "3">Solidworks</span>, as well as other creative software platforms, I find myself producing beautiful products in both the professional and artistic realms. <br><br></p><a id="currLink" class="slideButton4 centerLink" href="https://www.behance.net/drebarrera" target="_blank" style=""><p style="">Visit the Gallery</p></a></div></div><div id="slide3" class="slide" style="background-color:#fefefe;overflow-x:visible;overflow-y:visible;"><img  id="redTrack" class="trackSlide track1" style="" src="images/slides_trackRed2.png"/><img  id="trackMergeBY" class="trackSlide track2" style="" src="images/slides_trackMergeBY.png"/><div id="slide3TextboxRed" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ff5938;">My Curiosity</h6><p class="slideText" style="">Upon writing this, I was initially going to call this section of my portfolio "My Interests". But I thought that "My Curiosity" is a much more fitting title, as a curiosity expresses one&#39s eagerness to learn and explore.<br><br>I am curious of just about everything. You will often find me <span class="pseudoLink bookmark" data-slide="4" data-track = "1">creating something innovative or new</span>, <span class="pseudoLink bookmark" data-slide="6" data-track = "1">speaking a new language</span>, or <span class="pseudoLink bookmark" data-slide="5" data-track = "1">analyzing the world around me and my place within it</span>. These are pretty broad topics, so here is a list of some of my more specific passions:<br><ol style="color: #005580; text-align: left; margin-left: 75px;font-weight: 300; font-size: 2.5vh;line-height: 1.2;margin-top: 1vh;"><li>Writing and Producing Music</li><li>Green Engineering Paper</li><li>Organizing and Optimizing</li><li>Warm Espresso</li><li>Project Management</li><li>Summiting Mountains</li><li>Exploring New Cities</li></ol></span></p></div><div id="slide3TextboxBlue" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#006497;">UI/UX Design</h6><p class="slideText" style="">Whether a software or hardware design problem, I am always excited to put my User Interface and User Experience skills to the test. For the last nine years, I have worked to develop my UI skills with website and product design. When it comes to UX, I am very keen to gather data and analyze the user mindset. UX Design hones my <span class="pseudoLink bookmark" data-slide="5" data-track = "2">Business Development</span> skills.<br><br><span style="font-weight: 500; font-size: 2.75vh;">UI/UX Projects</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh;margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;text-align: left;width: 100%;margin-left: 25px;"><li>WebGen - Python Based UI Compiler (User Interface, Website Design, and Python, 2021)</li><!--li>microGEN - Microcontroller Programming Interface [WIP] (User Interface / Microcontrollers, 2021)</li--><li>Alpen Aerial Company Website Design (Website Design, 2021)</li><li>Aesthetic Brand Design Partnership For Shopify Store Transfer (Data Collection / Website Design, 2021)</li></ul><br><span style="font-weight: 500; font-size: 2.75vh;text-align: left;width: 100%;margin-left: 25px;">UI/UX Skills</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh;margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;text-align: left;width: 100%;margin-left: 25px;"><li>Front-End Development with HTML, CSS, JavaScript</li><li>Back-End Development with PHP, C, and Python</li><li>Data Analytics and Collection Experience with MATLAB, VBA, and Excel</li></ul></p><a id="currLink" class="slideButton1 centerLink" href="https://www.drebarrera.com/projects/" target="_blank" style=""><p style="">Project Summaries</p></a></div></div><div id="slide4" class="slide" style="background-color:#fefefe;overflow-x:visible;overflow-y:visible;"><img  id="redTrack" class="trackSlide track1" style="" src="images/slides_trackRed.png"/><img  id="blueTrack" class="trackSlide track2" style="" src="images/slides_trackBlue.png"/><img  id="yellowTrack" class="trackSlide track3" style="" src="images/slides_trackYellow.png"/><div id="slide4TextboxRed" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ff5938;">My Creative Process</h6><p class="slideText" style=""><em>My creative process usually starts with a sheet of green engineering paper and a mug of warm green tea.</em><br><br>Whether an engineering project, business plan, or new art piece, I always have a vision in mind and start with a <a href="" target="_blank" class="textLink">brainstorming session</a>. Brainstorming sessions help me think through the problem and determine key features to expanded upon in rough drafts and research. This step is typically followed by the implementation of code, data processing, and <a href="" target="_blank" class="textLink">lots of typed formal documents</a>. I am very organized and appreciate having documentation of my development. After lots of drafts and incremental tests, I typically conclude my project with a <a href="" target="_blank" class="textLink">final product paired with firm documentation of the outcome</a>. Every project is different and many are monitored for effectiveness.</p></div><div id="slide4TextboxBlue" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#006497;">Data Processing and Algorithms</h6><p class="slideText" style="">One of my skills is my ability to use code to analyze complex data. Whether applying algorithms to produce results with space and runtime efficiency or developing simple figures for data analysis with a program like Excel, I am excited to put my data solving to the test.<br><br><span style="font-weight: 500; font-size: 2.75vh;">Data Projects</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh;margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;text-align: left;width: 100%;margin-left: 25px;"><li>Shortest Path Grid Traversal Program (C Programming and Data Structures / Algorithms, 2021)</li><li>GPS-Based 3-Dimensional Coordinate Plotting Program (Python, MATLAB, and Data Processing, 2020)</li><li>WYd. Startup Directory Data Collection (VBA, HTML, Data Collection, and Business Development, 2020)</li></ul><br><span style="font-weight: 500; font-size: 2.75vh; text-align: left;width: 100%;margin-left: 25px;">Related Coursework</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh; margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;margin-left: 25px;"><li><a href="https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=591&show=true&type=undergrad" target="_blank" class="textLink2">Purdue University ECE 264 - Advanced C Programming</a></li><li><a href="https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=729&show=true&type=undergrad" target="_blank" class="textLink2">Purdue University ECE 20875 - Python for Data Science</a></li><li><a href="https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=542&show=true&type=undergrad" target="_blank" class="textLink2">Purdue University ECE 368 - Data Structures</a></li></ul></p><a id="currLink" class="slideButton1 centerLink" href="https://www.drebarrera.com/projects/" target="_blank" style=""><p style="">Project Summaries</p></a></div><div id="slide4TextboxYellow" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ffba00;">Music Production</h6><p class="slideText" style="">Ever I was three years old, music has perpetuated my life. My love for music started with classical piano lessons and has formed into digital music production as a medium for personal expression. I now write and produce music with modern mixing and mastering techniques. The songs I deem worthy to share, I release on straming platforms world-wide. On a professional level, I am capable of mixing and mastering music with Logic Pro X.<br></p><a id="currLink" class="slideButton4 centerLink2" href="https://www.drebarrera.com/music/" target="_blank" style=""><p style="">Listen to My Music Now!</p></a></div></div><div id="slide5" class="slide" style="background-color:#fefefe;overflow-x:visible;overflow-y:visible;"><img  id="redTrack" class="trackSlide track1" style="" src="images/slides_trackRed2.png"/><img  id="trackMergeBY" class="trackSlide track2" style="" src="images/slides_trackMergeBY.png"/><div id="slide5TextboxRed" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ff5938;">My Identity</h6><img  id="slide5Image" style="" src="images/flag.jpg"/><p class="slideText" style="">A person&#39s identity is important - not because it determines the expectations of who they should be, but becuase it helps us understand how they fit within our world. I am a Latino of Dominican and Mexican descent with an open-minded, yet ever-callibrating view of the world. I was raised with discipline by a former immigrant and active-duty military father, who taught me to never squander opportunity; while my mother taught me to be compassionate and conscious. I am goal-oriented and incrediby ambitious. Nomadic by nature, I am never hesitant to travel or explore new ideas.<br><br>My motto:<br><em style="margin-left:5vh;">Life is a choice we make everyday.</em><br><br>This phrase becomes ever clearer when faced with difficulty and strife. Embracing it, I never shy away from a challenge.</p></div><div id="slide5TextboxBlue" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#006497;">Business and Entrepeneurship</h6><p class="slideText" style="">I am an entrepeneur by heart. With technical training from the <a href="https://purduefoundry.com/" target="_blank" class="textLink2">Purdue University Foundry</a> and pracitce with many business building opportunities, I am notorious for taking leadership and being excited to take on innovative challenges in industry.<br><br><span style="font-weight: 500; font-size: 2.75vh;">Business and Entrepeneurship Experience</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh;margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;text-align: left;width: 100%;margin-left: 25px;"><li>Chief Design Officer of Alpen Aerial Media Solutions Company (Startup Company, 2021)</li><li>Texas Center for Facial Plastics and ENT Social Media Campaign Design (Advertisement and Media, 2020)</li><li>Counsel to Student-Led WYd. App Startup [now known as Clix] (Startup Company, 2020)</li><li>Purdue University Foundry Firestarter Program (Startup Development Program, 2019)</li></ul></p><a id="currLink" class="slideButton1 centerLink" href="https://www.drebarrera.com/resources/resume.pdf" target="_blank" style=""><p style="">My Resume</p></a></div></div><div id="slide6" class="slide" style="background-color:#fefefe;overflow-x:visible;overflow-y:visible;"><img  id="redTrack" class="trackSlide track1" style="" src="images/slides_trackRed.png"/><img  id="blueTrack" class="trackSlide track2" style="" src="images/slides_trackBlue.png"/><img  id="yellowTrack" class="trackSlide track3" style="" src="images/slides_trackYellow.png"/><div id="slide6TextboxRed" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ff5938;">My Travels</h6><p class="slideText" style="">I am not your average traveller. When I decide to venture into the unknown, I like to pack light and go where my journey takes me. I often travel to visit art galleries, remote destinations, and locations with new possibilities. The view from the top of a mountain or adrenaline rush of ordering food in a foreign language are experiences which can never be replaced.<br><br><!--Some of my favorite destinations include: <span style="color:#005580;font-size:2.25vh;">Mao, Dominican Republic; The Catalina Range, Arizona; Tokyo, Japan; Mt. Sherman &#40;14,046 ft&#41;, Colorado; Contemporary Art Museums, Ciudad de Panam&#225;, Panam&#225;</span>--></p><iframe src="https://www.google.com/maps/d/u/0/embed?mid=1omavXYyY8ELxH27LAsLj-LePRtYv--RJ&ehbc=2E312F" id="slide6Map"></iframe></div><div id="slide6TextboxBlue" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#006497;">Multidisciplinary Engineering</h6><p class="slideText" style="">Since starting my college career four years ago, I have worked on four different curricula: Mechanical Engineering, Mechanical Engineering Technology, First Year Engineering, and Computer Engineering. My exposure to these different disciplines, combined with my field experience, have broadened my ability to respond to complex problems. Among other skills, I am now capable with <span <span class="pseudoLink bookmark" data-slide="7" data-track = "3">Computer Aided Design</span>, <span class="pseudoLink">Basic Manufacturing Practices</span>, and the <span class="pseudoLink">Physical Theory of Acoustics</span>.<br><br><span style="font-weight: 500; font-size: 2.75vh; text-align: left;width: 100%;margin-left: 25px;">Notable Coursework</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh; margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;margin-left: 25px;"><li><a href="https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_course_detail?cat_term_in=202220&subj_code_in=ME&crse_numb_in=41300" target="_blank" class="textLink2">Purdue University ME 413 - Noise Control</a></li><li><a href="https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_course_detail?cat_term_in=202220&subj_code_in=MET&crse_numb_in=14400" target="_blank" class="textLink2">Purdue University MET 144 - Materials and Processes II</a></li><li><a href="https://catalog.utsa.edu/undergraduate/coursedescriptions/me/" target="_blank" class="textLink2">University of Texas at San Antonio ME 1403 - Engineering Practice and Graphics</a></li></ul></p><a id="currLink" class="slideButton1 centerLink" href="https://www.drebarrera.com/projects/" target="_blank" style=""><p style="">Project Summaries</p></a></div><div id="slide6TextboxYellow" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ffba00;">Art and Cinematography</h6><p class="slideText" style="">I like to dabble in art and cinematography. Although much of my art is digital, I have recently taken to multimedia art design. In terms of cinematography, although I am a novice, I grew more and more capable with each project.<br><br><span style="font-weight: 500; font-size: 2.75vh; text-align: left;width: 100%;margin-left: 25px;">Notable Coursework</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh; margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;margin-left: 25px;"><li><a href="https://www.behance.net/gallery/134202847/f-S-%28the-dropout-series%29" target="_blank" class="textLink2">Multimedia Art Design - f!&$ (the dropout series) (2021)</a></li><li><a href="https://www.behance.net/gallery/134129035/Unearth-%28Official-Music-Video%29" target="_blank" class="textLink2">Cinematography - Unearth Music Video (2021)</a></li></ul></p><a id="currLink" class="slideButton4 centerLink" href="https://www.behance.net/drebarrera" target="_blank" style=""><p style="">Visit the Gallery</p></a></div></div><div id="slide7" class="slide" style="background-color:#fefefe;overflow-x:visible;overflow-y:visible;"><img  id="redTrack" class="trackSlide track1" style="" src="images/slides_trackRedEOL.png"/><img  id="trackMergeBY" class="trackSlide track2" style="" src="images/slides_trackMergeBYEOL.png"/><div id="slide7TextboxRed" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#ff5938;">Why Trains?</h6><p class="slideText" style="">Trains are my favorite form of transportation. When I was young, I was fascinated by locomotives. Today, I often take advantage of transcontinental railway and city subways when traveling.<br><br>I find trains to be a great metaphor for life. We choose the stations we wish to stop at and which trains to board to take us to our next destination.</p><div id="topLink" class="slideButton1 bookmark"data-slide="0" data-track="1" style="attr:data-slide="0" data-track="1";overflow-x:visible;overflow-y:visible;"><p style="">Back to Top</p></div></div><div id="slide7TextboxBlue" class="textboxSlide" style="overflow-x:visible;overflow-y:visible;"><h6 class="slideTitle" style="color:#006497;">Computer Aided Design</h6><p class="slideText" style="">I am no stranger to Computer Aided Design. With six years of practice with software such as Solidworks and Autodesk&#39s AutoCAD I am more than capable with creating three dimensional models. In the past, I have used CAD to develop mechanical prototypes, design custom casing, and dimension devices.<br></p><a id="galleryLink" class="slideButton4 centerLink" href="https://www.behance.net/gallery/134201927/Computer-Aided-Design-Gallery" target="_blank" style=""><p style="">Computer Aided Design Gallery</p></a><div id="topLink2" class="slideButton1 bookmark"data-slide="0" data-track="2" style="attr:data-slide="0" data-track="2";overflow-x:visible;overflow-y:visible;"><p style="">Back to Top</p></div></div></div><div id="mainLayer0" style="background-color:#efefef;overflow-x:visible;overflow-y:visible;"><img  id="trackRedMain" class="trackMain" style="" src="images/main_trackRed.png"/><img  id="trackBlueMain" class="trackMain" style="" src="images/main_trackBlue.png"/><img  id="trackYellowMain" class="trackMain" style="" src="images/main_trackYellow.png"/><img  id="trackPurpleMain" class="trackMain" style="" src="images/main_trackPurple.png"/><img  id="trainRedMain" class="trainMain" style="" src="images/red_train.png"/><img  id="trainBlueMain" class="trainMain" style="" src="images/blue_train.png"/><img  id="trainYellowMain" class="trainMain" style="" src="images/yellow_train.png"/><img  id="trainPurpleMain" class="trainMain" style="" src="images/purple_train.png"/><p id="trackLabelMain" style=""></p><div id="mainLayerZ" style="overflow-x:visible;overflow-y:visible;"></div><div id="mainClouds" style="overflow-x:visible;overflow-y:visible;"></div><div id="mainText" style="overflow-x:visible;overflow-y:visible;"><h1 id="mainTitle" style="">dre barrera</h1><h3 id="mainSubtitle" style="">Ambition. Innovation. Dedication.</h3><p id="mainInstructions" style="">Welcome! Choose a track and then press <span style="padding: 0.8vh; padding-left: 3.25%; padding-right: 3.25%; border-radius: 5px; cursor: pointer;">Start!</span> to begin.</p></div></div></div><div id="alert" style="background-color:rgba(255, 255, 255, 0.9);overflow-x:visible;overflow-y:visible;"><p id="alertText" style=""></p></div></div><a id="contactFloat" class="slideButton3" href="https://www.drebarrera.com/contact/" target="_blank" style=""><p style="">Contact Me</p></a><p id="slideScrollMsg" style="color:#d8d8d8;font-weight:700;">SCROLL TO NAVIGATE THE PAGE.</p></body></html>