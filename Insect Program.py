import InsectClass as I

def main():
    housefly=I.Insect(2,4,'mosquito')
    mosquito=I.Insect(2,4,'housefly')
    housefly.fly()
    mosquito.fly()
    print("The ", housefly.get_name()," flew ",housefly.get_flight_length()," miles and the ", mosquito.get_name(), " flew ",mosquito.get_flight_length()," miles.",sep="")

main()