
import pymongo
import pickle
from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

# FLASK-SOVELLUKSEN MÄÄRITTELY

app = Flask(__name__)

# TIETOKANTOJEN KIRJAUTUSTIEDOT PICKLE-TIEDOSTOSSA
# {'secretkey':<secretkey>, 'db':<dbname>, 'host':<serveraddress>, 'port':<port>, username':<käyttäjätunnus>, 'password':<salasana>}

pickle_in = open("db_auth.pickle","rb")
db_auth = pickle.load(pickle_in)

#######################################################################################################################################
#######################################################################################################################################

##################################################################################################################################
# # MONGOENGINEN MÄÄRITTELY
# # MONGOENGINEÄ KÄYTETÄÄN VAIN USER AUTHENTICATIONIIN
##################################################################################################################################
app.config['SECRET_KEY'] = db_auth['secretkey']
app.config['MONGODB_SETTINGS'] = {
    'db':db_auth['db'],
    'host':db_auth['host'],
    'port':db_auth['port'],
    'username':db_auth['username'],
    'password':db_auth['password']
}

# LIITETÄÄN APP MONGOENGINEEN

db = MongoEngine(app)

# MÄÄRITETÄÄN LOGINMANAGER

login_manager = LoginManager() # Luodaan loginmanager
login_manager.init_app(app) # Linkitetään app login_manager olioon
login_manager.login_view = "login" # Linkitetään kirjautumisnäkymä 'login'



##################################################################################################################################
# # PYMONGO
# # PYMONGOA KÄYTETÄÄN MUUHUIN KUIN KÄYTTÄJÄTIETOIHIN
##################################################################################################################################

client = pymongo.MongoClient(db_auth['host'], db_auth['port']) # defaults to port 27017
client.admin.authenticate(db_auth['username'], db_auth['password'], mechanism = 'SCRAM-SHA-1', source = db_auth['db'])
db_mongo = client[db_auth['db']]

#######################################################################################################################################
#######################################################################################################################################

# REKISTERÖIDÄÄN BLUEPRINTIT
from app.ontime.views import ontime_blueprint
from app.demand.views import demand_blueprint
#from app.bike.views import bike_blueprint
# ...

app.register_blueprint(ontime_blueprint, url_prefix='/ontime')
app.register_blueprint(demand_blueprint, url_prefix='/demand')
#app.register_blueprint(bike_blueprint, url_prefix='/bike')
