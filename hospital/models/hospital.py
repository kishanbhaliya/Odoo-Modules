from odoo import api, models, fields
import random


class Hospital(models.Model):
    _name = 'hospital.hospital'

    name = fields.Char('Name')
    reg_no = fields.Integer("Register No")
    address = fields.Text('Address')
    city = fields.Char('City')
    number = fields.Integer('Phone No')
    patient_ids = fields.One2many('hospital.patient', 'hospital_id', 'Patient')
    department_ids = fields.Many2many('hospital.department', 'hospital_dept_rel', 'hospital_id', 'dept_id',
                                      string='Department')
    ward_ids = fields.Many2many('hospital.ward', 'hospital_ward_rel', 'hospital_id', 'ward_id', string='Ward')
    reg_ids = fields.One2many('hospital.register', 'hospital_id', 'Registration')
    color = fields.Integer("Color")

    @api.multi
    def open_patients(self):
        print("\n\nName... ", self.name)
        print("\n\nDept...", self.department_ids, self.department_ids.ids)
        print("\n\nWard No...", self.ward_ids, self.ward_ids.ids)
        print("\n\nSelf...", self.patient_ids, self.patient_ids.ids)
        # for patient in self.patient_ids:
        #     print("\n\nPatient name...", patient, patient.name, patient.age)
        # for dept in self.department_ids:
        #     print("\n\nDepartment...", dept, dept.name, dept._name)
        # for ward in self.ward_ids:
        #     print("\n\nWard No...", ward, ward.name, ward._name)
        return {
            'name': 'Patient Details',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'hospital.patient',
            'domain': [('id', 'in', self.patient_ids.ids)],
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

        # @api.multi
        # def open_reg(self):
        #     return {
        #         'name': 'Patient Registration',
        #         'view_type': 'form',
        #         'view_mode': 'tree,form',
        #         'res_model': 'hospital.register',
        #         'domain': [('id', 'in', self.reg_ids.ids)],
        #         'type': 'ir.actions.act_window',

        # }

        @api.model
        def create(self, vals):
            vals.update({'reg_no': str(random.randint(1, 100))})
            hospital = super(Hospital, self).create(vals)
            print("\n\nCreate method called....", self, vals, hospital)
            return hospital

        @api.multi
        def write(self, vals):
            hospital = super(Hospital, self).write(vals)
            print("\n\nWrite method called....", self, vals, hospital)
            return hospital

        @api.multi
        def unlink(self):
            print("\n\nUnlink method called....")
            return super(Hospital, self).unlink()

        # @api.multi
        # def read(self, vals):
        #     s = super(Hospital, self).read(vals)
        #     print("\n\nRead Method Called...",s)
        #     return s

        @api.multi
        def Search(self):
            print("\n\nSearch Method Called...")
            domain = [('name', '=', 'SVP')]
            s = self.env['hospital.hospital'].search(domain)
            print("\n", len(s))
            print(s[0].name)

        @api.multi
        def name_get(self):
            super(Hospital, self).name_get()
            data = []
            for record in self:
                x = record.name + ' ' + "[" + record.city + "]"
                data.append((record.id, x))
            return data
