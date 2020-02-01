(function () {
	function switchSlides(selector) {
		let listBlock = document.querySelector(`.${selector} ul`);
		let dotsBlock = document.querySelector(`.${selector} .dots`);

		let currentDot = dotsBlock.querySelector('.active');
		let position = 0;
		let dots = dotsBlock.querySelectorAll('.dot');
		for(let i = 0, j = 1;i < dots.length;i++, j++) dots[i].setAttribute('data-item', j);
		
		dotsBlock.onclick = function (event) {
			let tg = event.target;
			if(tg.tagName == "SPAN"){


				let diff =  tg.dataset.item - currentDot.dataset.item;
				if(diff > 0){
					position -= 260 * diff;
					listBlock.style.marginLeft = position + 'px';
				}
				if(diff < 0){
					position += Math.abs(diff) * 260;
					listBlock.style.marginLeft = position + 'px';
				}
				currentDot.classList.remove('active');
				tg.classList.add('active');
				currentDot = tg;
			}
		}
	}
	switchSlides('deals');
})();