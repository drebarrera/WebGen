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
});i