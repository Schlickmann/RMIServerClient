import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        print('Someone called get_fortune method')
        return nameServer + ": Hello, {0}. Here is your fortune message:\n Tomorrow's lucky number is 12345678.".format(name)

daemon = Pyro4.Daemon()                # make a Pyro daemon
try:
    ns = Pyro4.locateNS()                  # find the name server
except Pyro4.errors.NamingError:
    print('You need to run pyro4-ns before you start a server.')
    exit()

nameServer = raw_input('Insert server name: ')

uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
ns.register('greeting-' + nameServer, uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls