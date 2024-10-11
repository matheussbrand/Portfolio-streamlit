import streamlit as st
from pathlib import Path

def about_me(about_me_data, source_path):
    # Set layout page to wide

    name = about_me_data.get("name", "Your Name")
    # Adding introductory message
    st.title(name)
    if "intro" in about_me_data:
        st.markdown(about_me_data["intro"])
    st.write("""___""")

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

    # Link to Github
    with col4:
        if "github" in about_me_data:
            # st.image("portfolio_app\images\menu\github.png", width=25)
            github_logo = "https://github.com/matheussbrand/img-ref/blob/8b1cbf95c2f788f19ce51bd441a5527e9dfc65bf/menu/github.png"
            st.markdown(
                f"""
                    <a href='{ about_me_data["github"]}' target='_blank'>
                        <img src='{github_logo}' width='25px'/>
                    </a>""",
                unsafe_allow_html=True,
            )
        # Link to Youtube
        if "youtube_link" in about_me_data:
            st.image('portfolio_app\images\menu\youtu.png', width=30)

        # youtube_logo = "outube_ic.png"
            # st.markdown(
            #     f"""
            #         <a href='{ about_me_data["youtube"]}' target='_blank'>
            #             <img src='{youtube_logo}' width='25px'/>
            #         </a>""",
            #     unsafe_allow_html=True,
            # )

    # Link to email
    with col5:
        if "email" in about_me_data:
            # st.image('portfolio_app\images\menu\mail.png', width=25)
            mail_logo = "https://raw.githubusercontent.com/matheussbrand/img-ref/8b1cbf95c2f788f19ce51bd441a5527e9dfc65bf/portfolio_app/images/menu/mail.png"
            st.markdown(
                f"""
                    <a href='{ about_me_data["email"]}' target='_blank'>
                        <img src='{mail_logo}' width='25px'/>
                    </a>""",
                unsafe_allow_html=True,
            )

        # Link to Odysee
        if "odysee" in about_me_data:
            st.image("portfolio_app\images\menu\odysee.png", width=30)
            # odysee_logo = "https://raw.githubusercontent.com/youngpada1/portfolio-app/efa44604e838ff5218db9a9229b8fff256df5ae6/portfolio-app/portfolio_app/images/menu/odysee.png"
            # st.markdown(
            #     f"""
            #         <a href='{ about_me_data["odysee"]}' target='_blank'>
            #             <img src='{odysee_logo}' width='25px'/>
            #         </a>""",
            #     unsafe_allow_html=True,
            # )    


   # Link to LinkedIn
    with col6:
        if "linkedin" in about_me_data:
            linkedin_logo = "portfolio_app\images\menu\linkedin.png"
            st.markdown(
                f"""
                    <a href='{ about_me_data["linkedin"]}' target='_blank'>
                        <img src='{linkedin_logo}' width='20px'/>
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
        st.subheader("Projects")

        # Organizing links per column
        cols = st.columns(len(links))

        for i, col in enumerate(cols):
            with col:
                try:
                    title = links[i]["title"]
                    url = links[i]["url"]
                    image = links[i]["image"]
                except KeyError as exc:
                    st.error(f"'{exc}' property missing for link #{i}")
                    continue

                col.markdown(
                    f"""
                                { title }
                                <a href='{url}'>
                                <img src='{image}' width=100%/>
                                </a>""",
                    unsafe_allow_html=True,
                )
        st.write("""""")  # Space between links & Youtube Videos

    if "youtube" in about_me_data:
        # Adding Youtube Videos
        youtube = about_me_data["youtube"]
        cols = st.columns(len(youtube))

        for i, col in enumerate(cols):
            with col:
                try:
                    st.markdown(youtube[i]["title"])
                    st.video(youtube[i]["url"])
                except KeyError as exc:
                    st.error(f"'{exc}' property missing for youtube video #{i}")
                    continue
