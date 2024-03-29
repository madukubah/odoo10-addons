{
    'name': 'Website Link Tracker',
    'category': 'Hidden',
    'description': """
Website interface to create short and trackable URLs.
=====================================================

        """,
    'version' : '1.1.1',
    'depends': ['website', 'link_tracker'],
    'data': [
        'views/website_links_template.xml',
        'views/website_links_graphs.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'auto_install': True,
}
