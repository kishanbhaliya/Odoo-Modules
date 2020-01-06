from odoo import models, fields, api


class joining(models.Model):
    _inherit = 'hr.employee'

    id_proof = fields.Boolean()
    address_proof = fields.Boolean()
    exp_letter = fields.Boolean()
    computer_no = fields.Integer()
    biomatric_code = fields.Integer()
    access_code = fields.Char()
    pancard = fields.Char()
    final_degree = fields.Boolean()
    nda = fields.Boolean()
    cheque_scan = fields.Char()
    bank_account_no = fields.Char()
    pf_form = fields.Boolean()
    esic = fields.Selection([('y', 'Yes'), ('n', 'No')])
    background_check_detail = fields.Selection([('y', 'Yes'), ('n', 'No')])
    background_verification = fields.Char()
    alternate_email = fields.Char()
    phone = fields.Char()
    emp_add = fields.Boolean()
    verify_phone = fields.Boolean()
    background_check = fields.Boolean()
    nda_sign = fields.Boolean()
   
    progress_rate = fields.Integer("Progress")
