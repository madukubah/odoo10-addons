from odoo import api, fields, models, _

class ExpenseType(models.Model):
    _name='expense.type'
    _description = 'Expense Type'

    expense_type = fields.Char('Expense Type', required = True)
    interval = fields.Char('Interval' , required=True)
    duration_type = fields.Selection([
        ('year','Year'),
        ('month','Month'),
        ('week','Week'),
        ('day', 'Day')
        ],required=True)
    qty_limit = fields.Float('Qty Limit')
    amount_limit = fields.Float('Amount Limit')
    job_position = fields.Many2many('hr.job',string="Job Position")
    duration = fields.Char('Duration of Employment (months)')
    employment_status = fields.Selection([
        ('active','Active'),
        ('probation','Probation'),
        ('full','Full Time'),
        ('part', 'Part Time'),
        ('contract_based','Contract Based'),
        ('notice','In Notice'),
        ('internship','Internship'),
        ('terminated','Terminated'),
        ('outsourced', 'Outsourced'),
        ('others', 'Others')],string='Employment Status')