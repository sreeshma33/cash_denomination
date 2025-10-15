# -*- coding: utf-8 -*-
{
    'name': "cash_denomination",
    'version': "1.1",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
      Cash Denomination
    """,

    'author': "iCodeBees",
    'website': "https://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','account','website'],

    'data': [
        'security/ir.model.access.csv', 
        'views/cash_denomination_views.xml',
        'views/cash_counter_views.xml',
        'views/cash_transfer_views.xml',
        'views/templates.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'cash_denomination/static/src/js/cash_denomination.js',
            'web/static/src/components/pager/pager_indicator.js',
        ],
},


}

