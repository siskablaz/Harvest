############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        

def make_melon_types():
    """Returns a list of current melon types."""
    
    all_melon_types = []

    Muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    Muskmelon.add_pairing('mint')
    all_melon_types.append(Muskmelon)

    Casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    Casaba.add_pairing("strawberries")
    Casaba.add_pairing("mint")
    all_melon_types.append(Casaba)
    
    Crenshaw = MelonType("cren", 1996, "green", True, False, "Crenshaw")
    Crenshaw.add_pairing("prosciutto")
    all_melon_types.append(Crenshaw)
    
    yellowWatermelon = MelonType("yw", 2013, "yellow", True, True, "Yellow Watermelon")
    yellowWatermelon.add_pairing('ice Cream')
    all_melon_types.append(yellowWatermelon)

    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"""{melon.name} pairs with""")
        for pair in melon.pairings:
            print(f"- {pair}")
        
    
print(print_pairing_info(make_melon_types()))

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    
    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict

print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    def __init__(self,type, shape_rating, color_rating, harvest_field, harvested_by):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating>5 and self.harvest_field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
   
    melons_list = []

    melons_by_id = make_melon_type_lookup(make_melon_types())
    
    Melon1 = Melon(melons_by_id['yw'],8,7,2,"Sheila")
    melons_list.append(Melon1)

    Melon2 = Melon(melons_by_id['yw'],3,4,2,"Sheila")
    melons_list.append(Melon2)

    Melon3 = Melon(melons_by_id['yw'],9,8,3,"Sheila")
    melons_list.append(Melon3)
    
    Melon4 = Melon(melons_by_id['cas'],10,6,35,"Sheila")
    melons_list.append(Melon4)

    Melon5 = Melon(melons_by_id['cren'],8,9,35,"Michael")
    melons_list.append(Melon5)

    Melon6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melons_list.append(Melon6)

    Melon7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melons_list.append(Melon7)

    Melon8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melons_list.append(Melon8)

    Melon9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")
    melons_list.append(Melon9)

    return melons_list
 

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        if melon.is_sellable:
            sellable = "(CAN BE SOLD)"
        else:
            sellable = "(NOT SELLABLE)"
        print(f"Harvested by {melon.harvested_by} from Field {melon.harvest_field} {sellable}")


get_sellability_report(make_melons(make_melon_type_lookup(make_melon_types())))


def melons_from_file(filepath):
    melons_data = open(filepath)
    file_melons_list = []
    file_melons_by_id = make_melon_type_lookup(make_melon_types())

    for line in melons_data:
        line_data = line.rstrip().split()
        melon_object = Melon(shape_rating=line_data[1], 
                             color_rating=line_data[3], 
                             type=file_melons_by_id[line_data[5]], 
                             harvest_field=line_data[11], 
                             harvested_by=line_data[8])
        file_melons_list.append(melon_object)

    return file_melons_list
    
print(melons_from_file('harvest_log.txt'))
                        
#  type, shape_rating, color_rating, harvest_field, harvested_by
# [1 = shape, 3 = color, 5 = Type, 8 = harvested_by, 11 = harvest_field]
