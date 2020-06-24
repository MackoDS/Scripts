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


create_html('site_content.html', 'site.html')
