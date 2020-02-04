(function () {
	function chose(blockSelector, changeSelector) {
		let block = $(`${blockSelector}`);
		let changeList = $(`${changeSelector}`);
		let coords = document.querySelector('.search__button').getBoundingClientRect();
		changeList.css('left', coords.left);
		changeList.css('top', coords.bottom);

		block.mouseenter(function (event) {
			changeList.slideDown(300);
		});

		block.mouseleave(function (event) {
			changeList.slideUp(300);
		});
	}
	chose('.shopping__cart', '.chosenGoods');
})();