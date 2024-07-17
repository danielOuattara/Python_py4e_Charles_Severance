class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()

an.party()
an.party() 
an.party()

print('\n',dir(PartyAnimal), '\n')
print("Type", type(an), '\n')
print("Dir ", dir(an), '\n')
