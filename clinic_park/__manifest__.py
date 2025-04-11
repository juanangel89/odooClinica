{
    'name': 'clinic_park',
    'version': '1.0.1',
    'depends': ['base', 'mail','web', 'account'],
    'data': [
        'security/ir.model.access.csv', 
        'views/clinic_park_menus.xml',
        'views/clinic_park_patient_view.xml',
        'views/clinic_park_triage_view.xml',
        'views/clinic_park_consultations_view.xml',
        'views/clinic_park_procedure_view.xml',
        'views/clinic_park_preparation_view.xml',
        'views/clinic_park_surgery_view.xml',
        'views/clinic_park_recovery_view.xml',
        'views/clinic_park_bill_view.xml',



    ],
    'application': True,
    'installable': True,
}