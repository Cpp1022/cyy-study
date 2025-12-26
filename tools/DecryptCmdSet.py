import pathlib
import re
from AutoTestScript import (DEFAULT_DB_FILE, TEST_CASE_FOLDER)
from AutoTestScript.Tools import UnzipDB
from AutoTestScript.Framework import Database
from AutoTestScript.RunnerConfigs import Config
from AutoTestScript.Utility import BasicMethods
from AutoTestScript.TCAction import CmdHandler

UnzipDB.unzip_database(pathlib.Path(TEST_CASE_FOLDER))
DB = Database.DB(db_file=DEFAULT_DB_FILE)
filter = [
    {'Default': {'SDK': 'FPGA_IDF', 'Test App': 'QACT_BLE_DEFAULT'}},
    {'Add': {
        'SDK': 'FPGA_IDF',
        'Test App': ['QACT_BLE_DEFAULT', 'QACT_BLE_5_DEFAULT'],
        'module': 'BLUEDROID',
        'sub module': 'GAP',
    }}
]
class TestEnv:
    def __init__(self, env_data, node_num):
        self.env_data = env_data
        self.node_num = node_num
    def get_variable_by_name(self, var_name):
        if 'node_num' in var_name:
            node_num = self.node_num
            return ['node_num', eval(var_name)]
        else:
            return [var_name, var_name]

filtered_cases = Config.filter_test_cases(DB, filter)
test_cases = []
origin_pattern = re.compile(r'BLUEDROID_GAP_\d{5}$')
for case in filtered_cases:
    if origin_pattern.search(case['ID']) is None or case.get_attr('SDK') != 'FPGA_IDF':
        continue
    # decryption cmd_set
    env_tag = case.get_attr('test environment')
    env = TestEnv(DB.get_test_env_by_tag(env_tag),
                  int(env_tag.split('_')[1][1:]))
    cmd_set = CmdHandler.process_raw_cmd_set(case, env)
    if cmd_set[0] != '':
        continue
    cmd_set = CmdHandler.merge_yml_sequence(cmd_set[1:])
    cmd_set = CmdHandler.handle_loop(cmd_set, env)
    test_cases.append({
        'ID': case['ID'],
        'cmd_set': cmd_set,
    })

print('count', len(test_cases))
data = {'test cases': test_cases}
yaml_path = 'bluedroid_gap.yml'
BasicMethods.dump_to_yaml_file(data, yaml_path)
