
import sys
import os

parent_folder = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(parent_folder, '..')


sys.path.insert(0, project_root)

from coffee import Coffee   
from customer import Customer   
from order import Order         