import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="Composite Wall Heat Transfer",
    page_icon="🌡️",
    layout="wide"
)


# ============================================================
# TEAM DETAILS
# CHANGE THESE LATER
# ============================================================

GROUP_NO = "Python Titans"

MEMBERS = "Moksh Dhaval Dave | Jay Paraskumar Chaudhary | Anmol Arvindbhai Prajapati"

ENROLLMENTS = "25012250610045 | 25012250610046 | 25012250610064"


# ============================================================
# MATERIAL DATABASE
# ============================================================

materials = {
    "Firebrick": 1.50,
    "Insulating Brick": 0.30,
    "Red Brick": 0.70,
    "Concrete": 1.40,
    "Glass": 1.05,
    "Custom": None
}


# ============================================================
# HEADER
# ============================================================

st.title("🌡️ Conduction Heat Transfer Through a Composite Wall")

st.subheader("Diploma in Mechanical Engineering - Semester 3")

st.info(
    GROUP_NO +
    "   |   Members: " +
    MEMBERS +
    "   |   Enrollment: " +
    ENROLLMENTS
)

st.write(
    """
    This interactive application calculates heat transfer through a
    three-layer composite wall using thermal resistance theory.
    It calculates total thermal resistance, heat-transfer rate,
    heat flux and interface temperatures.
    """
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚙️ Wall Inputs")

st.sidebar.header("Wall Conditions")

area = st.sidebar.number_input(
    "Wall Area A (m²)",
    min_value=0.01,
    value=1.0,
    step=0.1
)

inside_temperature = st.sidebar.number_input(
    "Inside Temperature Ti (°C)",
    value=200.0,
    step=5.0
)

outside_temperature = st.sidebar.number_input(
    "Outside Temperature To (°C)",
    value=30.0,
    step=5.0
)


# ============================================================
# LAYER 1
# ============================================================

st.sidebar.header("Layer 1")

material1 = st.sidebar.selectbox(
    "Material 1",
    list(materials.keys())
)

if materials[material1] is None:

    k1 = st.sidebar.number_input(
        "Thermal Conductivity k₁ (W/m·K)",
        min_value=0.0001,
        value=1.0
    )

else:

    k1 = st.sidebar.number_input(
        "Thermal Conductivity k₁ (W/m·K)",
        min_value=0.0001,
        value=float(materials[material1])
    )

L1 = st.sidebar.number_input(
    "Thickness L₁ (m)",
    min_value=0.001,
    value=0.10,
    step=0.01
)


# ============================================================
# LAYER 2
# ============================================================

st.sidebar.header("Layer 2")

material2 = st.sidebar.selectbox(
    "Material 2",
    list(materials.keys()),
    index=1
)

if materials[material2] is None:

    k2 = st.sidebar.number_input(
        "Thermal Conductivity k₂ (W/m·K)",
        min_value=0.0001,
        value=1.0
    )

else:

    k2 = st.sidebar.number_input(
        "Thermal Conductivity k₂ (W/m·K)",
        min_value=0.0001,
        value=float(materials[material2])
    )

L2 = st.sidebar.number_input(
    "Thickness L₂ (m)",
    min_value=0.001,
    value=0.08,
    step=0.01
)


# ============================================================
# LAYER 3
# ============================================================

st.sidebar.header("Layer 3")

material3 = st.sidebar.selectbox(
    "Material 3",
    list(materials.keys()),
    index=2
)

if materials[material3] is None:

    k3 = st.sidebar.number_input(
        "Thermal Conductivity k₃ (W/m·K)",
        min_value=0.0001,
        value=1.0
    )

else:

    k3 = st.sidebar.number_input(
        "Thermal Conductivity k₃ (W/m·K)",
        min_value=0.0001,
        value=float(materials[material3])
    )

L3 = st.sidebar.number_input(
    "Thickness L₃ (m)",
    min_value=0.001,
    value=0.12,
    step=0.01
)


# ============================================================
# CALCULATE BUTTON
# ============================================================

calculate = st.sidebar.button(
    "🔍 CALCULATE",
    type="primary",
    use_container_width=True
)


# ============================================================
# CALCULATIONS
# ============================================================

if calculate:

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if area <= 0:

        st.error("Wall area must be greater than zero.")

        st.stop()


    if L1 <= 0 or L2 <= 0 or L3 <= 0:

        st.error(
            "All layer thicknesses must be greater than zero."
        )

        st.stop()


    if k1 <= 0 or k2 <= 0 or k3 <= 0:

        st.error(
            "Thermal conductivity must be greater than zero."
        )

        st.stop()


    if inside_temperature == outside_temperature:

        st.warning(
            "Inside and outside temperatures are equal. "
            "Heat transfer rate is zero."
        )


    # --------------------------------------------------------
    # THERMAL RESISTANCE
    # --------------------------------------------------------

    R1 = L1 / (k1 * area)

    R2 = L2 / (k2 * area)

    R3 = L3 / (k3 * area)


    # Total resistance

    R_total = R1 + R2 + R3


    # Temperature difference

    delta_T = inside_temperature - outside_temperature


    # Heat transfer rate

    Q = delta_T / R_total


    # Heat flux

    heat_flux = Q / area


    # --------------------------------------------------------
    # INTERFACE TEMPERATURES
    # --------------------------------------------------------

    T_interface1 = inside_temperature - Q * R1

    T_interface2 = T_interface1 - Q * R2

    T_interface3 = T_interface2 - Q * R3


    # ========================================================
    # RESULTS
    # ========================================================

    st.divider()

    st.header("📊 Calculation Results")


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "R₁",
        f"{R1:.5f} K/W"
    )

    col2.metric(
        "R₂",
        f"{R2:.5f} K/W"
    )

    col3.metric(
        "R₃",
        f"{R3:.5f} K/W"
    )

    col4.metric(
        "Total Resistance",
        f"{R_total:.5f} K/W"
    )


    col5, col6, col7 = st.columns(3)


    col5.metric(
        "Heat Transfer Rate",
        f"{Q:.3f} W"
    )

    col6.metric(
        "Heat Flux",
        f"{heat_flux:.3f} W/m²"
    )

    col7.metric(
        "Temperature Difference",
        f"{delta_T:.2f} °C"
    )


    # ========================================================
    # INTERFACE TEMPERATURES
    # ========================================================

    st.subheader("🌡️ Interface Temperatures")


    c1, c2, c3, c4, c5 = st.columns(5)


    c1.metric(
        "Inside",
        f"{inside_temperature:.2f} °C"
    )

    c2.metric(
        "Interface 1",
        f"{T_interface1:.2f} °C"
    )

    c3.metric(
        "Interface 2",
        f"{T_interface2:.2f} °C"
    )

    c4.metric(
        "Interface 3",
        f"{T_interface3:.2f} °C"
    )

    c5.metric(
        "Outside",
        f"{outside_temperature:.2f} °C"
    )


    # ========================================================
    # COMPOSITE WALL DIAGRAM
    # ========================================================

    st.subheader("🧱 Composite Wall Diagram")


    total_thickness = L1 + L2 + L3


    width1 = L1 / total_thickness

    width2 = L2 / total_thickness

    width3 = L3 / total_thickness


    fig1, ax1 = plt.subplots(
        figsize=(12, 2.5)
    )


    ax1.barh(
        0,
        width1,
        left=0,
        height=0.5
    )

    ax1.barh(
        0,
        width2,
        left=width1,
        height=0.5
    )

    ax1.barh(
        0,
        width3,
        left=width1 + width2,
        height=0.5
    )


    ax1.text(
        width1 / 2,
        0,
        material1,
        ha="center",
        va="center"
    )


    ax1.text(
        width1 + width2 / 2,
        0,
        material2,
        ha="center",
        va="center"
    )


    ax1.text(
        width1 + width2 + width3 / 2,
        0,
        material3,
        ha="center",
        va="center"
    )


    ax1.set_xlim(0, 1)

    ax1.set_ylim(-0.5, 0.5)

    ax1.axis("off")


    st.pyplot(fig1)


    # ========================================================
    # TEMPERATURE GRADIENT
    # ========================================================

    st.subheader("📈 Temperature Gradient")


    x = np.array([
        0,
        L1,
        L1 + L2,
        L1 + L2 + L3
    ])


    temperature = np.array([
        inside_temperature,
        T_interface1,
        T_interface2,
        outside_temperature
    ])


    fig2, ax2 = plt.subplots(
        figsize=(10, 5)
    )


    ax2.plot(
        x,
        temperature,
        marker="o",
        linewidth=2
    )


    ax2.axvline(
        L1,
        linestyle="--"
    )


    ax2.axvline(
        L1 + L2,
        linestyle="--"
    )


    ax2.set_xlabel(
        "Distance from Inside Surface (m)"
    )


    ax2.set_ylabel(
        "Temperature (°C)"
    )


    ax2.set_title(
        "Temperature Profile Through Composite Wall"
    )


    ax2.grid(True)


    st.pyplot(fig2)


    # ========================================================
    # LAYER TABLE
    # ========================================================

    st.subheader("📋 Layer-wise Results")


    table = pd.DataFrame({

        "Layer": [
            "Layer 1",
            "Layer 2",
            "Layer 3"
        ],

        "Material": [
            material1,
            material2,
            material3
        ],

        "Thermal Conductivity (W/m·K)": [
            k1,
            k2,
            k3
        ],

        "Thickness (m)": [
            L1,
            L2,
            L3
        ],

        "Thermal Resistance (K/W)": [
            R1,
            R2,
            R3
        ]

    })


    st.dataframe(
        table,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # FORMULAS
    # ========================================================

    st.subheader("📐 Engineering Formulas")


    st.write("Thermal resistance of each layer:")

    st.latex(
        r"R_i = \frac{L_i}{k_i A}"
    )


    st.write("Total thermal resistance:")

    st.latex(
        r"R_{total} = R_1 + R_2 + R_3"
    )


    st.write("Heat transfer rate:")

    st.latex(
        r"Q = \frac{T_i - T_o}{R_{total}}"
    )


    st.write("Heat flux:")

    st.latex(
        r"q'' = \frac{Q}{A}"
    )


    # ========================================================
    # VERIFICATION
    # ========================================================

    st.subheader("✅ Manual vs App Verification")


    st.write(
        f"""
        For the current input values:

        **Total Thermal Resistance = {R_total:.5f} K/W**

        **Heat Transfer Rate = {Q:.3f} W**

        These values can be compared with the manual calculation
        from your textbook numerical.
        """
    )


# ============================================================
# INITIAL SCREEN
# ============================================================

else:

    st.divider()

    st.header("🚀 How to Use This Calculator")

    st.write(
        """
        1. Enter the wall area.
        2. Enter inside and outside temperatures.
        3. Select materials for the three layers.
        4. Enter thermal conductivity and thickness.
        5. Click the CALCULATE button.
        6. View thermal resistance, heat transfer rate,
           interface temperatures and temperature gradient.
        """
    )


    st.subheader("📐 Main Formula")

    st.latex(
        r"R_{total} = \frac{L_1}{k_1 A}"
        r"+\frac{L_2}{k_2 A}"
        r"+\frac{L_3}{k_3 A}"
    )


    st.latex(
        r"Q = \frac{T_i-T_o}{R_{total}}"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "D Conduction Heat Transfer through a Composite Wall | "
    "Python + Streamlit | Diploma Mechanical Engineering - Semester 3"
)
