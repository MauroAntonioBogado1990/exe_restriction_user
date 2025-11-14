from odoo import models, fields, api
from odoo.exceptions import AccessError

# Inventario
class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    def search(self, args, **kwargs):
        if self.env.user.id == 9:
            raise AccessError("No tenés permiso para ver Inventario.")
        return super().search(args, **kwargs)

# Fabricación
class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def search(self, args, **kwargs):
        if self.env.user.id == 9:
            raise AccessError("No tenés permiso para ver Fabricación.")
        return super().search(args, **kwargs)

# Empleados
class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def search(self, args, **kwargs):
        if self.env.user.id == 9:
            raise AccessError("No tenés permiso para ver Empleados.")
        return super().search(args, **kwargs)

# Sitio Web
class Website(models.Model):
    _inherit = 'website'

    def search(self, args, **kwargs):
        if self.env.user.id == 9:
            raise AccessError("No tenés permiso para ver el Sitio Web.")
        return super().search(args, **kwargs)

# Tableros
class Board(models.Model):
    _inherit = 'board.board'

    def search(self, args, **kwargs):
        if self.env.user.id == 9:
            raise AccessError("No tenés permiso para ver Tableros.")
        return super().search(args, **kwargs)

# Aplicaciones (Apps)
class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    def search(self, args, **kwargs):
        if self.env.user.id == 9:
            raise AccessError("No tenés permiso para ver Aplicaciones.")
        return super().search(args, **kwargs)