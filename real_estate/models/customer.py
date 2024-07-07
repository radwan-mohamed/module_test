
from odoo import models, fields

class Customer(models.Model):
    _name = 'real.estate.customer'
    _description = 'Real Estate Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    properties = fields.Many2many('real.estate.property', string='Properties')

