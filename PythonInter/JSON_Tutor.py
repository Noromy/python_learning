import json
person = {"name": "Zara", "age": 7, "city": "Badung", "hasChildren": False, "titles": ["Pedofil", "engineer", "editor"]}

personJSON = json.dumps(person, indent=4)  #separators=(":", " = "), sort_keys=True) # Making easier to read dan structured then it can be read by JavaScript or Node.js                                                                   # Sortkey is to sort the key in alphabetical order
print(personJSON) #only in terminal


# with open('person.json', 'w') as files: #making file json
     # json.dump(person, files, indent=4,)
with open('person.json', 'r') as files: #reading file json
    person = json.load(files) #convert JSON to dictionary
    print(person)
person = json.loads(personJSON) #convert JSON to dictionary
print(person) 

#Encode custom object

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User("imron", 21)


def encode_user(object):
    if isinstance(object, User):
        return {'name': object.name, 'age': object.age, object.__class__.__name__: True}
    else:
        raise TypeError('Object of type User in not JSON serializable')

# UserJSON = json.dumps(user, default=encode_user)

# Second method by subclassing JSONEncoder

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default (self, object):
        if isinstance(object, User):
             return {'name': object.name, 'age': object.age, object.__class__.__name__: True}
        return JSONEncoder.default(self, object)

 
UserJSON = json.dumps(user, cls=UserEncoder)
print(UserJSON)

# Third method by subclassing JSONEncoder and using encode method

UserJSON = UserEncoder().encode(user) 
print(UserJSON)

# Decoding custom object back to python object (User Object)
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    return dict



# Decoding custom object back to python object
user = json.loads(UserJSON, object_hook=decode_user) #become dictionary but its still not a user object you have to decode it

print(type(user)) 
print(user.name) 