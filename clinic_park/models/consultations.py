from odoo import models, fields,api

class ClinicParkConsultation(models.Model):
    _name = 'clinic.park.consultations'
    _description = 'Consulta'

    procedure_id = fields.One2many('clinic.park.procedure', 'consultations_id', string='Procedimientos', ondelete='cascade')

    triage_id = fields.Many2one('clinic.park.triage', string='Triage', ondelete='cascade')
    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    name = fields.Char(string='Nombre', related='patient_id.name', store=True)
    dni = fields.Char(string='Cedula', related='patient_id.dni', store=True)

    # Prescripciones
    tratamiento = fields.Text(string='Tratamiento Prescrito')
    procedimientos = fields.Text(string='Procedimientos Recomendados')

    def action_ir_a_preparacion(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cirugía',
            'res_model': 'clinic.park.preparation',
            'view_mode': 'form',
            'target': 'current',
            'context': {
            'default_patient_id': self.patient_id.id,
            'default_triage_id': self.triage_id.id,
            'default_consultation_id': self.id,
            }
        }

    def action_ir_a_procedimientos(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Procedimientos',
            'res_model': 'clinic.park.procedure',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_triage_id': self.triage_id.id,
                'default_consultations_id': self.id,  # Muy importante para enlazarlo con la consulta
                'default_procedimiento': self.procedimientos,  # Este es el texto del procedimiento recomendado
            }
        }
    @api.onchange('triage_id')
    def _onchange_triage_id(self):
        if self.triage_id and self.triage_id.clasificacion == 'consulta':
            self.patient_id = self.triage_id.patient_id