from manager import Manager
import pytest

manager = Manager()

@manager.command
def test():
    pytest.main()

if __name__ == '__main__':
    manager.main()
