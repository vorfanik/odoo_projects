# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Works(models.Model):
    _name = "projects.works"
    _description = "Works"

    name = fields.Char(string=_("Name"), required=True)
    project_id = fields.Many2one('projects.project', string = _("Project"), ondelete="set null")
    color = fields.Integer()
