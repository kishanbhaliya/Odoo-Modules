from odoo import api, models, fields
from datetime import datetime
from odoo.exceptions import UserError


class Shift(models.Model):
    _name = 'shift.shift'

    name = fields.Char('Name', required=True)
    start_date = fields.Datetime('Start', required=True)
    end_date = fields.Datetime('End', required=True)
    hospital_id = fields.Many2one('hospital.hospital', 'hospital')
    patient_id = fields.Many2one('hospital.patient', 'patient')

    # shift_type = fields.Selection([('m', 'First Shift'), ('e', 'Second Shift'),
    #                                ('n', 'Third Shift')], 'Shift Shedule',
    #                               required=True)
    shift_lines = fields.One2many('shift.line', 'shift_id', 'Shifts')
    state = fields.Selection([('draft', 'Draft'),
                              ('create', 'Create'),
                              ('start', 'Start'),
                              ('end', 'End'),
                              ('cancel', 'Cancel')], 'State', default='draft')
    shift = fields.Selection([('f', 'First'), ('s', 'Second'), ('t', 'Third')], 'Shift Shedule')


    @api.multi
    def copy(self, default=None):
        '''self will always have single recordset'''
        if default is None:
            default = {}
            default.update({'name': self.name + '-' + 'Duplicate'})
            return super(Shift, self).copy(default)

    @api.onchange('patient_id')
    def change_hospital(self):
        '''onchange will be called when defined field (patient_id) is changed
        onchange performs following operations
        1)set a value
        2)set a domain
        3)show warning message
        '''
        print("\n\nonchange...", self, self.patient_id)
        # set a value
        self.hospital_id = self.patient_id.hospital_id.id
        return {'warning': {'title': 'My warning...', 'message': 'This is warning from onchange...'}}

    @api.multi
    def action_create(self):
        new_pat = self.create({'name': 'Default', 'start_date': datetime.now(), 'end_date': datetime.now(),
                               'shift_type': 'm'})
        print("\n\nWelCome...", new_pat)

    @api.multi
    def create_shift(self):
        rec = self.create(['name', 'create_date', 'patient_id'])
        self.write({'state': 'create'})
        print("\n\nCreate My Shift...", rec)

    @api.multi
    def draft_shift(self):
        rec = self.write({'state': 'draft'})

    @api.multi
    def start_shift(self):
        rec = self.read(['name', 'start_date', 'patient_id'])
        self.write({'state': 'start'})
        print("\n\nStart My Shift...", rec)

    @api.multi
    def end_shift(self):
        self.write({'state': 'end'})
        print("\n\nEnd My Shift...")

    @api.multi
    def cancel_shift(self):
        self.write({'state': 'cancel'})
        print("\n\nCancel My Shift...")

    @api.multi
    def unlink(self):
        for shift in self:
            if shift.state != 'draft':
                raise UserError('Only draft shift can be deleted.')
        return super(Shift, self).unlink()


class ShiftLine(models.Model):
    _name = 'shift.line'

    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')])
    shift_id = fields.Many2one('shift.shift', 'Shift')
