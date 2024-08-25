from pathlib import Path

CONST_SAVE_BASE = "/home/sonata/syslink/TheFarmerWasReplacedSaves/"
CONST_DEFAULT_FILE = "Save0"
CONST_BUILTIN = "__builtins__.py"
CONST_MAIN = "main.py"
CONST_CODE_GLOB = "**/*.py"

pathlist = Path().resolve().glob(CONST_CODE_GLOB)

target_file_path = CONST_SAVE_BASE + CONST_DEFAULT_FILE + "/" + CONST_MAIN
target_file = open(target_file_path, 'w')


def write_file_to_main(read_path):
    with open(read_path, 'r') as reader:
        target_file.write("# " + read_path + "\n")
        target_file.write(reader.read())
        target_file.write("\n\n\n")


main_path = None
for path in pathlist:
    path_in_str = str(path)
    if path_in_str.endswith(CONST_BUILTIN) or path_in_str.endswith("_imports.py") or path_in_str.endswith("__init__.py"):
        continue
    if path_in_str.endswith(CONST_MAIN):
        main_path = path_in_str
        continue
    write_file_to_main(path_in_str)

write_file_to_main(main_path)
target_file.close()
