import os

file_names = []

# walk through working and sub directories and add html and php files names to list
for root, dirs, files in os.walk('./'):
    for name in files:

        if name.endswith('.html') or name.endswith('.php'):
            file_names.append(name)
            '''
            name_content = name[:-5] + '_content.html'
            f = open('text.txt', 'a')
            text = 'create_html(' + "'" + name_content + "'" + ', ' + "'" + name + "'" +  ')\n'
            f.write(text)
            f.close()
            '''
            
#print([n[-4:] for n in file_names])

# list comprehension to change new files names
file_names = [n[:-5] + '_content.html' if n[-13:] != '_content.html' and n[-5:] == '.html' else n[:-4] + '_content.php' if n[-12:] != '_content.php' and n[-4:] == '.php' else n for n in file_names]

# change directory to templates/
os.chdir('templates')

# create new file if doesnt already exist
for f_name in file_names:
    if os.path.exists(f_name):
        pass
    else:
        new_file = open(f_name, 'w', encoding="utf-8")
        new_file.write("{% extends 'base.html' %}\n\n")
        new_file.write("{% block meta_title_name %}\n\n{% endblock %}\n\n")
        new_file.write("{% block content %}\n\n{% endblock %}\n")
        new_file.close()
