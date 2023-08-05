# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsonformer']

package_data = \
{'': ['*']}

install_requires = \
['termcolor>=2.3.0,<3.0.0']

setup_kwargs = {
    'name': 'jsonformer',
    'version': '0.5.0',
    'description': '',
    'long_description': '# Jsonformer: A Bulletproof Way to Generate Structured JSON from Language Models.\n\n### Problem: Getting models to output structed JSON is hard\n\n### Solution: Only generate the content tokens and fill in the fixed tokens\n\n![cover](img/cover4.png)\n\nGenerating structured JSON from language models is a challenging task. The\ngenerated JSON must be syntactically correct, and it must conform to a schema\nthat specifies the structure of the JSON.\n\nCurrent approaches to this problem are brittle and error-prone. They rely on prompt engineering, fine-tuning, and post-processing, but they still fail to generate syntactically correct JSON in many cases.\n\nJsonformer is a new approach to this problem. In structured data, many tokens are fixed and predictable. Jsonformer is a wrapper around HuggingFace models that fills in the fixed tokens during the generation process, and only delegates the generation of content tokens to the language model. This makes it more efficient and bulletproof than existing approaches.\n\nThis currently supports a subset of JSON Schema. Below is a list of the supported schema types:\n\n- number\n- boolean\n- string\n- array\n- object\n\n## Example\n\n```python\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nmodel = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-12b")\ntokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-12b")\n\nschema = {\n    "type": "object",\n    "properties": {\n        "name": {"type": "string"},\n        "age": {"type": "number"},\n        "is_student": {"type": "boolean"},\n        "courses": {\n            "type": "array",\n            "items": {"type": "string"}\n        }\n    }\n}\n\nprompt = "Generate a person\'s information based on the following schema:"\njsonformer = Jsonformer(model, tokenizer, json_schema, prompt)\ngenerated_data = jsonformer()\n\nprint(generated_data)\n```\n\n## Features\n\n- Bulletproof JSON generation: Jsonformer ensures that the generated JSON is always syntactically correct and conforms to the specified schema.\n- Efficiency: By generating only the content tokens and filling in the fixed tokens, Jsonformer is more efficient than generating a full JSON string and parsing it.\n- Flexible and extendable: Jsonformer is built on top of the HuggingFace transformers library, making it compatible with any model that supports the HuggingFace interface.\n\n## Installation\n\n```bash\npip install jsonformer\n```\n\n## License\n\nJsonformer is released under the MIT License. You are free to use, modify, and distribute this software for any purpose, commercial or non-commercial, as long as the original copyright and license notice are included.\n',
    'author': '1rgs',
    'author_email': 'rgsduke@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
