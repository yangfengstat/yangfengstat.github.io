import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import plotly.express as px

# === STEP 1: Load your schedule.csv ===
file_path = 'schedule.csv'  # change if needed
df = pd.read_csv(file_path)

# === STEP 2: Extract speakers and chairs ===
talk_speakers = df[df['type'] == 'talk'][['speaker', 'Affliation']].dropna()
chair_rows = df[df['chair'].notna()][['chair', 'Affliation']]
chair_rows.columns = ['speaker', 'Affliation']
people = pd.concat([talk_speakers, chair_rows]).drop_duplicates()
people = people[people['Affliation'].notna() & (people['Affliation'].str.strip() != "")]

# === STEP 3: Geocode unique affiliations ===
affiliations = people['Affliation'].unique()
geolocator = Nominatim(user_agent="conference_map")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

geo_dict = {}
for aff in affiliations:
    try:
        location = geocode(aff)
        if location:
            geo_dict[aff] = (location.latitude, location.longitude)
    except Exception as e:
        print(f"Failed to geocode {aff}: {e}")

# === STEP 4: Map speakers to lat/lon ===
people['lat'] = people['Affliation'].map(lambda x: geo_dict.get(x, (None, None))[0])
people['lon'] = people['Affliation'].map(lambda x: geo_dict.get(x, (None, None))[1])
people = people.dropna(subset=['lat', 'lon'])

# === STEP 5: Plot interactive map ===
fig = px.scatter_geo(
    people,
    lat='lat',
    lon='lon',
    text='speaker',
    hover_name='speaker',
    hover_data={'Affliation': True, 'lat': False, 'lon': False},
    title='SNAB 2025 Speakers & Chairs by Affiliation'
)
fig.update_geos(projection_type="natural earth")
fig.update_layout(height=600)

# === STEP 6: Export to HTML ===
fig.write_html("network_map.html")
print("✅ Interactive map saved as network_map.html")
