# -*- coding: utf-8 -*-
from odoo import http

# class HrTask(http.Controller):
#     @http.route('/hr_task/hr_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_task/hr_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_task.listing', {
#             'root': '/hr_task/hr_task',
#             'objects': http.request.env['hr_task.hr_task'].search([]),
#         })

#     @http.route('/hr_task/hr_task/objects/<model("hr_task.hr_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_task.object', {
#             'object': obj
#         })