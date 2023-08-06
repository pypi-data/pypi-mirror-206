from unittest import TestCase
from coordsim.simulation.flowsimulator import FlowSimulator
from coordsim.simulation.simulatorparams import SimulatorParams
from coordsim.network import dummy_data
from coordsim.reader import reader
import simpy
import logging
from coordsim.metrics.metrics import Metrics
log = logging.getLogger(__name__)

NETWORK_FILE = "params/networks/triangle.graphml"
SERVICE_FUNCTIONS_FILE = "params/services/abc.yaml"
RESOURCE_FUNCTION_PATH = "params/services/resource_functions"
CONFIG_FILE = "params/config/sim_config.yaml"
SIMULATION_DURATION = 100
SEED = 1234


class TestFlowSimulator(TestCase):
    flow_simulator = None
    simulator_params = None

    def setUp(self):
        """
        Setup test environment
        """
        logging.basicConfig(level=logging.ERROR)

        self.env = simpy.Environment()
        # Configure simulator parameters
        network, ing_nodes, eg_nodes = reader.read_network(NETWORK_FILE, node_cap=10, link_cap=10)
        sfc_list = reader.get_sfc(SERVICE_FUNCTIONS_FILE)
        sf_list = reader.get_sf(SERVICE_FUNCTIONS_FILE, RESOURCE_FUNCTION_PATH)
        config = reader.get_config(CONFIG_FILE)

        self.metrics = Metrics(network, sf_list)

        sf_placement = dummy_data.triangle_placement
        schedule = dummy_data.triangle_schedule

        # Initialize Simulator and SimulatoParams objects
        self.simulator_params = SimulatorParams(
            log, network, ing_nodes, eg_nodes, sfc_list, sf_list, config, self.metrics,
            sf_placement=sf_placement, schedule=schedule)
        self.flow_simulator = FlowSimulator(self.env, self.simulator_params)
        self.flow_simulator.start()
        self.env.run(until=SIMULATION_DURATION)

    def test_simulator(self):
        """
        Test the simulator
        """
        # Collect metrics
        self.metric_collection = self.metrics.get_metrics()
        # Check if Simulator is initiated correctly
        self.assertIsInstance(self.flow_simulator, FlowSimulator)
        # Check if Params are set correctly
        self.assertIsInstance(self.simulator_params, SimulatorParams)
        # Check if generated flows are equal to processed flow + dropped + active flows
        gen_flow_check = self.metric_collection['generated_flows'] == (self.metric_collection['processed_flows'] +
                                                                       self.metric_collection['dropped_flows'] +
                                                                       self.metric_collection['total_active_flows'])
        self.assertIs(gen_flow_check, True)
        # More tests are to come
