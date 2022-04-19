from sepal_ui import sepalwidgets as sw
from .aoi_view import AoiView


class AoiTile(sw.Card):
    def __init__(self, map_):

        # get the map as a member
        self.map = map_

        # add the base widgets
        self.close = sw.Icon(children=["mdi-close"], small=True)
        self.title = sw.CardTitle(
            class_="pa-0 ma-0", children=[sw.Spacer(), self.close]
        )

        # add the nested AoiView
        self.view = AoiView(map_=self.map)

        # create the object
        super().__init__(
            max_width="410px",
            class_="pa-1",
            children=[self.title, self.view],
            viz=False,
        )

        # add javascript events
        self.close.on_event("click", lambda *args: self.hide())
