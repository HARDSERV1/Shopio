(function () {
	let upBtn = $('#up__bttn');
	upBtn.click(function (event) {
		window.scrollTo(0, 0);
	});

	$(window).scroll(function (event) {
		if(window.pageYOffset > 315){
			upBtn.show();
		}else upBtn.hide();
	})
})();