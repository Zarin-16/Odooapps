# -*- coding: utf-8 -*-

{
    'name': 'bdtask School Management System',
    'version': '15.0.0.4',
    'summary': 'School Management System',
    'description': ' School Management System',
    'category': ' School management system',
    'author': 'Zarin',
    'company': '',
    'maintainer': '',
    'depends': ['base', 'sale_management', 'purchase'],
    'website': '',
    'data': [
    'security/ir.model.access.csv',
    'views/management.xml',
    'views/teacher.xml',
    'views/student.xml',
    'views/sale_order.xml',
    'views/purchase_order.xml',
    'reports/report.xml',
    'reports/student_card.xml',
    'reports/sale_report_inherit.xml',
    'reports/student_summary.xml',
    # 'reports/teacher_card.xml',
    # 'reports/teacher_summary.xml',
    ],
    'images': ["static/description/banner.png"],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
