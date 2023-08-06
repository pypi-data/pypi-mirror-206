# streamlit-deckgl

Streamlit component for deck.gl visualisation with bi-directional transport for onClick events.

## Installation instructions

```sh
pip install streamlit-deckgl
```

## Usage instructions

```python
import streamlit as st
import pydeck as pdk
import pandas as pd

from streamlit_deckgl import st_deckgl


st.write("## Example")

chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)

r = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=37.76, longitude=-122.4, zoom=11, pitch=50, height=600
    ),
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=chart_data,
            get_position="[lon, lat]",
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
        pdk.Layer(
            "ScatterplotLayer",
            data=chart_data,
            get_position="[lon, lat]",
            get_color="[200, 30, 0, 160]",
            get_radius=200,
        ),
    ],
    tooltip={
        "html": "<b>Temperature:</b> {value} °C",
        "style": {"backgroundColor": "steelblue", "color": "white"},
    },
)

value = st_deckgl(r)

st.write(value)
```
