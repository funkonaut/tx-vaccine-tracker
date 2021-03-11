import pandas as pd
import streamlit as st
from vaccinetracker import *


if __name__ == "__main__":
    # The coordinates for the Texas Capitol.
    st.markdown("# To run the vaccine alert system: \n- Enter in the Lat and Lon coordinates (you can find these using google maps the longitude is negative if it is a W coordiante)\n- Enter in the search radius if you would like to search larger then 20km \n- Once the data is correctly input the program will take over and will launch a web page for a signup appointment when it finds a vaccine\n- To do another search with a differnet location or search radius you will need to refresh the page")
    old_lat = 0.0
    old_lon = 0.0
    home_lat = float(st.number_input("Latitude",step=.00001)) 
    home_lon = float(st.number_input("Longitude",step=.00001))
    dist = float(st.slider("Search Radius:",1,100,20))
    if home_lat != old_lat and home_lon != old_lon: 
        home_coords = [home_lat,home_lon]
        app = Application(
            notifiers=[
                WinBeeper(200, 400),  # play a 200Hz tone for 400ms
               # ConsolePrinter(home_coords),  # Print appointment info to the console
                LinkOpener()  # Open the link to the signup form
            ],
            origin=home_coords,
            min_qty=1,  # Don't show notifications less than 1
            max_dist=dist,  # Search within 20 miles
            rate=10  # update the results every 10 seconds
        )
        app.run()
        old_lat = home_lat
        old_lon = home_lon
    else:
        st.text(f"Please input correct information")

