(function () {
	function chose(blockSelector, changeSelector) {
		let block = document.querySelector(`${blockSelector}`);
		let changeList = document.querySelector(`${changeSelector}`);

		block.onmouseenter = function (event) {
			let blockCoords = block.getBoundingClientRect();
			changeList.style.top = blockCoords.bottom +
			window.pageYOffset + 'px';
			changeList.style.left = blockCoords.left + 'px';
			changeList.classList.remove('unvisible');
		}
		block.onmouseleave = function (event) {
			changeList.classList.add('unvisible');
		}
	}
	chose('.preline__section .lg-block', '.switch-lg');
	chose('.preline__section .currency-block', '.switch-currency');
})();