from odoo import models, fields, api


class APIAutomation(models.Model):
    _name = 'api.automation'
    _description = 'API Automation'
    _rec_name = 'api_endpoint'

    api_endpoint = fields.Char("API endpoint", required=True)
    model_id = fields.Many2one("ir.model", ondelete='cascade', required=True)
    method = fields.Char("Method", required=True)
    args = fields.Char("Arguments", required=True)
    kwargs = fields.Char("Keyword arguments", required=True)

    _sql_constraints = [
        ("api_endpoint_unique", "unique (api_endpoint)", "API Endpoint must be unique")
    ]

    @api.constrains
    def validate_api_endpoint(self):
        for record in self:
            pass
            # if not record.api_endpoint.startswith('http'):
            #     raise ValidationError("API endpoint must start with 'http'")
