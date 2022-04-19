from sepal_ui import sepalwidgets as sw

from component import widget as cw
from component.model import WeplanModel
from .aoi_tile import AoiTile


class MapTile(sw.Tile):
    def __init__(self):

        # set the map in the center
        self.map = cw.Map()

        # I decided to set the widgets here instead of in the map to avoid
        # complexity with model sharing
        self.aoi_tile = AoiTile(map_=self.map)

        # extract the models
        self.aoi_model = self.aoi_tile.view.model
        self.model = WeplanModel()

        # create the other tiles

        # place them in the map
        self.map.add_widget_as_control(self.aoi_tile, "bottomright")

        # link to the btn for activation
        self.map.aoi_btn.on_click(lambda *args: self.aoi_tile.toggle_viz())

        # create the tile
        super().__init__(id_="map_tile", title="", inputs=[self.map])
