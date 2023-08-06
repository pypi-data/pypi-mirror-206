const { DeckGL, JSONConverter, carto } = deck;

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */

function onRender(event) {
  // Only run the render code the first time the component is loaded.
  if (!window.rendered) {
    const {
      spec,
      width,
      height,
      tooltip,
      customLibraries,
      configuration,
      events,
    } = event.detail.args;

    const eventlist = events && events.map((event) => `deck-${event}-event`);

    const container = document.getElementById("root");
    container.style.width = width + "px";
    container.style.height = height + "px";

    const mapEventHandler = (eventType, info) => {
      if (events && eventlist.includes(eventType) && info.object) {
        Streamlit.setComponentValue(info.object);
      }
    };

    const deckInstance = createDeck({
      container,
      jsonInput: JSON.parse(spec),
      tooltip,
      customLibraries,
      configuration,
      handleEvent: mapEventHandler,
    });

    Streamlit.setFrameHeight(height);
    window.rendered = true;
  }
}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady();
// Render with the correct height, if this is a fixed-height component
