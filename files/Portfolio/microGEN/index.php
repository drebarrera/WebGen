<?php $visitInfo = $_SERVER['REQUEST_URI'].',';
$visitInfo .= $_SERVER['REMOTE_ADDR'];
date_default_timezone_set("America/New_York");
$visitInfo .= ','.date("Y-m-d;h:i:sA").','.$email.PHP_EOL;
file_put_contents('../data/visitInfo.txt', $visitInfo, FILE_APPEND); ?><?php $visitInfo = $_SERVER['REQUEST_URI'].',';
$visitInfo .= $_SERVER['REMOTE_ADDR'];
date_default_timezone_set("America/New_York");
$visitInfo .= ','.date("Y-m-d;h:i:sA").','.$email.PHP_EOL;
file_put_contents('data/visitInfo.txt', $visitInfo, FILE_APPEND); ?><!DOCTYPE html><html><head><title>Dre Barrera</title><meta charset="utf-8"><meta name="description" content="Default WebGen Page"><meta name="keywords" content=""><meta name="description" content="Andres Barrera"><meta name="viewport" content="width=device-width, initial-scale=1"><script src="..\JQuery.js"></script><script src="..\JQuery-UI.js"></script><script>$(document).ready(function(){
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
	if($('#lang').val() == 'C'){
		$('.cR').hide();
		$('.cVar').show();
	}
	else if($('#lang').val() == 'ASM'){
		$('.cR').show();
		$('.cVar').hide();
	}
	$('.cBit').hide();

	$("#commandC").on("click", ".ctriangle", function() {
		prevHeight = $(this).parent().height();
		$(this).parent().css('height', '1.5vh');
		compHeight = $(this).parent().height();
		$(this).parent().css('height', 'auto');
		autoHeight = $(this).parent().height();
		
		if(Math.floor(prevHeight) < Math.floor(autoHeight)-10){
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
		if(Math.floor(prevHeight) < Math.floor(autoHeight) - 10){
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
					$('#codeC').find('.cT').css('height','1.5vh');
					$('#codeC').find('.ctriangle').css({transform:'rotate(0)'});
					$('#codeC').find('.c').css('margin-top','0px');
					x = $(this).parent();
					y = $('#codeC').children().eq(waitForReplace - 1);
					$('#codeC').children().eq(waitForReplace - 1).children().css({'border':'0px solid black'});
					xc = x.clone();
					xc.find('textarea, select, input').bind('input propertychange', function() {
						update();
					});
					yc = y.clone();
					yc.find('textarea, select, input').bind('input propertychange', function() {
						update();
					});
					z1 = y.replaceWith(xc);
					z2 = x.replaceWith(yc);
					
					z2.find('textarea').bind('input propertychange', function() {
						update();
					});
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
				$('#codeC').find('select, input').bind('input propertychange', function() {
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
				$('#codeC').find('select, input').bind('input propertychange', function() {
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
			$('.cR').hide();
			$('.cVar').show();
			const codeList = document.getElementById('codeC');
			for (i = 0; i < codeList.children.length; i++) {
				x = $('#codeC').children().eq(i);

				function registerC(rName){
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
							else if(val == "DIS"){
								if(rName.split("-> ")[1] != "PUPDR"){
									bStrClr = (bStrClr  | (0b1 << parseInt(bit.text())));
								}
								else{
									bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
								}
							}
							else if(val == "IN"){
								bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
							}
							else if(val == "OUT" || val == "PU"){
								bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
								bStrSet = (bStrSet  | (0b1 << parseInt(bit.text().split(':')[1])));
							}
							else if(val == "ALT" || val == "PD"){
								bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
								bStrSet = (bStrSet  | (0b1 << parseInt(bit.text().split(':')[0])));
							}
							else if(val == "AM"){
								bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
								bStrSet = (bStrSet  | (0b11 << parseInt(bit.text().split(':')[1])));
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

				function readC(rName){
					var out = "";	
					var vName = x.find('.cVar').find('input').val();	
					var rType = x.find('.cType').val();

					if(rType == "Register" && vName != ""){
						x.find('.cBit').hide();
						out = vName + " = " + rName + ";";
					}
					else if(rType == "Bit Value" && vName != ""){
						x.find('.cBit').show();
						out = vName + " = (" + rName + " >> "+ x.find('.cBit').val().split(' ')[1] + ") & 0xfffffffe;";
					}
					else{
						out = "// No selection made. Make sure you have provided a variable assignment."
					}
					
					return out;
				}

				function setC(sysName){
					var out = "";	
					const timx_reg = {
						"dummy": ["CNT","PSC","ARR","CCR1","CCR2","CCR3","CCR4","DMAR"],
						"TIM1": [1, 1, 1, 1, 1, 1, 1, 1],
						"TIM2": [1, 1, 1, 1, 1, 1, 1, 1],
						"TIM3": [1, 1, 1, 1, 1, 1, 1, 1],
						"TIM6": [1, 1, 1, 0, 0, 0, 0, 0],
						"TIM7": [1, 1, 1, 0, 0, 0, 0, 0],
						"TIM14": [1, 1, 1, 1, 0, 0, 0, 0],
						"TIM15": [1, 1, 1, 1, 1, 0, 0, 1],
						"TIM16": [1, 1, 1, 1, 0, 0, 0, 1],
						"TIM17": [1, 1, 1, 1, 0, 0, 0, 1]
					};
					const timx_ind = {
						"CNT": 0,
						"PSC": 1,
						"ARR": 2,
						"CCR1": 3,
						"CCR2": 4,
						"CCR3": 5,
						"CCR4": 6,
						"DMAR": 7
					}

					for (j = 0; j < x.find('input').length; j++){
						var val = x.find('input').eq(j).val();
						var rName = x.find('input').eq(j).attr('name');
						var tim = x.find('.cTIMS').val();
						
						if(timx_reg[tim][timx_ind[rName]] == 0){
							x.find('input[name="'+rName+'"]').parent().parent().hide();
						}
						else{
							x.find('input[name="'+rName+'"]').parent().parent().show();
						}
						
						if(j != 0){
							out = out + "\n";
						}

						if(val != ""){
							out = out + sysName + " -> " + rName + " = "+parseInt(val).toString(16)+";";
						}
						else{
							out = out + "// No "+rName+" selection made."
						}
					}
					
					return out;
				}

				const cDict = {
					"custom": x.find('textarea').val(),
					"rccAHBENR": registerC("RCC -> AHBENR"),
					"rccAPB1ENR": registerC("RCC -> APB1ENR"),
					"rccAPB2ENR": registerC("RCC -> APB2ENR"),
					"gpioMODER": registerC(x.find('.cSel').find('select').val()+"-> MODER"),
					"gpioPUPDR": registerC(x.find('.cSel').find('select').val()+"-> PUPDR"),
					"gpioODR": registerC(x.find('.cSel').find('select').val()+"-> ODR"),
					"gpioIDR": readC(x.find('.cSel').find('select').val()+" -> IDR"),
					"timxS": setC(x.find('.cTIMS').val())
				};

  				$('#compiledT > textarea').val($('#compiledT > textarea').val() + cDict[codeList.children[i].id] + '\n');
			}
		}
		else if($('#lang').val() == 'ASM'){
			$('.cR').show();
			$('.cVar').hide();
			const codeList = document.getElementById('codeC');
			for (i = 0; i < codeList.children.length; i++) {
				x = $('#codeC').children().eq(i);

				function registerASM(sysName, rName){
					
					var r0 = x.find('.cR').find('select').eq(0).val();
					var r1 = x.find('.cR').find('select').eq(1).val();

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
							else if(val == "DIS"){
								if(rName != "PUPDR"){
									bStrClr = (bStrClr  | (0b1 << parseInt(bit.text())));
								}
								else{
									bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
								}
							}
							else if(val == "IN"){
								bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
							}
							else if(val == "OUT" || val == "PU"){
								bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
								bStrSet = (bStrSet  | (0b1 << parseInt(bit.text().split(':')[1])));
							}
							else if(val == "ALT" || val == "PD"){
								bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
								bStrSet = (bStrSet  | (0b1 << parseInt(bit.text().split(':')[0])));
							}
							else if(val == "AM"){
								bStrClr = (bStrClr  | (0b11 << parseInt(bit.text().split(':')[1])));
								bStrSet = (bStrSet  | (0b11 << parseInt(bit.text().split(':')[1])));
							}
						}
					}
					//alert(bStrClr.toString(16));
					//alert(bStrSet.toString(16));
					
					if(bStrClr && r0 != r1){
						var out = "ldr "+r0+" ="+sysName+"\nldr "+r0+", ["+r0+", #"+rName+"]\nldr "+r1+", =0x"+bStrClr.toString(16)+"\nbics "+r0+", "+r1;
						if(bStrSet){
							out = out + "\nldr "+r1+", =0x"+bStrSet.toString(16)+"\norrs "+r0+", "+r1;
						}
						out = out + "\nldr "+r1+", ="+sysName+"\nstr "+r0+", ["+r1+", #"+rName+"]";
						return out;
					}
					else{
						return "// No selection made. Make sure you have selected two different registers.";
					}
				}
	
				function readASM(sysName, rName){
					var r0 = x.find('.cR').find('select').eq(0).val();
					var r1 = x.find('.cR').find('select').eq(1).val();		
					var rType = x.find('.cType').val();

					if(rType == "Register"){
						x.find('.cBit').hide();
					}

					else if(rType == "Bit Value"){
						x.find('.cBit').show();
					}

					if(rType == "Register"){
						return "ldr "+r0+", ="+sysName+"\nldr "+r0+", ["+r0+", #"+rName+"]";
					}

					else if(rType == "Bit Value" && r0 != r1){
						return "ldr "+r1+", ="+rName+"\nadds "+r1+", "+r1+", #"+x.find('.cBit').val().split(' ')[1]+"\nldr "+r0+", ="+sysName+"\nldrb "+r0+", ["+r0+", #"+r1+"]";
					}

					else{
						return "// No selection made. Make sure you have selected two different registers."
					}
				}

				function setASM(sysName){
					var r0 = x.find('.cR').find('select').eq(0).val();
					var r1 = x.find('.cR').find('select').eq(1).val();
					var out = "";		
					
					const timx_reg = {
						"dummy": ["CNT","PSC","ARR","CCR1","CCR2","CCR3","CCR4","DMAR"],
						"TIM1": [1, 1, 1, 1, 1, 1, 1, 1],
						"TIM2": [1, 1, 1, 1, 1, 1, 1, 1],
						"TIM3": [1, 1, 1, 1, 1, 1, 1, 1],
						"TIM6": [1, 1, 1, 0, 0, 0, 0, 0],
						"TIM7": [1, 1, 1, 0, 0, 0, 0, 0],
						"TIM14": [1, 1, 1, 1, 0, 0, 0, 0],
						"TIM15": [1, 1, 1, 1, 1, 0, 0, 1],
						"TIM16": [1, 1, 1, 1, 0, 0, 0, 1],
						"TIM17": [1, 1, 1, 1, 0, 0, 0, 1]
					};
					const timx_ind = {
						"CNT": 0,
						"PSC": 1,
						"ARR": 2,
						"CCR1": 3,
						"CCR2": 4,
						"CCR3": 5,
						"CCR4": 6,
						"DMAR": 7
					}

					for (j = 0; j < x.find('input').length; j++){
						var val = x.find('input').eq(j).val();
						var rName = x.find('input').eq(j).attr('name');
						var tim = x.find('.cTIMS').val();
		
						if(timx_reg[tim][timx_ind[rName]] == 0){
							x.find('input[name="'+rName+'"]').parent().parent().hide();
						}
						else{
							x.find('input[name="'+rName+'"]').parent().parent().show();
							if(j != 0){
								out = out + "\n";
							}

							if(val != "" && r0 != r1){
								out = out + "ldr "+r0+", =0x"+parseInt(val).toString(16)+"\nldr "+r1+", ="+sysName+"\nstr "+r0+", ["+r1+", #"+rName+"]";
							}
							else{
								out = out + "// No "+rName+" selection made. Make sure you have selected two different registers."
							}
						}

						
					}
					
					return out;
				}

				const asmDict = {
					"custom": x.find('textarea').val(),
					"rccAHBENR": registerASM("RCC","AHBENR"),
					"rccAPB1ENR": registerASM("RCC","APB1ENR"),
					"rccAPB2ENR": registerASM("RCC","APB2ENR"),
					"gpioMODER": registerASM(x.find('.cSel').find('select').val(),"MODER"),
					"gpioPUPDR": registerASM(x.find('.cSel').find('select').val(),"PUPDR"),
					"gpioODR": registerASM(x.find('.cSel').find('select').val(),"ODR"),
					"gpioIDR": readASM(x.find('.cSel').find('select').val(),"IDR"),
					"timxS": setASM(x.find('.cTIMS').val())
				};

  				$('#compiledT > textarea').val($('#compiledT > textarea').val() + asmDict[codeList.children[i].id] + '\n')
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

	/*$('#codeC').find('textarea').bind('input propertychange', function() {
		update();
	});
	
	$('#codeC').find('select').bind('input propertychange', function() {
		update();
	});

	$('#codeC').find('input').bind('input propertychange', function() {
		update();
	});*/

	$('#lang').bind('input propertychange', function() {
		update();
		$('#codeC').find('.cT').css('height','1.5vh');
		$('#codeC').find('.ctriangle').css({transform:'rotate(0)'});
		$('#codeC').find('.c').css('margin-top','0px');
	});

	$('.cType').change(function() {
		if($('.cType').find('select').val() == "Register"){
			$('.cBit').hide();
		}
		else{
			$('.cBit').show();
		}
		
	});

	$('.cTIMS').change(function() {
		const timx_reg = {
			"dummy": ["CNT","PSC","ARR","CCR1","CCR2","CCR3","CCR4","DMAR"],
			"TIM1": [1, 1, 1, 1, 1, 1, 1, 1],
			"TIM2": [1, 1, 1, 1, 1, 1, 1, 1],
			"TIM3": [1, 1, 1, 1, 1, 1, 1, 1],
			"TIM6": [1, 1, 1, 0, 0, 0, 0, 0],
			"TIM7": [1, 1, 1, 0, 0, 0, 0, 0],
			"TIM14": [1, 1, 1, 1, 0, 0, 0, 0],
			"TIM15": [1, 1, 1, 1, 1, 0, 0, 1],
			"TIM16": [1, 1, 1, 1, 0, 0, 0, 1],
			"TIM17": [1, 1, 1, 1, 0, 0, 0, 1]
		};

		const timx_ind = {
			"CNT": 0,
			"PSC": 1,
			"ARR": 2,
			"CCR1": 3,
			"CCR2": 4,
			"CCR3": 5,
			"CCR4": 6,
			"DMAR": 7
		}

		var tim = $('.cTIMS').val();
		for (j = 0; j < $('#timxS').find('input').length; j++){
			var rName = $('#timxS').find('input').eq(j).attr('name');
			if(timx_reg[tim][timx_ind[rName]] == 0){
				$('#timxS').find('input[name="'+rName+'"]').parent().parent().hide();
			}
			else{
				$('#timxS').find('input[name="'+rName+'"]').parent().parent().show();
			}
		}
	});

	observer.observe($('#codeC').get(0), config);
});i</script><style>#title{ 	font-size: 5.2vh; 	line-height: 0.9; 	width: 50%; 	height: auto; 	padding-left: 5%; }  #description{ 	width: 50%; 	height: auto; 	font-size: 2.2vh; 	padding-right: 5%; 	font-weight: 300; }  #selectLangC{ 	font-size: 2vh; }  #commandToCode{ 	height: 80vh; 	width: 100%; }  #command{ 	height: 95%; 	width: 40%; }  #code{ 	height: 95%; 	width: 40%; 	margin-left: 5%; }  .ctcTitle{ 	font-size: 4vh; 	font-weight: 300; 	margin-top: 2vh; 	margin-left: 4%; 	width: 100%; 	position: relative; 	margin-block-end: 0.25em; }  .ctcContainer{ 	height: 65vh; 	width: 92%; 	margin-left: 4%; 	overflow-y: scroll; }  .c{ 	width: 100%; 	height: 4vh; 	display: inline-block; 	position: relative; }  .cT:hover{ 	border: 2px solid black; }  .cT{ 	padding-top: 1vh; 	padding-bottom: 1vh; 	padding-left: 2.5%; 	padding-right: 2.5%; 	font-size: 1.5 vh; 	border-radius: 1vh; 	display: inline-block; 	width: 80%; 	height: 1.5vh; 	position: relative; 	cursor: pointer; 	margin-left: 3%; 	margin-top: 0.5vh; 	overflow-y: hidden; }  .ctriangle{ 	font-size: 1.6vh; 	float: right; 	color: black; }  .ctriangle:hover{ 	color: white; }  .cinfo{ 	display: block; 	margin-top: 1vh; 	color: #006497; 	background-color: #fafafa; 	padding: 0.5vh; 	border-radius: 0.5vh; }  .ctitle{ 	margin-block-end: 0em; 	margin-block-start: 0em; 	margin-top: 1vh; 	margin-left: 2%; 	padding-bottom: 0.5vh; 	font-weight: 300; 	font-size: 2.5vh; 	width: 100%; }  .cR{ 	color: black; }  .cSel{ 	color: black; }  .ctable{ 	width: 98%; 	margin-top: 0.5vh; 	border:2px solid black;  	border-collapse: collapse;  }  .ctable tr, .ctable td{ 	color: black; 	border:1px solid black;  	border-collapse: collapse;  	padding: 0.25vh; }  .misc{ 	background-color: lightBlue; }  .rcc{  	background-color: coral; }  .tim{ 	background-color: mediumOrchid; }  .gpio{ 	background-color: lightseagreen; }  #compiledC{ 	width: 100%; 	height: 50vh; }  #compiledT{ 	text-align: center; 	font-size: 3vh; 	width: 100%; }</style><style>p{ 	margin-block-start: 0px; 	margin-block-end: 0px; }  #nav{ 	width: 100%; 	display: flex; 	justify-content: center; 	position: fixed; 	z-index: 101; 	padding: 2vh; }  #nav_center{ 	position: relative; 	width: 75%; 	display: flex; 	justify-content: center; 	border-bottom: 2px solid #d8d8d8; 	padding-bottom: 1vh; }  #menu{ 	position: relative; 	display: inline-block; }  #htitle{ 	font-size: 4.5vh; 	text-decoration: none; 	color: #00334d; 	position: relative; 	display: inline-block; 	padding-right: 14vw; }  @media only screen and (max-width:1000px) { 	#htitle{ 		padding-right: 5vw; 	}  	#nav_center{ 		width: 90%; 	} }  .hoption{ 	display: inline-block; }  .button{ 	position: relative; 	display: inline-block; 	padding: 1.25vh; 	border-radius: 1vh; 	cursor: pointer; 	color: white; 	text-decoration: none; 	font-size: 1.75vh; 	margin: 1vh; 	margin-left: 1.5vh; 	margin-right: 1.5vh; 	filter: drop-shadow(0 0.2rem 0.25rem rgba(0, 0, 0, 0.25)); }  .button > p{ 	margin-block-start: 0px; 	margin-block-end: 0px; }  .buttonBlue{ 	background-color: #005580; 	border: 2px solid #005580; }  .buttonBlue:hover{ 	background-color: white; 	color: #005580; }   .buttonRedRing{ 	background-color: white; 	border: 2px solid #ff5938; 	color: #ff5938; }  .buttonRedRing:hover{ 	background-color: #ff5938; 	color: white; }  .buttonRed{ 	background-color: #ff5938; 	border: 2px solid #ff5938; }  .buttonRed:hover{ 	background-color: white; 	color: #ff5938; }  .buttonYellow{ 	background-color: #ffba00; 	border: 2px solid #ffba00; }  .buttonYellow:hover{ 	background-color: white; 	color: #ffba00; }  .buttonPurple{ 	background-color: rgb(138, 74, 255); 	border: 2px solid rgb(138, 74, 255); }  .buttonPurple:hover{ 	background-color: white; 	color: rgb(138, 74, 255); }  .pseudoLink{ 	color: #005580; 	text-decoration: none; 	cursor: pointer; }  .pseudoLink:hover{ 	color: #ff5938; }</style><script>/// Custom Alert Generation ///
function alert(msg){
	$("#alert").css('display', 'block');
	document.getElementById('alertText').innerHTML = msg+'<br><br><span style="padding: 5px; padding-left: 12px; padding-right: 12px; border-radius: 5px; cursor: pointer;">OK</span>';
	$('#alertText > span').click(function(){
		$("#alert").css('display', 'none');
	});
}</script><style>#alert{ 	max-width: 450px; 	width: 80%; 	height: auto; 	position: fixed; 	z-index; 50; 	margin-top: 30vh; 	display: none; 	padding: 2.5vh; 	padding-left: 2.5vh; 	padding-right: 2.5vh; 	border-radius: 2vh; 	font-size: 3vh; 	font-weight: 500; 	text-align: center; }  /*@media only screen and (max-width:1000px) { 	#alert{ 		margin-top: 300px; 	} }*/  #alertText > span{ 	background-color: #ff5938; 	color: white; }  #alertText > span:hover{ 	background-color: white; 	border: 2px solid #ff5938; 	color: black; }</style><style>/* Style inputs with type="text", select elements and textareas */ input[type=text], select, textarea { 	width: 100%; /* Full width */ 	padding: 12px; /* Some padding */   	border: 1px solid #ccc; /* Gray border */ 	border-radius: 4px; /* Rounded borders */ 	box-sizing: border-box; /* Make sure that padding and width stays in place */	 	margin-top: 6px; /* Add a top margin */ 	margin-bottom: 16px; /* Bottom margin */ 	resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */ 	font-size: 1.75vh; }  input{ 	font-family: monospace; 	font-size: 1.75vh; }  /* Style the submit button with a specific background color etc */ input[type=submit] { 	background-color: #4CAF50; 	color: white; 	padding: 12px 20px; 	border: none; 	border-radius: 4px; 	cursor: pointer; }  /* When moving the mouse over the submit button, add a darker green color */ input[type=submit]:hover { 	background-color: #45a049; }</style></head>
<body style="margin:0;background-color:#fefefe;overflow-x:hidden;font-family:Helvetica;color:black;"><div style="background-color:#242323;overflow-x:visible;overflow-y:visible;"><div style="overflow-x:visible;overflow-y:visible;display:flex;justify-content:center;align-items:center;position:relative;"><p id="title" style="color:white;display:inline-block;position:relative;">microGEN<br><span style="font-size: 2.75vh; font-weight: 300;">Assembly and C code for Microprocessor Systems</span></p><p id="description" style="color:white;display:inline-block;position:relative;">microGEN is a microprocessor program generator for Assembly and C. Select your programming language below to begin. Then, click the desired commands / register modifications from the "Commands" section to append them to the "Code" section. Click the commands appended to "Code" in order to remove them. Click the arrow on each command to edit their adjustable fields. When you are happy with your program, hit compile to write the command blocks to code.</p></div><div id="selectLangC" style="overflow-x:visible;overflow-y:visible;display:flex;justify-content:center;"><p style="color:white;">Select Language <select id="lang"><option value = "ASM">ASM</option><option value = "C">C</option></select></p></div><div id="commandToCode" style="overflow-x:visible;overflow-y:visible;display:flex;justify-content:center;align-items:center;position:relative;"><div id="command" style="background-color:#fafafa;overflow-x:visible;overflow-y:visible;display:inline-block;position:relative;"><p class="ctcTitle" style="">Commands</p><div id="commandC" class="ctcContainer" style="background-color:white;overflow-x:visible;overflow-y:scroll;display:block;position:relative;"><p class="ctitle" style="">RCC Configuration</p><div id="rccAHBENR" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT rcc">RCC: AHBENR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="DMAEN is used to enable the internal clock for the Digital Memory Access"><td>0</td><td>DMAEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>1</td><td>DAM2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="SRAMEN is used to keep SRAM enabled in sleep mode."><td>2</td><td>SRAMEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>4</td><td>FLITFEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>6</td><td>CRCEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPAEN is used to enable the internal clock for Peripheral A"><td>17</td><td>IOPAEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPBEN is used to enable the internal clock for Peripheral B"><td>18</td><td>IOPBEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPCEN is used to enable the internal clock for Peripheral C"><td>19</td><td>IOPCEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPDEN is used to enable the internal clock for Peripheral D"><td>20</td><td>USART4RST</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPEEN is used to enable the internal clock for Peripheral E"><td>21</td><td>IOPEEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPFEN is used to enable the internal clock for Peripheral F"><td>22</td><td>IOPFEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>24</td><td>TSCEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></table></span></div></div><div id="rccAPB1ENR" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT rcc">RCC: APB1ENR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="TIM2EN is used to enable the internal clock for Timer TIM2"><td>0</td><td>TIM2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM3EN is used to enable the internal clock for Timer TIM3"><td>1</td><td>TIM3EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM6EN is used to enable the internal clock for Timer TIM6"><td>4</td><td>TIM6EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM7EN is used to enable the internal clock for Timer TIM7"><td>5</td><td>TIM7EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM14EN is used to enable the internal clock for Timer TIM14"><td>8</td><td>TIM14EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>11</td><td>WWDGEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="SPI2EN is used to enable the internal clock for Serial Peripheral Interface SPI2"><td>14</td><td>SPI2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>17</td><td>USART2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>18</td><td>USART3EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>19</td><td>USART4EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>20</td><td>USART5EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>21</td><td>I2C1EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>22</td><td>I2C2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>23</td><td>USBEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>25</td><td>CANEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>27</td><td>CRSEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>28</td><td>PWREN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="DACEN is used to enable the internal clock for the Digital to Analog Converter"><td>29</td><td>DACEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>30</td><td>CECEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></table></span></div></div><div id="rccAPB2ENR" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT rcc">RCC: APB2ENR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr><td>0</td><td>SYSCFGCOMPEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>5</td><td>USART6EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>6</td><td>USART7EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>7</td><td>USART8EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="ADCEN is used to enable the internal clock for the Analog to Digital Converter"><td>9</td><td>ADCEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM1EN is used to enable the internal clock for Timer TIM1"><td>11</td><td>TIM1EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="SPI1EN is used to enable the internal clock for Serial Peripheral Interface SPI1"><td>12</td><td>SPI1EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>14</td><td>USART1EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM15EN is used to enable the internal clock for Timer TIM15"><td>16</td><td>TIM15EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM16EN is used to enable the internal clock for Timer TIM16"><td>17</td><td>TIM16EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM17EN is used to enable the internal clock for Timer TIM17"><td>18</td><td>TIM17EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>22</td><td>DBGMCUEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></table></span></div></div><p class="ctitle" style="">GPIO Configuration</p><div id="gpioMODER" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT gpio">GPIOx: MODER Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select IN for Input, OUT for Output, ALT for Alternate Function Mode, or AM for Analog Mode for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cSel"><br>Select the peripheral you wish to use. <select><option>GPIOA</option><option>GPIOB</option><option>GPIOC</option><option>GPIOD</option><option>GPIOE</option><option>GPIOF</option></select></span><!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>1:0</td><td>MODER0</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>3:2</td><td>MODER1</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>5:4</td><td>MODER2</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>7:6</td><td>MODER3</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>9:8</td><td>MODER4</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>11:10</td><td>MODER5</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>13:12</td><td>MODER6</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>15:14</td><td>MODER7</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>17:16</td><td>MODER8</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>19:18</td><td>MODER9</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>21:20</td><td>MODER10</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>23:22</td><td>MODER11</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>25:24</td><td>MODER12</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>27:26</td><td>MODER13</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>29:28</td><td>MODER14</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>31:30</td><td>MODER15</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr></table></span></div></div><div id="gpioPUPDR" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT gpio">GPIOx: PUPDR Set <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select PU for Pull Up, PD for Pull Down, or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cSel"><br>Select the peripheral you wish to use. <select><option>GPIOA</option><option>GPIOB</option><option>GPIOC</option><option>GPIOD</option><option>GPIOE</option><option>GPIOF</option></select></span><!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>1:0</td><td>PUPDR0</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>3:2</td><td>PUPDR1</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>5:4</td><td>PUPDR2</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>7:6</td><td>PUPDR3</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>9:8</td><td>PUPDR4</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>11:10</td><td>PUPDR5</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>13:12</td><td>PUPDR6</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>15:14</td><td>PUPDR7</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>17:16</td><td>PUPDR8</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>19:18</td><td>PUPDR9</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>21:20</td><td>PUPDR10</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>23:22</td><td>PUPDR11</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>25:24</td><td>PUPDR12</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>27:26</td><td>PUPDR13</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>29:28</td><td>PUPDR14</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>31:30</td><td>PUPDR15</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></table></span></div></div><div id="gpioODR" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT gpio">GPIOx: ODR Set <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cSel"><br>Select the peripheral you wish to use. <select><option>GPIOA</option><option>GPIOB</option><option>GPIOC</option><option>GPIOD</option><option>GPIOE</option><option>GPIOF</option></select></span><!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>0</td><td>ODR0</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>1</td><td>ODR1</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>2</td><td>ODR2</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>3</td><td>ODR3</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>4</td><td>ODR4</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>5</td><td>ODR5</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>6</td><td>ODR6</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>7</td><td>ODR7</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>8</td><td>ODR8</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>9</td><td>ODR9</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>10</td><td>ODR10</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>11</td><td>ODR11</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>12</td><td>ODR12</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>13</td><td>ODR13</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>14</td><td>ODR14</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>15</td><td>ODR15</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr></table></span></div></div><div id="gpioIDR" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT gpio">GPIOx: IDR Read <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select whether you would like to read the entire Register or a Single Bit.<!----><span class="cSel"><br>Select the peripheral you wish to use. <select><option>GPIOA</option><option>GPIOB</option><option>GPIOC</option><option>GPIOD</option><option>GPIOE</option><option>GPIOF</option></select></span><!----><span class="cR"><br>The Register configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><span class="cRead" style="color:black;"><br>Read Type: <select class="cType"><option>Register</option><option>Bit Value</option></select><select class="cBit"><option>Bit 0</option><option>Bit 1</option><option>Bit 2</option><option>Bit 3</option><option>Bit 4</option><option>Bit 5</option><option>Bit 6</option><option>Bit 7</option><option>Bit 8</option><option>Bit 9</option><option>Bit 10</option><option>Bit 11</option><option>Bit 12</option><option>Bit 13</option><option>Bit 14</option><option>Bit 15</option></select><br><span class="cVar">Variable Assignment: <input></input></span></span></span></div></div><p class="ctitle" style="">Timer Configuration</p><div id="timxS" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT tim">TIMx: Value Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select the Timer and set the values in each of its Set-Value Registers.<!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><br><span style="color:black;">Select a Timer: <select class="cTIMS"><option>TIM1</option><option>TIM2</option><option>TIM3</option><option>TIM6</option><option>TIM7</option><option>TIM14</option><option>TIM15</option><option>TIM16</option><option>TIM17</option></select></span><!----><table class="ctable"><tr><td>Name</td><td>Set Value</td></tr><tr title="The Counter Register counts to ARR and then is updated to 0."><td>CNT</td><td><input name="CNT"></input></td></tr><tr title="The Prescaler Register divides the 48MHz clock."><td>PSC</td><td><input name="PSC"></input></td></tr><tr title="The Auto-Reload Register is the value counted to by the counter."><td>ARR</td><td><input name="ARR"></input></td></tr><tr title="This Compare-Capture Register provides the value to be compared to CNT. When CNT = CCR1, Channel 1 is subject to the state change defined by the OCM1M bit of the CCMR register."><td>CCR1</td><td><input name="CCR1"></input></td></tr><tr title="This Compare-Capture Register provides the value to be compared to CNT. When CNT = CCR2, Channel 2 is subject to the state change defined by the OCM2M bit of the CCMR register."><td>CCR2</td><td><input name="CCR2"></input></td></tr><tr title="This Compare-Capture Register provides the value to be compared to CNT. When CNT = CCR3, Channel 3 is subject to the state change defined by the OCM3M bit of the CCMR register."><td>CCR3</td><td><input name="CCR3"></input></td></tr><tr title="This Compare-Capture Register provides the value to be compared to CNT. When CNT = CCR4, Channel 4 is subject to the state change defined by the OCM4M bit of the CCMR register."><td>CCR4</td><td><input name="CCR4"></input></td></tr><tr><td>DMAR</td><td><input name="DMAR"></input></td></tr></table></span></div></div><div id="timxCR1" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT tim">TIMx: CR1 Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<br><span style="color:black;">Select a Timer: <select class="cTIMS"><option>TIM1</option><option>TIM2</option><option>TIM3</option><option>TIM6</option><option>TIM7</option><option>TIM14</option><option>TIM15</option><option>TIM16</option><option>TIM17</option></select></span><!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="The Counter Enable state enables the counter to start counting. This bit should be set after the output configurations have been set."><td>0</td><td>CEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Update Disable state disables the update event on counter overflow/underflow when enabled."><td>1</td><td>UDIS</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr><td>2</td><td>URS</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="One Pulse Mode limits the counter to one whole pulse before clearing the CEN bit and stopping the counter."><td>3</td><td>OPM</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The counter counts as an Upcounter when the Direction state is Disabled and a Downcounter when the Direction state is Enabled"><td>4</td><td>DIR</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Center-Aligned Mode Selection determines the counting configuration. Select EDG for Edge-Mode, where the counter counts as selected by DIR. Select CM1, CM2, or CM3 for Alternating Up-Down Counting, where output compare interrupt flags are set when counting down, counting up, or both, respectively."><td>6:5</td><td>CMS</td><td><select><option></option><option>EDG</option><option>CM1</option><option>CM2</option><option>CM3</option></select></td></tr></tr><tr title="The Auto-Reload Preload Enable bit determines whether the ARR register is buffered. If the ARPE state is set, the PWM period will change at the next cycle - not immediately."><td>7</td><td>ARPE</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Clock Division setting determines the rate of the FDTS Sampling Clock. Setting the Clock Division to X will divide the internal clock rate by X to produce the FTDS Sampling Clock Symbol."><td>9:8</td><td>CKD</td><td><select><option></option><option>DIV1</option><option>DIV2</option><option>DIV4</option></select></td></tr></tr></table></span></div></div><p class="ctitle" style="">Miscellaneous</p><div id="custom" class="c" style="overflow-x:visible;overflow-y:visible;"><div class="cT misc">Custom Code <span class="ctriangle">&#9654;</span><br><span class="cinfo">Type your code in the textbox below:<br><textarea style="width: 98%; margin-top: 0.5vh;max-width: 98%; height: 12vh;resize: none;"></textarea></span></div></div></div></div><div id="code" style="background-color:#fafafa;overflow-x:visible;overflow-y:visible;display:inline-block;position:relative;"><p class="ctcTitle" style="">Code</p><div id="codeC" class="ctcContainer" style="background-color:white;overflow-x:visible;overflow-y:scroll;display:flex;flex-direction:column;position:relative;"></div></div></div><div id="compiledC" style="background-color:#fafafa;overflow-x:visible;overflow-y:visible;display:flex;justify-content:center;position:relative;"><p id="compiledT" style="">Compiled Code<br><textarea style="width:80%; height: 36vh; margin-top: 2vh; font-size: 2vh;"></textarea></p></div></div></body></html>