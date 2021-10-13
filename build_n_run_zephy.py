import argparse
import os.path


def build_zephyr(board, path):
    # west build -p auto -b <your-board-name> samples/basic/blinky
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

    build_zephyr(board=args.board,  path=args.path)


    print(args.board)
    print(args.path)
    pass