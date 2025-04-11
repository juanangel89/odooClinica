from odoo import models, fields, api

class ClinicParkBill(models.Model):
    _name = 'clinic.park.bill'
    _description = 'Alta y Facturación'

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    recovery_id = fields.Many2one('clinic.park.recovery', string='Recuperación')
    surgery_id = fields.Many2one('clinic.park.surgery', string='Cirugía')
    discharge_date = fields.Datetime(string='Fecha de Egreso', default=fields.Datetime.now, required=True)

    consolidated_items = fields.Text(string='Insumos y Procedimientos Consolidados', readonly=True)
    digital_signature = fields.Binary(string='Firma Digital del Paciente')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('done', 'Egresado'),
        ('invoiced', 'Facturado')
    ], string='Estado', default='draft')

    invoice_id = fields.Many2one('account.move', string='Factura')

    def action_consolidar(self):
        """
        Consolida los insumos y procedimientos de cirugía y recuperación
        """
        consolidated_text = ""

        if self.surgery_id:
            consolidated_text += f"**Procedimiento**: {self.surgery_id.procedure_detail or ''}\n"
            consolidated_text += f"**Anestesia**: {self.surgery_id.anesthesia_type or ''}\n"

        if self.recovery_id:
            consolidated_text += f"\n**Notas de recuperación**:\n{self.recovery_id.shift_notes or ''}\n"
            consolidated_text += f"\n**Alertas**:\n{self.recovery_id.alerts or ''}\n"
            consolidated_text += f"\n**Tareas**:\n{self.recovery_id.tasks or ''}\n"

        self.consolidated_items = consolidated_text

    def action_generar_factura(self):
        """
        Genera un borrador de factura vinculado al módulo de contabilidad
        """
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.patient_id.partner_id.id,  # Asumiendo que el paciente está vinculado a un res.partner
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': [
                (0, 0, {
                    'name': f'Procedimientos e Insumos - {self.patient_id.name}',
                    'quantity': 1,
                    'price_unit': 500000.0,  # Puedes calcular dinámicamente el valor
                })
            ],
        })
        self.invoice_id = invoice.id
        self.state = 'invoiced'
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'view_mode': 'form',
            'res_id': invoice.id,
            'target': 'current',
        }

    def action_confirmar_alta(self):
        self.state = 'done'

    # Botón: Enviar a recuperación
    def action_send_to_recovery(self):
        for record in self:
            record.state = 'recovery'

    # Botón: Marcar como facturado
    def action_mark_billed(self):
        for record in self:
            record.state = 'billed'
