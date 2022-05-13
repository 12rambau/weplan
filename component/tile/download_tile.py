from shutil import copy
import time

from sepal_ui import sepalwidgets as sw
from sepal_ui.scripts import utils as su

from component import parameter as cp


class DownloadTile(sw.Card):
    def __init__(self, model):

        # read the model
        self.model = model

        # add the base widgets
        self.close = sw.Icon(children=["mdi-close"], small=True)
        self.title = sw.CardTitle(
            class_="pa-0 ma-0", children=[sw.Spacer(), self.close]
        )

        # create the widgets
        self.w_target = sw.Select(
            small=True,
            items=[{"text": f"{i+1}0%", "value": i + 1} for i in range(cp.nb_target)],
            v_model=[model.target],
            label="target",
            dense=True,
            multiple=True,
            clearable=True,
            chips=True,
        )
        self.w_weight = sw.Select(
            small=True,
            items=[i + 1 for i in range(cp.nb_weight)],
            v_model=[model.weight],
            label="weight",
            dense=True,
            multiple=True,
            clearable=True,
            chips=True,
        )

        # compulsory component to display a process
        self.btn = sw.Btn("Retreive to SEPAL", color="secondary")
        self.actions = sw.CardActions(
            class_="pa-0 ma-0", children=[sw.Spacer(), self.btn]
        )
        self.alert = sw.Alert()

        # create the object
        super().__init__(
            max_width="410px",
            min_width="410px",
            class_="pa-1",
            children=[
                self.title,
                self.w_target,
                self.w_weight,
                self.actions,
                self.alert,
            ],
            viz=False,
        )

        # add javascript events
        self.close.on_event("click", lambda *args: self.hide())
        self.btn.on_event("click", self.retreive)

    def add_target(self, target):
        """add a target to the v_model values"""

        tmp = list(set([target, *self.w_target.v_model]))
        self.w_target.v_model = tmp

        return

    def add_weight(self, weight):
        """add a weight to the v_model values"""

        tmp = list(set([weight, *self.w_weight.v_model]))
        self.w_weight.v_model = tmp

        return

    @su.loading_button(debug=True)
    def retreive(self, widget, event, data):
        """retreive the files from the tmp directory to SEPAL folders"""

        # check that the folder exist
        to_dir = cp.weplan_dir / self.model.iso
        to_dir.mkdir(exist_ok=True)

        # fill it with the selected files
        from_dir = cp.tmp_dir / f"{self.model.iso}_{cp.version}"

        # available
        copy(from_dir / cp.f_available.format(cp.version), to_dir)

        for target in self.w_target.v_model:

            # mincost
            copy(from_dir / cp.f_mincost.format(target, cp.version), to_dir)

            for weight in self.w_weight.v_model:

                # ce
                copy(from_dir / cp.f_ce.format(target, weight, cp.version), to_dir)

                # mb
                copy(from_dir / cp.f_mb.format(target, weight, cp.version), to_dir)

        # wait at least 3 seconds so that the user can see the actual
        # spinning wheel
        time.sleep(3)

        return

    def reset(self):

        self.w_target.v_model = []
        self.w_weight.v_model = []

        self.hide()

        return
