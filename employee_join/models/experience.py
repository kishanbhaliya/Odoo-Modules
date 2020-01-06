from odoo import api, fields, models
from datetime import datetime


class Experience(models.Model):
    _name = 'hr.emp.experience'

    start_date = fields.Date("Joining Date")
    end_date = fields.Date("Resigning Date")
    company = fields.Char("Company Name")
    pre_exp = fields.Float("Company Experience", compute='onchange_pre_experience')
    pre_experience_ids = fields.Many2one('hr.employee', 'Experience')

    @api.depends('start_date', 'end_date')
    def onchange_pre_experience(self):
        if self.start_date and self.end_date:
            dt_join = datetime.strptime(self.start_date, '%Y-%m-%d')
            dt_resign = datetime.strptime(self.end_date, '%Y-%m-%d')
            self.pre_exp = dt_resign.year - dt_join.year

    