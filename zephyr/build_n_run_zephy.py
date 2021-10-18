import argparse
import os.path
import subprocess


def build_zephyr(board, path):
    command = f'west build -p always -b {board} {path}'  # command to be executed

    res = subprocess.call(command, shell=True)
    # the method returns the exit code

    print("Returned Value: ", res)
    return res
    pass


def run_flash():
    command = f'west flash'  # command to be executed

    res = subprocess.call(command, shell=True)
    # the method returns the exit code

    print("Returned Value: ", res)
    return res
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='build information')

    parser.add_argument('--board', dest='board', type=str, help='Name of the board')
    parser.add_argument('--path', dest='path', type=str, help='path to the source directory')

    args = parser.parse_args()

    if (args.board is None) or (args.path is None):
        print("no board or path were given")
        print("use '--help' or '-h' for more information")
        exit(1)
        pass

    if not os.path.exists(args.path):
        print("the given path '" + args.path + "' doesn't exist")
        exit(2)
        pass

    if not build_zephyr(board=args.board, path=args.path) == 0:
        print("error in build")
        exit(3)
        pass

    input("press enter to flash")
    if not run_flash() == 0:
        print("error in flash")
        exit(3)
        pass

    print(f"flashed {args.path} on {args.board} successfully")
    exit(0)
