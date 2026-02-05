任务1：
    将当前log tx rx写入方式改成新的写入方式
    当前方式： 逐条写入，写不下的话写入新文件，文件名用时间戳{dut_name}_RX_{ts}.log
    新方式： 每个case生成一个文件，文件名用case_id_{dut_name}_RX_{ts}.log


保存tx rx log函数：
save_boot_log


tx rx路径
self.rx_log_path
self.set_rx_log_path(new_file)
time.sleep(0.1)

self.tx_log_path = os.path.join(base_log_dir, f'{dut_name}_TX_{ts}.log')
self.rx_log_path = os.path.join(base_log_dir, f'{dut_name}_RX_{ts}.log')

class UartBase:
    def __init__(self, dut_name, base_log_dir, bin_path: str = ''):

    def save_boot_log(self):
        # save reboot log
        old_file = self.rx_log_path
        port_name = self.remote_port.device.replace('/', '_')
        new_file = old_file.replace('_RX_', f'_{self.remote_port.ip}{port_name}_BOOT_')
        self.set_rx_log_path(new_file)
        time.sleep(0.1)

        self.reboot_target()
        match, kwargs = self.port_check_rsp('ready!!!', None, strict=False, timeout=30)
        if not match:
            self.LOGGER.error('Failed to check `ready!` after reboot')
        time.sleep(0.1)
        self.set_rx_log_path(old_file)

    def set_rx_log_path(self, path):
        """ set RX log path """
        is_set = self.logging_flag.is_set()
        self.set_uart_logging_flag(False)  # force closed
        self.rx_log_path = path
        with open(self.rx_log_path, 'w') as f:
            f.write('\n')
        self.set_uart_logging_flag(is_set)

    def set_tx_log_path(self, path):
        """ set TX log path """
        is_set = self.logging_flag.is_set()
        self.set_uart_logging_flag(False)  # force closed
        self.tx_log_path = path
        with open(self.tx_log_path, 'w') as f:
            f.write('\n')
        self.set_uart_logging_flag(is_set)


TODO：
1. 生成以下文件夹结构
base_log_dir
 ┗ tc_log
 ┃ ┣ BLUEDROID_GAP_01001
 ┃ ┃ ┣ ESP32C6.BLUEDROID_GAP_01001_17202155_000.html
 ┃ ┃ ┣ ESP32C6.BLUEDROID_GAP_01001_InitCond_17202149_000.html
 ┃ ┃ ┣ ESP32C6.BLUEDROID_GAP_01001_TearDown_17202158_000.html
 ┃ ┃ ┣ SSC1_RX_17202148.log
 ┃ ┃ ┣ SSC1_TX_17202148.log
 ┃ ┃ ┣ SSC1_dev_ttyUSB2_BOOT_17202126.log
 ┃ ┃ ┣ SSC2_RX_17202149.log
 ┃ ┃ ┣ SSC2_TX_17202149.log
 ┃ ┃ ┗ SSC2_dev_ttyUSB3_BOOT_17202126.log
 ┃ ┣ BLUEDROID_GAP_01002
 ┃ ┃ ┣ ESP32C6.BLUEDROID_GAP_01002_17202213_000.html
 ┃ ┃ ┣ ESP32C6.BLUEDROID_GAP_01002_InitCond_17202207_000.html
 ┃ ┃ ┗ ESP32C6.BLUEDROID_GAP_01002_TearDown_17202220_000.html
 ┃ ┗ BLUEDROID_GAP_01003
 ┃ ┃ ┣ ESP32C6.BLUEDROID_GAP_01003_17202235_000.html
 ┃ ┃ ┣ ESP32C6.BLUEDROID_GAP_01003_InitCond_17202230_000.html
 ┃ ┃ ┗ ESP32C6.BLUEDROID_GAP_01003_TearDown_17202248_000.html

 问题：原case_name casebody部分与initcond teardown格式不一致
 BLUEDROID_GAP_01003_InitCond
 BLUEDROID_GAP_01003
 BLUEDROID_GAP_01003_TearDown

格式对齐
预期对齐后生成文件顺序为
BLUEDROID_GAP_01003_InitCond
BLUEDROID_GAP_01003_CaseBody
BLUEDROID_GAP_01003_TearDown
需要将CaseBody换成一个在InitCond和TearDown之间的词
可以用RunCase RunCaseBody ExecuteCase

完成！

2. TX RX log 分case生成，放入对应case的log文件夹
问题： self.tx_log_path self.rx_log_path都在UartBase中，UartBase中的信息在PortManager中实现更改
UartBase和PortManager的交点self.uart_port.items()
跑case时更改tx rx log，但是板子开机启动的log不属于case
单独把chip_boot_log作为一个文件夹，放入tc_log

保存boot log的代码在save_boot_log中
原self.rx_log_path = os.path.join(base_log_dir, f'{dut_name}_RX_{ts}.log')
原boot_log路径.{log_folder}/SSC1_dev_ttyUSB2_BOOT_18174456.log
要改成 {log_folder}/tc_log/0_boot_log/SSC1_dev_ttyUSB2_BOOT_18174456.log
    def save_boot_log(self):
        # save reboot log
        old_file = self.rx_log_path
        port_name = self.remote_port.device.replace('/', '_')
        new_file = old_file.replace('_RX_', f'_{self.remote_port.ip}{port_name}_BOOT_')
        self.set_rx_log_path(new_file)
        time.sleep(0.1)

        self.reboot_target()
        match, kwargs = self.port_check_rsp('ready!!!', None, strict=False, timeout=30)
        if not match:
            self.LOGGER.error('Failed to check `ready!` after reboot')
        time.sleep(0.1)
        self.set_rx_log_path(old_file)



base_dir = os.path.dirname(self.uart_port.rx_log_path)
for log_file in glob.glob(os.path.join(base_dir, "**/*.log"), recursive=True):
    pattern = re.compile(r'SSC\d+_RX_\d+\.log$')
    if pattern.search(os.path.basename(log_file)):
        print(log_file)
        self.delete_empty_log(log_file)


def delete_empty_log(self, file_path):
    """删除空日志文件（仅含时间戳和空行）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        # 检查是否为空或仅包含时间戳和空行
        if not content or all(line.strip() == '' or ']:' in line for line in content.split('\n')):
            os.remove(file_path)
            print(f"Deleted empty log: {file_path}")
            return True
    except Exception as e:
        print(f"Error checking {file_path}: {e}")
    return False                        


完成！

3. heapsize一个芯片一个
    NativeLog.add_heap_size_trace(value)

    def get_free_heap_size(self):
        for dut in self.dut_list:
            heapsize = GENERAL.get_ram(dut)

NativeLog.add_heap_size_trace(heapsize)
完成！
