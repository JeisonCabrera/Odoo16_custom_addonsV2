# -*- coding: utf-8 -*-
from odoo import models, fields, api

class custom_contactos(models.Model):
    _inherit = 'res.partner'

    vertical_mercado = fields.Selection([
        ('key', 'value')
    ], string='VERTICAL DE MERCADO')