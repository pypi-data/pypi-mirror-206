from pathlib import Path
from typing import Optional, Dict

import streamlit as st
import streamlit.components.v1 as components

import pydeck as pdk

# Tell streamlit that there is a component called streamlit_deckgl,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "streamlit_deckgl", path=str(frontend_dir)
)

# Create the python function that will be called
def st_deckgl(
    deck: pdk.Deck,
    width: int = 1000,
    height: int = 500,
    configuration: Optional[Dict] = None,
    key: Optional[str] = "deck_gl",
    events: Optional[list] = None,
):
    """Create a deck.gl map in Streamlit.

    Parameters
    ==========
    deck : pydeck.Deck instance
        The pydeck map to render.
    width : int, default 1000
        The width of the map in pixels.
    height : int, default 500
        The height of the map in pixels.
    configuration : dict, default None
        A dictionary of configuration options for the map.
    key : str, default "deck_gl"
        The key for the component. This must be unique for each map in the app.
    events : list, default ['click','hover','drag']
        A dict of events to listen for. Can be one or more of:
        - 'click'
        - 'hover'
        - 'drag'

    Returns
    =======
    component_value : dict
        A dictionary containing the info dictionary of the event.

    """
    json = deck.to_json()
    tooltip = deck._tooltip
    customLibraries = pdk.settings.custom_libraries
    configuration = pdk.settings.configuration

    component_value = _component_func(
        key=key,
        width=width,
        height=height,
        spec=json,
        tooltip=tooltip,
        customLibraries=customLibraries,
        configuration=configuration,
        events=events,
    )

    return component_value
