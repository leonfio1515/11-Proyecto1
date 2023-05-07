$(function () {
    $('#tabla').DataTable({
        "language": {
            url: "{% static 'lib/DataTables/js/spanish.txt' %}"
        },
        responsive: true,
        dom: 'Bfrtilp',
        order: [[0, 'asc']],
        buttons: [{
            extend: 'excelHtml5',
            text: '<i class="bi bi-file-earmark-excel"></i>',
            titleAttr: 'Exportar a Excel',
            className: 'btn btn-success',
        }],
    });
}); 