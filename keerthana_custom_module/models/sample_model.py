from odoo import models, fields

class SampleModel(models.Model):
    _name = 'keerthana.sample'
    _description = 'Sample Model'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
