#!/bin/bash

# 获取输入参数
src_file=$1
executable_name=$2
onefile_option=$3

# 默认可执行文件名为源文件名（去除扩展名）
if [ -z "$executable_name" ]; then
  executable_name=$(basename "$src_file" | cut -d. -f1)
fi

# 构建命令
build_command="pyinstaller"
if [ -n "$onefile_option" ]; then
  build_command+=" --onefile"
fi
build_command+=" --name $executable_name $src_file"

# 执行构建命令
echo "开始构建..."
echo "$build_command"
$build_command

# 检查构建结果
if [ -e "dist/$executable_name" ]; then
  echo "构建成功！可执行文件位于 dist/$executable_name"
  
  # 将可执行文件移动到系统的 PATH 中
  sudo mv "dist/$executable_name" /usr/local/bin/
  echo "可执行文件已移动到 /usr/local/bin/"

else
  echo "构建失败！请检查错误信息。"
fi
