# -*- coding: utf-8 -*-
from odoo import models, fields, api

class prueba(models.Model):
    _inherit = 'product.template'

    x_value = fields.Integer()

class prueba_technical(models.Model):
    _name = 'prueba.technical'
    _description = 'prueba.technical'

    name = fields.Char()
    value = fields.Integer()
    
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