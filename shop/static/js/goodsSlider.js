(function () {

	let menuSelectors = ['first', 'second', 'third'];
	let bigMenuSelector = ['first', 'second', 'third', 'forth'];

	function goodsElectronic(selector, atrSelector, width) {
		let goodsList = document.querySelector(`.${selector} .goods-list div[data-item="${atrSelector}"] ul`);
		let count = 0, position = 0;

		document.querySelector(`.${selector} .goods-list div[data-item="${atrSelector}"] .arrow-right`).addEventListener('click', clickRight);
		document.querySelector(`.${selector} .goods-list div[data-item="${atrSelector}"] .arrow-left`).addEventListener('click', clickLeft);

		function clickRight(){
			if(count < 2){
				position += -1 * width;
				goodsList.style.marginLeft = position + 'px';
				count++;
			}
		}
		function clickLeft() {
			if(count > 0){
				position += width;
				goodsList.style.marginLeft = position + 'px';
				count--;
			}
		}
	}
	menuSelectors.forEach(item => goodsElectronic('section-electronic', item, 220));
	bigMenuSelector.forEach(item => goodsElectronic('section-computer', item, 220));
	bigMenuSelector.forEach(item => goodsElectronic('section-smartphone', item, 220));
	menuSelectors.forEach(item => goodsElectronic('goods-bottom-cotainer', item, 283));
})();
