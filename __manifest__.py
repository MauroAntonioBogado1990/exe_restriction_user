{
    'name': 'Exe Restricción por usuario',
    'version': '15.0',
    'category': 'Tools',
    'author':'Mauro Bogado,Exemax',
    'depends': ['stock', 'mrp', 'hr', 'website', 'base','sale','board'],
    'data': [

    'data/groups.xml',
    #'security/ir.model.access.csv',
    'security/record_rules.xml',
    'views/hide_menus.xml',
    ],

    'installable': True,
    'application': False,
}
