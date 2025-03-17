from Planner import Planner
from Driver import Driver

def main():
    """Program entry point.
    
    Creates a Driver instance and starts the simulation by calling
    its run method.
    """
    driver = Driver()
    driver.run()

if __name__ == '__main__':
    main()