import pathlib
import argparse 

from modules.Config import Config
from modules.Log import Log

class DataDudeCLI:
    def __init__(self):
        self.argumentParser = None
        self.init()

    def init(self):
        Config.load(pathlib.Path(__file__).parent.absolute() / "app.ini")
        Log.init()
        Log.info(Config.get("application", "name") + " " + Config.get("application", "version"))
        self.prepare_arguments()

    def prepare_arguments(self):
        Log.info("parsing arguments ...")

        self.argument_parser = argparse.ArgumentParser(prog=Config.get("application", "name"))
        subparsers = self.argument_parser.add_subparsers()

        searchParser = subparsers.add_parser("search", help="searches for patterns in data")
        searchParser.add_argument("-p", "--pattern", required=True, help="pattern to search for")
        searchParser.add_argument("-r", "--resource", required=True, help="target file or device for search process")
        searchParser.add_argument("-m", "--inmemory", action="store_true", default=False, help="load resource to memory before search")
        searchParser.set_defaults(func=self.searchAction)

        patchParser = subparsers.add_parser("patch", help="patch data in data")
        patchParser.add_argument("-i", "--input", required=True, help="data to write")
        patchParser.add_argument("-r", "--resource", required=True, help="target file or device to write data")
        patchParser.set_defaults(func=self.patchAction)

    def run(self):
        args = self.argument_parser.parse_args()
        if not hasattr(args, "func"):
            self.argument_parser.print_usage()
            quit()
        args.func(args)

    def searchAction(self, args = None):
        Log.info("searching process ...")
        pattern = args.pattern
        resource = args.resource
        inMemory = args.inmemory
    
        Log.info(pattern)
        Log.info(resource)

        if (inMemory):
            Log.info("* search-option: in-memory-search")
        else:
            Log.info("* search-option: searching in resource directly")

    def patchAction(self, args = None):
        Log.info("patching process ...")
        data = args.input
        resource = args.resource
        Log.info(data)
        Log.info(resource)

def main():
    cli = DataDudeCLI()
    cli.run()

if __name__ == "__main__":
    main()