
class Cookie:
    def __init__(self, color):
        self.color = color 
        
    def get_color(self):
        return self.color 
    
    def set_color(self, color):
        self.color = color 
        return self.color
        
cookie_1 = Cookie("green")
cookie_2 = Cookie("red")

print(cookie_2.set_color("blue"))