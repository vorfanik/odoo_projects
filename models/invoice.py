# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Invoice(models.Model):
    _name = 'projects.invoice'
    _description = "Invoice"


    name = fields.Char(string="Name", required=True)
    project_id = fields.Many2one('projects.project', string = "Project", ondelete="set null")
    works_id = fields.Many2many('projects.works', string="Works")
    sum = fields.Float("Sum", digits=(6, 2))

    status = fields.Selection([
        ('draft', "Draft"),
        ('started', "Started"),
        ('done', "Done"),
        ('cancelled', "Cancelled"),
    ], string="Progress", default='draft', translate=True)