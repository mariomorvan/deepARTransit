import argparse


def get_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-c', '--config',
        metavar='C',
        default='None',
        help='The Configuration file')
    argparser.add_argument(
        '-e', '--experiment',
        metavar='E',
        help='The experiment name')
    argparser.add_argument(
        '-r', '--radius',
        metavar='R', type=int,
        help='The aperture radius')

    args = argparser.parse_args()
    return args

