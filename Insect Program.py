import InsectClass as I

def main():
    housefly=I.Insect(2,4,'mosquito')
    mosquito=I.Insect(2,4,'housefly')
    housefly.fly()
    mosquito.fly()
    print("The house fly flew ",housefly.get_flight_length()," miles and the mosquito flew ",mosquito.get_flight_length()," miles.",sep="")

main()