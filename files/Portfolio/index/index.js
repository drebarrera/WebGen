$(document).ready(function(){
	var winHeight = jQuery(window).height();
	var winWidth = jQuery(window).width();
	xNorm = 1368;
	yNorm = 783;
	xMin = 1075;
	ratio = winHeight / winWidth;
	ratioNorm = yNorm / xNorm;
	ratioMin = yNorm / xMin;
	if(!(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) && ratio < ratioMin) {
		window.open("https://www.drebarrera.com/interactive", '_self');
	}

	$('#interactive').click(function(){
		var winHeight = jQuery(window).height();
		var winWidth = jQuery(window).width();
		ratio = winHeight / winWidth;
		if(ratio < ratioMin){
			window.open("https://www.drebarrera.com/interactive", '_blank');
		}
		else{
			alert("Your browser does not properly support the display of the portfolio. Please try again on a widescreen browser.");
		}
	});
	
	
});