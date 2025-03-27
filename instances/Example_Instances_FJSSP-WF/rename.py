import os
path = r'instances/Example_Instances_FJSSP-WF'
files = os.listdir(path)
for file in files:
    if file.endswith('.fjs'):
        print(file)
        new_name = ''.join(file.split('_')[1:-1])
        new_name += '.fjs'
        print(new_name)
        with open(path + '/' + file, 'r') as f:
            content = f.readlines()
            with open(f'{path}/newnames/{new_name}', 'w') as o:
                o.writelines(content)