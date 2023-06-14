# -*- coding: utf-8 -*-
{
    'name': 'Compras Yeapdata',

    'summary': 'Personaliza las ordenes de compra',

    'description': 'Personalización del modulo de compras de acuerdo a los requerimientos de Yeapdata',

    'author': 'Jeison Cabrera',
    'website': '',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    # 'category': 'Inventory/Purchase',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'contacts', 'hr'],

    # always loaded
    'data': [
        'security/purchase_yeapdada_security.xml',
        'security/ir.model.access.csv',
        'views/custom_view_purchase_order_form.xml',
        'views/custom_view_res_partener_form.xml',
        'report/custom_report_oc_yeapdata.xml',
        'report/custom_report_oc_yeapdata_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,

    'sequence': -100,
}
