from markdown2 import markdown
from json import load
from jinja2 import Environment, FileSystemLoader

# Load the template from the current directory
template_env = Environment(loader=FileSystemLoader(searchpath="./"))
template = template_env.get_template("template.html")

with open('article.md','r') as markdown_file:
    data = markdown(markdown_file.read(), extras=['fenced-code-blocks','code-friendly','metadata'])
    
with open('index.html','w') as output_file:
    output_file.write(
        template.render(
            title=data.metadata["title"],
            subtitle=data.metadata["subtitle"],        
            content=data,
            primary=data.metadata["primary"],
            secondary=data.metadata["secondary"],
            accent=data.metadata["accent"],
            background=data.metadata["background"],
            foreground=data.metadata["foreground"]
        )
    )