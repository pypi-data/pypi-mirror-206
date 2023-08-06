# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gpt_json', 'gpt_json.tests']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=2.2.1,<3.0.0',
 'openai>=0.27.6,<0.28.0',
 'pydantic>=1.10.7,<2.0.0',
 'tiktoken>=0.3.3,<0.4.0']

setup_kwargs = {
    'name': 'gpt-json',
    'version': '0.1.0',
    'description': '',
    'long_description': '# gpt-json\n\nJSON is a beautiful format. It\'s both human readable and machine readable, which makes it a great format for structured output of LLMs (after all - LLMs are somewhere in the middle). `gpt-json` is a wrapper around GPT that allows for declarative definition of expected output format when you\'re trying to parse results into a downstream pipeline.\n\nSpecifically it:\n- Relies on Pydantic schema definitions and type validations\n- Allows for defining both dictionaries and lists\n- Includes some lightweight manipulation of the output to remove superfluous context and fix broken json\n- Includes retry logic for the most common API failures\n- Adds typehinting support for both the API and the output schema\n\n## Getting Started\n\n```bash\npip install gpt-json\n```\n\nHere\'s how to use it to generate a schema for simple tasks:\n\n```python\nimport asyncio\n\nfrom gpt_json import GPTJSON, GPTMessage, GPTMessageRole\nfrom pydantic import BaseModel\n\nclass SentimentSchema(BaseModel):\n    sentiment: str\n\nSYSTEM_PROMPT = """\nAnalyze the sentiment of the given text.\n\nRespond with the following JSON schema:\n\n{json_schema}\n"""\n\nasync def runner():\n    gpt_json = GPTJSON[SentimentSchema](API_KEY)\n    response = await gpt_json.run(\n        messages=[\n            GPTMessage(\n                role=GPTMessageRole.SYSTEM,\n                content=SYSTEM_PROMPT,\n            ),\n            GPTMessage(\n                role=GPTMessageRole.USER,\n                content="Text: I love this product. It\'s the best thing ever!",\n            )\n        ]\n    )\n    print(response)\n    print(f"Detected sentiment: {response.sentiment}")\n\nasyncio.run(runner())\n```\n\n```bash\nsentiment=\'positive\'\nDetected sentiment: positive\n```\n\nThe `json_schema` is a special keyword that will be replaced with the schema definition at runtime. You should always include this in your payload to ensure the model knows how to format results. However, you can play around with _where_ to include this schema definition; in the system prompt, in the user prompt, at the beginning, or at the end.\n\nYou can either typehint the model to return a BaseSchema back, or to provide a list of Multiple BaseSchema. Both of these work:\n\n```python\ngpt_json_single = GPTJSON[SentimentSchema](API_KEY)\ngpt_json_single = GPTJSON[list[SentimentSchema]](API_KEY)\n```\n\nIf you want to get more specific about how you expect the model to populate a field, add hints about the value through the "description" field. This helps the model understand what you\'re looking for, and will help it generate better results.\n\n```python\nfrom pydantic import BaseModel, Field\n\nclass SentimentSchema(BaseModel):\n    sentiment: int = Field(description="Either -1, 0, or 1.")\n```\n\n```\nsentiment=1\nDetected sentiment: 1\n```\n\n## Comparison to Other Libraries\n\nA non-exhaustive list of other libraries that address the same problem. None of them were fully compatible with my deployment (hence this library), but check them out:\n\n[jsonformer](https://github.com/1rgs/jsonformer) - Works with any Huggingface model, whereas `gpt-json` is specifically tailored towards the GPT-X family.\n',
    'author': 'Pierce Freeman',
    'author_email': 'pierce@freeman.vc',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
