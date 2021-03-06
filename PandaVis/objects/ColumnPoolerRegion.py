from .region import cRegion
from objects.cell import cCell

class cColumnPoolerRegion(cRegion):

    def __init__(self, name, cellData, gui):
        super().__init__(name, cellData, gui)

        self.cellCount = self.parameters["cellCount"]# 2048
        self.cells = []

        for i in range(self.cellCount):
            c = cCell(None)
            self.cells.append(c)

        self.subObjects = self.cells

        self.CELL_OFFSET = 0.4  # space between cells

        self.SUBOBJ_DISTANCE_X = 1 + self.CELL_OFFSET
        self.SUBOBJ_DISTANCE_Y = 1 + self.CELL_OFFSET

        # connection definitions - key is connection type, follows value
        # with file suffix name (array, one region can have multiple distal connections for example)
        self.connections = {'proximal': ['proximal'], 'distal': ['distal']}

    def getBoundingBoxSize(self):
        return [self.SUBOBJ_PER_ROW * self.SUBOBJ_DISTANCE_X, 1]  # [horizontal, vertical]

    def UpdateState(self, regionData):  # regionData is cRegionData class from dataStructs.py
        super().UpdateState(regionData)

        for cellID in range(len(self.cells)):  # for each cell
            isActive = regionData.data["activeCells"][cellID]

            self.cells[cellID].UpdateState(active=isActive, predictive=False, winner=False, focused=False,
                                           presynapticFocus=False,
                                           showPredictionCorrectness=False, prev_predictive=False)