# -*-coding: utf-8 -*-
{
    'name': 'Equipment',
    'version': '1.0.0',
    'category': 'stock',
    "sequence": 1,
    'summary': 'Manage Equipment',
    'complexity': "easy",
    'author': 'VNITPro',
    'website': 'http://vnitpro.vn',
    'depends': ['base','mail'],
    'data': [
        'view/equipment_view.xml',
        'menu/equipment_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
