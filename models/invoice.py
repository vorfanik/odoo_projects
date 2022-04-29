# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Invoice(models.Model):
    _name = 'projects.invoice'
    _description = "Invoice"


    name = fields.Char(string=_("Name"), required=True)
    project_id = fields.Many2one('projects.project', string = _("Project"), ondelete="set null")
    works_id = fields.Many2many('projects.works', string=_("Works"))
    sum = fields.Float(string=_("Sum"), digits=(6, 2))

    status = fields.Selection([
        ('draft', "Draft"),
        ('started', "Started"),
        ('done', "Done"),
        ('cancelled', "Cancelled"),
    ], string=_("Progress"), default='draft', translate=True)