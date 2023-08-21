#%%
# Import the dependencies.
#%%
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt


#################################################
# Database Setup
#################################################
#%%
engine = create_engine("sqlite:///Resources/hawaii.sqlite")



# reflect an existing database into a new model

Base = automap_base()

#%%
# reflect the tables
#%%
Base.prepare(engine, reflect=True)

#%%
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
#%%
session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#%%

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )
# %%

@app.route("/api/v1.0/precipitation")
def precipitation():
    one_year_ago = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)


    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= one_year_ago).\
    order_by(Measurement.date).all()
    
    return jsonify(precipitation_dict)  
# %%
@app.route('/api/v1.0/stations')
def stations():
    
 
    return jsonify(stations_list)


@app.route('/api/v1.0/tobs')
def tobs():

    return jsonify(temperature_list)
# %%
