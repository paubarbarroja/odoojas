from odoo import http




class berp_website(http.Controller):
    @http.route('/web', auth='public')
    def index(self, **kw):
        return "Hello world"