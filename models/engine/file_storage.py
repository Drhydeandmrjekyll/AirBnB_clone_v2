from models.user import User

class FileStorage:
    """ Represent an abstracted storage engine.
	
    Atrributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
	
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Return a dictionary of instantiated objects in  __objects.

        If cls specified, retunrs dictionary of objects of that type.
        Otherwise, return the __objects dictionary.
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] == cls:
            return cls_dict
        return self.__objects
    def new(self, obj):
        """Set in __objects obj with key <obj class name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj
    
    def save(self):
        """Serialize __objects to JSON file __file_path."""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.key()}
        with open(self.__file_path, "w", encoding= "utf-8") as f:
            json.dump(odict, f)
   	   
    def reload(self):
        """Deserialize JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """call reload() method for deserializing JSON file objects"""
        self.reload()
