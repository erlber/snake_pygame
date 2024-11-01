class Kopp:
    def __init__(self, name=str, color=str, handle=bool):
        self.name = name
        self.height = 20
        self.width = 10
        self.veskeInnhold = 0
        self.maxVolum = 300
        self.color = color
        self.handle = handle

    def fill(self, ml):
        self.veskeInnhold += ml

        if(self.veskeInnhold >= self.maxVolum):
            print("oh no!!! det rant over!")
            self.veskeInnhold = self.maxVolum
        
minKopp = Kopp("erlends kopp", "black", False)
dinKopp = Kopp("Iris sin kopp", "yellow", True)
odinsKopp = Kopp("odins kjempe kule kopp", "rainbow", True)

minKopp.fill(350)

print(f"{minKopp.name} har {minKopp.veskeInnhold} ml i seg")
print(f"{odinsKopp.name} har {odinsKopp.veskeInnhold} ml i seg")

