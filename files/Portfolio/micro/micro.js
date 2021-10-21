$(document).ready(function(){
	/* -------------------- JQuery .clone() Fixes ------------------ */
	(function (original) {
  		jQuery.fn.clone = function () {
    			var result           = original.apply(this, arguments),
        			my_textareas     = this.find('textarea').add(this.filter('textarea')),
        			result_textareas = result.find('textarea').add(result.filter('textarea')),
        			my_selects       = this.find('select').add(this.filter('select')),
        			result_selects   = result.find('select').add(result.filter('select'));

    			for (var i = 0, l = my_textareas.length; i < l; ++i) $(result_textareas[i]).val($(my_textareas[i]).val());
    			for (var i = 0, l = my_selects.length;   i < l; ++i) {
      				for (var j = 0, m = my_selects[i].options.length; j < m; ++j) {
        					if (my_selects[i].options[j].selected === true) {
          					result_selects[i].options[j].selected = true;
        					}
      				}
   			}
    			return result;
  		};
	}) (jQuery.fn.clone);

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
				$(this).css({'border':'2px solid black'});
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
					waitForReplace = 0;
				}
			}
		}
	});

	// Clone from Command to Code
	$('.cT').click(function(e){
		if(e.target == e.currentTarget){
			if(waitForReplace == 0){
				$('#codeC').find('.cT').css('height','1.5vh');
				$('#codeC').find('.ctriangle').css({transform:'rotate(0)'});
				$('#codeC').find('.c').css('margin-top','0px');
				x = $(this).parent().clone().appendTo( "#codeC" );
				x.children().css('height','1.5vh');
				x.find('.ctriangle').css({transform:'rotate(0)'});
				x.find('textarea').bind('input propertychange', function() {
					update();
				});
				$('#codeC').find('select').bind('input propertychange', function() {
					update();
				});
			}
			else{
				$('#codeC').find('.cT').css('height','1.5vh');
				$('#codeC').find('.ctriangle').css({transform:'rotate(0)'});
				$('#codeC').find('.c').css('margin-top','0px');
				y = $('#codeC').children().eq(waitForReplace - 1);
				x = $(this).parent().clone();
				y.after(x);
				y.remove();
				x.children().css('height','1.5vh');
				x.find('.ctriangle').css({transform:'rotate(0)'});
				x.find('textarea').bind('input propertychange', function() {
					update();
				});
				$('#codeC').find('select').bind('input propertychange', function() {
					update();
				});
				waitForReplace = 0;
			}
		}
	});

	$('.ctable > tbody > tr').click(function(){
		if($(this).attr('title')){
			alert($(this).attr('title'));
		}
	});

	// Compilation Functions

	function update(){
		$('#compiledT > textarea').val('');
		if($('#lang').val() == 'C'){
			const codeList = document.getElementById('codeC');
			for (i = 0; i < codeList.children.length; i++) {
				x = $('#codeC').children().eq(i);

				function register(rName){
					var bStrClr = 0b0;
					var bStrSet = 0b0;
					for (j = 0; j < x.find('tbody').children().length; j++){
						var row = x.find('tbody').children().eq(j);
						var bit = row.find('td').eq(0);
						var name = row.find('td').eq(1);
						var val = row.find('select').val();
						if(bit.text() != "Bit"){
							if(val == "EN"){
								bStrClr = (bStrClr  | (0b1 << parseInt(bit.text())));
								bStrSet = (bStrSet  | (0b1 << parseInt(bit.text())));
							}
							else if(val == "DN"){
								bStrClr = (bStrClr  | (0b1 << parseInt(bit.text())));
							}
						}
					}
					//alert(bStrClr.toString(16));
					//alert(bStrSet.toString(16));
					if(bStrClr){
						var out = rName + " &= ~0x"+bStrClr.toString(16)+";"
						if(bStrSet){
							out = out + "\n"+rName+" |= 0x"+bStrSet.toString(16)+";"
						}
						return out;
					}
					else{
						return "// No selection made.";
					}
				}

				const cDict = {
					"custom": x.find('textarea').val(),
					"rccAHBENR": register("RCC -> AHBENR"),
					"rccAPB1ENR": register("RCC -> APB1ENR"),
					"rccAPB2ENR": register("RCC -> APB2ENR")
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
	
	$('#codeC').find('select').bind('input propertychange', function() {
		update();
	});

	$('#lang').bind('input propertychange', function() {
		update();
	});

	observer.observe($('#codeC').get(0), config);
});