from odoo import models, fields

class ClinicParkSurgery(models.Model):
    _name = 'clinic.park.surgery'
    _description = 'Registro de Cirugía'

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    procedure_details = fields.Text(string='Detalles del Procedimiento')
    surgery_date = fields.Datetime(string='Fecha de Cirugía')
    documents = fields.Binary(string='Documento Quirúrgico', attachment=True)
    vital_signs_notes = fields.Text(string='Signos Vitales Intraoperatorios')
