from odoo import models, fields

class ClinicaPaciente(models.Model):
    _name = 'clinica.paciente'
    _description = 'Paciente'

    name = fields.Char(string='Nombre completo', required=True)
    dni = fields.Char(string='DNI')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro')
    ])
    telefono = fields.Char()
    direccion = fields.Char()
    acompanante = fields.Char(string='Acompañante')
    motivo_ingreso = fields.Text()