import sys, os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import random

class randomNum(FlowLauncher):
    def query(self, query):
        results = []
        number = str(random.randint(0, 10000))
        if query == 'number':
            results.append({
                'title': number,
                'subtitle': 'Click to copy',
                'icon': 'app.png'
            })
        else:
            results.append({
                'title': 'Random Number',
                'subtitle': 'Type "number" and press enter',
                'arg': 'number',
                'icon': 'app.png'
            })
        return results

if __name__ == "__main__":
    randomNum()

