
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

	function addMenu(){
		let firstListItem = document.querySelector('.first-list-item');
		let firstBlockMenu = document.querySelector('.first-item');
		let categoriesBlock = document.querySelector('.categories');

		let listItemCoords = firstListItem.getBoundingClientRect();
		firstBlockMenu.style.top = listItemCoords.top + 'px';
		firstBlockMenu.style.left = listItemCoords.right + 'px';

		firstListItem.onmouseenter = function (event) {
			firstBlockMenu.classList.remove('unvisible');
		}
		categoriesBlock.onmouseout = function (event) {
			if(event.relatedTarget.closest('.first-item') != firstBlockMenu){
				firstBlockMenu.classList.add('unvisible');
			}
		}
	}

	plusOptions();
	addMenu();
})();