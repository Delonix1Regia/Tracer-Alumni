from odoo import models, fields

class Fakultas(models.Model):
    _name = 'tracer_alumni.fakultas'
    _description = 'Data Fakultas'

    name = fields.Char(string='Nama Fakultas', required=True)