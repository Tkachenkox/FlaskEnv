import os
import shutil

from helpers_strings import *
class FlaskEnv:

    def __init__(self, dir_path: str = None):
        self.os_name = os.name
        self.dir_names = ['bll', 'dal', 'app']
        self.app_dirs = ['exceptions', 'extensions', 'middleware', 'validation', 'controller']
        if dir_path:
            self.dir_path = dir_path
        else:
            self.dir_path = os.path.join(os.getcwd(), "TestProj")
        self.commad_nt = 'py'
        self.commad_other = 'python3'

    def run(self):
        self.creator()


    def creator(self):
        command = ''
        if self.os_name == "nt":
            command = self.commad_nt
        else:
            command = self.commad_other
        try:
            os.system(f"mkdir {self.dir_path}")
            os.system(f"{command} -m pip install virtualenv")
            os.system(f"{command} -m virtualenv {self.dir_path}")
            self.__main_copier()
            for project_dir in self.dir_names:
                self.__dirs_creator(project_dir)
            
        
        except FileExistsError:
            print('Directory already had files')

        except Exception as e:
            print(f'Somethig wrong. Try one more time. Error - {str(e)}')

    
    def __main_copier(self):
        base_path = os.path.join(os.getcwd(), 'samples')
        shutil.copy(os.path.join(base_path, 'main.py'), self.dir_path)
        shutil.copy(os.path.join(base_path, 'config.py'), self.dir_path)
        shutil.copy(os.path.join(base_path, 'requirements.txt'), self.dir_path)
        shutil.copy(os.path.join(os.getcwd(), ".gitignore"), self.dir_path)
        print('Created root files')

    # creates an empty file
    def __file_creator(self, file_path: str, file_name: str, content: str = None):
        path_to_file = os.path.join(file_path, file_name)
        with open(path_to_file, 'w', encoding='utf8') as f: 
            if content is None:
                pass
            else:
                f.writelines(content)
        print(path_to_file, ' ctreated')

    # creates an directory
    def __dirs_creator(self, name: str, addtional_name: str = None):
        file_path = ''
            
        if addtional_name:
            file_path = os.path.join(self.dir_path, addtional_name, name)
            os.mkdir(file_path)
        else:
            file_path = os.path.join(self.dir_path, name)
            os.mkdir(file_path)

        self.__file_creator(file_path, '__init__.py')

        if name == "dal":
            self.__dirs_creator("models", addtional_name=name)
        if name == "app":
            self.__file_creator(file_path, 'app.py', content=app_string)
            self.__file_creator(file_path, 'BlueprintGroup.py', content=blieprint_group_string)
            for app_dir in self.app_dirs:
                self.__dirs_creator(app_dir, addtional_name=name)
        if name == 'extensions':
            self.__file_creator(file_path, 'extension.py', content=extensions_string)
