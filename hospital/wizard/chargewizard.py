from odoo import api, fields, models


class ChargeWizard(models.TransientModel):
    _name = 'wiz_hospital.charge'

    days = fields.Float("No oF Days")
    charge_day = fields.Float("Total Charge")
    payment = fields.Float("Total Payment")

    @api.multi
    def charge_cost(self):
        print("\n\n Method Called.......")
        charge = self.env['hospital.payment'].browse(self.env.context.get('active_id'))
        payment = self.days * self.charge_day
        charge.write({'payment': payment})


