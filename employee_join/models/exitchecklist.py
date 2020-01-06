from odoo import models, fields, api


class ExitCheckList(models.Model):
    _inherit = 'hr.employee'

    supervisor_approve = fields.Boolean()
    notice = fields.Boolean()
    resource = fields.Boolean()
    check_receipt = fields.Boolean()
    security = fields.Boolean()
    loan = fields.Boolean()
    pf_no = fields.Boolean()
    esi_no = fields.Boolean()
    tsd_cut = fields.Boolean()
    tds_certificate = fields.Boolean()
    experience = fields.Boolean()
    complete_notice = fields.Boolean()
    non_due = fields.Boolean()

