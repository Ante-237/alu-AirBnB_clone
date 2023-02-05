***************************THE AirBnB Clone *****************************************

	01 - Creating the Console Support for line-oriented command interpreter AirBnB Clone
**The Console for the AirBnB clone**

Here at the AirBnB Clone project, you may manage and replicate 
your own bookings and listings on AirBnB. This project is intended
to provide you practice with Python and to show you how to use an
Object-Relational Mapping (ORM) system to handle data.

**GETTING STARTED.**
1. Make a local copy of this repository on your computer:
   `git clone "airbnb_clone.git" https://github.com/YOUR_USERNAME/AirBnB_clone.git`
2. Navigate to the project's root directory: `cd AirBnB clone`
3. Enter `./console.py` on your terminal to launch the console.

**Write a command interpreter as a first step to managing your AirBnB objects**

- This initial step is crucial because it will allow you to use the things 
  you create for this project in all subsequent ones. database store, API, 
  front-end in HTML/CSS,

**USING THE CONSOLE.**

The AirBnB data model may be accessed using the console.
You can utilize the following fundamental commands
1. create <class name> - creates a new instance of the specified class and saves it to the JSON file
2. show <class name> <object id> - displays the string representation of the specified object
    `show User 1`
3. all <class name> - displays all instances of the specified class, if no class name is provided, it displays all objects
    `destroy User 1`
4. destroy <class name> <object id> - deletes the specified object
    `update User 1 name "John Doe"`
5. update <class name> <object id> <attribute name> "<attribute value>" - updates the 
   specified object with the new attribute value 



**BUILT WITH**.
Python - The programming language used.
JSON - Data serialization format.

**RECOGNIZED CLASSES.**
- Basemodel : The base model class, provides common attributes and methods for all other classes
- User : Represents a user, who can create bookings and listings on the platform
- State : Represents a state, where places are located
- Amenity : Represents an amenity, that a place can offer
- Review : Represents a review, written by a user about a place
- Place : Represents a place, that can be booked on the platform
- City : Represents a city, where places are located

**Example Code for Recognized Classes.**
    `# Define the Basemodel class`
`class Basemodel:`
    `def __init__(self, id, created_at, updated_at):`
        `self.id = id`
        `self.created_at = created_at`
        `self.updated_at = updated_at`

`# Define the User class`
`class User(Basemodel):`
    `def __init__(self)` 

**AUTHORS.**
Nwalahnjie Anye <akumawahanye@gmail.com>
Shema Fred <fredshema24@gmail.com>


