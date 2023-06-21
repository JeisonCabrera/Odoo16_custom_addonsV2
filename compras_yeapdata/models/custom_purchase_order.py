# -*- coding: utf-8 -*-
from odoo import models, fields, api

class compras_yeapdata(models.Model):
    _inherit = 'purchase.order'

    #Contacto relacionado con proveedor
    contacto_proveedor_id = fields.Many2one('res.partner', string='CONTACTO', domain="[('parent_id', '=', partner_id)]")
    #Direccion de factura
    contacto_factura_id = fields.Many2one('res.partner', string='FACTURACIÓN', domain="['&', ('parent_id', '=', company_id), ('type', '=', 'invoice')]")
    Orden_compra_emergencia  = fields.Boolean('Orden de compra de emergencia')

    #Informacion General

    canal = fields.Char(string='CANAL')
    linea_producto = fields.Char(string='LÍNEA DE PRODUCTO', related='product_id.categ_id.name')
    producto = fields.Char(string='PRODUCTO', related='product_id.name')
    descripcion_producto = fields.Char(string='DESCRIPCIÓN PRODUCTO')
    qrn_tid_cotizacion = fields.Char(string='QRN-TID-COTIZACIÓN')
    ship_to_ipa = fields.Char(string='SHIP TO-IPA')
    fk = fields.Char(string='FK')
    orden_compra_cliente = fields.Char(string='ORDEN DE COMPRA - CLIENTE')
    razon_social_cliente_id = fields.Many2one('res.partner', string='RAZÓN SOCIAL - CLIENTE')
    nit = fields.Char(string='NIT', related='razon_social_cliente_id.vat')
    contacto_cliente_id = fields.Many2one('res.partner', string='CONTACTO', domain="[('parent_id', '=', razon_social_cliente_id)]")
    telefono = fields.Char(string='TELÉFONO', related='razon_social_cliente_id.phone')
    direccion_envio = fields.Char(string='DIRECCIÓN DE ENVÍO', related='razon_social_cliente_id.street')
    vertical_mercado = fields.Selection(string='VERTICAL DE MERCADO', readonly=True, related='razon_social_cliente_id.vertical_mercadox') #CREAR CAMPO EN CONTACTOS PARA RELACIONARLO ACÁ

    #Valores y Observaciones
    tipo_orden = fields.Selection([
        ('proyectos', 'Proyectos'),
        ('servicios', 'Servicios'),
        ('yeapdata', 'Yeapdata')
    ], string='TIPO DE ORDEN')
    nombre_proyecto = fields.Char(string='NOMBRE DEL PROYECTO')
    fecha_finalizacion_contrato = fields.Date('FECHA DE FINALIZACIÓN DE CONTRATO')

    #VALORES ONE TIME
    valore_onetime_ids = fields.One2many('valores.onetime', 'clave_id', string='VALORES ONE TIME')
    # centro_cotos_onetime = fields.Char('CENTRO DE COSTOS ONE TIME', index=True, copy=False, readonly=False)
    centro_cotos_onetime = fields.Char(compute='_compute_centro_costos_onetime', string='CENTRO DE COSTOS ONE TIME', store=True)
    @api.depends('valore_onetime_ids.centro_costos_id.name')
    def _compute_centro_costos_onetime(self):
        for order in self:
            order.centro_cotos_onetime = ', '.join(order.valore_onetime_ids.centro_costos_id.mapped('name'))

    # valor_oc_onetime = fields.Float('VALOR OC')
    valor_oc_onetime = fields.Float(compute='_compute_valor_oc_onetime', string='VALOR OC')
    @api.depends('valore_onetime_ids.valor')
    def _compute_valor_oc_onetime(self):
        for order in self:
            order.valor_oc_onetime = sum(order.valore_onetime_ids.mapped('valor'))

    moneda_onetime_id = fields.Many2one('res.currency', string='MONEDA')
    trm_onetime = fields.Float(string='TRM', default='1')
    valor_oc_pesos_onetime = fields.Float(compute='_compute_valor_oc_pesos_onetime', store=True, string='VALOR DE OC EN PESOS')
    @api.depends('valor_oc_onetime', 'trm_onetime')
    def _compute_valor_oc_pesos_onetime(self):
        for record in self:
            record.valor_oc_pesos_onetime = record.valor_oc_onetime * record.trm_onetime
    
    #VALORES RECURRENTES
    valore_recurrentes_ids = fields.One2many('valores.recurrentes', 'clave_id', string='VALORES RECURRENTES')
    centro_cotos_recurrente = fields.Char(compute='_compute_centro_cotos_recurrente', string='CENTRO DE COSTOS RECURRENTES', store=True)
    @api.depends('valore_recurrentes_ids.centro_costos_id.name')
    def _compute_centro_cotos_recurrente(self):
        for order in self:
            order.centro_cotos_recurrente = ', '.join(order.valore_recurrentes_ids.centro_costos_id.mapped('name'))

    valor_oc_recurrente = fields.Float(compute='_compute_valor_oc_recurrente', string='VALOR OC')
    @api.depends('valore_recurrentes_ids.valor')
    def _compute_valor_oc_recurrente(self):
        for order in self:
            order.valor_oc_recurrente = sum(order.valore_recurrentes_ids.mapped('valor'))

    moneda_recurrente_id = fields.Many2one('res.currency', string='MONEDA')
    trm_recurrente = fields.Float(string='TRM', default='1')

    valor_oc_pesos_recurrente = fields.Float(compute='_compute_valor_oc_pesos_recurrente', store=True, string='VALOR DE OC EN PESOS')
    @api.depends('valor_oc_recurrente', 'trm_recurrente')
    def _compute_valor_oc_pesos_recurrente(self):
        for record in self:
            record.valor_oc_pesos_recurrente = record.valor_oc_recurrente * record.trm_recurrente

    tiempo_meses_recurrente = fields.Integer(string='TIEMPO EN MESES', default='1')

    valor_cuota_recurrente = fields.Float(compute='_compute_valor_cuota_recurrente', string='VALOR CUOTA')
    @api.depends('valor_oc_recurrente','tiempo_meses_recurrente')
    def _compute_valor_cuota_recurrente(self):
        for record in self:
            record.valor_cuota_recurrente = record.valor_oc_recurrente / record.tiempo_meses_recurrente

    valor_cuota_pesos_recurrente = fields.Float(compute='_compute_valor_cuota_pesos_recurrente', string='VALOR CUOTA EN PESOS')
    @api.depends('valor_oc_pesos_recurrente','tiempo_meses_recurrente')
    def _compute_valor_cuota_pesos_recurrente(self):
        for record in self:
            record.valor_cuota_pesos_recurrente = record.valor_oc_pesos_recurrente / record.tiempo_meses_recurrente

    #OBSERVACIONES
    observaciones = fields.Text('OBSERVACIONES')
    solicitado_por_id = fields.Many2one('hr.employee', string='SOLICITADO POR')
    autorizo_id = fields.Many2one('hr.employee', string='AUTORIZO')
    elaborado_por = fields.Char(string='ELABORADO POR', related='user_id.name')

    #Detalles de Orden de compra
    detalle_oc_ids = fields.One2many('detalle.oc', 'clave_id', string=' ')
    imagenv2 = fields.Binary('Imagen')
    
    #Tratamiento de datos
    tratamiento_datos_id = fields.Many2one('tratamiento.datos', string='TRATAMIENTO DE DATOS')
    
    # Resumen
    tiempo_related = fields.Integer('TIEMPO EN MESES', related='tiempo_meses_recurrente')
    centro_costos_ot_related = fields.Char('CENTRO DE COSTOS ONE TIME', related="centro_cotos_onetime")
    centro_costos_rec_related = fields.Char('CENTRO DE COSTOS RECURRENTES', related="centro_cotos_recurrente")
    fecha_finalizacion_contrato_related = fields.Date('FECHA DE FINALIZACIÓN DE CONTRATO', related='fecha_finalizacion_contrato')


    valor_total_oc = fields.Char(compute='_compute_valor_total_oc', string='VALOR TOTAL OC')
    @api.depends('valor_oc_onetime', 'valor_oc_recurrente')
    def _compute_valor_total_oc(self):
        for record in self:
            record.valor_total_oc = record.valor_oc_onetime + record.valor_oc_recurrente

    valor_total_oc_pesos = fields.Float(compute='_compute_valor_total_oc_pesos', string='VALOR TOTAL OC EN PESOS')
    @api.depends('valor_oc_pesos_onetime', 'valor_oc_pesos_recurrente')
    def _compute_valor_total_oc_pesos(self):
        for record in self:
            record.valor_total_oc_pesos = record.valor_oc_pesos_onetime + record.valor_oc_pesos_recurrente

    nombre_orden_compra = fields.Char(compute='_compute_nombre_orden_compra', string='nombre_orden_compra')
    @api.depends('name', 'tipo_orden', 'partner_id', 'razon_social_cliente_id', 'nombre_proyecto', 'Orden_compra_emergencia')
    def _compute_nombre_orden_compra(self):
        for record in self:
            if record.Orden_compra_emergencia == True:
                record.nombre_orden_compra = 'OC-EMR-%s-%s-%s-%s-%s' %(record.name, record.tipo_orden[:4], record.partner_id.name[:7], record.razon_social_cliente_id.name[:10], record.nombre_proyecto[:15])
            else: 
                record.nombre_orden_compra = 'OC-%s-%s-%s-%s-%s' %(record.name, record.tipo_orden[:4], record.partner_id.name[:7], record.razon_social_cliente_id.name[:10], record.nombre_proyecto[:15])
