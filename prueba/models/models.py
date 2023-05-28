# -*- coding: utf-8 -*-
from odoo import models, fields, api

class x_prueba(models.Model):
    _inherit = 'product.template'

    x_value = fields.Integer() 
    x_centro_costos_onetime = fields.One2many('centro.costos.onetime', 'x_clave', string='Centro de costos One Time')
    

class x_centro_costos_onetime(models.Model):
    _name = 'centro.costos.onetime'
    _description = 'centro.costos.onetime'

    x_clave = fields.Many2one('product.template')
    x_name = fields.Char('Nombre')
    x_centro_costos = fields.Many2one('centro.costos', 'Centro de costos')
    x_proces = fields.Many2one('procesos', 'Procesos')
    x_valor = fields.Float('Valor')
    
    


class x_centro_costos(models.Model):
    _name = 'centro.costos'
    _description = 'centro.costos'

    x_centro = fields.Char('Centro de costos')

class x_procesos(models.Model):
    _name = 'procesos'
    _description = 'procesos'
    
    x_procesos = fields.Char('Procesos')
    
#comentarios    
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
