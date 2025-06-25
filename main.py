# DO NOT MODIFY THE COUCH CLASS
class Couch:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


##########################################
#       Add your new classes here!       #
# (Make sure not to accidentally indent) #
##########################################
class SleeperSofa(Couch):
    def __init__(self, length, width):
        super().__init__(length, width)
        self.sheets = None
        self.folded_out = False

#def convert(self), folded_out invert, width double if true
    def convert(self):     
        if not self.folded_out:
            self.folded_out = True
            self.width *= 2
        elif self.sheets is None:
            self.folded_out = False
            self.width //= 2
       
    def put_on_sheets(self, sheets):
        if self.folded_out and self.sheets is None:
            self.sheets = sheets

    def remove_sheets(self):
        self.sheets = None
#Create a Sheets class with an optional attribute material with default "cotton"
class Sheets:
    def __init__(self,material="cotton"):
        self.material = material


#Method put_on_sheets
########## WAVE 1 ##########
# Checking the behavior for creating an instance of SleeperSofa
assert issubclass(SleeperSofa, Couch), "SleeperSofa must be a subclass of Couch"
my_sofa = SleeperSofa(84, 40)
assert my_sofa.length == 84
assert my_sofa.width == 40
assert my_sofa.sheets is None
assert my_sofa.folded_out == False
assert my_sofa.area() == 3360
print("Wave 1 passed!")


########## WAVE 2 ##########
# Check behavior for folding sofa out
my_sofa.convert()
assert my_sofa.folded_out == True
assert my_sofa.length == 84
assert my_sofa.width == 80

# Check behavior for folding sofa back in
my_sofa.convert()
assert my_sofa.folded_out == False
assert my_sofa.length == 84
assert my_sofa.width == 40
print("Wave 2 passed!")


########## WAVE 3 ##########
# Check behavior for creating Sheets
silk_sheets = Sheets("silk")
assert silk_sheets.material == "silk"

# Check behavior for default Sheets material
cotton_sheets = Sheets()
assert cotton_sheets.material == "cotton"

# Test putting on sheets
my_sofa.convert()
my_sofa.put_on_sheets(silk_sheets)
assert my_sofa.sheets == silk_sheets

# Test that new sheets are NOT put on if there are other sheets already on the sofa
my_sofa.put_on_sheets(cotton_sheets)
assert my_sofa.sheets == silk_sheets

# Test removing sheets
my_sofa.remove_sheets()
assert my_sofa.sheets is None

# Test that sheets are NOT put on if the sofa is not folded out
my_sofa.convert()
my_sofa.put_on_sheets(silk_sheets)
assert my_sofa.sheets is None
print("Wave 3 passed!")


########## WAVE 4 ##########
# Fold out sofa and put on sheets to prepare for next test
my_sofa.convert()
my_sofa.put_on_sheets(cotton_sheets)

# Test that sofa does NOT convert if sheets are still on
my_sofa.convert()
assert my_sofa.folded_out == True
assert my_sofa.width == 80
assert my_sofa.sheets == cotton_sheets
print("Wave 4 passed!")

print("All tests passed!")
print("If time remains, discuss alternate design decisions you could have made, or other ways you may think to add more functionality to your code.")