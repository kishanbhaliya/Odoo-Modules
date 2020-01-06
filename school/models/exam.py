from odoo import api, models, fields


class Exam(models.Model):
    _name = 'student.exam'

    name = fields.Char('Name')
    start_date = fields.Datetime("Start", required=True)
    end_date = fields.Datetime("End", required=True)
    student_id = fields.Many2one('student.student', 'Student', required=True)
    school_id = fields.Many2one('school.school', 'School', required=True)
    exam_type = fields.Selection([('int', 'Internal'),
                                  ('ext', 'External'),
                                  ('fin', 'Final')], 'Type', required=True)
    exam_lines = fields.One2many('exam.line', 'exam_id', 'Exams', copy=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('start', 'Start'),
                              ('end', 'End'),
                              ('cancel', 'Cancel')], 'State', default='draft')

    @api.multi
    def action_create(self):
        from datetime import datetime
        new_std = self.create({'name': '223', 'start_date': datetime.now(), 'end_date': datetime.now(),
                               'exam_type': 'int', 'student_id': 3})
        print("\n\nWel Come...", new_std)

    @api.multi
    def copy(self, default=None):
        if default is None:
            default = {}
            default.update({'name': self.name + '-' + 'Duplicate'})
            return super(Exam, self).copy(default)

    @api.onchange('student_id')
    def change_student(self):
        print("\n\nOnchange ...", self, self.student_id)
        self.school_id = self.student_id.school_id.id
        return {'warning': {'title': 'My warning...', 'message': 'This is warning from onchange...'}}

    @api.multi
    def start_exam(self):
        rec = self.read(['name', 'start_date', 'student_id'])
        self.write({'state': 'start'})
        print("\n\nStart My Exam....", rec)

    @api.multi
    def end_exam(self):
        self.write({'state': 'end'})
        print("\n\nEnd My Exam...")

    @api.multi
    def cancel_exam(self):
        self.write({'state': 'cancel'})
        print("\n\nCancel My Exam...")


class ExamLine(models.Model):
    _name = 'exam.line'

    sub_name = fields.Char('Subject')
    mark = fields.Float('Mark')
    exam_id = fields.Many2one('exam.exam', 'Exam')
