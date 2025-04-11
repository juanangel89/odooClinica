from odoo import models, fields

class ClinicParkRecovery(models.Model):
    _name = 'clinic.park.recovery'
    _description = 'Recuperación y Hospitalización'

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    shift_notes = fields.Text(string='Notas por Turno')
    nurse_evolution = fields.Text(string='Evolución de Enfermería')
    alerts = fields.Text(string='Alertas Postoperatorias')
    tasks = fields.Text(string='Tareas de Seguimiento')
    date = fields.Date(string='Fecha de Registro', default=fields.Date.today)