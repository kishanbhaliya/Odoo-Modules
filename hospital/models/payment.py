from odoo import api, models, fields


class Payment(models.Model):
    _name = 'hospital.payment'

    patient_id = fields.Many2one('hospital.patient', 'Patient')
    payment = fields.Float("Total Payment")

    @api.depends('p_amount', 'p_day')
    def compute_total(self):
        total = 0
        for pay in self:
            pay.total += pay.p_amount * pay.p_day
