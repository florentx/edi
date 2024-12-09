# Copyright 2022 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import mock

from odoo.tests.common import Form, SavepointCase


class TestCommon(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        # Execute directly, no job
        cls.wiz_model = cls.env["product.import"].with_context(queue_job__no_delay=True)
        cls.supplier = cls.env["res.partner"].create({"name": "Catalogue Vendor"})

    def _mock(self, method_name, **kw):
        return mock.patch.object(type(self.wiz_model), method_name, **kw)

    @property
    def wiz_form(self):
        return Form(self.wiz_model)
