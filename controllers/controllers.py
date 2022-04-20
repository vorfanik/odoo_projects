# -*- coding: utf-8 -*-
# from odoo import http


# class Projects(http.Controller):
#     @http.route('/projects/projects', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projects/projects/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('projects.listing', {
#             'root': '/projects/projects',
#             'objects': http.request.env['projects.projects'].search([]),
#         })

#     @http.route('/projects/projects/objects/<model("projects.projects"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projects.object', {
#             'object': obj
#         })
