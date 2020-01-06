from odoo import models, fields


class Student(models.Model):
    _name = 'student.student'
    _order = 'dob'

    name = fields.Char('Name', required=True)
    dob = fields.Date('Date of Birth')
    age = fields.Integer('Age', readonly=True)
    class_id = fields.Integer('Class ID')
    address = fields.Text('Address')
    city = fields.Char('City')
    gender = fields.Selection([('m','Male'),('f','Female'),('o','Other')],'Gender', required=True)
    school_id = fields.Many2one('school.school', 'School')