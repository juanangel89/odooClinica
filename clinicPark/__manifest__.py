{
    'name': 'Clinic Park - Gestión de Pacientes',
    'version': '1.0',
    'summary': 'Módulo de gestión de pacientes para la Clínica del Parque',
    'description': 'Permite registrar pacientes, edad, género y motivo de ingreso.',
    'author': 'juanangel89',
    'category': 'Healthcare',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
    ],
    'installable': True,
    'application': True,
}