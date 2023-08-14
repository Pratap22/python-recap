# from package_2 import file_1_package_2
# from package_1.sub_package_1 import file_1_package_1_sub_package_1

# . -> current package
#  .. -> parent package

# from ..package_2 import file_1_package_2
from .sub_package_1 import file_1_package_1_sub_package_1

def run_file_1_packge_1():
    print("I am file_1_package_1")
    # file_1_package_2.run_file_1_packge_2()
    file_1_package_1_sub_package_1.run_file_1_package_1_sub_package_1()

