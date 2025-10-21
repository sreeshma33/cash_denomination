# -*- coding: utf-8 -*-
{
    'name': "cash_denomination",
    'version': "1.5",

    'summary': "Short (1 phrase/line) summary of the module's purpose",#????  please change

    'description': """
      Cash Denomination
    """,

    'author': "iCodeBees",
    'website': "https://www.yourcompany.com",
    # change website and category
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','account','website'],

    'data': [
        'security/ir.model.access.csv', 
        'views/cash_denomination_views.xml',
        'views/cash_counter_views.xml',
        'views/cash_transfer_views.xml',
        'views/cash_denomination_templates.xml',
    ],
    'assets': {
            'web.assets_frontend': [
                'cash_denomination/static/src/js/cash_denomination.js',
            ],
        },


}

