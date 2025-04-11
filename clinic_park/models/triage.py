from odoo import models, fields,api

class ClinicParkTriage(models.Model):
    _name = 'clinic.park.triage'
    _description = 'Triage'

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True, ondelete='cascade')
    current_date= fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    reason = fields.Text(string='Motivo de Consulta', required=True)
    name = fields.Char(string='Nombre', related='patient_id.name', store=True)
    age = fields.Integer(string='Edad', related='patient_id.age', store=True)
    dni = fields.Char(string='Cedula', related='patient_id.dni', store=True)
    # signos vitales
    temperatura = fields.Float(string='Temperatura', required=True)
    pulso = fields.Integer(string='Pulso', required=True)
    presion = fields.Char(string='Presion', required=True)
    # clasificacion
    atencion = fields.Selection([ 
        ('por clasificar', 'A.Por Clasificar'),
        ('consulta', 'B.Consulta'),
        ('preparacion', 'C.Preparación Quirúrgica'),
        ('cirugia', 'D.Cirugía'),
        ('recuperacion', 'E.Recuperación y Hospitalización'),
        ('facturacion', 'F.Facturación'),
    ],default="por clasificar",string="clasificacion",copy=False,required=True)

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente')

    @api.model
    def create(self, vals):
        record = super().create(vals)
        record._crear_registro_según_clasificacion()
        return record

    def write(self, vals):
        anteriores = self.mapped('atencion')
        res = super().write(vals)

        for record, anterior in zip(self, anteriores):
            nueva = vals.get('atencion', record.atencion)
            if nueva != anterior:
                record._eliminar_registro_anterior(anterior)
                record._crear_registro_según_clasificacion()
        return res

    def _crear_registro_según_clasificacion(self):
        self.ensure_one()
        clasificacion = self.atencion

        mapping = {
            'consulta': ('clinic.park.consultations', {
                'triage_id': self.id,
                'patient_id': self.patient_id.id,
            }),
            'preparacion': ('clinic.park.preparation', {
                'triage_id': self.id,
                'patient_id': self.patient_id.id,
            }),
            'cirugia': ('clinic.park.surgery', {
                'triage_id': self.id,
                'patient_id': self.patient_id.id,
            }),
            'recuperacion': ('clinic.park.recovery', {
                'triage_id': self.id,
                'patient_id': self.patient_id.id,
            }),
            'facturacion': ('clinic.park.bill', {
                'triage_id': self.id,
                'patient_id': self.patient_id.id,
            }),
        }

        if clasificacion in mapping:
            model_name, valores = mapping[clasificacion]
            ya_existe = self.env[model_name].search([('triage_id', '=', self.id)], limit=1)
            if not ya_existe:
                self.env[model_name].create(valores)

    def _eliminar_registro_anterior(self, clasificacion_anterior):
        self.ensure_one()
        mapping = {
            'consulta': 'clinic.park.consultations',
            'preparacion': 'clinic.park.preparation',
            'cirugia': 'clinic.park.surgery',
            'recuperacion': 'clinic.park.recovery',
            'facturacion': 'clinic.park.bill',
        }

        if clasificacion_anterior in mapping:
            model_name = mapping[clasificacion_anterior]
            registros = self.env[model_name].search([('triage_id', '=', self.id)])
            registros.unlink()