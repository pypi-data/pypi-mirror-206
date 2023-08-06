# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiofauna']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'aiohttp-devtools',
 'aiohttp-sse>=2.1.0,<3.0.0',
 'aiohttp>=3.8.4,<4.0.0',
 'aiohttp_cors>=0.7.0,<0.8.0',
 'iso8601>=1.1.0,<2.0.0',
 'pydantic[email,dotenv]>=1.10.7,<2.0.0']

setup_kwargs = {
    'name': 'aiofauna',
    'version': '0.1.0',
    'description': 'An opinionated aiohttp based framework based on a FaunaDB backend.',
    'long_description': '---\ntitle: AioFauna\n---\n# AioFauna\n\n`pip install aiofauna`\n\n🚀 Introducing aiofauna: A powerful web framework inspired by FastAPI, focused on Developer Experience, productivity while providing an opinionated architecture around FaunaDB, also supports most async frameworks, supercharge your FaunaDB experience with modern asynchronous Python! 🔥\n\n🌟 Features:\n\n✅ FastAPI like Developer Experience with decorators, automatic Swagger UI documentation and view function signature request parameters and request body parsing.\n\n✅ Async/await coroutines: Leverage the power of async programming for enhanced performance and responsiveness, not only by serving data, but also by leveraging the fastest http client available on python ecosystem to create seamless integrations.\n\n✅ SSE (Server-Sent Events) support to deliver real time event based communication from the server to single or multiple clients, solving several use cases.\n\n✅ Pydantic-based Document Object Mapper (DOM): Define and validate your data models with ease by using pydantic Field metadata tags, offering a full typed development workflow.\n\n✅ Auto-provisioning: Automatic management of collections, indexes and unique constraints, providing the already well known relational modelling pattern.\n\n✅ Standardized CRUD operations: Regarding the complexity of Fauna Query Language functional and expressive approach, a layer of abstraction on top allows to easily perform the common create, read, update and delete operations, with a customizable query method and filtering operators.\n\n✅ Full JSON communication: Fauna custom json encoder ensures data exchange between client side application and Fauna collections through python objects abstract representations.\n\n✅ ASGI compliant: Provides a middleware to comply with the ASGI protocol, implementing the Scope, Receive and Send parts of the signature in order to provide broader compatibility with further asgi based servers such as `uvicorn`, `tornado` and `daphne`.\n\n💡 Aiofauna is one of the quickest ways to get from a barebones idea to a fully functional MVP, enhance your workflow by embracing this tool and experience a blazingly fast development cycle.\n\n🌐 Due to the dual server/client implementation of aiohttp that aiofauna is built on top of, robust and lightweight integrations with third party APIs, Cloud Services and even protocols beyond http can be possible without the burden of increasing the bundle with lots of third party libraries.\n\n📚 Check out the aiofauna library, and start building your next-gen applications today! 🚀\n\n\n#Python #FaunaDB #Async #Pydantic #aiofauna\n\n⚙️ If you are using a synchronous framework check out [Faudantic](https://github.com/obahamonde/faudantic) for a similar experience with FaunaDB and Pydantic.\n\n📚 [Documentation](https://aiofauna.smartpro.solutions)\n\n📦 [PyPi](https://pypi.org/project/aiofauna/)\n\n📦 [GitHub](https://github.com/obahamonde/aiofauna)\n\n📦 [Demo](https://aiofaunastreams-fwuw7gz7oq-uc.a.run.app/) (Stream data in real-time to your clients)\n',
    'author': 'Oscar Bahamonde',
    'author_email': 'oscar.bahamonde.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/obahamonde/aiofauna',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
