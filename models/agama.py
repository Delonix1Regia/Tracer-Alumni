from odoo import models, fields

class Agama(models.Model):
    _name = 'tracer_alumni.agama'
    _description = 'Data Agama'

    name = fields.Char(string='Agama', required=True)