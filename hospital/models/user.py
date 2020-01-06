from odoo import fields, models


class User(models.Model):
    _name = 'user.res'

    _inherits = {
        'res.partner': 'dpt'
    }

    detail = fields.Char("Detail")
    dpt = fields.Many2one('res.partner', 'dpt')  # delegate=True
