from odoo import api, models, fields
from datetime import datetime
import time
from dateutil.relativedelta import relativedelta


class Employee(models.Model):
    _inherit = 'hr.employee'

    upload_file = fields.Binary(string="Upload File")
    file_name = fields.Char(string="File Name")
    private_address = fields.Text("Private Address")
    badge_id = fields.Many2one("hr.employee", "Badge Id")
    team_id = fields.Many2one("hr.employee", "Team Leader")
    project_id = fields.Many2one("hr.employee", "Project Manager")
    joining_date = fields.Date("Joning Date")
    last_salary = fields.Char("Last Salary Reviewed")
    f_name = fields.Char('First Name')
    l_name = fields.Char('Last Name')
    spouse_name = fields.Char('Father/Spouse Name')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('o', 'Other')], 'Gender')
    marital = fields.Selection(
        [('single', 'Single'), ('married', 'Married')], 'Marital Status')
    birthday = fields.Date("Birth Date")
    age = fields.Integer("Age", compute='onchange_birthday')
    temp_address = fields.Text('Temporary Address')
    perm_address = fields.Text('Permanent Address')
    phone = fields.Char("Mobile Number")
    email = fields.Char("Personal Email")
    emergency_contact = fields.Char("Emergency Contact Number")
    emergency_name = fields.Char("Emergency Contact Name")
    school_college = fields.Char("School/College")
    education = fields.Selection([('btech', 'B.Tech'), ('mtech', 'M.Tech')])

    @api.depends('birthday')
    def onchange_birthday(self):
        """Updates age field when birth_date is changed"""
        if self.birthday:
            b_date = self.birthday
            today = datetime.today()
            print("\n\nToday's date...", today, "\n")
            self.age = today.year - b_date.year
 