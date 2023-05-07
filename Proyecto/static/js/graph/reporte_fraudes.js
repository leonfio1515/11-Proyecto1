// Data retrieved from https://netmarketshare.com/
// Radialize the colors
Highcharts.setOptions({
    colors: Highcharts.getOptions().colors.map(function(color) {
        return {
            radialGradient: {
                cx: 0.5,
                cy: 0.3,
                r: 0.7
            },
            stops: [
                [0, color],
                [1, Highcharts.color(color).brighten(-0.4).get('rgb')] // darken
            ]
        };
    })
});

// Build the chart
var graphPieFinan = Highcharts.chart('container-pie-finan', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Fraudes segun financiera',
        align: 'left'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                connectorColor: 'silver'
            }
        }
    },
});

var graphPieEstPago = Highcharts.chart('container-pie-est-pago', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Estado pago',
        align: 'left'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                connectorColor: 'silver'
            }
        }
    },
});

var graphPieEstEntrega = Highcharts.chart('container-pie-est-entrega', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Estado entrega',
        align: 'left'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                connectorColor: 'silver'
            }
        }
    },
});

var graphBarsAno = Highcharts.chart('container-bars', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Fraudes por mes'
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: [
            'Ene',
            'Feb',
            'Mar',
            'Abr',
            'May',
            'Jun',
            'Jul',
            'Ago',
            'Sep',
            'Oct',
            'Nov',
            'Dic',
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Totales $'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
});

function graph_bars_ano(){
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action':'graph_bars_ano'},
        dataType: 'json',
    }).done(function(data){
        $.each(data, function(i, series){
            graphBarsAno.addSeries(series);
        });
        return false;
    }).fail(function(jqXHR, textStatus, errorThrown){
        alert(textStatus + ': '+errorThrown);
    }).always(function(data){

    });
}

function graph_pie_finan(){
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action':'graph_pie_finan'},
        dataType: 'json',
    }).done(function(data){
        graphPieFinan.addSeries(data);
        return false;
    }).fail(function(jqXHR, textStatus, errorThrown){
        alert(textStatus + ': '+errorThrown);
    }).always(function(data){

    });
}

function graph_pie_est_pago(){
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action':'graph_pie_est_pago'},
        dataType: 'json',
    }).done(function(data){
        graphPieEstPago.addSeries(data);
        return false;
    }).fail(function(jqXHR, textStatus, errorThrown){
        alert(textStatus + ': '+errorThrown);
    }).always(function(data){

    });
}

function graph_pie_est_entrega(){
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action':'graph_pie_est_entrega'},
        dataType: 'json',
    }).done(function(data){
        graphPieEstEntrega.addSeries(data);
        return false;
    }).fail(function(jqXHR, textStatus, errorThrown){
        alert(textStatus + ': '+errorThrown);
    }).always(function(data){

    });
}
