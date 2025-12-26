### check_external_files流程:
    初始化环境和变量
        ↓
    确定目标分支和合并基准点
        ↓
    获取当前提交与基准点的差异文件列表
        ↓
    检查是否有文件变更?
        ├── 无变更 → 标记为仅内部变更 → 成功退出
        ↓ 有变更
    遍历每个变更文件进行外部性检查
        ↓
    文件检查逻辑:
        ├── 在预忽略列表中? → 跳过检查
        ├── 在预检查列表中? → 标记为外部变更
        ├── 是Python/SO文件且在忽略目录中? → 跳过检查
        └── 其他情况 → 标记为外部变更
        ↓
    检查结果判断:
        ├── 发现外部变更 → 报错并要求外部MR审查 → 失败退出
        ↓ 无外部变更
    标记为仅内部变更 → 成功退出

文件分类规则:
预忽略文件: 测试文件、CI工具、已知问题等内部文件
预检查文件: 核心脚本目录，总是视为外部变更
忽略脚本: 框架内部的Python/SO文件不视为外部变更
其他文件: 默认都视为外部变更

---

##### check_external_files详细流程:
    设置 set -e 严格模式
        ↓
    初始化 EXTERNAL_CHANGED="false"
        ↓
    定义 CheckFileWasExternal 函数
        ↓
    设置CI环境变量默认值
        ↓
    删除 INTERNAL_CHANGES_ONLY 文件
        ↓
    输出分支和提交信息
        ↓
    确定合并基准点(MERGE_BASE)
        ↓
    获取变更文件列表(CHANGED_FILES)
        ↓
    是否有文件变更?
        ├── 否 → 创建 INTERNAL_CHANGES_ONLY 文件 → 退出状态0(成功)
        ↓ 是
    遍历每个变更文件
        ↓
    调用 CheckFileWasExternal 函数
        ↓
    文件检查流程:
        ├── 在 PRE_IGNORE_FILES 中? → 是 → 返回(不标记)
        ↓ 否
        ├── 在 PRE_CHECK_FILES 中? → 是 → 标记为外部变更 → 返回
        ↓ 否
        ├── 是.py或.so文件?
        │   ├── 是 → 在 IGNORE_SCRIPT_FILES 目录中? → 是 → 返回(不标记)
        ↓   ↓ 否
        │   标记为外部变更 → 返回
        ↓
        └── 其他文件 → 标记为外部变更 → 返回
        ↓
    所有文件检查完成
        ↓
    EXTERNAL_CHANGED 是否为 "yes"?
        ├── 是 → 输出错误信息 → 退出状态1(失败)
        ↓ 否
    创建 INTERNAL_CHANGES_ONLY 文件
        ↓
    退出状态0(成功)



##### CheckFileWasExternal 函数详细流程:
    输入: FILE
        ↓
    遍历 PRE_IGNORE_FILES
        ↓
    FILE 是否匹配任一忽略项?
        ├── 是 → 直接返回
        ↓ 否
    遍历 PRE_CHECK_FILES
        ↓
    FILE 是否匹配任一预检查项?
        ├── 是 → 输出变更信息 → 设置 EXTERNAL_CHANGED="yes" → 返回
        ↓ 否
    FILE 后缀是 .py 或 .so?
        ├── 是 → 遍历 IGNORE_SCRIPT_FILES
        │   ↓
        │   FILE 是否在忽略目录中?
        │   ├── 是 → 直接返回
        │   ↓ 否
        │   输出变更信息 → 设置 EXTERNAL_CHANGED="yes" → 返回
        ↓ 否
    输出变更信息 → 设置 EXTERNAL_CHANGED="yes" → 返回




##### 关键文件分类:
    PRE_IGNORE_FILES (完全忽略):
    - TestCaseFiles/YAMLFiles
    - tools/ci
    - tools/ats_unit_test/internal
    - 等测试和工具文件

    PRE_CHECK_FILES (总是标记为外部):
    - packages/AutoTestScript/TestCaseScript/TearDown
    - packages/AutoTestScript/TestCaseScript/ATSExamples
    - 等核心脚本目录

    IGNORE_SCRIPT_FILES (Python/SO文件忽略):
    - packages/AutoTestScript/TestCaseScript/
    - packages/AutoTestScript/Runner/
    - 等框架目录

