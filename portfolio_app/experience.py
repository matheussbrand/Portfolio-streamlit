from pathlib import Path
import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie


def experience(experience_data: dict):

    ### Creating columns to add animation to column3
    col1, col2, col3, col4 = st.columns(4)
    with col1: # Page title
        st.title('Experience')
    with col2: # There's nothing here, bleh!
        st.write('''''')
    with col3: # There's nothing here, bleh!
        st.write('''''')
    with col4: # Load Lottie animation
        with (Path(__file__).parent / 'Wrench.json').open() as f:
            data = json.load(f)
            st_lottie(data,
            speed=1,
            reverse=False,
            loop=True,
            width='200px',
            height='150px'
            )


    companies = st.selectbox(
        'Select a company',
        list(experience_data.keys())
    )
    st.write(''' ''')

    company_data = experience_data[companies]

    # Images
    if "images" in company_data:
        cols = st.columns(len(company_data["images"]))
        for i, image in enumerate(company_data["images"]):
            cols[i].markdown(f'''
                            <img src='{image["url"]}' width='{image["width"]}' alt='{image["name"]}' />
                            </a>''',
                unsafe_allow_html=True
            )
    # Space       
    st.write(''' ''')

    # Skills
    if "skills" in company_data:
        select = option_menu(
                    menu_title=None,
                    menu_icon=None, default_index=0,
                    options=list(company_data["skills"].keys()),
                    orientation='horizontal',
                    styles={
                'container': {'padding': '5!important', 'background-color': '#000000'},
                'icon': {'color': 'orange', 'font-size': '10px'}, 
                'nav-link': {'font-size': '12px', 'text-align': 'center', 'margin':'0px', '--hover-color': '#eee'},
                'nav-link-selected': {'background-color': '#000000'},
                }
            )
        
        # Adding Role Title to Expander 
        title_info = company_data.get("title", {})
        if title_info:
            title_name = title_info.get("name", "")
            start_date = title_info.get("start date", "")
            end_date = title_info.get("end date", "")

        skill_details = st.expander(f"{title_name} | {start_date} to {end_date}", expanded=True)
        skill_details.markdown(company_data["skills"][select])  