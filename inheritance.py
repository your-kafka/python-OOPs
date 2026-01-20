#Simple inheritance 

class animal : #Base class
    def __init__(self,name):
     self.name = name

    def speak(self):
       print(f'{self.name} makes a sound.')
    

# anim = animal('lion')
# anim.speak()


#derived class 
class Dog(animal):     #Dog class inherit the animal class here 
   
   def __init__(self,behaviour,name):
      super().__init__(name)                      #use of super keyword to inherit all the attributes from parent class 
      self.behaviour = behaviour
   def speak1(self):
     super().speak()
     print(f'{self.name} barks and he is very {self.behaviour}')

dog = Dog('friendly','lion')
dog.speak1()