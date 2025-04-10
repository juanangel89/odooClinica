from odoo import models, fields

class ClinicPatient(models.Model):
    _name = 'clinic.patient'
    _description = 'Patient Admission'

    # Datos del paciente
    name = fields.Char(string='Full Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')

    # Acompañante
    companion_name = fields.Char(string='Companion Name')
    companion_phone = fields.Char(string='Companion Phone')
    companion_relationship = fields.Char(string='Relationship to Patient')

    # Motivo de ingreso
    admission_reason = fields.Text(string='Reason for Admission')
    admission_date = fields.Datetime(string='Admission Date', default=fields.Datetime.now)