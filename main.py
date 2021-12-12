import sys
from FlaskEnv import FlaskEnv

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        FlaskEnv(sys.argv[1]).run()
    else:
        FlaskEnv().run()