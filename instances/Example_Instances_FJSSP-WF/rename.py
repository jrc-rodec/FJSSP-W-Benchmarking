import os
path = r'instances/Example_Instances_FJSSP-WF'
files = os.listdir(path)
for file in files:
    if file.startswith('Behnke') and file.endswith('.fjs'):
        print(file)
        new_name = file.replace('Geiger', '')
        print(new_name)
        with open(f'{path}/{file}', 'r') as f:
            content = f.readlines()
            with open(f'{path}/newnames/{new_name}', 'w') as o:
                o.writelines(content)