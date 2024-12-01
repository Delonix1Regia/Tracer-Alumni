# -*- coding: utf-8 -*-
# from odoo import http


# class TracerAlumni(http.Controller):
#     @http.route('/tracer_alumni/tracer_alumni', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tracer_alumni/tracer_alumni/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tracer_alumni.listing', {
#             'root': '/tracer_alumni/tracer_alumni',
#             'objects': http.request.env['tracer_alumni.tracer_alumni'].search([]),
#         })

#     @http.route('/tracer_alumni/tracer_alumni/objects/<model("tracer_alumni.tracer_alumni"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tracer_alumni.object', {
#             'object': obj
#         })

