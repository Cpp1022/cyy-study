#!/bin/bash

# 获取命令行参数
bin_path="$1"
debug_file_dir="$2"
# debug_file_path="$2/BLUEDROID.yml"
debug_file_path="$2/NIMBLE.yml"
log_dir="$3"
num_loops="$4"

# 创建log_dir目录
mkdir -p "$log_dir"

# 读取初始value值
value=$(grep 'line_number:' "$debug_file_path" | awk '{print $2}')


# 循环执行
for ((i = 1; i <= num_loops; i++)); do
    # 打印Python指令
    echo "Executing: python bin/MultiConfigRunner.py -p $bin_path -d $debug_file_dir -f $log_dir/$value.log"

    # 执行Python指令
    eval "python bin/MultiConfigRunner.py -p $bin_path -d $debug_file_dir -f $log_dir/$value.log"

    # 更新debug文件中的value值
    sed -i "s/line_number: $value/line_number: $((value + 1))/" "$debug_file_path"

    # value增加1
    value=$((value + 1))

    # 休眠一段时间（可根据需要调整）
    sleep 1
done
