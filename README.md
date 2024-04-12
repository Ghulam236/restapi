
## Q-- What is api?

API, which stands for Application Programming Interface, is a set of rules and protocols that allow different software applications to communicate with each other. APIs define the methods and data formats that applications can use to request and exchange information. They serve as intermediaries that enable different software systems to work together, share data, and perform tasks.

## `REST API`
A REST API, or Representational State Transfer Application Programming Interface, is a specific type of API that follows the principles of the REST architectural style. REST is an architectural style for designing networked applications, and RESTful APIs adhere to these principles. Some key characteristics of a REST API include:


API, which stands for Application Programming Interface, is a set of rules and protocols that allow different software applications to communicate with each other. APIs define the methods and data formats that applications can use to request and exchange information. They serve as intermediaries that enable different software systems to work together, share data, and perform tasks.

A REST API, or Representational State Transfer Application Programming Interface, is a specific type of API that follows the principles of the REST architectural style. REST is an architectural style for designing networked applications, and RESTful APIs adhere to these principles. Some key characteristics of a REST API include:

`Stateless`:

Each request from a client to a server must contain all the information needed to understand and process the request. The server should not store information about the client's state between requests.

`Resource-Based:`

 REST APIs are resource-based, where resources are identified by URIs (Uniform Resource Identifiers). These resources can represent objects, data, or entities.

`CRUD Operations:`

 RESTful APIs typically use HTTP methods (GET, POST, PUT, DELETE) to perform CRUD (Create, Read, Update, Delete) operations on resources. For example, a GET request retrieves resource data, while a POST request creates a new resource.

`Representation:`

 Resources can have multiple representations, such as JSON or XML. Clients can specify the representation they want through request headers.

Stateless Communication: Communication between clients and servers in a RESTful system is stateless. Each request/response is independent, and no client state is stored on the server.

Uniform Interface: A REST API should have a uniform and consistent interface. It means that you use the same HTTP methods and standards for all resources.

Layered System: A RESTful architecture allows for the introduction of intermediary servers and load balancers without affecting the client's interaction with the system.

