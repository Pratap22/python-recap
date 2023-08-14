# Absolute import vs Relative import

from package_1 import file_1_package_1

def run():
    print("I am root")
    file_1_package_1.run_file_1_packge_1()

run()


#  __init__.py