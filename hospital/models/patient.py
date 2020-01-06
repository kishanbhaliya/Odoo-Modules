from odoo import api, models, fields, exceptions
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hospital.patient'

    name = fields.Char("Name", required=True)
    city = fields.Char("City")
    admit_date = fields.Datetime('Admit')
    discharge_date = fields.Datetime('Discharge')
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'),
                               ('o', 'Other')], 'Gender', required=True)
    status = fields.Selection([('treatment', 'Treatment'), ('admit', 'Admitted'),
                               ('discharge', 'Discharged')], 'Status')
    image = fields.Binary("Image")
    age = fields.Integer("Age")
    address = fields.Text("Adderss")
    number = fields.Integer("Mobile No")

    hospital_id = fields.Many2one('hospital.hospital', 'hospital')
    ward_ids = fields.Many2many('hospital.ward', 'patient_ward_rel', 'patient_id',
                                'ward_id', string='Ward')
    payment_ids = fields.Many2many('hospital.payment', 'patient_pay_rel', 'patient_id', 'pay_id', string='Payment')
    total = fields.Integer()
    color = fields.Integer("Color")

    # @api.constrains('age')
    # def _check_something(self):
    #     for patient in self:
    #         if patient.age > 21:
    #             raise ValidationError("Your record is too old: %s", patient.age)
    #
    # _sql_constraints = [
    #     ('number',
    #      'UNIQUE(number)',
    #      "The Name must be unique"),
    # ]
