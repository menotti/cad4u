import argparse
import subprocess


def get_argparser():
    parser = argparse.ArgumentParser(description='NVCCPlugin params')
    parser.add_argument("-t", "--timeit", action='store_true',
                        help='flag to return timeit result instead of stdout')
    return parser


def print_out(out: str):
    for l in out.split('\n'):
        print(l)

'''
    Installing dependencies
'''
def update_install(self, args : str):
    print("Installing dependencies. Please wait... ", end="")

    output = subprocess.check_output(args.split(" "), stderr=subprocess.STDOUT)
    output = output.decode('utf8')
    #helper.print_out(output)
    print("done!")
