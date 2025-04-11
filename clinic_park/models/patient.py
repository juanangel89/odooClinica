from odoo import models, fields

class ClinicParkPatient(models.Model):
    _name = 'clinic.park.patient'
    _description = 'Paciente'

    triage_id = fields.One2many('clinic.park.triage', 'patient_id', string='Triage')
    consultations_id = fields.One2many('clinic.park.consultations', 'patient_id', string='Consulta')
    procedure_id = fields.One2many('clinic.park.procedure', 'patient_id', string='Procedimiento')
    surgery_id = fields.One2many('clinic.park.surgery', 'patient_id', string='Cirugía')
    procedure_id = fields.One2many('clinic.park.procedure', 'patient_id', string='Procedimientos')
    preparation_id = fields.One2many('clinic.park.preparation', 'patient_id', string='Preparación Quirúrgica')
    recovery_id = fields.One2many('clinic.park.recovery', 'patient_id', string='Recuperación y Hospitalización')
    # datos de la consulta
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
    siganture = fields.Binary(string='Firma')