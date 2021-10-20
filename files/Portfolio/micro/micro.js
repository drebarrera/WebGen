$(document).ready(function(){
	$("#commandC").on("click", ".ctriangle", function() {
		prevHeight = $(this).parent().height();
		$(this).parent().css('height', 'auto');
		autoHeight = $(this).parent().height();
		if(Math.floor(prevHeight) != Math.floor(autoHeight)){
			$(this).parent().css('height', '1.5vh');
			$(this).parent().animate({
				height: autoHeight,
				deg: 90 
			},
    			{
      				duration: 500,
      				step: function(now) {
        					$(this).children('.ctriangle').css({ transform: 'rotate(' + now + 'deg)' });
      				}
			});
			$(this).parent().parent().next('.c').animate({
				marginTop: autoHeight
			}, 500);
		}
		else{
			$(this).parent().animate({
				height: "1.5vh",
				deg: 0 
			},
    			{
      				duration: 500,
      				step: function(now) {
        					$(this).children('.ctriangle').css({ transform: 'rotate(' + now + 'deg)' });
      				}
			});
			$(this).parent().parent().next('.c').animate({
				marginTop: 0
			}, 500);
		}
	});

	$("#codeC").on("click", ".ctriangle", function() {
		prevHeight = $(this).parent().height();
		$(this).parent().css('height', 'auto');
		autoHeight = $(this).parent().height();
		if(Math.floor(prevHeight) != Math.floor(autoHeight)){
			$(this).parent().css('height', '1.5vh');
			$(this).parent().animate({
				height: autoHeight,
				deg: 90 
			},
    			{
      				duration: 500,
      				step: function(now) {
        					$(this).children('.ctriangle').css({ transform: 'rotate(' + now + 'deg)' });
      				}
			});
			$(this).parent().parent().next('.c').animate({
				marginTop: autoHeight
			}, 500);
		}
		else{
			$(this).parent().animate({
				height: "1.5vh",
				deg: 0 
			},
    			{
      				duration: 500,
      				step: function(now) {
        					$(this).children('.ctriangle').css({ transform: 'rotate(' + now + 'deg)' });
      				}
			});
			$(this).parent().parent().next('.c').animate({
				marginTop: 0
			}, 500);
		}
	});

	$("#codeC").on("click", ".cT", function(e) {
		if(e.target == e.currentTarget){
			$(this).parent().remove();
		}
	});

	$('.cT').click(function(e){
		if(e.target == e.currentTarget){
			x = $(this).parent().clone().appendTo( "#codeC" );
			x.children().css('height','1.5vh');
			x.find('.ctriangle').css({transform:'rotate(0)'});
			x.find('textarea').bind('input propertychange', function() {
				update();
			});
		}
	});

	function update(){
		$('#compiledT > textarea').val('');
		if($('#lang').val() == 'C'){
			const codeList = document.getElementById('codeC');
			for (let i = 0; i < codeList.children.length; i++) {
				x = $('#codeC').children().eq(i);

				const cDict = {
					"custom": x.find('textarea').val()
				};

  				$('#compiledT > textarea').val($('#compiledT > textarea').val() + cDict[codeList.children[i].id] + '\n')
			}
		}
	}

	var observer = new MutationObserver(function(mutations) {
 		mutations.forEach(function(mutation) {
			update();
  		});
	});
	
	var config = {
  		childList: true,
  		subtree: true,
  		characterData: true
	};

	$('#codeC').find('textarea').bind('input propertychange', function() {
		update();
	});

	observer.observe($('#codeC').get(0), config);
});