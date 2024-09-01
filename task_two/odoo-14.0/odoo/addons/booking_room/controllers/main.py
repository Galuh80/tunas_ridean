from odoo import http
from odoo.http import request, Response
import json
from odoo.exceptions import AccessError
import logging
from urllib.parse import unquote

_logger = logging.getLogger(__name__)

class RoomBookingController(http.Controller):

    @http.route('/api/room_booking/status/<string:booking_name>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_booking_status(self, booking_name, **kwargs):
        try:
            decoded_booking_name = unquote(booking_name)  # Decode the booking name
            _logger.info(f"Encoded booking_name: {booking_name}")
            _logger.info(f"Decoded booking_name: {decoded_booking_name}")
            
            booking = request.env['room.booking.booking'].sudo().search([('name', '=', decoded_booking_name)], limit=1)
            if not booking:
                return Response(json.dumps({'error': 'Booking not found'}), status=404, mimetype='application/json')
            
            booking_data = {
                'id': booking.id,
                'name': booking.name,
                'status': booking.state,
                'room': booking.room_id.name,
                'date': booking.booking_date.strftime('%Y-%m-%d') if booking.booking_date else False,
                'booker': booking.booker_name
            }
            return Response(json.dumps(booking_data), status=200, mimetype='application/json')
        except AccessError:
            _logger.exception("Access denied error")
            return Response(json.dumps({'error': 'Access denied'}), status=403, mimetype='application/json')
        except Exception as e:
            _logger.exception("Error while fetching booking status")
            return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')

    @http.route('/api/room_booking/swagger.json', type='http', auth='public')
    def get_swagger_json(self):
        return json.dumps({
            "swagger": "2.0",
            "info": {
                "title": "Room Booking API",
                "version": "1.0"
            },
            "paths": {
                "/api/room_booking/status/{booking_name}": {
                    "get": {
                        "summary": "Get booking status",
                        "parameters": [
                            {
                                "name": "booking_name",
                                "in": "path",
                                "required": True,
                                "type": "string"
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Successful response",
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "integer"},
                                        "name": {"type": "string"},
                                        "status": {"type": "string"},
                                        "room": {"type": "string"},
                                        "date": {"type": "string"},
                                        "booker": {"type": "string"}
                                    }
                                }
                            },
                            "404": {
                                "description": "Booking not found"
                            },
                            "403": {
                                "description": "Access denied"
                            },
                            "500": {
                                "description": "Internal server error"
                            }
                        }
                    }
                }
            }
        })

    @http.route('/api/room_booking/swagger', type='http', auth='public')
    def swagger_ui(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Room Booking API Swagger</title>
            <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.51.1/swagger-ui.min.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.51.1/swagger-ui-bundle.min.js"></script>
        </head>
        <body>
            <div id="swagger-ui"></div>
            <script>
                window.onload = function() {
                    SwaggerUIBundle({
                        url: "/api/room_booking/swagger.json",
                        dom_id: '#swagger-ui',
                        presets: [
                            SwaggerUIBundle.presets.apis,
                            SwaggerUIBundle.SwaggerUIStandalonePreset
                        ],
                        layout: "BaseLayout"
                    })
                }
            </script>
        </body>
        </html>
        """