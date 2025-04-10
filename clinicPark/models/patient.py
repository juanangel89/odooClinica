from odoo import models, fields

class ClinicaPaciente(models.Model):
    _name = 'clinic.patient'
    _description = 'Patient'

    name = fields.Char(string="Nombre completo", required=True)
    age = fields.Integer(string="Edad")
    gender = fields.Selection([
        ('male', 'Masculino'),
        ('female', 'Femenino'),
        ('other', 'Otro'),
    ], string="Género")
    motivo_ingreso = fields.Text(string="Motivo de ingreso")
