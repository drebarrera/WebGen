const title = 'dre barrera';

function titleSet(text, time){
	setTimeout(function(){	
		$('#title').html(text + '_');
	}, time);
}

function titleType(){
	for(x = 0; x < title.length; x++){
		titleSet(title.slice(0,x+1), x * 100);
	}
	setTimeout(function(){	
		titleRecurse();
	}, (title.length * 100) + 500);
}

function titleRecurse(){
	titleReturn = Math.floor(Math.random() * (title.length - 1) + 1);
	for(x = title.length; x > title.length - titleReturn; x--){
		titleSet(title.slice(0,x+1), (title.length - x) * 100);
	}
	setTimeout(function(){	
		for(x = x; x < title.length; x++){
			titleSet(title.slice(0,x+1), x * 100);
		}
	}, (titleReturn * 100) + 100);
	
	setTimeout(function(){	
		titleRecurse();
	}, (2 * (titleReturn * 100) + 2000))
}

function projectHover(i,overlay){
	//$('#'+i+' > div').css('background-color', overlay);
	//$('#'+i+' > div > p').css('display', 'block');
}

function projectOut(i){
	//$('#'+i+' > div').css('background-color', 'rgba(0,0,0,0)');
	//$('#'+i+' > div > p').css('display', 'none');
}

function projectClick(i,a){
	alert(i);
	alert(a);
}

$(document).ready(function(){
	titleType();
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
					//pauseVideo();
					
					if(scrollCoeff == 1){
					}
					else{
					}
					if(scrollCoeff == 2){
					}
					setTimeout(function(){
						scrollReady = 1;
						$('#header').show(1000);
					}, readySpeed);
				}, 200);
			}
		}
		else {
			if (scrollReady == 1) {
				scrollReady = 0;
				$('#header').hide(1000);
				setTimeout(function(){
					jQuery("html, body").animate({ scrollTop: winHeight * (scrollCoeff - 1) + "px" }, animationSpeed);
					setTimeout(function(){
						scrollReady = 1; 
						if(scrollCoeff == 1){
							//$("#vid").get(0).play();
						}
					}, readySpeed);
				}, 200);
			}
		}
		lastScrollTop = scrollTop;
	});
});