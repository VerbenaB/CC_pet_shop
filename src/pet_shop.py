# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return(shop["name"])


def get_total_cash(shop):
    return(shop["admin"]["total_cash"])


def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash


def get_pets_sold(shop):
    return(shop["admin"]["pets_sold"])


def increase_pets_sold(shop, pets_sold):
    shop["admin"]["pets_sold"] = 2


def get_stock_count(shop):
    return len(shop["pets"])


def get_pets_by_breed(shop, breed):
    breeds = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            breeds.append(breed)
    return (breeds) 
    
        
def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet
        else:
            None
    
def remove_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
         shop["pets"].remove(pet)   


def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)
    get_stock_count(shop)


def get_customer_cash(customer):
    return(customer["cash"])


def remove_customer_cash(customer, cash_removed):
    customer["cash"] -= cash_removed 


def get_customer_pet_count(customer):
    return(len(customer["pets"]))


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)



