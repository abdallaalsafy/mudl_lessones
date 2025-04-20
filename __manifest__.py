# -*- coding: utf-8 -*-
{
    'name': "mudl_lessones",

    'summary': """
        Seed project for managing private lessons""",

    'description': """
        Seed project for managing private lessons
    """,
    'website': "http://www.facebook.com/abdalla6alsafy",
    'author': "Abdalla alsafy",
    'category': 'Uncategorized',
    'version': '13.0.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/students.xml',
        'views/sttaf.xml',
        'views/courses.xml',
        'views/groups.xml',
        'views/hogozat.xml',
        'views/templates.xml',
        'demo/days.xml',
    ],
    'demo': [
    ],
}
