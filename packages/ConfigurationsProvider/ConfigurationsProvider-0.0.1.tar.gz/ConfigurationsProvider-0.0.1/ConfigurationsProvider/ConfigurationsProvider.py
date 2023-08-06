import logging
import os


class ConfigurationsProvider:

    def __init__(self, base_path=os.getcwd()):
        if base_path.endswith("/"):
            self.base_path = base_path
        else:
            self.base_path = base_path + '/'

    def get_property(self, file_name):
        try:
            with open(self.base_path + file_name, 'r') as infile:
                return infile.readline().strip('\n')
        except OSError as error:
            logging.error(error)
