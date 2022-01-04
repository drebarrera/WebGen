$(document).ready(function(){
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
});