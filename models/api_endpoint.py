from odoo import models, fields


class APIEndpoint(models.Model):
    _name = 'api.endpoint'
    _description = 'API Endpoint'
    _rec_name = 'path'

    path = fields.Char("Path", required=True)
    model = fields.Char(string="Model", required=True)
    method = fields.Char("Method", required=True)
    args = fields.Char("Arguments", required=True)
    kwargs = fields.Char("Keyword arguments", required=True)

    _sql_constraints = [
        ("path_unique", "unique (path)", "Path must be unique")
    ]

    # @api.constrains('path')
    # def validate_path(self):
    #     """
    #     Validate the path
    #     """
    #     for record in self:
    #         pass
