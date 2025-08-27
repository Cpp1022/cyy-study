#### 一、ATS新框架适配[用于跑case]  (@cuiyiyi)

##### 1. 所有import 引用路径修改
##### 2. initcond cmd set 都改成调脚本，脚本中根据case配置寻找对应函数
  - 解决每个case一个initcond的问题-直接走BLEInitCond.py根据initcond直接找函数，去调原来sp_op的过程
  - cmd_set解决BTSTK和BLUEDROID NIMBLE覆盖的问题
##### 3. initcond和teardown适配新框架：基于原ats环境-->基于新框架
  - self.xxx = self.case_parameters['xx'] -> case_config['xx']
  - `DEFAULT_PARAMS` sp_op/ble_check_flag / client server / target_dut 放入case_config中，统一读取
  - 新增Action中各模块注入函数inject_modules_to_module，initcond和teardown的init过程中自动注入
  - 重写BLEInitCond脚本，直接调action中的函数
  - teardown 读写指令函数改成调用新框架中的函数write_serial_line -> write / check_response&check_regular_expression -> check（待优化：调action）
  - cable env处理: 新增cable_env_init函数 根据原cable_env默认值配置 [cable_enable, txp_lvl, rx_sens_thresh, agc_max_gain]

#### 二、新框架功能与内容优化  (@cuiyiyi)

##### 1. 化检查指令：
  - check_response&check_regular_expression -> check
      - 优化1：兼容指定字符串检查和正则表达式匹配
      - 优化2：增加自动转义尝试 - 新增ensure_compiled_pattern和is_regex_safe函数，并内嵌至Port的check函数中
          - 自动处理 pattern，确保返回的是编译后的 re.Pattern 对象
          - 如果 pattern 是 str，尝试编译，失败则转义后再编译
          - 如果已是 Pattern，则直接返回
          - 若尝试转义失败则报错提示
      - 优化3：直接返回match.group(1)
  - 支持 ['a', 'AND', 'b'] 形式，要求 a 和 b 同时命中
  - 支持 ['a', 'OR', 'b'] 形式，任一命中即可
  - 不支持超出 3 项的复杂逻辑
  
##### 2. class BLEModuleBase中优化功能函数(目的：使需匹配的检查更方便)
  - read_cache -> read(cls, dut_name: str, clear_cache=True, timeout=1)
      - 将sleep封装进read函数read(dut_name, timeout=5)表示读5秒的cache，不需要先time.sleep再read_cache
  - 新增check_cache函数 check_cache(cls, dut_name: str, pattern, timeout=10, clear_cache=True)
      - 将正则匹配封进函数 check_cache(dut_name, pattern, timeout=5) 表示读5s的cache，匹配pattern(指定字符串/正则表达式)
      - 直接返回match.group(1)
  - 新增multi_check_cache函数 multi_check_cache(cls, dut_name: str, pattern_list: list, clear_cache=True)
      - 支持检查多个pattern，以list形式输入即可
      - pattern可以是['abcd', r'(\d+).*xxxx', fr'xxx(\w+).*,{variable}']
  - 新增clear_cache函数，处理read_cache系列函数clear_cache=False情况
  
##### 3. Log新增内容适配旧ats框架
  - 新增3种预设的html格式 simple_red_box / animated_border_box / animated_alert_box
    - 用于区分bug性质，eg.上一个case teardown错误导致的initcond错误，采用最严重animated_alert_box，红色底&边框闪烁&警铃闪烁
  - 新增allure(支持pytest的log框架)log
    - 结合allure.attach功能，新封装attach_warning_to_allure函数，用于针对不同级别bug设置报错样式
      - attach_warning_to_allure(fail_msg, title="04_FAILED_CASE_ANALYSIS", style="simple", level="analysis") 
      - 通过level控制报错格式级别，'simple' | 'border' | 'animated'分别对应simple_red_box / animated_border_box / animated_alert_box
    - VNC里没有allure，需要将上述功能拆分，额外封装函数到NativLog中，然后调用外部写好的allure相关函数

#### 三、case迁移特殊问题进一步处理 (@cuiyiyi)

##### 1. yaml中anchor和loop交错的复杂场景
  - anchor中包含loop
  - loop中包含anchor
  - loop内容中包含非数字('C' 'NC')
  - loop中包含range
  - anchor/loop中包含<node_num> (迁case时不知道node_num)

##### 2. action.py进一步完善
  - action.py新增class CTE,新增CTE指令 完善cte指令rsp
  - action.py新增TAG指令，针对anchor中包含<node_num>的tag   
      - dut1_connected_by_slaves
      - dut1_connected_by_slaves_ext
  - action.py中大批量换行，目的过pipline检测(麻烦，函数入参过多，缺省加长参数名)
  - action.py中 Optional[list]=None过不了pipline，改成xxx: list | None = None

#### 四、适配数据库筛选 (@kongxiangyu)

##### 1. 优化 Case 筛选流程

* 原流程：

  1. 筛选 case；
  2. 获取 test env；
  3. 检查本地环境是否满足 test env；
  4. 再次筛选出可运行的 case。

* 新流程：

  1. 筛选出要运行的 case，并保存；
  2. 检查本地环境是否满足这些 case 所需的 test env；
  3. 直接运行已保存的 case。

这样避免了“筛选 → 检查 → 再筛选”的重复逻辑，提高了效率。

##### 2. 适配数据库的 `cmd set` 与 `teardown` 解密

* 问题背景：

  * 原 ATS 的 `EnvBase` 结构与每个 case 的 `test env` 绑定，解密流程依赖 `EnvBase`。
  * 新框架中，`env` 与 case 解耦，无法直接传入解密函数。

* 解决方案：

  * 从数据库中根据每个 case 的 `test env` 筛选出 env data；
  * 将 `EnvBase` 中的 data 模块单独抽取出来，作为解密函数的输入参数；
  * 在新框架外部构造 `env data`，以适配原有的解密流程；
  * 研究 VNC 中 `cmd set` 与 `teardown` 的解密逻辑，定位对应的解密函数并完成适配。

##### 3. 支持 Case ID 抽象筛选

* 新增筛选规则，支持参数化 case 的范围与随机选择：

  * `NIMBLE_AUDIO_05008@[1/4-10]` → 运行 `_001, _004, _005, ... _010`；
  * `NIMBLE_AUDIO_05008@[1/4-10]{3}` → 在上述范围内随机选 3 个；
  * `NIMBLE_AUDIO_05008@{3}` → 在所有 case 中随机选 3 个。


##### 4. 统一 Case 调用流程

* 问题：迁移后的 case 以函数形式存在，与原脚本类 case、teardown 的调用方式不统一
* 方案：

  * 引入统一的 **BLECaseSimple / BTCaseSimple** 调度流程；
  * 通过解析 caseid 与 test_case 信息，获取 `id / module / submodule`；
  * 根据 `module + submodule` 确定目标模块，再结合 `id` 找到对应函数；
  * 在统一流程中调用目标函数并传入参数。


##### 5. Case 配置参数统一化

* 原框架中 `cable_enable / target / test_points / sp_op` 等变量分散在用例参数、环境参数和 test_case 配置中，导致逻辑混乱。
* 新方案：将这些变量统一收敛到 **case_config** 中集中管理，简化流程并提升可维护性。

#### 五、BT 适配新框架 (@weiruohe)
- 迁case
  - 将经典蓝牙的inicond，case对应的yml,python文件，teardown适配入新框架。
- 新增功能函数
  - 新增not_check_cache函数，实现，下发命令后check 语句1->Delay time->Not Check指定语句