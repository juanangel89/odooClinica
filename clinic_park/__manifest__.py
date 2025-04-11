{
    'name': 'clinic_park',
    'version': '1.0.1',
    'depends': ['base', ],
    'data': [
        'security/ir.model.access.csv',  # Carga primero los permisos de acceso
        'views/clinic_park_views.xml',       # Carga primero vistas/modelos
        'views/clinic_park_menus.xml',
        'views/clinic_park_recovery_view.xml',
        'views/clinic_park_surgery_view.xml',

    ],
    'application': True,
    'installable': True,
}