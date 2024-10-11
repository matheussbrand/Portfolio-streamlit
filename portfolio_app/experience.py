from pathlib import Path
import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie


def experience(experience_data: dict):
    # Criando colunas para adicionar animação à coluna3
    col1, col2, col3, col4 = st.columns(4)
    with col1:  # Título da página
        st.title("Experience")
    # with col2:
    #     st.write("""""")
    # with col3:
    #     st.write("""""")
    with col4:  # Carregar animação Lottie
        with (Path(__file__).parent / "Wrench.json").open() as f:
            data = json.load(f)
            st_lottie(
                data, speed=1, reverse=False, loop=True, width="150px", height="150px"
            )

    # Iterando sobre as empresas no dict experience_data
    for company_key, company_data in experience_data.items():
        # Obtendo os dados do título da experiência
        title_info = company_data.get("title", {})
        if title_info:
            title_comp = title_info.get("comp", "")
            title_name = title_info.get("name", "")
            start_date = title_info.get("start date", "")
            end_date = title_info.get("end date", "")
            location = title_info.get("location", "")
            about = title_info.get("about", "")

            # Expander que mostra o 'comp' como título, e o restante das informações abaixo
            with st.expander(f"{title_comp}", expanded=False):
                st.write(f"**Position:** {title_name}")
                st.write(f"**Start:** {start_date}")
                st.write(f"**End:** {end_date}")
                st.write(f"**Location:** {location}")
                st.write(f"**About:** {about}")

