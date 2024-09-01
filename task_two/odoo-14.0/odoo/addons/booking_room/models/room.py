from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Room(models.Model):
    _name = 'room.booking.room'
    _description = 'Room'

    name = fields.Char(string='Room Name', required=True)
    room_type = fields.Selection([
        ('small', 'Meeting Room Small'),
        ('large', 'Meeting Room Large'),
        ('hall', 'Hall')
    ], string='Room Type', required=True)
    location = fields.Selection([
        ('1A', '1A'), ('1B', '1B'), ('1C', '1C'),
        ('2A', '2A'), ('2B', '2B'), ('2C', '2C')
    ], string='Room Location', required=True)
    photo = fields.Binary(string='Room Photo', required=True)
    capacity = fields.Integer(string='Room Capacity', required=True)
    description = fields.Text(string='Description')

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise ValidationError("Room name must be unique!")