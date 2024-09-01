# models/booking.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Booking(models.Model):
    _name = 'room.booking.booking'
    _description = 'Room Booking'

    name = fields.Char(string='Booking Number', required=True, readonly=True, default='New', copy=False, index=True)
    room_id = fields.Many2one('room.booking.room', string='Room', required=True)
    booker_name = fields.Char(string='Booker Name', required=True)
    booking_date = fields.Date(string='Booking Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')
    ], string='Status', default='draft')
    notes = fields.Text(string='Booking Notes')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The booking number must be unique"),
    ]

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self._generate_booking_number(vals)
        return super(Booking, self).create(vals)

    def _generate_booking_number(self, vals):
        room = self.env['room.booking.room'].browse(vals.get('room_id'))
        sequence = self.env['ir.sequence'].next_by_code('room.booking.sequence') or '_'
        
        # Handle both string and Date object inputs for booking_date
        booking_date = vals.get('booking_date')
        if isinstance(booking_date, str):
            booking_date = fields.Date.from_string(booking_date)
        elif isinstance(booking_date, datetime):
            booking_date = booking_date.date()
        
        return f"{room.room_type[:3].upper()}_{room.location}_{booking_date}_{sequence}"

    @api.constrains('room_id', 'booking_date')
    def _check_room_availability(self):
        for record in self:
            conflicting_bookings = self.search([
                ('room_id', '=', record.room_id.id),
                ('booking_date', '=', record.booking_date),
                ('id', '!=', record.id)
            ])
            if conflicting_bookings:
                raise ValidationError("This room is already booked for the selected date!")

    @api.constrains('booker_name')
    def _check_unique_booker(self):
        for record in self:
            if self.search_count([('booker_name', '=', record.booker_name), ('booking_date', '=', record.booking_date)]) > 1:
                raise ValidationError("A person cannot have multiple bookings on the same date!")

    def action_confirm(self):
        self.write({'state': 'ongoing'})

    def action_done(self):
        self.write({'state': 'done'})