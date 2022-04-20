# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Project(models.Model):
    _name = "projects.project"
    _description = "Projects"

    name = fields.Char(string="Name", required=True)
    description = fields.Text()
    manager_id = fields.Many2one('hr.employee', string="Project Manager", ondelete='set null')
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date")
    invoice_ids = fields.One2many('projects.invoice', 'project_id')
    work_ids = fields.One2many('projects.works', 'project_id')