from odoo import models, fields, api
from datetime import datetime


class PreExperience(models.Model):
    _inherit = 'hr.employee'

    age = fields.Integer("Age", compute='onchange_birthday')
    join_dt = fields.Date("Joining Date")
    current_exp = fields.Float(
        "Current Experience", compute='onchange_current_exp')
    total_exp = fields.Float("Total Experience", compute='compute_total_exp')
    experience_id = fields.One2many(
        "hr.emp.experience", "pre_experience_ids", "Experience")

    @api.depends('birthday')
    def onchange_birthday(self):
        if self.birthday:
            date_today = datetime.today()
            b_date = datetime.strptime(self.birthday, '%Y-%m-%d')
            self.age = date_today.year - b_date.year

    @api.depends('join_dt')
    def onchange_current_exp(self):
        if self.join_dt:
            today_dt = datetime.today()
            date_join = datetime.strptime(self.join_dt, '%Y-%m-%d')
            self.current_exp = today_dt.year - date_join.year

    @api.depends('current_exp', 'experience_id')
    def compute_total_exp(self):
        total = 0
        for i in self.experience_id:
            total = i.pre_exp + total
        self.total_exp = self.current_exp + total
