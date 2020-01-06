from odoo import models, fields


class Subject(models.Model):
    _name = 'student.subject'

    name = fields.Char('Name')
    code = fields.Integer('Code')
