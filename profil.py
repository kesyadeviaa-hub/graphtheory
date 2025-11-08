import streamlit as st

# Judul halaman
st.title("Team Profile")

# Data anggota tim
team_members = [
    {
        "name": "Kesya Devia Anandita",
        "major": "Actuarial Science",
        "foto": "https://raw.githubusercontent.com/kesyadeviaa-hub/teamphoto/refs/heads/main/ACS_25102523320.jpg"
    },
    {
        "name": "Arganta Mahadana Wibowo",
        "major": "Actuarial Science",
        "foto": "https://raw.githubusercontent.com/kesyadeviaa-hub/teamphoto/refs/heads/main/ACS_25102553036.jpg"
    },
    {
        "name": "Alfazri Nurahman",
        "major": "Actuarial Science",
        "foto": "https://raw.githubusercontent.com/kesyadeviaa-hub/teamphoto/refs/heads/main/ACS_25102540760.jpg"
    },
]

# Tampilkan profil dalam 3 kolom
cols = st.columns(3)
for i, member in enumerate(team_members):
    with cols[i % 3]:
        st.image(member["foto"], width=180)
        st.markdown(f"**{member['name']}**")
        st.caption(member["major"])
