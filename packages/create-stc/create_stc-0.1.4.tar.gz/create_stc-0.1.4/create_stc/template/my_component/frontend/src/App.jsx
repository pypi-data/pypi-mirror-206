import { useState, useEffect } from "react";
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import "./App.css";

function App() {
	useEffect(() => Streamlit.setFrameHeight());

	return <h1>Component: Hello, World!</h1>;
}

export default withStreamlitConnection(App);
