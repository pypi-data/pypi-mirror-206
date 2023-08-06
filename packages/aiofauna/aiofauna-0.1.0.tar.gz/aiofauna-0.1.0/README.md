---
title: AioFauna
---
# AioFauna

`pip install aiofauna`

🚀 Introducing aiofauna: A powerful web framework inspired by FastAPI, focused on Developer Experience, productivity while providing an opinionated architecture around FaunaDB, also supports most async frameworks, supercharge your FaunaDB experience with modern asynchronous Python! 🔥

🌟 Features:

✅ FastAPI like Developer Experience with decorators, automatic Swagger UI documentation and view function signature request parameters and request body parsing.

✅ Async/await coroutines: Leverage the power of async programming for enhanced performance and responsiveness, not only by serving data, but also by leveraging the fastest http client available on python ecosystem to create seamless integrations.

✅ SSE (Server-Sent Events) support to deliver real time event based communication from the server to single or multiple clients, solving several use cases.

✅ Pydantic-based Document Object Mapper (DOM): Define and validate your data models with ease by using pydantic Field metadata tags, offering a full typed development workflow.

✅ Auto-provisioning: Automatic management of collections, indexes and unique constraints, providing the already well known relational modelling pattern.

✅ Standardized CRUD operations: Regarding the complexity of Fauna Query Language functional and expressive approach, a layer of abstraction on top allows to easily perform the common create, read, update and delete operations, with a customizable query method and filtering operators.

✅ Full JSON communication: Fauna custom json encoder ensures data exchange between client side application and Fauna collections through python objects abstract representations.

✅ ASGI compliant: Provides a middleware to comply with the ASGI protocol, implementing the Scope, Receive and Send parts of the signature in order to provide broader compatibility with further asgi based servers such as `uvicorn`, `tornado` and `daphne`.

💡 Aiofauna is one of the quickest ways to get from a barebones idea to a fully functional MVP, enhance your workflow by embracing this tool and experience a blazingly fast development cycle.

🌐 Due to the dual server/client implementation of aiohttp that aiofauna is built on top of, robust and lightweight integrations with third party APIs, Cloud Services and even protocols beyond http can be possible without the burden of increasing the bundle with lots of third party libraries.

📚 Check out the aiofauna library, and start building your next-gen applications today! 🚀


#Python #FaunaDB #Async #Pydantic #aiofauna

⚙️ If you are using a synchronous framework check out [Faudantic](https://github.com/obahamonde/faudantic) for a similar experience with FaunaDB and Pydantic.

📚 [Documentation](https://aiofauna.smartpro.solutions)

📦 [PyPi](https://pypi.org/project/aiofauna/)

📦 [GitHub](https://github.com/obahamonde/aiofauna)

📦 [Demo](https://aiofaunastreams-fwuw7gz7oq-uc.a.run.app/) (Stream data in real-time to your clients)
