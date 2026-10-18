import Pyro5.api

def main():
    try:
        # Locate the product proxy object via Name Server lookup
        laptop = Pyro5.api.Proxy("PYRONAME:laptop@127.0.0.1:9090")

        # Invoke remote methods
        laptop_name = laptop.get_name()
        laptop_description = laptop.get_description()
        price = laptop.get_price()

        # Display results
        print(f"Name: {laptop_name}")
        print(f"Description: {laptop_description}")
        print(f"Price: {price}")

    except Exception as e:
        print(f"Exception in client side: {e}")

if __name__ == "__main__":
    main()