from odoo import models, fields

class ClinicParkCirugia(models.Model):
    _name = 'clinic.park.surgery'
    _description = 'Cirugía'

    triage_id = fields.Many2one('clinic.park.triage', string='Triage', ondelete='cascade')
    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    name= fields.Char(string='Nombre', related='patient_id.name', store=True)
    dni = fields.Char(string='Cedula', related='patient_id.dni', store=True)
    
    documents = fields.Binary(string='Documento Quirúrgico')
    procedure_details = fields.Text(string='Detalles del Procedimiento')
    surgery_date = fields.Datetime(string='Fecha de Cirugía')
    documents = fields.Binary(string='Documento Quirúrgico')
    vital_signs_notes = fields.Binary(string='Signos Vitales Intraoperatorios')
    anesthesia_type = fields.Selection([
        ('general', 'General'),
        ('local', 'Local'),
    ], string='Tipo de Anestesia', required=True)

    def action_ir_a_recuperacion(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'Recuperación',
        'res_model': 'clinic.park.recovery',
        'view_mode': 'form',
        'target': 'current',
        'context': {
            'default_patient_id': self.patient_id.id,
            'default_anesthesia_type': self.anesthesia_type,
            'default_procedure_detail': self.procedure_details,
            }
        }    