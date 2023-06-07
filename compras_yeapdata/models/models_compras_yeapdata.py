# -*- coding: utf-8 -*-
from odoo import models, fields, api

class valores_onetime(models.Model):
    _name = 'valores.onetime'
    _description = 'valores.onetime'

    name = fields.Char('Nombre')
    centro_costos_id = fields.Many2one(comodel_name='centro.costos', string='Centro de Costos')
    procesos_id = fields.Many2one(comodel_name='procesos', string='Procesos')
    valor = fields.Float('Valor')
    clave_id = fields.Many2one('purchase.order', string='Clave')

class valores_recurrentes(models.Model):
    _name = 'valores.recurrentes'
    _description = 'valores.recurrentes'

    name = fields.Char('Nombre')
    centro_costos_id = fields.Many2one(comodel_name='centro.costos', string='Centro de Costos')
    procesos_id = fields.Many2one(comodel_name='procesos', string='Procesos')
    valor = fields.Float('Valor')
    clave_id = fields.Many2one('purchase.order', string='Clave')

class centro_costos(models.Model):
    _name = 'centro.costos'
    _description = 'centro.costos'

    name = fields.Char('Centro de Costos')

class procesos(models.Model):
    _name = 'procesos'
    _description = 'procesos'

    name = fields.Char('Procesos')

class detalle_oc(models.Model):
    _name = 'detalle.oc'
    _description = 'detalle.oc'

    name = fields.Char('Parte')
    qty = fields.Integer('QTY')
    precio_unitario = fields.Float('Precio Unitario')
    descripcion = fields.Text('Descripción')
    precio_total = fields.Float(compute='_compute_precio_total', string='Precio Total')
    
    @api.depends('qty', 'precio_unitario')
    def _compute_precio_total(self):
        for record in self:
            record.precio_total = record.qty * record.precio_unitario
            
    clave_id = fields.Many2one('purchase.order', string='Clave')

class tratamiento_datos(models.Model):
    _name = 'tratamiento.datos'
    _description = 'tratamiento.datos'

    name = fields.Char('NOMBRE')
    condiciones_oc = fields.Html('CONDICIONES GENERALES DE LA ORDEN DE COMPRA')   