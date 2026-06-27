When desiging an website we can follow one of these approaches
1. Design the web layer and work down:
    Evolve the Web interface first with fake calls to the lower layers until you know what you'll expect of them
2. Design the data layer and work up:
    If we have database ready and want to build an application around the data, then build the data layer codes and tests first, then the service layer and write the Web layer last
3. Design the servier layer and workout in both directions
    If we are following Domain Driven design, then start with Service layer defining our core entities and data models


For More Architectural understanding:
1. Clean Architectures in Python  by Leonardo Giordani
2. Architecture Patterns with Python by Harry J.W. Percival and Bob Gregory
3. Micrservice APIs by Jose Haro Peralta

### RESTful API Design Components:
* Resources - The data elememts you application manages
* IDs - Unique resource identifiers
* URLs - Strcutrued resource and ID strings
* Verbs or Actions - Terms that accompany URLs for different purposes:
    - GET - Retrieve a resource
    - POST - Create a new resource
    - PUT - Completely replace a resource
    - PATCH - Partially replace a resource
    - DELETE - Delete a resource

General way of creating path parameters with verbs, resourses and ids  
**verb /resource**  - Aplly verb to all resources of type resource  
**verb /resource/id**  - Apply verb to resource with ID id.

Parameters can be epxressed as
- Path parameters (comes after / at the end)
- Query paramaters (var=val type after ?)
- HTTP Body Parameters (for large requests, as URLs have size limits)
- HTTP Header Parameters

### File and Directory site layout:




