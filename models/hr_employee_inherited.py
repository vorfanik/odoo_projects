# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    manager_ids = fields.Boolean("Managerial Duties", default=False)
    project_employee = fields.Many2many('projects.project', string = "Projects employee", readonly=True)
    project_manager = fields.One2many('projects.project', 'manager_id', string="Project manager", readonly=True)
