
import subprocess
import sys

VOLUME_MOUNT = '--volume .:/data'
JUPYTER_PORTS = '--publish 8888:8888'
IMAGE = 'ghcr.io/phargogh/prototype-natcap-devstack


def main(arg):
    # TODO: make this work automatically, working out of CWD
    if arg == 'jupyter':
        docker_cmd = (
            f'docker run --rm --tty --interactive '
            f'{VOLUME_MOUNT} {JUPYTER_PORTS}')
        subprocess.call(docker_cmd)

    # TODO: make this work like a shell application
    elif arg == 'python':
        docker_cmd = (
            f'docker run --rm --tty --interactive ')



if __name__ == '__main__':
    main(sys.argv[1])
