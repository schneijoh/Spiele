import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Notendurchschnitt Rechner", page_icon="📚", layout="centered")

# ---------- Style ----------
st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}
.block-container {
    padding-top: 2rem;
}
h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.title("📚 Zeugnis-Notendurchschnitt Rechner")
st.write("Berechne deinen Notendurchschnitt und sieh deine Noten im Diagramm 📊")

# ---------- Eingabe ----------
anzahl_faecher = st.number_input("📘 Wie viele Fächer hast du?", min_value=1, max_value=50, step=1)

fach_namen = []
noten = []

for i in range(int(anzahl_faecher)):
    col1, col2 = st.columns(2)
    with col1:
        fach = st.text_input(f"Fachname {i+1}", value=f"Fach {i+1}", key=f"fach_{i}")
    with col2:
        note = st.number_input(f"Note {i+1}", min_value=1.0, max_value=6.0, step=0.1, format="%.1f", key=f"note_{i}")

    fach_namen.append(fach)
    noten.append(note)

# ---------- Berechnung ----------
if st.button("📊 Durchschnitt berechnen"):
    durchschnitt = sum(noten) / len(noten)

    st.success(f"🎯 Dein Notendurchschnitt ist: **{durchschnitt:.2f}**")

    # Bewertung
    if durchschnitt <= 1.5:
        st.balloons()
        st.write("🌟 Sehr stark! Top Leistung!")
    elif durchschnitt <= 2.5:
        st.write("👍 Gut gemacht!")
    elif durchschnitt <= 3.5:
        st.write("🙂 Solide Leistung")
    else:
        st.write("💪 Da geht noch was – du schaffst das!")

    # ---------- Diagramm ----------
    st.markdown("### 📈 Noten-Diagramm")

    fig, ax = plt.subplots()
    ax.bar(fach_namen, noten)
    ax.axhline(y=durchschnitt, linestyle='--', label=f'Durchschnitt: {durchschnitt:.2f}')
    ax.set_xlabel("Fächer")
    ax.set_ylabel("Noten")
    ax.set_title("Notenübersicht")
    ax.legend()
    plt.xticks(rotation=45)

    st.pyplot(fig)

st.markdown("---")
st.caption("✨ Moderne Streamlit WebApp | Notenrechner mit Diagramm")
