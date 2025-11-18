from odoo import models
from odoo.exceptions import AccessError

# Inventario
class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    def search(self, args, **kwargs):
        if self.env.user.has_group('exe_restriction_user.group_no_permission'):
            raise AccessError("No tenés permiso para ver Inventario.")
        return super().search(args, **kwargs)

# Fabricación
class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def search(self, args, **kwargs):
        if self.env.user.has_group('exe_restriction_user.group_no_permission'):
            raise AccessError("No tenés permiso para ver Fabricación.")
        return super().search(args, **kwargs)

# Empleados
class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def search(self, args, **kwargs):
        if self.env.user.has_group('exe_restriction_user.group_no_permission'):
            raise AccessError("No tenés permiso para ver Empleados.")
        return super().search(args, **kwargs)

# Sitio Web (ajustado para evitar romper vistas públicas)
class Website(models.Model):
    _inherit = 'website'

    def search(self, args, **kwargs):
        if self.env.user.has_group('exe_restriction_user.group_no_permission') and not self.env.context.get('website_id'):
            raise AccessError("No tenés permiso para ver el Sitio Web.")
        return super().search(args, **kwargs)

# Tableros (comentado por ser modelo abstracto, solo usar si sabés que no rompe vistas)
# class Board(models.AbstractModel):
#     _inherit = 'board.board'
#
#     def search(self, args, **kwargs):
#         if self.env.user.has_group('exe_restriction_user.group_no_permission'):
#             raise AccessError("No tenés permiso para ver Tableros.")
#         return super().search(args, **kwargs)

# Aplicaciones (Apps)
class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    def search(self, args, **kwargs):
        # Evitar bloquear procesos internos o públicos
        if (
            self.env.user.has_group('exe_restriction_user.group_no_permission')
            and not self.env.context.get('frontend_asset_loading')  # contexto interno
            and not self.env.context.get('website_id')              # vistas públicas
            and not self.env.is_superuser                          # procesos del sistema
        ):
            raise AccessError("No tenés permiso para ver Aplicaciones.")
        return super().search(args, **kwargs)