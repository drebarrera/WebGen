$(document).ready(function(){
	var w = window,
    	d = document,
    	e = d.documentElement,
    	g = d.getElementsByTagName('body')[0],
    	x = w.innerWidth || e.clientWidth || g.clientWidth,
    	y = w.innerHeight|| e.clientHeight|| g.clientHeight;
	
	$("#mtc").hide();
	
	$("#menuicon").click(function(){
		$("#mtc").fadeIn(1000);
	});
	
	$("#closeicon").click(function(){
		$("#mtc").fadeOut(1000);
	});

	$('#mimg1').hover(function() {
		$(this).animate({ deg: 360 },{duration: 1200,step: function(now) {
                	$(this).css({ transform: 'rotate(' + now + 'deg)' });
        	}});
	});

	function animateImg(ref, s, z, l, w , callback){
		if(z == 1){
			var img = document.getElementById(ref);
			for(x = s; x < l+1; x++){
				(function(x){
					window.setTimeout(function(){
						y = (x-1)*-1*w;
						img.style.backgroundPosition = '0px '+y+'px';
						if(ref == "blink" & x == l){
							setTimeout(function(){
								y = (s-1)*-1*w;
								img.style.backgroundPosition = '0px '+y+'px';
								if(callback){
									callback();
								}
							}, 100)
						}
					},x*100);
				}(x));
			}
		}
	}
	z2 = 0;
	z3 = 0;
	$('#mimg2').hover(function() {
		z2 += 1;
		animateImg("mimg2", 1, z2, 16, 122.5);
	});
	$('#mimg3').hover(function() {
		z3 += 1;
		animateImg("mimg3", 1, z3, 14, 122.5);
	});

	var bScrollCheck = 0;
	var bAnimateCheck = 0;
	function blink(){		
		function call(){
			if(bScrollCheck == 1){
				//alert('call');
				bAnimateCheck = 1;
				var winHeight = jQuery(window).height();
				var scrollTop = jQuery(this).scrollTop();
				var action = Math.floor(Math.random() * (7 - 1) + 1);
				switch(action){
					case 1:
						bBlink(call);
						break;
					case 2:
						bMove(call);
						break;
					case 3:
						bMove(bMoveDeskx, 0, -300);
						break;
					case 4:
						bMove(bMovePhotox);
						break;
					case 5:
						bMove(bMoveCinemax, 0, 200);
						break;
					case 6:
						bMove(bMovePenx, 0, -300);
						break;
				}
			}
			else{
				bAnimateCheck = 0;
			}		
		}
		
		function bBlink(callback){
			animateImg("blink", 1, 1, 3, 100, function(){
				setTimeout(function(){
					callback();		
				}, 3000);
			});
		}

		function bMoveDeskx(){
			bMove(bDesk, 100, 0);
		}
	
		function bMovePhotox(){
			bMove(bPhoto);
		}

		function bMoveCinemax(){
			bMove(bCinema, 400, 0);
		}

		function bMovePenx(){
			bMove(bPen, 900, 0);
		}
		
		function bMove(callback, xsend, ysend){
			var arena = $("#blinkc");
			var blink = $("#blink");
			var posx = parseInt(blink.css('margin-left').slice(0, -2));
			var posy = parseInt(blink.css('margin-top').slice(0, -2));
			var arenax = arena.width();
			var arenay = arena.height();			
			
			if(xsend){
				var angle = 2;
			} else if (ysend){
				var angle = 1;
			} else{
				var angle = Math.floor(Math.random() * (3 - 1) + 1);
			}
			if(angle == 1){ // Up-down
				if (ysend){
					var posM = ysend;
				} else {
					var posM = Math.floor(Math.random() * (arenay/2));
					posM *= Math.round(Math.random()) ? 1 : -1;
				}
				var dy = posM - posy;
				if(dy){
					var img = document.getElementById("blink");
					for(x = 0; x < Math.abs(dy)/20; x++){
						if(x == 0){
							setTimeout(function(){
								img.style.backgroundPosition = '0px 0px';
								setTimeout(function(){
									callback();		
								}, 100);
							}, Math.ceil(Math.abs(dy)*100/20)+100);
						}
						(function(x){
							window.setTimeout(function(){
								if(dy > 0){ // Down
									y = (7+(x%3))*-100;
									var my = 20;
								}
								else{
									y = (10+(x%3))*-100;
									var my = -20;
								}
								img.style.backgroundPosition = '0px '+y+'px';
								$("#blink").animate({marginTop: "+="+my}, 100, "linear");
							},x*100);
						}(x));
					}

				}
				else{
					setTimeout(function(){
						callback();		
					}, 100);
				}
			}
			if(angle == 2){ // Left-right
				if (xsend){
					var posM = xsend;
				} else{
					var posM = Math.floor(Math.random() * (arenax - 100));
				}
				var dx = posM - posx;
				if(dx){
					var img = document.getElementById("blink");			

					if(dx < 0){ // left
						$("#blink").css({"transform": "scaleX(-1)"});
						var mx = -20;
					}
					else{
						var mx = 20;
					}
				
					for(x = 0; x < Math.abs(dx)/20; x++){
						if(x == 0){
							setTimeout(function(){
								$("#blink").css({"transform": "scaleX(1)"});
								img.style.backgroundPosition = '0px 0px';
								setTimeout(function(){
									callback();		
								}, 100);
							}, Math.ceil(Math.abs(dx)*100/20) + 100);
						}
						(function(x){
							window.setTimeout(function(){
								y = (3+(x%4))*-100;
								img.style.backgroundPosition = '0px '+y+'px';
								$("#blink").animate({marginLeft: "+="+mx}, 100, "linear");
							},x*100);
						}(x));
					}
				}
				else{
					setTimeout(function(){
						callback();		
					}, 100);
				}
			}					
		}

		function bDesk(){
			//alert('desk');
			call();
		}

		function bPhoto(){
			var img = document.getElementById("blink");
			setTimeout(function(){
				y = (14-1)*-100;
				img.style.backgroundPosition = '0px '+y+'px';				
			}, 150);
			for(x = 15; x < 20+1; x++){
				(function(x){
					window.setTimeout(function(){
						y = (x-1)*-100;
						img.style.backgroundPosition = '0px '+y+'px';
						if(x == 20){
							for(x = 19; x < 20+1; x++){
								(function(x){
									window.setTimeout(function(){
										y = (x-1)*-100;
										img.style.backgroundPosition = '0px '+y+'px';
										if(x == 20){
											setTimeout(function(){
												img.style.backgroundPosition = '0px 0px';
												call();
								
											}, 200);
										}
									},(x-18)*200);
								}(x));
							}
						}
					},(x*100)+150);
				}(x));
			}
		}
		
		function bCinema(){
			//alert('cinema');
			call();
		}

		function bPen(){
			//alert('pen');
			call();
		}

		call();
	}

	function animateUnearth(){
		$(unearthc).animate({marginTop: 95, marginLeft: 45},1500,'linear');
		setTimeout(function(){$(unearthc).animate({marginTop: 105, marginLeft: 55},3000,'linear');},1500);
		setTimeout(function(){$(unearthc).animate({marginTop: 110, marginLeft: 45},3000,'linear');},4500);
		setTimeout(function(){$(unearthc).animate({marginTop: 100, marginLeft: 50},3000,'linear');},7500);
		setTimeout(function(){animateUnearth();},10500);
	}

	vidPlay = 1;
	$('#vid').click(function(){
		if(vidPlay == 1){
			$(this).get(0).pause();
			vidPlay = 0;
		}
		else{
			$(this).get(0).play();
			vidPlay = 1;
		}
	});

	function pauseVideo(){
		var vol = 1,
    		interval = 200;
		var intervalID = setInterval(function() {
	        	// Reduce volume by 0.05 as long as it is above 0
	        	// This works as long as you start with a multiple of 0.05!
	        	if (vol > 0) {
	            		vol -= 0.05;
	            		// limit to 2 decimal places
                    		// also converts to string, works ok
                    		document.getElementById("vid").volume = vol.toFixed(2);
	        	} else {
	            		// Stop the setInterval when 0 is reached
	            		clearInterval(intervalID);
				$("#vid").get(0).pause();
				document.getElementById("vid").volume = 1;
	        	}
            	}, interval);
	}

	// Scroll Properties
	var lastScrollTop = 0;
	var animationSpeed = 1000;
	var readySpeed = animationSpeed + 100;
	var scrollReady = 1;
	// Scroll Event
	jQuery(window).scroll(function(event){
		var winHeight = jQuery(window).height();
		var scrollTop = jQuery(this).scrollTop();
		var scrollCoeff = Math.ceil(scrollTop / winHeight);
		scrollDirection = lastScrollTop - scrollTop;
		if (scrollDirection < 0){
			if (scrollReady == 1) {
				scrollReady = 0;
				setTimeout(function(){
					jQuery("html, body").animate({ scrollTop: winHeight * scrollCoeff + "px" }, animationSpeed);
					pauseVideo();
					if(scrollCoeff == 1){
						if(bAnimateCheck == 0){
							bScrollCheck = 1;
							blink();
						}
					}
					else{
						bScrollCheck = 0;
					}
					if(scrollCoeff == 2){
						animateUnearth();
					}
					setTimeout(function(){
						scrollReady = 1;
						if(scrollCoeff == 1){
							//animateImg("pimg1", 1, 1, 17, 300);
						}
					}, readySpeed);
				}, 200);
			}
		}
		else {
			if (scrollReady == 1) {
				scrollReady = 0;
				setTimeout(function(){
					jQuery("html, body").animate({ scrollTop: winHeight * (scrollCoeff - 1) + "px" }, animationSpeed);
					setTimeout(function(){
						scrollReady = 1; 
						if(scrollCoeff == 1){
							$("#vid").get(0).play();
						}
					}, readySpeed);
				}, 200);
			}
		}
		lastScrollTop = scrollTop;
	});
});