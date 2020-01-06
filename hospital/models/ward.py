from odoo import api, models, fields


class Ward(models.Model):
    _name = 'hospital.ward'

    name = fields.Selection(
        [('opd', 'OPD'), ('icu', 'ICU'), ('ot', 'Operation Theater'), ('cancer', 'Cancer'), ('ortho', 'Orthopadic'),
         ('physician', 'Physician'), ('gynec', 'Gynecology'), ('ent', 'ENT'), ('medicine', 'Medicine')], 'Enter Ward')
    no = fields.Integer("Ward No")
    patient_id = fields.Many2one('hospital.patient', 'patient')
