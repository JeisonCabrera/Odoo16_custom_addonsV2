# -*- coding: utf-8 -*-
from odoo import models, fields, api

class custom_contactos(models.Model):
    _inherit = 'res.partner'

    vertical_mercadox = fields.Selection([
        ('educacion', 'Educación'),
        ('financiero', 'Financiero'),
        ('gobierno', 'Gobierno'),
        ('health', 'Health'),
        ('hospitality', 'Hospitality'),
        ('industria_comercio', 'Industria y Comercio'),
        ('outsources_BPO', 'Outsources / BPO'),
        ('pendiente', 'PENDIENTE'),
        ('petroleo_gricultura', 'Petróleo / Agricultura / Minería / Ganadería'),
        ('recursos_enovables', 'Recursos Renovables'),
        ('servicios', 'Servicios'),
        ('transporte', 'Transporte'),
        ('retail', 'Retail')
    ], string='VERTICAL DE MERCADO')