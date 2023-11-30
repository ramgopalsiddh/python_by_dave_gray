class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along ...')
    
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()



class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')

class Golfcart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-123456')
tata = Truck('Tata', 'prima')
golfwagon = Golfcart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()

tata.get_make_model()
tata.moves()

golfwagon.get_make_model()
golfwagon.moves()


##################################################################################
print('\n\n')


## polymorphism method

for v in (my_car, your_car, cessna, tata, golfwagon):
    v.get_make_model()
    v.moves()
