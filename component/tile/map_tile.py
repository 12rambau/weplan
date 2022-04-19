from sepal_ui import sepalwidgets as sw

from component import widget as cw
from component.model import WeplanModel
from .aoi_tile import AoiTile
from .param_tile import ParamTile
from .download_tile import DownloadTile


class MapTile(sw.Tile):
    def __init__(self):

        # set the map in the center
        self.map = cw.Map()

        # extract the models
        self.model = WeplanModel()

        # create the tiles
        self.aoi_tile = AoiTile(map_=self.map, model=self.model)
        self.param_tile = ParamTile(model=self.model)
        self.download_tile = DownloadTile(model=self.model)

        # place them in the map
        self.map.add_widget_as_control(self.aoi_tile, "bottomright")
        self.map.add_widget_as_control(self.param_tile, "topright", first=True)
        self.map.add_widget_as_control(self.download_tile, "bottomleft")

        # link to the btn for activation
        self.map.aoi_btn.on_click(lambda *_: self.aoi_tile.toggle_viz())
        self.map.param_btn.on_click(lambda *_: self.param_tile.toggle_viz())
        self.map.download_btn.on_click(lambda *_: self.download_tile.toggle_viz())

        # create the tile
        super().__init__(id_="map_tile", title="", inputs=[self.map])
