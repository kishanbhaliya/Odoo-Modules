from odoo import api, fields, models


class Demo1(models.Model):
    _name = 'delegation.demo1'

    field_1 = fields.Integer()
    _rec_name = 'field_1'


class Demo2(models.Model):
    _name = 'delegation.parent'

    _inherits = {
        'delegation.demo1': 'field_1'
    }
    field_2 = fields.Char()
    field_1 = fields.Many2one('delegation.demo1', 'Demo1')
