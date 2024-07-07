

from odoo import models, fields

class Agent(models.Model):
    _name = 'real.estate.agent'
    _description = 'Real Estate Agent'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    properties = fields.One2many('real.estate.property', 'agent_id', string='Properties')

