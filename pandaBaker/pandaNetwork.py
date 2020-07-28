import os
from htm.bindings.engine_internal import Network as BaseNetwork

from pandaBaker.pandaBaker import PandaBaker


BAKE_DATABASE_FILE_PATH = os.path.join(os.getcwd(), 'bakedDatabase', 'pandaVis.db')

class Network(BaseNetwork):
    def __init__(self):
        self.firstRun = True
        self.pandaBaker = PandaBaker(BAKE_DATABASE_FILE_PATH)
        self.iteration = 0
        super().__init__()

    def run(self, n):
        print("Running "+str(n)+" times")
        for i in range(n):
            super().run(1)
            if self.firstRun:
                self.FirstRun()
            self.pandaBaker.StoreIteration(self, self.iteration)
            self.iteration += 1
        self.pandaBaker.CommitBatch() # called too often? performance issue?

    def FirstRun(self):
        print("first run")
        self.firstRun = False

        structure = {}
        regions = {}
        links = {}
        structure["regions"] = regions
        structure["links"] = links

        for region in self.getRegions():
            print(region[1])
            regions[region[0]] = [region[1].getType(), region[1]]

        i = 0
        for l in self.getLinks():
            links[i] = [l.getSrcRegionName(), l.getSrcOutputName(), l.getDestRegionName(), l.getDestInputName()]

            i = i+1

        self.pandaBaker.PrepareDatabase(structure)



