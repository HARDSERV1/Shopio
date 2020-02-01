(function () {
      let modalWindow = document.querySelector('.modal-window-wrapper');
      
      function showModal() {
        document.querySelector('.goods-container').onclick = function (event) {
          let target = event.target;
          if(target.matches('.fa-search-plus')){
            event.preventDefault();
            document.body.style.overflow = 'hidden';
            modalWindow.style.top = window.pageYOffset + 'px'
            modalWindow.style.display = 'block';
          }
        }  
      }

      function hideModal() {
        modalWindow.onclick = function (event) {
          if(event.target == this){
            this.style.display = '';
            document.body.style.overflow = '';
          }
        }
        document.querySelector('.close-btn').onclick = function () {
          modalWindow.style.display = '';
          document.body.style.overflow = '';
        }
      }

      function switchPhotos() {
          let photoBlock = modalWindow.querySelector('.photos');
          let mainImage = modalWindow.querySelector('.mainImage');

          photoBlock.onclick = function (event) {
            let tg = event.target;
            if(tg.tagName == "IMG"){
              mainImage.src = tg.dataset.bigImg;
              this.querySelectorAll('img').forEach(item => item.classList.remove('active'));
              tg.classList.add('active');
            }
          }
      }
      showModal();
      hideModal();
      switchPhotos();
})();