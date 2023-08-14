import sys, os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flox import Flox
import webbrowser
import random

class randomNum(Flox):
    def query(self, query):
        results = []
        if query == 'number':
            results.append({
                'title': str(random.randint(0, 10000)),
                'subtitle': 'Random Number',
                'arg': str(random.randint(0, 10000)),
                'icon': 'icon.png'
            })
        else:
            results.append({
                'title': 'Random Number',
                'subtitle': 'Type "number" and press enter',
                'arg': 'number',
                'icon': 'app.png'
            })

if __name__ == "__main__":
    randomNum()

