(function () {
	function bestsellerSlider(selector, width, count) {
		count--;
		let List = document.querySelector(`.${selector} ul`);
		let countList = 0, position = 0;

		document.querySelector(`.${selector} .arrow-right`).addEventListener('click', clickRight);
		document.querySelector(`.${selector} .arrow-left`).addEventListener('click', clickLeft);

		function clickRight(){
			if(countList < count){
				position += -1 * width;
				List.style.marginLeft = position + 'px';
				countList++;
			}
		}
		function clickLeft() {
			if(countList > 0){
				position += width;
				List.style.marginLeft = position + 'px';
				countList--;
			}
		}
	}

	if($('.companies__logos')) bestsellerSlider('companies__logos', 195, 4);
	if($('.bestsellers')) bestsellerSlider('bestsellers', 262, 2);
})();