from sepal_ui import aoi
from sepal_ui.scripts import utils as su


class AoiTile(aoi.AoiTile):
    def __init__(self):

        # create the aoitile
        super().__init__(
            # gee=False,
            methods=["ADMIN0"]
        )

        # preselect country selection and prevent user to change
        self.view.w_method.readonly = True
        self.view.w_method.viz = False
        self.view.w_method.v_model = "ADMIN0"

        # bind an extra js behaviour
        self.view.observe(self.check_prototype, "updated")

    def check_prototype(self, change):
        """only allow the selection of Uganda in this prototype"""

        # exit if nothing
        if self.view.model.name is None:
            return

        print(self.view.model.name.lower())
        if self.view.model.name.lower() != "uganda":
            self.view.reset()
            self.view.w_method.v_model = "ADMIN0"
            self.view.w_admin_0.viz = True
            self.view.alert.add_msg(
                "This module is a prototype, only Uganda can be selected in the list",
                "error",
            )

        return
