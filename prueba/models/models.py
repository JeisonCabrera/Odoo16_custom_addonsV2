# -*- coding: utf-8 -*-
from odoo import models, fields, api

class x_prueba(models.Model): 
    _inherit = 'product.template' #Modelo puchase.order

    x_value = fields.Integer() 
    x_centro_costos_onetime_ids = fields.One2many('centro.costos.onetime', 'x_clave_id', string='Centro de costos One Time') #Campo orden_line
    
class x_centro_costos_onetime(models.Model): 
    _name = 'centro.costos.onetime'                 #Modelo purchase.order.line
    _description = 'centro.costos.onetime'

    name = fields.Char('Nombre')
    x_centro_costos_id = fields.Many2one(comodel_name='centro.costos', string='Centro de Costos')  #Campo product_id    , change_default=True, index='btree_not_null', widget='list.many2one'
    x_proces_id = fields.Many2one('procesos', string='Procesos')
    x_valor = fields.Float('Valor')
    x_clave_id = fields.Many2one('product.template', string='ReferenceXXX') #, index=True, required=True, ondelete='cascade'
    productxx_id = fields.Char(string='ProductXXX', related='x_centro_costos_id.name') #ya me trae el valor del centro de costo
  
# class prueba(models.Model):
#     _name = 'prueba.prueba'
#     _description = 'prueba.prueba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
