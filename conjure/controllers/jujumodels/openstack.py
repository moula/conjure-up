from conjure.ui.views import OpenStackJujuModelView
from conjure.models.models import OpenStackJujuModel
from conjure.controllers.deploy import DeployController


class OpenStackJujuModelController:
    def __init__(self, common):
        self.common = common
        self.view = OpenStackJujuModelView(self.common,
                                           self.finish)
        self.model = OpenStackJujuModel

    def finish(self, result):
        """ Deploys to the openstack model
        """
        self.model.config.update({k: v.value for k, v in result.items()})
        DeployController(self.common, self.model).render()

    def render(self):
        self.common['ui'].set_header(
            title="OpenStack Juju Model",
            excerpt="Enter your OpenStack credentials to "
            "enable deploying to this model."
        )
        self.common['ui'].set_body(self.view)