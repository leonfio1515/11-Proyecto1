    var promoButtons = document.querySelectorAll('.card-promo .btn');

    // Asignamos el evento click a cada botón
    promoButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Obtenemos la información de la promoción correspondiente
            var cardPromo = this.querySelector('.card-promo');
            var medioPromo = cardPromo.querySelector('h4').innerText;
            var valorPromo = cardPromo.querySelector('h5').innerText;
            var descripcionPromo = cardPromo.querySelector('h3').innerText;
            var imagenPromo = cardPromo.querySelector('img').src;
            var fechaFinPromo = cardPromo.querySelector('.th-card').innerText;
            var condicionesPromo = cardPromo.nextElementSibling.innerText.trim();
            var condiciones2Promo = cardPromo.nextElementSibling.nextElementSibling.innerText.trim();

            // Asignamos los valores de la promoción al modal
            var modalTitlePromo = document.querySelector('.modal-title-promo');
            modalTitlePromo.innerText = medioPromo + ' ' + valorPromo;
            var modalBodyPromo = document.querySelector('.modal-body-promo');
            modalBodyPromo.querySelector('h3').innerText = descripcionPromo;
            modalBodyPromo.querySelector('img').src = imagenPromo;
            modalBodyPromo.querySelector('h4').innerText = 'Fecha fin: ' + fechaFinPromo;
            modalBodyPromo.querySelector('h4 + br + hr + h3').innerText = 'CONDICIONES:';
            modalBodyPromo.querySelector('h4 + br + hr + h4').innerText = condicionesPromo;
            modalBodyPromo.querySelector('h4 + br + h4').innerText = condiciones2Promo;

            // Abrimos el modal
            var modalCreate = document.querySelector('#modal-create');
            var modal = new bootstrap.Modal(modalCreate);
            modal.show();
        });
    });