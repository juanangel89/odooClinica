{
    'name': 'Clinica del Parque',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Tu Nombre',
    'category': 'Healthcare',
    'description': 'Gestión clínica de pacientes desde ingreso hasta alta y facturación',
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/clinica_menu.xml',
    ],
    'installable': True,
    'application': True,
}
