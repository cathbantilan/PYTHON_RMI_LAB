import Pyro5.api
from product import Product

def main():
    # Instantiate product objects (similar to Java's p1, p2, p3, p4)
    p1 = Product("Laptop", "Lenovo laptop", 800000.0)
    p2 = Product("Mobile", "MI 9 mobile", 24000.0)
    p3 = Product("Bag", "Branded bag", 800.0)
    p4 = Product("Charger", "MI Charger", 230.0)

    # Initialize Pyro Daemon
    daemon = Pyro5.api.Daemon(host="127.0.0.1")

    # Locate the Pyro Name Server (equivalent to LocateRegistry.getRegistry)
    ns = Pyro5.api.locate_ns(host="127.0.0.1", port=9090)

    # Register objects with daemon and bind to the Name Server
    uri1 = daemon.register(p1)
    uri2 = daemon.register(p2)
    uri3 = daemon.register(p3)
    uri4 = daemon.register(p4)

    ns.register("laptop", uri1)
    ns.register("ram", uri2)
    ns.register("bag", uri3)
    ns.register("charger", uri4)

    print("Server is booting and products are registered in Name Server...")
    # Start listening for remote calls
    daemon.requestLoop()

if __name__ == "__main__":
    main()