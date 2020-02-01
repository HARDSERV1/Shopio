(function(){
	function slider(){
		let dots = document.querySelectorAll('.slider-wrapper .dot');
		let slides = document.querySelectorAll('.slider-wrapper .slide');

		for(let i = 0;i < dots.length;i++){

			if(dots[i].classList.contains('active')){

				if(i == dots.length - 1){

					dots[i].classList.remove('active');				
					slides[i].classList.remove('visible');
			
					dots[0].classList.add('active');
					slides[0].classList.add('visible');
					return;
				} 

				dots[i].classList.remove('active');
				slides[i].classList.remove('visible');

				dots[i + 1].classList.add('active');
				slides[i + 1].classList.add('visible');
				return;
			}
		}
	}

	function switchSlide(n) {
		let dots = document.querySelectorAll('.slider-wrapper .dot');
		let slides = document.querySelectorAll('.slider-wrapper .slide');

		for(let i = 0;i < dots.length;i++){
			if(dots[i].classList.contains('active')){
				dots[i].classList.remove('active');				
				slides[i].classList.remove('visible');
			}
		}

		dots[n].classList.add('active');
		slides[n].classList.add('visible');
	}

	function dotClick() {
		let dotsBlock = document.querySelector('.slider-wrapper .dots');
		dotsBlock.onclick = function(event){
			let elem = event.target;
			if(elem.tagName == 'SPAN'){
				if(elem.nextElementSibling === null){
					clearInterval(timer);
					switchSlide(2);
					timer = setInterval(slider, time);
				}
				else if(elem.previousElementSibling === null){
					clearInterval(timer);
					switchSlide(0);
					timer = setInterval(slider, time);
				} 
				else{
					clearInterval(timer);
					switchSlide(1);
					timer = setInterval(slider, time);
				}
			}
		}
	}

	let time = 3000;
	let timer = setInterval(slider, time);

	dotClick();
})();