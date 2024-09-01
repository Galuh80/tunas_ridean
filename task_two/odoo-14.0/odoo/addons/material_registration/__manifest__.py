{
    'name': 'Custom Product Management',
    'version': '1.0',
    'depends': ['base'],
    'category': 'Product',
    'summary': 'Manage custom products',
    'description': """Manage custom products with specific constraints""",
    'images': [],
    'data': [
        'security/ir.model.access.csv',
        'views/product_custom_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'author': 'Galuh Esa Ibrahim',
    'sequence': 1,
    'odoo-apps': True,
    'active': True,
    'demo': [
        'demo/demo.xml',
    ],
    'test': [
        'tests/test_product_custom.py',
    ],
}
