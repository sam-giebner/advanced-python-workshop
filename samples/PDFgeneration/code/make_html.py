# load dynamic content into html template

from jinja2 import Environment, FileSystemLoader

def load_template(in_file="../../data/weasyprint_example/map_test.html"):
    env = Environment(loader=FileSystemLoader('.'))
    return env.get_template(in_file)
    
def export_html(template, content):
    
    return template.render(content)
    

def main(path_to_template, content):
    """Run script
    """
    loaded_template = load_template(path_to_template)
    print(export_html(template=loaded_template, content=content))
    

    
# Runner
if __name__ == "__main__":

    html_template = "../../data/weasyprint_example/map_test.html"
    content = {
            'title': "Test Report",
            'map_title': "Test Map",
            'map': "../../output/umd_buildings_test.png",
        }
    main(html_template, content)