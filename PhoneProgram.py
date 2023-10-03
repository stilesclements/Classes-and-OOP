import PhoneClass as pc

def main():
    Iphone=pc.Phone("Apple","iPhone 15",1200)


    Iphone.set_retail_price(1400)

    print(Iphone.get_manufact())
    print(Iphone.get_model())
    print(Iphone.get_retail_price())


main()