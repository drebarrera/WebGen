$(document).ready(function(){
	var waitForReplace = 0;

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

	$("#codeC").on("dblclick", ".cT", function(e) {
		if(e.target == e.currentTarget){
			if(waitForReplace - 1 == $(this).parent().index()){
				waitForReplace = 0;
			}
			else if(waitForReplace - 1 > $(this).parent().index()){
				waitForReplace = waitForReplace - 1;
			}
			$(this).parent().remove();
		}
	});

	$("#codeC").on("click", ".cT", function(e) {
		if(e.target == e.currentTarget){
			if(waitForReplace == 0){
				waitForReplace = $(this).parent().index() + 1;
				$(this).css({'border':'1px solid black'});
			}
			else{
				if($(this).parent().index() + 1 == waitForReplace){
					waitForReplace = 0;
					$(this).css({'border':'0px solid black'});
				}
				else{
					x = $(this).parent();
					y = $('#codeC').children().eq(waitForReplace - 1);
					$('#codeC').children().eq(waitForReplace - 1).children().css({'border':'0px solid black'});
					z1 = y.replaceWith(x.clone());
					z2 = x.replaceWith(y.clone());

					//$(this).parent().remove();
					//$('#codeC').children().eq(waitForReplace - 1).remove();
					waitForReplace = 0;
				}
			}
		}
	});

	$('.cT').click(function(e){
		if(e.target == e.currentTarget){
			if(waitForReplace == 0){
				x = $(this).parent().clone().appendTo( "#codeC" );
				x.children().css('height','1.5vh');
				x.find('.ctriangle').css({transform:'rotate(0)'});
				x.find('textarea').bind('input propertychange', function() {
					update();
				});
			}
			else{
				y = $('#codeC').children().eq(waitForReplace - 1);
				x = $(this).parent().clone();
				y.after(x);
				y.remove();
				x.children().css('height','1.5vh');
				x.find('.ctriangle').css({transform:'rotate(0)'});
				x.find('textarea').bind('input propertychange', function() {
					update();
				});
				waitForReplace = 0;
			}
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

	$('#lang').bind('input propertychange', function() {
		update();
	});

	observer.observe($('#codeC').get(0), config);
});