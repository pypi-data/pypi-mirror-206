import os
from pathlib import Path

from steam_pysigma.comsol.BuildComsolModel import BuildComsolModel
from steam_pysigma.data import DataSIGMA as dS
import yaml
from steam_pysigma.utils import Util
import steam_pysigma.pysigma as ps
import logging


class MainSIGMA:
    """
        Class to generate SIGMA models
    """

    def __init__(self, input_file_path: str = None, model_folder: str = None, dm=None,
                 system_settings: dict = None, verbose: bool = False):
        """
              Main class for working with FiQuS simulations
              :param input_file_path: input file full path
              :param verbose: if True, more info is printed in the console
              """
        self.start_folder = os.getcwd()
        self.wrk_folder = model_folder
        self.g = ps.GatewaySIGMA()

        logger = logging.getLogger()
        if verbose:
            logger.setLevel(logging.INFO)
        else:
            logger.setLevel(logging.DEBUG)

        #if Path.exists(system_settings_path):
           # with open(system_settings_path, 'r') as stream:
                #self.settings = yaml.safe_load(stream)
        self.settings = system_settings
        # Load yaml input file
        if not dm:
            self.dm = Util.FilesAndFolders.read_data_from_yaml(input_file_path, dS.DataSIGMA)
        else:
            self.dm = dm
        self.sdm = Util.FilesAndFolders.read_data_from_yaml(f'{input_file_path[:-5]}.set', dS.MultipoleSettings)
        self.roxie_data = Util.FilesAndFolders.read_data_from_yaml(f'{input_file_path[:-5]}.geom', dS.SIGMAGeometry)

        # domains = self.build_domains()

        BuildComsolModel(self.dm, self.sdm, self.settings, self.wrk_folder, self.roxie_data)


if __name__ == "__main__":
    # if len(sys.argv) < 4:
    #     mp = MainFiQuS(sys.argv[1], sys.argv[2])

    magnet = 'MQXA_SIGMA'
    yaml_file = f'{magnet}.yaml'
    output_folder = r"C:\Users\jlidholm\Git-projects\steam-pysigma\steam-pysigma"
    print(os.path.join(output_folder))
    system_settings_path = (Path.joinpath(Path(__file__).parent, "../steam_pysigma/settings.SYSTEM.yaml"))
    if Path.exists(system_settings_path):
        with open(system_settings_path, 'r') as stream:
            settings = yaml.safe_load(stream)
    sim_result = MainSIGMA(input_file_path=yaml_file,
                           system_settings=settings, model_folder=os.path.join(output_folder))
