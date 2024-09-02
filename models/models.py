from odoo import models, api


class BaseModel(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def advanced_web_search_read(self, *args, **kwargs):
        """
        Advanced web_search_read with pagination
        """

        page = kwargs.pop('page', 1)
        page_size = kwargs.pop('page_size', 20)

        kwargs['limit'] = page_size
        kwargs['offset'] = (page - 1) * page_size

        result = super().web_search_read(*args, **kwargs)
        length = result['length']
        result['previous'] = page - 1 if page > 1 else None
        result['next'] = page + 1 if kwargs['offset'] + page_size < length else None
        return result
