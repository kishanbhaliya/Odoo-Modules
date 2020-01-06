from odoo import api, models, fields, exceptions
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'hospital.doctor'

    name = fields.Char("Name")
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'),
                               ('o', 'Other')], 'Gender', required=True)
    speciality = fields.Char("Speciality")
    age = fields.Integer("Age")
    d_id = fields.Integer("Doctor Id")
    city = fields.Char("City")
    patient_id = fields.Many2one('hospital.patient', 'Patient')
    hospital_id = fields.Many2one('hospital.hospital', 'Hospital')
    image = fields.Binary("Image", attachment=True)
    file = fields.Binary("File")
    mbbs = fields.Boolean("MBBS")
    md = fields.Boolean("M.D")
    ms = fields.Boolean("M.S")
    color = fields.Integer("Color")
    maximum_rate = fields.Integer()

    # @api.onchange('patient_id')
    # def change_hospital(self):
    #     '''onchange will be called when defined field (patient_id) is changed
    #     onchange performs following operatons
    #     1)set a value
    #     2)set a domain
    #     3)show warning message
    #     '''
    #     print("\n\nonchange...", self, self.patient_id)
    #     # set a value
    #     self.hospital_id = self.patient_id.hospital_id.id
    #     return {'warning': {'title': 'My warning...', 'message': 'This is warning from onchange...'}}

    # @api.multi
    # def check_in(self, vals):
    #     # self.write({'check_in': 'Check In'})
    #     print("\n", fields.Datetime.now(), "\n")
    #     print("\n\nCheck In...")
    #
    # @api.multi
    # def check_out(self, vals):
    #     self.write({'check_out': 'Check Out'})
    #     print("\n", fields.datetime.now())
    #     print("\n\nCheck Out...")


    # @api.constrains('age')
    # def _check_something(self):
    #     for doct in self:
    #         if doct.age > 21:
    #             raise ValidationError("Your record is too old: %s", doct.age)
    #
    # _sql_constraints = [
    #     ('city',
    #      'UNIQUE(city)',
    #      "The city title must be unique"),
    # ]
