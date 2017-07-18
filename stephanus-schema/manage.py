from manager import Manager
from subprocess import call, Popen, PIPE
import os
import pip
import pytest

manager = Manager()

@manager.command
def watch():
    call('ptw')

@manager.command
def test():
    pytest.main()

@manager.command
def install(pkg):
    dir = os.path.dirname(__file__)

    reqs_to_frz = os.path.join(dir, 'requirements-to-freeze.txt')
    with open(reqs_to_frz, 'a') as f:
        f.write(pkg)

    pip.main(['install', '-r', reqs_to_frz])
    reqs = os.path.join(dir, 'requirements.txt')
    p = Popen(['pip', 'freeze', '-r', reqs_to_frz], stdout=PIPE)
    (out, err) = p.communicate()

    with open(reqs, 'w') as f:
        f.write(out.decode('utf-8'))

if __name__ == '__main__':
    manager.main()
