import sys
#python -m PyInstaller --onefile VerificarEncode.py
def is_utf8_without_bom(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        try:
            content.decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False

input_file = sys.argv[1]
result = is_utf8_without_bom(input_file);
print(result);