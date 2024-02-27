import subprocess
import time
import sys


def start_program(start_command):
	subprocess.Popen(start_command, shell=True)


def check_program(program_name):
	result = subprocess.run(["pgrep", "-f", program_name], stdout=subprocess.PIPE)
	return result.returncode == 0


def main(program_name, start_command):
	while True:
		if not check_program(program_name):
			print(f"程序 '{program_name}' 已终止，重启中...")
			start_program(start_command)
		time.sleep(5)


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: python monitor.py <program_name> <start_command>")
		sys.exit(1)

	program_name = sys.argv[1]
	start_command = sys.argv[2]

	main(program_name, start_command)
