import streamlit as st
import streamlit.components.v1 as components

my_component = components.declare_component("my_component", url="http://localhost:3000")
component_name = my_component.name
st.write(component_name)
my_component()
