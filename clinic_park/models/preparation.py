from odoo import models, fields,api

class ClinicParkPreparation(models.Model):
    _name = 'clinic.park.preparation'
    _description = 'Preparación Quirúrgica'

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True, ondelete='cascade')
    triage_id = fields.Many2one('clinic.park.triage', string='Triage', ondelete='cascade')
    consultation_id = fields.Many2one('clinic.park.consultations', string='Consulta')

    preoperative_form = fields.Text(string='Formulario Preoperatorio')
    supplies = fields.Text(string='Insumos Utilizados', required=True)
    nurse_signature = fields.Binary(string='Firma de enfermeria')
    checklist_consent = fields.Boolean(string='Consentimiento informado firmado')
    checklist_exams = fields.Boolean(string='Exámenes preoperatorios revisados')
    checklist_equipment = fields.Boolean(string='Equipo quirúrgico preparado')
    checklist_allergies = fields.Boolean(string='Alergias conocidas verificadas')
    checklist_documents = fields.Boolean(string='Documentación completa')

    preparation_date = fields.Datetime(string='Fecha de Preparación', required=True)
    patient_signature = fields.Binary(string='Firma del Paciente')

    def action_ir_a_cirugia(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cirugía',
            'res_model': 'clinic.park.surgery',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_patient_id': self.patient_id.id,
            }
        }

    @api.onchange('triage_id')
    def _onchange_triage_id(self):
        if self.triage_id and self.triage_id.atencion == 'preparacion':
            self.patient_id = self.triage_id.patient_id