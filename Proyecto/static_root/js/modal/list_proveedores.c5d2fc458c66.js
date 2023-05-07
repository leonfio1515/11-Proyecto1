$(function () {
    var tablaList = $('#tabla').DataTable({
        "language": {
            url: "{% static 'lib/DataTables/js/spanish.txt' %}"
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

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        $('form')[0].reset();
        $('#modal-create').modal('show');
    });

    $('.btnEdit').on('click', function () {
        var data = tablaList.row($(this).parents('tr')).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data[0]);
        $('input[name="proveedor"]').val(data[2]);
        $('#id_importe').val(data[3]);
        $('#id_documentos').val(data[4]);
        $('#id_comentarios').val(data[5]);
        $('#modal-create').modal('show');
    });
   

    $('.btnConf').on('click', function () {
        var data = tablaList.row($(this).parents('tr')).data();
   
        console.log(data);
        $('input[name="action"]').val('confirm');
        $('input[name="id"]').val(data[0]);
        $('form')[0].reset();
        $('#modal-confirm').modal('show', function(){
            window.location.reload();
        });
    });
    
    
    $('.btnDel').on('click', function () {
        var data = tablaList.row($(this).parents('tr')).data();

        var parameters = new FormData();
        parameters.append('action','delete');
        parameters.append('id', data[0]);

        jqueryconfirm(window.location.pathname, 'Notificacion', 'Estas seguro que desea eliminar?', parameters, function () {
            window.location.reload();
        });
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