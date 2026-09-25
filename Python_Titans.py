import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit.components.v1 as components
import json


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

GROUP_NO = "Group No. PYTHON TITANS"

MEMBERS = [
    "Moksh Dhaval Dave",
    "Jay Paraskumar Chaudhary",
    "Anmol Arvindbhai Prajapati"
          ]

ENROLLMENTS = [
    " 25012250610045 ",
    " 25012250610046 ",
    " 25012250610064 "
]


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
    # ANIMATED COMPOSITE WALL
    # ========================================================

    st.subheader("🧱 Animated Composite Wall")


    animation_data = {
        "material1": material1,
        "material2": material2,
        "material3": material3,

        "L1": L1,
        "L2": L2,
        "L3": L3,

        "T_inside": inside_temperature,
        "T_interface1": T_interface1,
        "T_interface2": T_interface2,
        "T_interface3": T_interface3,
        "T_outside": outside_temperature,

        "Q": Q,
        "area": area
    }


    animation_json = json.dumps(animation_data)


    ANIMATION_HTML = """
    <style>

    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        padding: 0;
        font-family: "Segoe UI", Arial, sans-serif;
        background: #f3f8fc;
    }

    .card {
        background: white;
        border: 1px solid #cfdde8;
        border-radius: 12px;
        overflow: hidden;
    }

    .toolbar {
        display: flex;
        align-items: center;
        gap: 18px;
        flex-wrap: wrap;

        padding: 10px 14px;

        border-bottom: 1px solid #dce7ef;

        color: #17384d;

        font-size: 13px;
    }

    button {
        background: #0b2a43;
        color: white;

        border: none;
        border-radius: 6px;

        padding: 7px 14px;

        cursor: pointer;

        font-size: 13px;
    }

    button:hover {
        background: #174c6d;
    }

    .legend {
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .dot {
        width: 11px;
        height: 11px;

        border-radius: 50%;

        display: inline-block;
    }

    .hot {
        background: #e74c3c;
    }

    .cold {
        background: #3498db;
    }

    canvas {
        display: block;

        width: 100%;
        height: 500px;
    }

    </style>


    <div class="card">

        <div class="toolbar">

            <button id="replay">
                ↻ Replay Animation
            </button>

            <span class="legend">
                <span class="dot hot"></span>
                Hot side
            </span>

            <span class="legend">
                <span class="dot cold"></span>
                Cold side
            </span>

            <span>
                ➜ Heat flows from hot side to cold side
            </span>

        </div>

        <canvas id="wallCanvas"></canvas>

    </div>


    <script>

    const D = __DATA__;

    const canvas =
        document.getElementById("wallCanvas");

    const ctx =
        canvas.getContext("2d");

    let W = 1000;

    let H = 500;

    let dpr =
        window.devicePixelRatio || 1;

    let startTime =
        performance.now();


    // ----------------------------------------------------
    // Canvas resize
    // ----------------------------------------------------

    function resizeCanvas() {

        W = canvas.getBoundingClientRect().width;

        canvas.width = W * dpr;

        canvas.height = H * dpr;

    }

    window.addEventListener(
        "resize",
        resizeCanvas
    );

    resizeCanvas();


    // ----------------------------------------------------
    // Replay
    // ----------------------------------------------------

    document
        .getElementById("replay")
        .onclick = function() {

            startTime =
                performance.now();

        };


    // ----------------------------------------------------
    // Easing
    // ----------------------------------------------------

    function ease(t) {

        t =
            Math.max(
                0,
                Math.min(1, t)
            );

        return t < 0.5
            ? 4 * t * t * t
            : 1 - Math.pow(
                -2 * t + 2,
                3
            ) / 2;

    }


    // ----------------------------------------------------
    // Arrow
    // ----------------------------------------------------

    function drawArrow(
        x1,
        y1,
        x2,
        y2,
        color
    ) {

        const angle =
            Math.atan2(
                y2 - y1,
                x2 - x1
            );

        const head = 9;


        ctx.strokeStyle = color;

        ctx.fillStyle = color;

        ctx.lineWidth = 3;

        ctx.lineCap = "round";


        ctx.beginPath();

        ctx.moveTo(x1, y1);

        ctx.lineTo(x2, y2);

        ctx.stroke();


        ctx.beginPath();

        ctx.moveTo(x2, y2);

        ctx.lineTo(
            x2 - head *
            Math.cos(angle - 0.5),

            y2 - head *
            Math.sin(angle - 0.5)
        );

        ctx.lineTo(
            x2 - head *
            Math.cos(angle + 0.5),

            y2 - head *
            Math.sin(angle + 0.5)
        );

        ctx.closePath();

        ctx.fill();

    }


    // ----------------------------------------------------
    // Heat particle
    // ----------------------------------------------------

    function drawParticle(x, y) {

        ctx.beginPath();

        ctx.arc(
            x,
            y,
            5,
            0,
            Math.PI * 2
        );

        ctx.fillStyle = "#ff6b35";

        ctx.shadowColor = "#ff6b35";

        ctx.shadowBlur = 10;

        ctx.fill();

        ctx.shadowBlur = 0;

    }


    // ----------------------------------------------------
    // Main animation
    // ----------------------------------------------------

    function animate(now) {

        const elapsed =
            (now - startTime) / 1000;

        const cycle =
            elapsed % 4;

        const progress =
            cycle / 4;


        ctx.setTransform(
            dpr,
            0,
            0,
            dpr,
            0,
            0
        );


        ctx.clearRect(
            0,
            0,
            W,
            H
        );


        // ------------------------------------------------
        // Background
        // ------------------------------------------------

        ctx.fillStyle = "#f3f8fc";

        ctx.fillRect(
            0,
            0,
            W,
            H
        );


        // ------------------------------------------------
        // Wall dimensions
        // ------------------------------------------------

        const wallLeft =
            W * 0.25;

        const wallRight =
            W * 0.75;

        const wallTop = 145;

        const wallHeight = 210;

        const wallWidth =
            wallRight - wallLeft;


        const totalL =
            D.L1 +
            D.L2 +
            D.L3;


        const w1 =
            wallWidth *
            D.L1 /
            totalL;

        const w2 =
            wallWidth *
            D.L2 /
            totalL;

        const w3 =
            wallWidth *
            D.L3 /
            totalL;


        // ------------------------------------------------
        // Hot area
        // ------------------------------------------------

        ctx.fillStyle = "#fff1eb";

        ctx.fillRect(
            0,
            wallTop,
            wallLeft,
            wallHeight
        );


        // ------------------------------------------------
        // Cold area
        // ------------------------------------------------

        ctx.fillStyle = "#eaf5ff";

        ctx.fillRect(
            wallRight,
            wallTop,
            W - wallRight,
            wallHeight
        );


        // ------------------------------------------------
        // Hot side
        // ------------------------------------------------

        ctx.textAlign = "center";

        ctx.font =
            "bold 18px Segoe UI";

        ctx.fillStyle = "#d63b27";

        ctx.fillText(
            "🔥 HOT SIDE",
            wallLeft / 2,
            wallTop - 35
        );


        ctx.font =
            "bold 16px Segoe UI";

        ctx.fillText(
            D.T_inside.toFixed(1) +
            " °C",

            wallLeft / 2,
            wallTop - 10
        );


        // ------------------------------------------------
        // Cold side
        // ------------------------------------------------

        ctx.fillStyle = "#2779b8";

        ctx.font =
            "bold 18px Segoe UI";

        ctx.fillText(
            "❄️ COLD SIDE",

            wallRight +
            (W - wallRight) / 2,

            wallTop - 35
        );


        ctx.font =
            "bold 16px Segoe UI";

        ctx.fillText(
            D.T_outside.toFixed(1) +
            " °C",

            wallRight +
            (W - wallRight) / 2,

            wallTop - 10
        );


        // ------------------------------------------------
        // Layer 1
        // ------------------------------------------------

        ctx.fillStyle = "#d98c5f";

        ctx.fillRect(
            wallLeft,
            wallTop,
            w1,
            wallHeight
        );


        // ------------------------------------------------
        // Layer 2
        // ------------------------------------------------

        ctx.fillStyle = "#e5d5a5";

        ctx.fillRect(
            wallLeft + w1,
            wallTop,
            w2,
            wallHeight
        );


        // ------------------------------------------------
        // Layer 3
        // ------------------------------------------------

        ctx.fillStyle = "#aeb8c2";

        ctx.fillRect(
            wallLeft + w1 + w2,
            wallTop,
            w3,
            wallHeight
        );


        // ------------------------------------------------
        // Wall border
        // ------------------------------------------------

        ctx.strokeStyle = "#273746";

        ctx.lineWidth = 3;

        ctx.strokeRect(
            wallLeft,
            wallTop,
            wallWidth,
            wallHeight
        );


        // ------------------------------------------------
        // Layer boundaries
        // ------------------------------------------------

        ctx.strokeStyle = "#596b78";

        ctx.lineWidth = 2;

        ctx.beginPath();

        ctx.moveTo(
            wallLeft + w1,
            wallTop
        );

        ctx.lineTo(
            wallLeft + w1,
            wallTop + wallHeight
        );

        ctx.moveTo(
            wallLeft + w1 + w2,
            wallTop
        );

        ctx.lineTo(
            wallLeft + w1 + w2,
            wallTop + wallHeight
        );

        ctx.stroke();


        // ------------------------------------------------
        // Layer names
        // ------------------------------------------------

        ctx.font =
            "bold 13px Segoe UI";

        ctx.fillStyle = "#222";

        ctx.textAlign = "center";


        ctx.fillText(
            D.material1,

            wallLeft +
            w1 / 2,

            wallTop +
            wallHeight / 2
        );


        ctx.fillText(
            D.material2,

            wallLeft +
            w1 +
            w2 / 2,

            wallTop +
            wallHeight / 2
        );


        ctx.fillText(
            D.material3,

            wallLeft +
            w1 +
            w2 +
            w3 / 2,

            wallTop +
            wallHeight / 2
        );


        // ------------------------------------------------
        // Thickness labels
        // ------------------------------------------------

        ctx.font =
            "12px Segoe UI";

        ctx.fillStyle = "#34495e";


        ctx.fillText(
            "L₁ = " +
            D.L1.toFixed(3) +
            " m",

            wallLeft +
            w1 / 2,

            wallTop +
            wallHeight +
            25
        );


        ctx.fillText(
            "L₂ = " +
            D.L2.toFixed(3) +
            " m",

            wallLeft +
            w1 +
            w2 / 2,

            wallTop +
            wallHeight +
            25
        );


        ctx.fillText(
            "L₃ = " +
            D.L3.toFixed(3) +
            " m",

            wallLeft +
            w1 +
            w2 +
            w3 / 2,

            wallTop +
            wallHeight +
            25
        );


        // ------------------------------------------------
        // Heat flow direction
        // ------------------------------------------------

        const arrowY =
            wallTop +
            wallHeight / 2 +
            55;


        ctx.font =
            "bold 14px Segoe UI";

        ctx.fillStyle = "#c0392b";

        ctx.textAlign = "center";


        ctx.fillText(
            "Heat flow direction",
            W / 2,
            arrowY - 20
        );


        drawArrow(
            wallLeft - 100,
            arrowY,
            wallRight + 100,
            arrowY,
            "#e74c3c"
        );


        // ------------------------------------------------
        // Animated heat particles
        // ------------------------------------------------

        const particleCount = 10;


        for (
            let i = 0;
            i < particleCount;
            i++
        ) {

            let p =
                (
                    progress +
                    i / particleCount
                ) % 1;


            p = ease(p);


            const x =
                wallLeft -
                30 +
                p *
                (wallWidth + 60);


            const y =
                wallTop +
                wallHeight * 0.25 +
                (i % 4) * 42;


            drawParticle(
                x,
                y
            );

        }


        // ------------------------------------------------
        // Temperature points
        // ------------------------------------------------

        const tempPoints = [

            {
                x: wallLeft,
                temp: D.T_inside
            },

            {
                x: wallLeft + w1,
                temp: D.T_interface1
            },

            {
                x: wallLeft + w1 + w2,
                temp: D.T_interface2
            },

            {
                x: wallRight,
                temp: D.T_outside
            }

        ];


        tempPoints.forEach(
            function(point) {

                ctx.beginPath();

                ctx.arc(
                    point.x,
                    wallTop - 5,
                    4,
                    0,
                    Math.PI * 2
                );

                ctx.fillStyle = "#17202a";

                ctx.fill();


                ctx.font =
                    "bold 11px Segoe UI";

                ctx.fillStyle =
                    "#17202a";

                ctx.fillText(
                    point.temp.toFixed(1) +
                    " °C",

                    point.x,

                    wallTop - 18
                );

            }
        );


        // ------------------------------------------------
        // Heat transfer rate
        // ------------------------------------------------

        ctx.font =
            "bold 15px Segoe UI";

        ctx.fillStyle =
            "#8e2c20";

        ctx.textAlign =
            "center";


        ctx.fillText(
            "Q = " +
            D.Q.toFixed(3) +
            " W",

            W / 2,
            H - 35
        );


        // ------------------------------------------------
        // Temperature difference
        // ------------------------------------------------

        ctx.font =
            "12px Segoe UI";

        ctx.fillStyle =
            "#52616b";


        ctx.fillText(
            "ΔT = " +
            (
                D.T_inside -
                D.T_outside
            ).toFixed(2) +
            " °C",

            W / 2,
            H - 15
        );


        requestAnimationFrame(
            animate
        );

    }


    // ----------------------------------------------------
    // Start animation
    // ----------------------------------------------------

    requestAnimationFrame(
        animate
    );

    </script>
    """


    ANIMATION_HTML = ANIMATION_HTML.replace(
        "__DATA__",
        animation_json
    )


    components.html(
        ANIMATION_HTML,
        height=580
    )


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

    plt.close(fig2)


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


    st.write(
        "Thermal resistance of each layer:"
    )

    st.latex(
        r"R_i = \frac{L_i}{k_i A}"
    )


    st.write(
        "Total thermal resistance:"
    )

    st.latex(
        r"R_{total} = R_1 + R_2 + R_3"
    )


    st.write(
        "Heat transfer rate:"
    )

    st.latex(
        r"Q = \frac{T_i - T_o}{R_{total}}"
    )


    st.write(
        "Heat flux:"
    )

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

st.info(
    f"""
**{GROUP_NO}**

**Members:**

{chr(10).join("- " + member for member in MEMBERS)}

**Enrollments:**

{chr(10).join("- " + enrollment for enrollment in ENROLLMENTS)}
"""
)



st.caption(
    "Conduction Heat Transfer through a Composite Wall | "
    "Python + Streamlit | "
    "Diploma Mechanical Engineering - Semester 3"
)
