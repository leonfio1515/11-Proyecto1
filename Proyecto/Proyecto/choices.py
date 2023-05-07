##################CHOICES FRAUDE##################################
estado_mercaderia = (
    ("Entregado", "Entregado"),
    ("No entregado", "No entregado"),
)

estado_pago = (
    ("Descontado", "Descontado"),
    ("No descontado", "No descontado"),
)

##################CHOICES GENERAL##################################
estado_chequera = (
    ("En uso", "En uso"),
    ("Terminada", "Terminada"),
)

empresas = (
    ("Cybe", "Cybe"),
    ("Wermax", "Wermax"),
)

monedas = (
    ("Pesos", "Pesos"),
    ("Dolares", "Dolares"),
)

tipo_cheque = (
    ("Al dia", "Al dia"),
    ("Diferidos", "Diferidos"),
)

mes = (
    ("Enero", "Enero"),
    ("Febrero", "Febrero"),
    ("Marzo", "Marzo"),
    ("Abril", "Abril"),
    ("Mayo", "Mayo"),
    ("Junio", "Junio"),
    ("Julio", "Julio"),
    ("Agosto", "Agosto"),
    ("Septiembre", "Septiembre"),
    ("Octubre", "Octubre"),
    ("Noviembre", "Noviembre"),
    ("Diciembre", "Diciembre")
)

sexo = (
    ("Hombre", "Hombre"),
    ("Mujer", "Mujer"),
)

estado_funcionario = (
    ("Activo", "Activo"),
    ("Deudor", "Deudor"),
    ("Egreso", "Egreso"),
    ("Seg_Paro", "Seg_Paro"),
    ("Seg_Medico", "Seg_Medico"),
    ("Nuevo Ingreso", "Nuevo Ingreso"),

)
#######################################################################
estado_pedido = (
    ("Pendiente", "Pendiente"),
    ("En curso", "En curso"),
    ("Resuelto", "Resuelto"),
)

autorizacion = (
    ("Si", "Si"),
    ("No", "No"),
    ("Pendiente", "Pendiente"),
)

cuotas = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)
#####################CHOICE CAMBIO##################
monedas_ch = (
    (0, 0),
    (100, 100),
    (200, 200),
    (300, 300),
    (400, 400),
    (500, 500),
    (600, 600),
    (700, 700),
    (800, 800),
    (900, 900),
    (1000, 1000),
)

monedas_gr = (
    (0, 0),
    (500, 500),
    (1000, 1000),
    (1500, 1500),
    (2000, 2000),
)

billetes = (
    (0, 0),
    (1000, 1000),
    (2000, 2000),
    (3000, 3000),
    (4000, 4000),
    (5000, 5000),
    (6000, 6000),
    (7000, 7000),
    (8000, 8000),
    (9000, 9000),
    (10000, 10000),
)
#####################CHOICE CAJAS##################
promo_promotora = (
    ("No", "No"),
    ("Si", "Si"),
)

estado_reclamo = (

    ("Retirado", "Retirado"),
    ("Rechazado", "Rechazado"),
    ("Pendiente Retiro", "Pendiente Retiro"),
    ("Cerrado", "Cerrado"),
)

tipo_reclamo = (

    ("Reclamo", "Reclamo"),
    ("Devolucion", "Devolucion"),
)


###############  POR VER ##########################
descuentos = (
    ("18.03", "18.03"),
    ("20", "20"),
    ("25", "25"),
)

tema_noticia = (
    ("Pago Sueldos", "Pago Sueldos"),
    ("Pago Aguinaldo", "Pago Aguinaldo"),
    ("Beneficios Funcionarios", "Beneficios Funcionarios"),
    ("Comunicado General", "Comunicado General"),
    ("Campaña", "Campaña"),
)

camisa_abrigo = (
    ("No solicita", "No solicita"),
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
    ("2XL", "2XL"),
    ("3XL", "3XL"),
    ("4XL", "4XL"),
    ("5XL", "5XL"),
)

pantalon = (
    ("No solicita", "No solicita"),
    ("36", "36"),
    ("38", "38"),
    ("40", "40"),
    ("42", "42"),
    ("44", "44"),
    ("46", "46"),
    ("48", "48"),
    ("50", "50"),
    ("52", "52"),
    ("54", "54"),
    ("Maternal", "Maternal"),
)


tipo_doc_finan = (
    ("Factura", "Factura"),
    ("Resguardo", "Resguardo"),
    ("Liquidacion", "Liquidacion"),
    ("NC", "NC"),
)

estado_doc_finan_est = (
    ("OK", "OK"),
    ("REVISAR", "REVISAR"),
)

estado_doc_finan = (
    ("CORREGIDO", "CORREGIDO"),
    ("NO CORREGIDO", "NO CORREGIDO"),
)


prioridad = (
    ("Alta", "Alta"),
    ("Media", "Media"),
    ("Baja", "Baja"),
)

#######################################################
tipo_actualiza = (
    ("Correccion", "Correccion"),
    ("Modificacion", "Modificacion"),
    ("Creacion", "Creacion"),
)

rol = (
    ("Encargado", "Encargado"),
    ("Funcionario", "Funcionario"),
    ("Referente", "Referente"),
)

tipo_pago = (
    ("Al dia", "Al dia"),
    ("Mensual", "Mensual"),
)

pago_prov = (
    ("Cheque", "Cheque"),
    ("Transferencia", "Transferencia"),
)