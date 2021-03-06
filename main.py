from tests.playground import *
from src.class_factory import *
from src.base_running import *

DEBUG_MODE = True


def main(debug_mode):
    """
    Summary: 
        Entry point of program. 
        If debug mode then test code is run, otherwise
        main program is run

    Params:
        Takes global debug as bool

    """
    if(debug_mode):
        test_main()
    else:
        pass


if __name__ == '__main__':
    main(DEBUG_MODE)
