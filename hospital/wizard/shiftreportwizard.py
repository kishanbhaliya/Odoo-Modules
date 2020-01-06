from odoo import api, models, fields


class ShiftReportWizard(models.TransientModel):
    _name = 'shift.report.wizard'

    start_date = fields.Datetime('Start', required=True)
    end_date = fields.Datetime('End', required=True)

    @api.multi
    def get_report(self):
        print("\n\n Hello....")

        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'start_date': self.start_date
            }
        }
        return self.env.ref('hospital.doctor_shift').report_action(self, data=data)


class ReportShiftWizard(models.TransientModel):
    _name = 'report.shift.shift.hospital.report_shift'

    @api.model
    def get_report(self, data):
        start_date = data['form']['start_date']
        end_date = data['form']['end_date']

        docs = []
        data = self.env['shift.shift'].browse(self.env.context.get('active_id'))
        name = data.name

        docs.append({
            'name': name

        })
        return {

            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'start_date': start_date,
            'end_date': end_date,
            'docs': docs,
        }
