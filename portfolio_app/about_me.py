import streamlit as st
from pathlib import Path

def about_me(about_me_data, source_path):
    # Set layout page to wide

    name = about_me_data.get("name", "Your Name")
    # Adding introductory message
    
    st.title(name)
    if "intro" in about_me_data:
        st.markdown(about_me_data["header"])
        st.markdown(about_me_data["intro"])
    st.write("""___""")


    about_me_data.get("header", "")
    
    # Adding columns
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    # Profile photo section
    with col1:
        if "profile_pic" in about_me_data:
            st.image(about_me_data["profile_pic"], width=200)

    # Download Resume English
    with col3:
        if "resume" in about_me_data:
            resume = source_path / Path(about_me_data["resume"])
            # loading resume in PDF Formatß
            with open(resume, "rb") as f:
                bytes_data = f.read()
            # Adding download button
            st.download_button(
                label="Resume (:flag-us:)",
                data=bytes_data,
                file_name=f"{name} | Resume-English.pdf",
                mime="application/pdf",
                key="download",
            )
            st.download_button(
                label="Resume (:flag-br:)",
                data=bytes_data,
                file_name=f"{name} | Resume-Portuguese.pdf",
                mime="application/pdf",
                key="download-br",
            )

    # Link to Github
    with col4:
        if "github" in about_me_data:
            github_logo = "https://raw.githubusercontent.com/matheussbrand/Portfolio-streamlit/refs/heads/main/portfolio_app/images/menu/github.png"
            st.markdown(
                f"""
                    <a href='{ about_me_data["github"]}' target='_blank'>
                        <img src='{github_logo}' width='30px'/>
                    </a>""",
                unsafe_allow_html=True,
            )
        # Link to Youtube
        if "youtube_link" in about_me_data:
            youtube_logo = "https://raw.githubusercontent.com/matheussbrand/Portfolio-streamlit/refs/heads/main/portfolio_app/images/menu/youtube.png"
            st.markdown(
                f"""
                    <a href='{ about_me_data["youtube_link"]}' target='_blank'>
                        <img src='{youtube_logo}' width='30px'/>
                    </a>""",
                unsafe_allow_html=True,
            )

    # Link to email
    with col5:
        if "email" in about_me_data:
            mail_logo = "https://raw.githubusercontent.com/matheussbrand/Portfolio-streamlit/refs/heads/main/portfolio_app/images/menu/mail.png?token=GHSAT0AAAAAACYYOOHHN5REBIT3AA2QX2IWZYIXTCQ"
            st.markdown(
                f"""
                    <a href='{ about_me_data["email"]}' target='_blank'>
                        <img src='{mail_logo}' width='30px'/>
                    </a>""",
                unsafe_allow_html=True,
            )

        # Link to Odysee
        if "odysee" in about_me_data:
            odysee_logo = "https://raw.githubusercontent.com/matheussbrand/Portfolio-streamlit/refs/heads/main/portfolio_app/images/menu/odysee.png"
            st.markdown(
                f"""
                    <a href='{ about_me_data["odysee"]}' target='_blank'>
                        <img src='{odysee_logo}' width='30px'/>
                    </a>""",
                unsafe_allow_html=True,
            )    


   # Link to LinkedIn
    with col6:
        if "linkedin" in about_me_data:
            linkedin_logo = "https://raw.githubusercontent.com/matheussbrand/Portfolio-streamlit/refs/heads/main/portfolio_app/images/menu/linkedin.png?token=GHSAT0AAAAAACYYOOHGGYPLA57LRWLM26YSZYIXSPQ"
            st.markdown(
                f"""
                    <a href='{ about_me_data["linkedin"]}' target='_blank'>
                        <img src='{linkedin_logo}' width='30px'/>
                    </a>""",
                unsafe_allow_html=True,
            )

    # Page Intro
    if "Intro" in about_me_data:
        st.write(about_me_data["intro"])

    st.write(""" """)

    # Adding link (Photos and Hyperlinks)
    if "links" in about_me_data:
        links = about_me_data["links"]
        st.subheader("Recent Projects")

        # Iterar sobre os links em grupos de 4
        for i in range(0, len(links), 5):  # A cada 4 itens
            cols = st.columns(5)  # Cria 4 colunas

            # Iterar sobre cada coluna e adicionar os links
            for j, col in enumerate(cols):
                if i + j < len(links):  # Verifica se há um item para essa coluna
                    try:
                        title = links[i + j]["title"]
                        url = links[i + j]["url"]
                        image = links[i + j]["image"]
                    except KeyError as exc:
                        st.error(f"'{exc}' property missing for link #{i + j}")
                        continue

                    # Adiciona o conteúdo da coluna
                    col.markdown(
                        f"""
                        <div style='text-align: center'>
                            {title}
                            <a href='{url}' target='_blank'>
                                <img src='{image}' width='100%'/>
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

        st.write("""""")  # Space between links & Youtube Videos

    # if "youtube" in about_me_data:
    #     # Adding Youtube Videos
    #     youtube = about_me_data["youtube"]
    #     cols = st.columns(len(youtube))

    #     for i, col in enumerate(cols):
    #         with col:
    #             try:
    #                 st.markdown(youtube[i]["title"])
    #                 st.video(youtube[i]["url"])
    #             except KeyError as exc:
    #                 st.error(f"'{exc}' property missing for youtube video #{i}")
    #                 continue
