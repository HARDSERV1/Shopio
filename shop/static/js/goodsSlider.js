(function () {

	function goodsElectronic(selector) {
		let goodsList = document.querySelector(`.${selector} .goods-list ul`);
		let count = 0, position = 0;

		document.querySelector('.goods-list .arrow-right').addEventListener('click', clickRight);
		document.querySelector('.goods-list .arrow-left').addEventListener('click', clickLeft);

		function clickRight(){
			if(count < 2){
				position += -222;
				goodsList.style.marginLeft = position + 'px';
				count++;
			}
		}
		function clickLeft() {
			if(count > 0){
				position += 222;
				goodsList.style.marginLeft = position + 'px';
				count--;
			}
		}
	}
	goodsElectronic('section-electronic');
	goodsElectronic('section-f');
})();
