from odoo import models, fields

class Prodi(models.Model):
    _name = 'tracer_alumni.prodi'
    _description = 'Data Program Studi (Prodi)'

    name = fields.Char(string='Nama Prodi', required=True)
    fakultas_id = fields.Many2one('tracer_alumni.fakultas', string='Fakultas', required=True)