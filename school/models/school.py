from odoo import api, models, fields
import random


class School(models.Model):
    _name = 'school.school'

    name = fields.Char('Name')
    reg_number = fields.Char("Register No", Default=100)
    address = fields.Text('Address')
    city = fields.Char('City')
    student_ids = fields.One2many('student.student', 'school_id', 'Students')
    department_ids = fields.Many2many('school.department', 'school_dept_rel', 'school_id', 'dept_id',
                                      string='Department')

    @api.multi
    def open_students(self):
        print("Name....    ", self.name)
        print("Dept...    ", self.department_ids, self.department_ids.ids)
        print("\n\nSelf.........    ", self,
              self.student_ids, self.student_ids.ids)
        for student in self.student_ids:
            print('\n\nStudent Name....', student, student.name, student.dob)
        for dept in self.department_ids:
            print("\n\nDepartment..........    ", dept, dept.name, dept._name)
        return {
            'name': 'Student Details',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'student.student',
            'domain': [('id', 'in', self.student_ids.ids)],
            'type': 'ir.actions.act_window',
            #            'target': 'new',
        }

    @api.model
    def create(self, vals):
        vals.update({'reg_number': str(random.randint(1, 1000))})
        school = super(School, self).create(vals)
        print("\n\nCreate method called....", self, vals, school)
        return school

    @api.multi
    def write(self, vals):
        school = super(School, self).write(vals)
        print("\n\nWrite method called....", self, vals, school)
        return school

    @api.multi
    def unlink(self):
        print("\n\nUnlink method called....")
        return super(School, self).unlink


class SchoolDepartment(models.Model):
    _name = 'school.department'

    name = fields.Char('Name')
