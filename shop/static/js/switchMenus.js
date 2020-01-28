(function () {
	function switchMenus(selector) {
		let nav = document.querySelector(`.${selector} .navigation`);
		let options = nav.querySelectorAll('a');

		let lists = document.querySelectorAll(`.${selector} .menu-wrapper`);
		nav.onclick = function (event) {
			let tg = event.target;
			if(tg.tagName == 'A'){
				event.preventDefault();
				
				options.forEach(item => item.classList.remove('active'));
				tg.classList.add('active');

				lists.forEach(item => item.classList.remove('visibleGoods'));
				
				for(let item of lists){
					if(item.dataset.item == tg.dataset.item){
						item.classList.add('visibleGoods');
					}
				}
			}
		}
	}	
	switchMenus('section-electronic');			
})();