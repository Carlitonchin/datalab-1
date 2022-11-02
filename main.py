from jinja2 import Environment, PackageLoader, select_autoescape
from api import get_cat_facts

env = Environment(
    loader=PackageLoader("my_templates"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html")

data = get_cat_facts()

print(template.render({"data":data}))