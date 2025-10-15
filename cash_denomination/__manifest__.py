# -*- coding: utf-8 -*-
{
    'name': "cash_denomination",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
      Cash Denomination
    """,

    'author': "iCodeBees",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv', 
        'views/cash_denomination_views.xml',
        'views/cash_counter_views.xml',
        'views/cash_transfer_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

