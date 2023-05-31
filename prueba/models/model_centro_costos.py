# -*- coding: utf-8 -*-
from odoo import models, fields, api

class x_centro_costos(models.Model):
    _name = 'centro.costos'
    _description = 'centro.costos'

    name = fields.Char('Centro de Costos')

class x_procesos(models.Model):
    _name = 'procesos'
    _description = 'procesos'
    
    name = fields.Char('Proceso')