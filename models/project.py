# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, exceptions


class Project(models.Model):
    _name = "projects.project"
    _description = "Projects"

    name = fields.Char(string="Name", required=True)
    description = fields.Text()
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date")
    client_id = fields.Many2one('res.partner', string="Client", ondelete='set null')
    manager_id = fields.Many2one('hr.employee', string="Project Manager", domain=[('manager_ids', '=', True)])
    employe_ids = fields.Many2many('hr.employee', string="Employees")
    employee_max = fields.Integer(string="Max employees")
    employe_count = fields.Integer(
        string="Employee count", compute='_get_employee_count', store=True)
    employees_percentage = fields.Float(string="Employees percentage (%)", compute='_employees_percentage')
    invoice_ids = fields.One2many('projects.invoice', 'project_id')
    work_ids = fields.One2many('projects.works', 'project_id')
    duration = fields.Integer(string="Project duration", compute='_set_duration')
    active = fields.Boolean(default=True)
    color = fields.Integer()

    @api.depends('employe_ids')
    def _get_employee_count(self):
        for record in self:
            record.employe_count = len(record.employe_ids)

    @api.depends('employe_count')
    def _employees_percentage(self):
        all = self.env['hr.employee'].search_count([])
        for record in self:
            record.employees_percentage = (record.employe_count / all) * 100.0

    # Perspeja, bet leidzia updatint
    @api.onchange('employe_count')
    def _verify_valid_employe_count(self):
        if self.employe_count > self.employee_max:
            return {
                'warning': {
                    'title': f"Incorrect 'employees' value",
                    'message': f"The number of available employees can't be more than {self.employee_max}: {self.employe_count}",
                },
            }

    # Perspeja ir neleidzia paspaust Save
    @api.constrains('employe_count')
    def _check_employe_count(self):
        for record in self:
            if record.employe_count > self.employee_max:
                raise exceptions.ValidationError(
                    f"The number of available employees can't be more than {self.employee_max}: {self.employe_count}")

    # Neleidzia manageri proskirti prie darbuotuju
    @api.constrains('manager_id', 'employe_ids')
    def _check_manager_not_in_employees(self):
        for record in self:
            if record.manager_id and record.manager_id in record.employe_ids:
                raise exceptions.ValidationError(f"The project manager can't be an employee: {self.manager_id.name}")

    @api.depends('start_date', 'end_date')
    def _set_duration(self):
        for record in self:
            if not (record.start_date and record.end_date):
                record.duration = 0
            else:
                record.duration = (record.end_date - record.start_date).days + 1
