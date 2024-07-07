
from odoo import models, fields

class Property(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    bedrooms = fields.Integer(string='Bedrooms')
    bathrooms = fields.Integer(string='Bathrooms')
    agent_id = fields.Many2one('real.estate.agent', string='Agent')
    customer_ids = fields.Many2many('real.estate.customer', string='Customers')
