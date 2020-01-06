from odoo import api, fields, models


class Registration(models.Model):
    _name = 'hospital.register'

    p_name = fields.Char("Patient Name")
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'),
                               ('o', 'Other')], 'Gender')
    dob = fields.Datetime("Date Of Birth")
    r_date = fields.Datetime("Registration Date")
    p_add = fields.Text("Address")
    p_city = fields.Char("City")
    p_pin = fields.Integer("Pin No")
    hospital_id = fields.Many2one('hospital.hospital', 'Hospital')
    # reg_id = fields.Many2one('hospital.register', 'registration')

