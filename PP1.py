#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:18:13 2024

@author: evakramarova
"""

import streamlit as st

st.set_page_config(page_title="Recipe Book", layout="wide")

st.title("Recipes for Ukrainian Dishes")

dishes = {
    "Borscht": {
        "image": "images/borscht.jpeg",
        "ingredients": "ingredients/borscht.txt",
        "recipe": "recipes/borscht.txt",
    },
    "Varenyky": {
        "image": "images/varenyky.jpeg",
        "ingredients": "ingredients/varenyky.txt",
        "recipe": "recipes/varenyky.txt",
    },  
    "Holubtsi": {
        "image": "images/holubtsi.png",
        "ingredients": "ingredients/holubtsi.txt",
        "recipe": "recipes/holubtsi.txt",
    },
    "Deruny": {
        "image": "images/deruny.webp",
        "ingredients": "ingredients/deruny.txt",
        "recipe": "recipes/deruny.txt",
    },
    "Chicken Kyiv": {
        "image": "images/chickenkyiv.webp",
        "ingredients": "ingredients/chickenkyiv.txt",
        "recipe": "recipes/chickenkyiv.txt",
    }, 
    "Syrniki": {
        "image": "images/syrniki.jpeg",
        "ingredients": "ingredients/syrniki.txt",
        "recipe": "recipes/syrniki.txt",
    }} 



def show_recipe(dish_name):
    st.subheader(dish_name)
    
    ingredients_file = dishes[dish_name]["ingredients"]
    recipe_file = dishes[dish_name]["recipe"]

    with open(ingredients_file, 'r') as file:
        ingredients = file.read()

    with open(recipe_file, 'r') as file:
        recipe = file.read()

    st.write("### Ingredients:")
    st.write(ingredients)
    st.divider()
    st.write("### Recipe:")
    st.write(recipe)

col1, col2 = st.columns(2, gap='medium')

with col1:
    st.subheader("Select a dish")
    # container = st.container()
    # with container:
    selected_dish = None
    for dish, details in dishes.items():
        if st.button(label = dish):
            selected_dish = dish
        st.image(details["image"], width=500)

with col2:
    if selected_dish is not None:
        show_recipe(dish_name = selected_dish)
    else:
        st.write("Please select a dish from the list to the left")


