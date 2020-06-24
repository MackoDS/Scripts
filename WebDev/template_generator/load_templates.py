import jinja2
import os

#script for connecting jinja templates and writing into html files

# first argument is template on which you build html page, second is desired output html file name
def create_html(content_template, output_html_file_name):

    # loads templates from /templates directory
    template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath='./templates/'))
    template = template_env.get_template(content_template)
    #print(template.render())

    with open('templates/generated_html/{}'.format(output_html_file_name), 'w', encoding="utf-8") as output_file:

        output_file.write(
            template.render()
        )

    print("New file '{}' based on template '{}', created successfully".format(output_html_file_name, content_template))


# gets full path of the directory script file is contained in
dir_path = os.path.dirname(os.path.realpath(__file__))

# dir_path parent directory
parent_path = os.path.abspath(os.path.join(dir_path, os.pardir))

print(os.listdir(dir_path))


create_html('audyt-rodo_content.html', 'audyt-rodo.html')
create_html('audyty_content.html', 'audyty.html')
create_html('czytniki-e-dowodu-cyberJack-PL_content.html', 'czytniki-e-dowodu-cyberJack-PL.html')
create_html('famoc_content.html', 'famoc.html')
create_html('hackingdept_content.html', 'hackingdept.html')
create_html('index_content.html', 'index.html')
create_html('kontakt_content.php', 'kontakt.php')
create_html('log-system_content.html', 'log-system.html')
create_html('mediaid_content.html', 'mediaid.html')
create_html('o-nas_content.html', 'o-nas.html')
create_html('pentesty_content.html', 'pentesty.html')
create_html('knowbe4_content.html', 'knowbe4.html')
