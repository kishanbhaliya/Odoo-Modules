from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer("Age")
    is_patient = fields.Boolean("Patient")
    is_doctor = fields.Boolean("Doctor")
    city = fields.Char("City")
    demo1_id = fields.Many2one('hospital.patient', 'Patient')
    demo2_id = fields.Many2one('hospital.patient', 'Patient')

    @api.model
    def create(self, vals):
        if self.age:
            self.age = 'is a field info'
        return super(ResPartner, self).create(vals)

    @api.multi
    def write(self, vals):
        resp = super(ResPartner, self).write(vals)
        print("\n\nWrite method called....", self, vals, resp)
        return resp

    @api.multi
    def unlink(self):
        print("\n\nUnlink method called....")
        return super(ResPartner, self).unlink()

    @api.multi
    def name_get(self):
        super(ResPartner, self).name_get()
        data = []
        for record in self:
            x = record.name + ' ' + "[" + record.city + "]"
            data.append((record.id, x))
        print("\n\n name_get method called...")
        return data
