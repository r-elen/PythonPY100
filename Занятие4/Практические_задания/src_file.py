#  src_file.py

def main():
    print(__name__)
    var_inside_main = "var_inside_main"


print(__name__)
var_outside_main = "var_outside_main"

if __name__ == '__main__':
    print(__name__)
    var_inside_main = "var_inside_main"
