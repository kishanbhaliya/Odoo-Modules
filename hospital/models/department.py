from odoo import api, models, fields


class Department(models.Model):
    _name = 'hospital.department'

    name = fields.Char("Name")
    p_name = fields.Char("Person Name")
    occupation = fields.Char("Occupation")
    exp = fields.Integer("Experience")
    hospital_id = fields.Many2one('hospital.hospital', 'hospital')
    hospital_id = fields.Many2one('hospital.hospital', 'hospital')
