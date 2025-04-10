from odoo import models, fields

class ClinicParkPatient(models.Model):
    _name = 'clinic.park.patient'
    _description = 'Paciente'

    # datos del paciente
    current_date = fields.Date(string='Fecha Actual', default=fields.Date.context_today, required=True)
    name = fields.Char(string='Nombre', required=True)
    age = fields.Integer(string='Edad', required=True)
    dni = fields.Char(string='Cedula', required=True)
    phone = fields.Char(string='Telefono', required=True)
    email = fields.Char(string='Correo', required=True) 
    address = fields.Text(string='Direccion')
    birth_date = fields.Date(string='Fecha de Nacimiento')
    reason = fields.Text(string='Motivo de Consulta', required=True) 
    # datos acompañante
    companion = fields.Char(string='Acompañante')
    companion_phone = fields.Char(string='Telefono Acompañante')
    