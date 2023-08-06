import subprocess

def get_cpu_info():
    command = "cat /proc/cpuinfo | grep 'model name' | uniq | awk -F ':' '{print $2}'"
    output = subprocess.check_output(command, shell=True)
    return output.decode().strip()


def get_disk_info():
    command = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB (%s)\", $3,$2,$5}'"
    output = subprocess.check_output(command, shell=True)
    return output.decode().strip()

def get_network_info():
    command = "ip -4 addr show | grep inet | awk '{print $2}' | cut -d'/' -f1"
    output = subprocess.check_output(command, shell=True)
    return output.decode().strip()

def get_uptime_info():
    command = "uptime | awk '{print $3,$4}' | sed 's/,//'"
    output = subprocess.check_output(command, shell=True)
    return output.decode().strip()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='A command line utility that fetches system data and utilities.')
    parser.add_argument('command', choices=['cpu_info', 'memory_info', 'disk_info', 'network_info', 'uptime_info'], help='the system data command to run')

    args = parser.parse_args()

    if args.command == 'cpu_info':
        print(get_cpu_info())
    elif args.command == 'memory_info':
        print(get_memory_info())
    elif args.command == 'disk_info':
        print(get_disk_info())
    elif args.command == 'network_info':
        print(get_network_info())
    elif args.command == 'uptime_info':
        print(get_uptime_info())

