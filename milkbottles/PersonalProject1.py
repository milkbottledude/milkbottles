#categorising favourite youtubers into different subclasses

class Youtuber(object):
    def __init__(self, medium, name, niche, personality):
        self.medium = medium
        self.name = name
        self.niche = niche
        self.personality = personality

    def display(self):
        print(
            f' name: {self.name} \n medium: {self.medium} \n niche: {self.niche} \n personality: {self.personality}'
        )

class Vtuber(Youtuber):
    def __init__(self, medium, name, niche, personality, colour):
        super().__init__(self, medium, name, niche, personality)
        self.colour = colour


    
idiots = Youtuber('irl', 'trentwins', 'gym', 'rowdy')
idiots.display()