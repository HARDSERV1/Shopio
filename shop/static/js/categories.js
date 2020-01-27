
(function(){
	function plusOptions(){
		let moreBtn = document.querySelector('.more-btn');
		let categoryList = document.querySelectorAll('.hide-option');
		let icon = document.querySelector('.fa-plus');

		moreBtn.onclick = function(event){

			if(this.firstChild.data == 'More Categories'){
				this.firstChild.data = 'Close Menu';
				icon.className = 'fa fa-minus';
			}else{
				this.firstChild.data = 'More Categories';
				icon.className = 'fa fa-plus';
			} 
			for(let item of categoryList) item.classList.toggle('unvisible');
		}
	}

	function addMenus(){
		let firstListItem = document.querySelector('.first-list-item');
		let secondListItem = document.querySelector('.second-list-item');
		let thirdListItem = document.querySelector('.third-list-item');

		let firstBlockMenu = document.querySelector('.first');
		let secondBlockMenu = document.querySelector('.second');
		let thirdBlockMenu = document.querySelector('.third');

		let categoriesBlock = document.querySelector('.categories');

		let firstlistItemCoords = firstListItem.getBoundingClientRect();
		firstBlockMenu.style.top = firstlistItemCoords.top + 'px';
		firstBlockMenu.style.left = firstlistItemCoords.right + 'px';

		let secondlistItemCoords = secondListItem.getBoundingClientRect();
		secondBlockMenu.style.top = secondlistItemCoords.top + 'px';
		secondBlockMenu.style.left = secondlistItemCoords.right + 'px';

		let thirdlistItemCoords = thirdListItem.getBoundingClientRect();
		thirdBlockMenu.style.top = thirdlistItemCoords.top + 'px';
		thirdBlockMenu.style.left = thirdlistItemCoords.right + 'px';

		firstListItem.onmouseenter = function (event) {
			firstBlockMenu.classList.remove('unvisible');
		}

		secondListItem.onmouseenter = function (event) {
			secondBlockMenu.classList.remove('unvisible');
		}

		thirdListItem.onmouseenter = function (event) {
			thirdBlockMenu.classList.remove('unvisible');
		}

		categoriesBlock.onmouseout = function (event) {
			if(event.relatedTarget.closest('.first') != firstBlockMenu){
				firstBlockMenu.classList.add('unvisible');
			}
			if(event.relatedTarget.closest('.second') != secondBlockMenu){
				secondBlockMenu.classList.add('unvisible');
			}
			if(event.relatedTarget.closest('.third') != thirdBlockMenu){
				thirdBlockMenu.classList.add('unvisible');
			}	
		}
	}

	plusOptions();
	addMenus();
})();