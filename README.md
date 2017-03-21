# Cheli

Cheli is a simple framework for developing CLI toolkits in python. 

# Why Use Cheli?

Frequently, internal tools used by teams of Systems Engineers, Software Developers, and/or DevOps Professionals are not developed or maintained with the same rigor and attention to detail as customer facing systems. This creates organizational issues, as a diverse toolset will develop with different styles, structures, and often languages and frameworks being utilized. 

Cheli is a simple framework that forces internal tools to be standardized in structure, language, and eforces certain documentation standards for commands. Why, you might be asking, would one want to do all of the above? Please consider the following advantages of cheli:

1) *Maintainability* -- by enforcing certain structural requirements, anyone with familiarity with how cheli commands are structured can jump in, and quickly understand how a given command works.

2) *Modularity* -- modularity is baked into cheli's architecture, and enforced within commands themselves. This creates an easily extendable system that can be maintained and modified iteratively. 

3) *Explicit* -- cheli requires exactly what commands can and cannot do to be defined via the arguments.json, options.json, and command.json file contained within each commands directory. By forcing this to be defined explicitly, and automatically generating help messages based on these definitions, cheli ensures that documentation is kept up to date. It also requires the developer of a given command to be explicit from a development perspective, as they will need to be able to define the commands functions via the schemas for the aforementioned files. 


# To-do
* Add schema validation on the json files
* generally speaking improve exception handling
* improve portability
* add support for "shared" library folder
