{
    'name': 'Room Booking',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manage room bookings',
    'description': """
        This module allows you to manage room bookings.
        Features:
        - Manage rooms (name, type, location, photo, capacity)
        - Book rooms
        - Track booking status
        - API for tracking booking status
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',  # Add this line
        'views/room_views.xml',
        'views/booking_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}