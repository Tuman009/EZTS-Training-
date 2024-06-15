class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
# Creating instances
s1 = Singleton()
s2 = Singleton()

# Checking if both instances are the same
print(s1 is s2)  # Output: True
