$(document).ready(function(){
	$('#interactive').click(function(){
		var winHeight = jQuery(window).height();
		var winWidth = jQuery(window).width();
		xNorm = 1368;
		yNorm = 783;
		xMin = 1075;
		ratio = winHeight / winWidth;
		ratioNorm = yNorm / xNorm;
		ratioMin = yNorm / xMin;
		if(ratio < ratioMin){
			window.location.href = "../interactive/index.html";
		}
		else{
			alert("Your browser does not properly support the display of the portfolio. Please try again on a widescreen browser.");
		}
	});
	
	
});