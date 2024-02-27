import subprocess
import time
import argparse

def start_program(start_command):
    # 启动程序
    return subprocess.Popen(start_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def check_program(process):
    # 检查程序是否在运行
    return process.poll() is None

def monitor(program_name, start_command):
    process = start_program(start_command)
    print(f"程序 '{program_name}' 已启动，PID: {process.pid}")
    while True:
        if not check_program(process):
            print(f"程序 '{program_name}' 已终止，重启中...")
            process = start_program(start_command)
            print(f"程序 '{program_name}' 已重新启动，PID: {process.pid}")
        # 输出程序的标准输出和标准错误输出
        for line in process.stdout:
            print(line.decode().strip())
        for line in process.stderr:
            print(line.decode().strip())
        time.sleep(1)  # 每隔1秒检查一次程序是否在运行

def main():
    parser = argparse.ArgumentParser(description="监控指定程序的运行状态，并在程序终止时自动重启")
    parser.add_argument("program_name", type=str, help="要监控的程序名称")
    parser.add_argument("start_command", type=str, help="启动程序的命令")
    args = parser.parse_args()
    monitor(args.program_name, args.start_command)

if __name__ == "__main__":
    main()
