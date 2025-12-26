检查 CI_FULL_BUILD 环境变量
    ↓
如果是全量编译 → 查找所有Python文件 → 生成编译列表
    ↓
如果是增量编译 → 计算MERGE_BASE → git diff获取变化文件 → 生成编译列表
    ↓
ARM架构特殊过滤 → 并行构建任务分割 → 输出最终编译列表
    ↓
后续任务读取 _BUILD_SRC_LIST 进行选择性编译