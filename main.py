from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("my_templates"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html")

print(template.render(the="variables", go="here"))