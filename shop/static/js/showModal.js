(function () {
  let modalWindow = document.querySelector('.modal-window-wrapper');
  document.querySelector('.goods-container').onclick = function (event) {
    let target = event.target;
    if(target.matches('.fa-search-plus')){
      document.body.style.overflow = 'hidden';
      //modalWindow.style.top = window.pageYOffset + 'px'
    }
  }
})();