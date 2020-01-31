(function () {
      let modalWindow = document.querySelector('.modal-window-wrapper');
      document.querySelector('.goods-container').onclick = function (event) {
        let target = event.target;
        if(target.matches('.fa-search-plus')){
          document.body.style.overflow = 'hidden';
          modalWindow.style.top = window.pageYOffset + 'px'
          modalWindow.style.display = 'block';
          //func('{{ g.name }}','{{ g.info }}','{{ g.current_price }}','{{ g.old_price }}','{{ MEDIA_URL }}{{ g.image.url }}';
        }
      }

      function getInfo(name,info,cur_price,old_price,image){
            document.getElementById('mg-name').innerText = name;
            document.getElementById('mg-info').innerText = info;
            document.getElementById('mg-current_price').innerText = "$"+cur_price;
            document.getElementById('mg-old_price').innerText = "$"+old_price;
            document.getElementById('mg-image').src = image;
        }  
})();