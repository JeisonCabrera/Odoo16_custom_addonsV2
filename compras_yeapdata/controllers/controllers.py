# -*- coding: utf-8 -*-
# from odoo import http


# class ComprasYeapdata(http.Controller):
#     @http.route('/compras_yeapdata/compras_yeapdata', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compras_yeapdata/compras_yeapdata/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('compras_yeapdata.listing', {
#             'root': '/compras_yeapdata/compras_yeapdata',
#             'objects': http.request.env['compras_yeapdata.compras_yeapdata'].search([]),
#         })

#     @http.route('/compras_yeapdata/compras_yeapdata/objects/<model("compras_yeapdata.compras_yeapdata"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compras_yeapdata.object', {
#             'object': obj
#         })
