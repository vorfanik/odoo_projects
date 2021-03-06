from odoo import models, fields, api, _

class Wizard(models.TransientModel):
    _name = 'projects.wizard'
    _description = "Quick Add of Employees to Projects"

    def _default_projects(self):
        return self.env['projects.project'].browse(self._context.get('active_ids'))

    project_ids = fields.Many2many('projects.project',
                                   string=_("Projects"), required=True, default=_default_projects)
    employe_ids = fields.Many2many('hr.employee', string=_("Employees"))

    def add_employees(self):
        for project in self.project_ids:
            project.employe_ids |= self.employe_ids
        return {}