var url_spanish = '../../static/lib/DataTables/js/spanish.txt'

$(function () {
    var tablaList = $('#tabla').DataTable({
        "language": {
            url: url_spanish
        },
        responsive: true,
        dom: 'Bfrtilp',
        order: [[0, 'desc']],
        buttons: [{
            extend: 'excelHtml5',
            text: '<i class="bi bi-file-earmark-excel"></i>',
            titleAttr: 'Exportar a Excel',
            className: 'btn btn-success',
        }],
    });


    $('.btnEdit').on('click', function () {
        var data = tablaList.row($(this).parents('tr')).data();
        console.log(data);
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data[2]);

        $('#modal-edit').modal('show');
    });

    

    $('#Form-form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        jqueryconfirm(window.location.pathname, 'Notificacion', 'Estas seguro que desea guardar?', parameters, function () {
            $('#modal-create').modal('hide');
            window.location.reload();
        });
    });
}); 