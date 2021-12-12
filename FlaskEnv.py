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
        self.path_python = os.path.join(self.dir_path, 'Scripts', 'python.exe')
        self.activation =  os.path.join(self.dir_path, 'Scripts', 'activate_this.py')
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
            os.system(f"{command} -m pip install virtualenv flask")
            os.system(f"{command} -m virtualenv {self.dir_path}")
            self.__file_creator(self.dir_path, 'main.py', content=main_string)
            for project_dir in self.dir_names:
                self.__dirs_creator(project_dir)
        
            self.__copier()
            
        
        except FileExistsError:
            print('Directory already had files')

        except Exception as e:
            print(f'Somethig wrong. Try one more time. Error - {str(e)}')
        
        finally:
            os.system('pip freeze > requirements.txt')
            os.system('pip uninstall -r requirements.txt -y')

    # copy installed packages
    def __copier(self):
        path_target = os.path.join(self.dir_path, 'Lib', 'site-packages')
        path_source = os.path.join(os.getcwd(), 'Lib', 'site-packages')
        list_targer = os.listdir(path_target)
        list_source = os.listdir(path_source)
        for package in list_source:
            if (package not in list_targer) and (package.find("virtualenv") == -1):
                try:
                    shutil.copytree(os.path.join(path_source, package), os.path.join(path_target, package))
                except:
                    shutil.copy(os.path.join(path_source, package), os.path.join(path_target, package))
                print(f'Package {package} copied')

    # creates an empty file
    def __file_creator(self, file_path: str, file_name: str, content: str = None):
        with open(os.path.join(file_path, file_name), 'w', encoding='utf8') as f: 
            if content is None:
                pass
            else:
                f.writelines(content)

    # creates an directory
    def __dirs_creator(self, name: str, addtional_name: str = None, create_main: bool = False):
        file_path = ''
            
        if addtional_name:
            file_path = os.path.join(self.dir_path, addtional_name, name)
            os.mkdir(file_path)
        else:
            file_path = os.path.join(self.dir_path, name)
            os.mkdir(file_path)

        if create_main:
            self.__file_creator(file_path, 'main.py', content=main_string)

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
