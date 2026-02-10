from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Intermolecular Forces Interactive Chemistry Project</title>

<style>
* {
    box-sizing: border-box;
}

body {
    font-family: 'Times New Roman', Times, serif;
    background: #000000;
    margin: 0;
    padding: 20px;
    min-height: 100vh;
    line-height: 1.5;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

h1 {
    color: white;
    text-align: center;
    font-size: 2.5em;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.subtitle {
    color: white;
    text-align: center;
    margin-bottom: 30px;
    font-size: 0.95em;
}

h2 {
    color: #1f3a60;
    border-bottom: 3px solid #667eea;
    padding-bottom: 10px;
    margin-top: 30px;
}

h3 {
    color: #333;
    margin-top: 20px;
}

.section {
    background: white;
    padding: 30px;
    border-radius: 15px;
    margin-bottom: 30px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
    border-left: 5px solid #667eea;
}

.definition-box {
    background: #f8f9fa;
    padding: 20px;
    border-left: 4px solid #28a745;
    margin: 15px 0;
    border-radius: 8px;
}

.imf-slider-wrap {
    display: flex;
    gap: 24px;
    align-items: stretch;
    margin-top: 18px;
    flex-wrap: wrap;
}

.imf-gauge {
    display: flex;
    gap: 10px;
    align-items: center;
}

.imf-gauge-labels {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 180px;
    font-size: 14px;
    color: #1f3a60;
}

.imf-gauge-bar {
    width: 26px;
    height: 180px;
    border: 2px solid #1f3a60;
    border-radius: 8px;
    background: #f1f3f5;
    position: relative;
    overflow: hidden;
}

.imf-gauge-fill {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 0%;
    background: linear-gradient(180deg, #28a745 0%, #ffc107 55%, #dc3545 100%);
}

.imf-slider-panel {
    flex: 1;
    min-width: 280px;
}

.imf-atoms-row {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 16px;
    margin: 72px 0 16px 520px;
}

.imf-atom {
    width: 96px;
    height: 96px;
    border-radius: 50%;
    background: #ff6b6b;
    color: black;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #c92a2a;
    font-size: 14px;
    position: relative;
}

.imf-atom.positive {
    background: #ff6b6b;
    border-color: #c92a2a;
}

.imf-atom.negative {
    background: #6ab04c;
    border-color: #2f7d32;
}

.imf-charge-badge {
    position: absolute;
    bottom: -8px;
    right: -8px;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: #1f3a60;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    font-weight: bold;
    border: 2px solid #0f1e33;
}

.imf-arrow {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    color: #1f3a60;
    width: 120px;
    text-align: center;
}

.imf-arrow-label {
    font-size: 18px;
    margin-bottom: 4px;
}

.imf-arrow-symbol {
    font-size: 72px;
    line-height: 1;
}

.imf-slider {
    margin: 12px 0;
}

.imf-slider label {
    display: block;
    font-weight: bold;
    color: #1f3a60;
    margin-bottom: 4px;
}

.imf-slider input[type="range"] {
    width: 30%;
    accent-color: #f1c40f;
    height: 10px;
}

.imf-slider input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #dc3545;
    border: 2px solid #991a3a;
    cursor: pointer;
}

.imf-slider input[type="range"]::-moz-range-thumb {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #dc3545;
    border: 2px solid #991a3a;
    cursor: pointer;
}

.imf-scale {
    display: flex;
    justify-content: space-between;
    width: 30%;
    font-size: 13px;
    color: #1f3a60;
}

.imf-note {
    font-size: 12px;
    color: #1f3a60;
    margin-top: 6px;
}

.bar {
    height: 35px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    margin: 12px 0;
    border-radius: 8px;
    color: white;
    padding-left: 12px;
    display: flex;
    align-items: center;
    font-weight: bold;
    box-shadow: 0 3px 8px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.bar:hover {
    transform: translateX(10px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 15px 0;
}

td, th {
    border: 2px solid #ddd;
    padding: 12px;
    text-align: left;
    background: white;
}

th {
    background: #667eea;
    color: white;
    font-weight: bold;
}

tr:hover td {
    background: #f0f4f8;
}

.comparison {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin: 20px 0;
}

.comparison-card {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 10px;
    border: 2px solid #667eea;
}

.comparison-card h4 {
    margin-top: 0;
    color: #667eea;
}

svg {
    margin-top: 20px;
    display: block;
    max-width: 100%;
    height: auto;
}

.slider-container {
    margin: 25px 0;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 10px;
}

.slider-label {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    font-weight: bold;
}

input[type="range"] {
    width: 100%;
    height: 8px;
    border-radius: 5px;
    background: #ddd;
    outline: none;
    -webkit-appearance: none;
}

input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #667eea;
    cursor: pointer;
}

input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #667eea;
    cursor: pointer;
    border: none;
}

.example-list {
    list-style: none;
    padding-left: 0;
}

.example-list li {
    padding: 10px;
    margin: 8px 0;
    background: #f0f4f8;
    border-left: 4px solid #667eea;
    border-radius: 4px;
}

.highlight {
    background: transparent;
    padding: 0;
    border-radius: 0;
    font-weight: normal;
}

.principle {
    background: #d4edda;
    padding: 15px;
    border-radius: 8px;
    margin: 12px 0;
    border-left: 4px solid #28a745;
}

canvas {
    border: 1px solid #ddd;
    border-radius: 8px;
    background: white;
    display: block;
    margin: 20px 0;
}

.atom-col {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
}

.charge-symbol {
    font-size: 20px;
    font-weight: bold;
    color: #1f3a60;
    min-width: 40px;
    text-align: center;
}

.charge-select-row {
    display: flex;
    gap: 20px;
    margin-top: 20px;
    justify-content: center;
}

.charge-select-row > div {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.charge-select-row label {
    font-weight: bold;
    color: #1f3a60;
    font-size: 14px;
}

.charge-select-row select {
    padding: 8px 12px;
    border: 2px solid #667eea;
    border-radius: 6px;
    font-size: 14px;
    font-weight: bold;
    background: white;
    cursor: pointer;
    min-width: 80px;
}

.charge-select-row select:hover {
    background: #f0f4f8;
}

</style>
</head>

<body>

<div class="container">

<h1>Logan Bayne Intermolecular Forces</h1>

<div class="section">
<h2>1. The Four Types of Intermolecular Forces</h2>

<p><b>Universal Principle:</b> All intermolecular forces are fundamentally based on the attraction between positive and negative charges. The stronger and more complete the charges, the stronger the force.</p>

<div class="definition-box">
<h3>A. Ionic Forces (Ionic Bonding)</h3>
<p><b>Definition:</b> Ionic forces are strong electrostatic attractions between a metal and a nonmetal. The highly electronegative nonmetal steals valence electrons from the low-electronegativity metal, creating full charges and a very secure bond where the electrons are not shared but stolen by the nonmetal. When multiple compounds that contain Ionic bonds are exposed to each other, the ionic forces from the nonmetals attract the metals of the other compounds, bonding the multiple compounds together through the same principle that the nonmetals attract the metals and vice versa due to electronegative differences.</p>
<p><b>Why they exist:</b> Ionic IMF forces exist becasue nonmetals have a very high electronegativity meaning that they pull on other electrons with a very strong force, and metals tend to have a weaker pull on electrons. Due to the disparities in the forces, the nonmetal's pull overwhelms the pull of the metal and completely steals the valence electrons in order to create a full valence shell for the atoms, creating an ionic bond. Multiple Ionic compounds create ionic IMF forces because the nonmetals of one compound have differenet charges from the metals in the other compound, so the multiple compounds "attach" themselves through this IMF force of opposite attraction.</p>
<p><b>Charges:</b> Ionic compounds have full constant charges because the atoms do not share electrons, they steal or lose, meaning that each atom now has complete control of their valence electrons, so there is no partial charges. (+1, +2, +3, -1, -2 , -3 etc...). Overall - no partial charge because there is no sharing of electrons.</p>
<p><b>Strength:</b> The strength of Ionic IM forces are the strongest becasue the atoms do not share, but rather they have full outer shells from the electrons they lost or gained, meaning each atom is completely stable and filled, creating a very strong bond that is extremely hard to undo.</p>
<p><b>Examples:</b> NaCl (salt) - Cl (nonmetal) steals a valence electron from Na (metal), making Na⁺ and Cl⁻. When many NaCl units come together, every Na⁺ is attracted to nearby Cl⁻ ions from other units, forming a crystal lattice. Those ion-to-ion attractions are caused for the reasons listed above.</p>

<svg width="100%" height="220" viewBox="0 0 900 220" aria-label="NaCl with crossed ionic IMF">
    <text x="450" y="24" text-anchor="middle" font-size="15" fill="#333" font-weight="bold">NaCl units (Ionic IMF)</text>

    <!-- Top NaCl (Cl left, Na right, touching) -->
    <circle cx="410" cy="70" r="28" fill="#5dade2" stroke="#21618c" stroke-width="2"/>
    <text x="410" y="76" text-anchor="middle" font-size="14" fill="white" font-weight="bold">Cl⁻</text>
    <circle cx="464" cy="70" r="26" fill="#ff6b6b" stroke="#c92a2a" stroke-width="2"/>
    <text x="464" y="76" text-anchor="middle" font-size="14" fill="white" font-weight="bold">Na⁺</text>

    <!-- Vertical striped IMF lines -->
    <line x1="410" y1="98" x2="410" y2="135" stroke="#1f3a60" stroke-width="3" stroke-dasharray="6,6"/>
    <line x1="464" y1="96" x2="464" y2="135" stroke="#1f3a60" stroke-width="3" stroke-dasharray="6,6"/>

    <!-- Bottom ions attached to lines (opposite charges) -->
    <circle cx="410" cy="150" r="26" fill="#ff6b6b" stroke="#c92a2a" stroke-width="2"/>
    <text x="410" y="156" text-anchor="middle" font-size="14" fill="white" font-weight="bold">Na⁺</text>
    <circle cx="464" cy="152" r="28" fill="#5dade2" stroke="#21618c" stroke-width="2"/>
    <text x="464" y="158" text-anchor="middle" font-size="14" fill="white" font-weight="bold">Cl⁻</text>

    <text x="450" y="210" text-anchor="middle" font-size="12" fill="#1f3a60" font-weight="bold">striped line = Ionic IMF</text>
</svg>
</div>

<div class="definition-box">
<h3>B. Hydrogen Bonding (Special Dipole-Dipole)</h3>
<p><b>Definition:</b> Hydrogen bonding is a strong dipole-dipole attraction that happens when Hydrogen is covalently bonded to a very electronegative atom (F, O, N, Cl). Once this covalent bond is created, since F, O, N, and Cl pull on other Hydrogen in other solutions extremely hard, connecting multiple ions through the F, O, N, and Cl pulling other Hydrogens in other solutions towards them, creating a hydrogen bond.</p>
<p><b>Why they exist:</b> Hydrogen bonding exists because hydrogen and fluorine, oxygen, and nitrogen are all nonmetals and form polar covalent bonds with hydrogen (another nonmetal) rather than transferring electrons completely. Fluorine, oxygen, and nitrogen are much more electronegative than hydrogen, so they pull the shared electrons closer to themselves, creating a strong partial negative charge on F, O, or N and a strong partial positive charge on hydrogen. Because hydrogen is extremely small and highly positive, it can be strongly attracted to the lone pair electrons on a nearby F, O, or N atom in another molecule, producing a hydrogen bond between the molecules.</p>
<p><b>Charges:</b> Large partial constant charges (strong δ+ on H and δ− on N,O,F, or Cl). Hydrogen bonds do not create a full charge becasue they still share the electrons, however the F, O, N, or Cl have a much higher partial negative due to their stronger pull on the electrons while the Hydrogen has a weaker pull and has a higher positive partial charge.</p>
<p><b>IMF between molecules:</b> The δ+ hydrogen on one molecule is attracted to the  δ− end (F, O, or N) of a neighboring molecule. That specific H,F,N, or Cl pull is the hydrogen-bond IMF holding the molecules together.</p>
<p><b>Strength:</b> Second Strongest IM force: weaker than Ionic because the atoms still share electrons though not equally, but stronger than typical dipole-dipole forces because of the vast disperities in electronegativity between H and F,O,N, or Cl.</p>
<p><b>Examples:</b> Ammonia (NH₃) - the nitrogen atom is strongly δ− due to its high electronegativity, while each hydrogen is δ+. When ammonia molecules come together, the δ+ hydrogen of one molecule is strongly attracted to the lone pair on the δ− nitrogen of another molecule, forming hydrogen bonds between them. Visual shown in Part 7 for Another Hydrogen Bond - Water.</p>
</div>

<div class="definition-box">
<h3>C. Dipole-Dipole Forces</h3>
<p><b>Definition:</b> Dipole-dipole forces are attractions between polar molecules where the δ+ end of one molecule is pulled toward the δ− end of another. When different ions with dipole-dipole bonds are exposed to each otehr, these ions connect through teh same principle in ionic bonding, except in this case instead of having full charges, the partial positives from one ion attract the partial negatives from another ion and vice versa.</p>
<p><b>Why they exist:</b> When two atoms have a moderate electronegativity difference, electrons are shared but unevenly. One side of the molecule becomes slightly negative (δ−) and the other becomes slightly positive (δ+). Neighboring polar molecules rotate and line up so opposite partial charges are close, creating an attraction between them.</p>
<p><b>Charges:</b> Permanent partial charges (δ+ and δ−). The charges are consistent for that molecule, but they are not full ionic charges because electrons are still shared, so neither has full control of the electrons.</p>
<p><b>Strength:</b> Third strongest; stronger than London dispersion because the dipoles are permanent and the charges are unequal, meaning that one pulls on the other more, creating a stronger bond, but weaker than hydrogen bonding and ionic forces because the charges are only partial and spread out, so the attraction is less concentrated. It is weaker than hydrogen bondign because in hyrdogen bonding the vast difference in electronegativity between Hydrogen and the 4 most electronegative elements creates a strong bond, but in this case there is not as much of a difference in electronegativities, creating a slightly weaker bond than H-bonding.</p>
<p><b>Examples:</b> HI (hydrogen iodide) - I has a high electronegativity, enough to pull on the Hydrogen, but not enough to steal the electrons, so I is δ− and H is δ+ because the iodine controls more of the electrons which are negatively charged.</p>

<svg width="100%" height="220" viewBox="0 0 900 220" aria-label="HI dipole-dipole IMF">
    <text x="450" y="24" text-anchor="middle" font-size="15" fill="#333" font-weight="bold">HI dipole-dipole IMF</text>

    <!-- Top HI molecule -->
    <circle cx="450" cy="70" r="30" fill="#6ab04c" stroke="#2f7d32" stroke-width="2"/>
    <text x="450" y="76" text-anchor="middle" font-size="14" fill="white" font-weight="bold">I δ−</text>
    <circle cx="400" cy="70" r="18" fill="#dfe6e9" stroke="#636e72" stroke-width="2"/>
    <text x="400" y="75" text-anchor="middle" font-size="12" fill="#2d3436" font-weight="bold">H δ+</text>

    <!-- Bottom HI molecule -->
    <circle cx="450" cy="170" r="30" fill="#6ab04c" stroke="#2f7d32" stroke-width="2"/>
    <text x="450" y="176" text-anchor="middle" font-size="14" fill="white" font-weight="bold">I δ−</text>
    <circle cx="500" cy="170" r="18" fill="#dfe6e9" stroke="#636e72" stroke-width="2"/>
    <text x="500" y="175" text-anchor="middle" font-size="12" fill="#2d3436" font-weight="bold">H δ+</text>

    <!-- Striped IMF lines (H δ+ to I δ−) -->
    <line x1="408" y1="86" x2="437" y2="143" stroke="#1f3a60" stroke-width="3" stroke-dasharray="6,6"/>
    <line x1="492" y1="154" x2="463" y2="97" stroke="#1f3a60" stroke-width="3" stroke-dasharray="6,6"/>

    <text x="450" y="210" text-anchor="middle" font-size="12" fill="#1f3a60" font-weight="bold">striped line = dipole-dipole IMF</text>
</svg>
</div>

<div class="definition-box">
<h3>D. London Dispersion Forces (LDF)</h3>
<p><b>Definition:</b> London dispersion forces are breif, shifting attractions between atoms with relatively similar electronegativities that cannot control the electrons more than the others. These forces shift from atoms to atom as the electron field fluctuates between the atoms since the electrons are not pulled to one or the other more, so they are much more free roaming..</p>
<p><b>Why they exist:</b>  Becasue the atoms in LDF forces share similar electronegativities, neither atom pulls the electron more than the other, so the electron are sort of free moving around the atoms. So, since the atoms are moving around in a random sense, one side will have more electrons, creating a momentary partial negative for this side since electrons are negative. when one side is mroe negative, the other side is thus more partially positive, and since positives attract negatives, the lectrons are pulled towards the positive side, making the once positive side now negative, and this shifts as the electrons are pulled bakc and forth from one to another.</p>
<p><b>Charges:</b> Instantaneous, temporary partial charges (δ+ and δ−) that appear and disappear continuously due to the shifting electrons. There are no permanent charges.</p>
<p><b>Strength:</b> In all the other examples of IMF forces, the atoms had differing electronegativies, creating stronger pulls. But in LDF's the electronegativities are very similar meaning that the forces are generally much weaker due to the pull on the otehr atoms being weaker. So, LDF's have the weakest charge of all the IMF's.</p>
<p><b>Examples:</b> Octane (C₈H₁₈) and Propane (C₃H₈) are nonpolar compounds only of carbon and hydrogen atoms with very similar electronegativities. Because neither atom pulls significantly harder on the electrons, the electrons are free to move around randomly. As electrons shift from one side of the molecule to the other, they create momentary and temporary partial charges that constantly appear and disappear. LDF visual displayed in section 8.</p>
</div>

</div>

<div class="section">
<h2>2. Relative Strengths of Intermolecular Forces</h2>




<div class="bar" style="width:95%; background: linear-gradient(90deg, #dc3545 0%, #991a3a 100%);">
    Ionic Forces (Strongest)
</div>
<div class="bar" style="width:80%; background: linear-gradient(90deg, #fd7e14 0%, #b85a0a 100%);">
    Hydrogen Bonding
</div>
<div class="bar" style="width:60%; background: linear-gradient(90deg, #ffc107 0%, #b89d00 100%);">
    Dipole-Dipole Forces
</div>
<div class="bar" style="width:30%; background: linear-gradient(90deg, #28a745 0%, #1a5c2d 100%);">
    London Dispersion Forces (Weakest)
</div>

<div class="principle">
<p><b></b> Ionic forces > Hydrogen bonds > Dipole-dipole forces > London dispersion forces</p>
<ul>
    <li><b>Ionic forces:</b> full charges (Na⁺/Cl⁻) create the strongest attraction because one atom completely takes the electrons, creating a very secure and strong bond that is difficult to undo.</li>
    <li><b>Hydrogen bonding:</b> very large partial charges from H bonded to F, O, N, and Cl make a strong dipole-dipole attraction, but it is stronger than the regular dipole dipole becasue F,O,N, and Cl are much stronger than other nonmetals, meaning that they pull harder and create stronger bonds than the regular dipole dipole, but not as strong as ionic bonds where the charges are full and the bond is absolute.</li>
    <li><b>Dipole‑dipole:</b> partial charges attract, but the charges are smaller becasue there is less difference in electronegativity than when H is bonded to one of the 4 most electronegative elements, creating a weaker bond than Hydrogen bonds.</li>
    <li><b>London dispersion:</b> only temporary, weak dipoles; the weakest because the charges are brief and not absolute and there is practically no difference in electronegativity, so neither atom has a particularly strong pull, creating the weakest bond of the four.</li>
</ul>
</div>

<h3>Ranking of IMF Strength by Compound</h3>

<table style="width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px;">
<tr style="background-color: #2c3e50; color: white;">
<th style="padding: 12px; text-align: left; border: 1px solid #34495e;">Rank</th>
<th style="padding: 12px; text-align: left; border: 1px solid #34495e;">Compound</th>
<th style="padding: 12px; text-align: left; border: 1px solid #34495e;">IMF Type</th>
<th style="padding: 12px; text-align: left; border: 1px solid #34495e;">Explanation</th>
</tr>
<tr style="background-color: #f8f9fa;">
<td style="padding: 12px; border: 1px solid #ddd;"><b>1</b></td>
<td style="padding: 12px; border: 1px solid #ddd;">MgO</td>
<td style="padding: 12px; border: 1px solid #ddd;">Ionic</td>
<td style="padding: 12px; border: 1px solid #ddd;">Highest charge magnitude ±2, creating the strongest attraction.</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ddd;"><b>2</b></td>
<td style="padding: 12px; border: 1px solid #ddd;">CaO</td>
<td style="padding: 12px; border: 1px solid #ddd;">Ionic</td>
<td style="padding: 12px; border: 1px solid #ddd;">High charge magnitude ±2, nearly as strong as MgO but its larger radius reduces strength slightly due to the forces being separated more.</td>
</tr>
<tr style="background-color: #f8f9fa;">
<td style="padding: 12px; border: 1px solid #ddd;"><b>3</b></td>
<td style="padding: 12px; border: 1px solid #ddd;">NaCl (salt)</td>
<td style="padding: 12px; border: 1px solid #ddd;">Ionic</td>
<td style="padding: 12px; border: 1px solid #ddd;">Lower charge magnitude ±1 compared to MgO and CaO, but still ionic with full charges resulting in weaker ionic attaraction.</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ddd;"><b>4</b></td>
<td style="padding: 12px; border: 1px solid #ddd;">KBr</td>
<td style="padding: 12px; border: 1px solid #ddd;">Ionic</td>
<td style="padding: 12px; border: 1px solid #ddd;">Charge magnitude ±1 but larger radius than NaCl, reducing the bond strength by separating the charges.</td>
</tr>
<tr style="background-color: #f8f9fa;">
<td style="padding: 12px; border: 1px solid #ddd;"><b>5</b></td>
<td style="padding: 12px; border: 1px solid #ddd;">H₂O (water)</td>
<td style="padding: 12px; border: 1px solid #ddd;">Hydrogen Bonding</td>
<td style="padding: 12px; border: 1px solid #ddd;">Very large partial charges due to O's high electronegativity, creating strong hydrogen bonds.</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ddd;"><b>6</b></td>
<td style="padding: 12px; border: 1px solid #ddd;">NH₃ (ammonia)</td>
<td style="padding: 12px; border: 1px solid #ddd;">Hydrogen Bonding</td>
<td style="padding: 12px; border: 1px solid #ddd;">Hydrogen bonding from H bonded to N, but slightly weaker than water due to N's lower electronegativity.</td>
</tr>
<tr style="background-color: #f8f9fa;">
<td style="padding: 12px; border: 1px solid #ddd;"><b>7</b></td>
<td style="padding: 12px; border: 1px solid #ddd;">H₂S</td>
<td style="padding: 12px; border: 1px solid #ddd;">Dipole-Dipole</td>
<td style="padding: 12px; border: 1px solid #ddd;">Polar molecule with partial charges, but no hydrogen bonding as S is not electronegative enough to pull as hard as F, O, N or Cl.</td>
</tr>
<tr style="background-color: #f8f9fa;">
<td style="padding: 12px; border: 1px solid #ddd;"><b>8</b></td>
<td style="padding: 12px; border: 1px solid #ddd;">C₈H₁₈ (octane)</td>
<td style="padding: 12px; border: 1px solid #ddd;">London Dispersion</td>
<td style="padding: 12px; border: 1px solid #ddd;">Moderate electron cloud size produces modium temporary dipoles.</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ddd;"><b>9</b></td>
<td style="padding: 12px; border: 1px solid #ddd;">C₃H₈ (propane)</td>
<td style="padding: 12px; border: 1px solid #ddd;">London Dispersion</td>
<td style="padding: 12px; border: 1px solid #ddd;">Smallest electron cloud among all compounds, producing the weakest temporary dipoles.</td>
</tr>
</table>

</div>

<div class="section">
<h2>3. Principles of IMF Forces and Ionic Forces</h2>

<h3>A. Charge Magnitude and IMF Strength</h3>

<p><span class="highlight">Larger charges produce stronger inter molecular attractions.</span></p>

<p>Inter molecular force strength increases with the magnitude of the charges (for example: +2 interacting with -2 is much stronger than +1 with -1). This is because larger charges create stronger attractions since the increased separation of positive and negative charges produces a more powerful electric force between molecules.</p>



<div class="imf-slider-wrap">
    <div class="imf-gauge">
        <div class="imf-gauge-labels">
            <span>a lot IMF</span>
            <span>some IMF</span>
            <span>no IMF</span>
        </div>
        <div class="imf-gauge-bar">
            <div id="imfGaugeFill" class="imf-gauge-fill"></div>
        </div>
    </div>

    <div class="imf-slider-panel">
        <div class="imf-atoms-row">
            <div id="a1Atom" class="imf-atom">Compound 1<span id="a1Charge" class="imf-charge-badge">δ+</span></div>
            <div class="imf-arrow">
                <div id="imfArrow" class="imf-arrow-symbol">→</div>
            </div>
            <div id="a2Atom" class="imf-atom">Compound 2<span id="a2Charge" class="imf-charge-badge">δ−</span></div>
        </div>

        <div class="imf-slider">
            <label for="chargeA1">Compound 1 charge</label>
            <input type="range" id="chargeA1" min="0" max="100" value="30">
            <div class="imf-scale"><span>smaller charge</span><span>larger charge</span></div>
        </div>

        <div class="imf-slider">
            <label for="chargeA2">Compound 2 charge</label>
            <input type="range" id="chargeA2" min="0" max="100" value="70">
            <div class="imf-scale"><span>smaller charge</span><span>larger charge</span></div>
        </div>

    </div>
</div>

<p>NaCl (salt), where Na⁺ has a +1 charge and Cl⁻ has a −1 charge. The charge difference is 2, compared to MgO (magnesium oxide), where Mg²⁺ has a +2 charge and O²⁻ has a −2 charge, giving a charge difference of 4. Because MgO has larger charges, its intermolecular forces are much stronger, resulting in a melting point of 2,852°C compared to NaCl's 801°C (more energy to separate MgO proving it has a stronger IMF when larger charges are present).</p>

<h3>B. Diameter Effect on Ionic Force Strength</h3>

<p><span class="highlight">Smaller ions produce stronger ionic forces because their charge is concentrated in a smaller space, making the attraction stronger.</span></p>

<p>When ions are smaller, their full charge is packed into a smaller area. This makes the positive and negative charges attract each other more strongly, like two magnets being pulled together—the closer they are, the stronger the force. As the ions grow larger, the charges are farther apart, and the attraction weakens.</p>

<div class="imf-slider-wrap">
    <div class="imf-gauge">
        <div class="imf-gauge-labels">
            <span>strong IMF</span>
            <span>moderate IMF</span>
            <span>weak IMF</span>
        </div>
        <div class="imf-gauge-bar">
            <div id="diameterIMFGauge" class="imf-gauge-fill"></div>
        </div>
    </div>

    <div class="imf-slider-panel">
        <div id="atomsContainer" style="display: flex; justify-content: center; align-items: center; gap: 100px; margin: 72px 0 16px 0; height: 120px;">
            <div id="atomA" class="imf-atom positive">A</div>
            <div id="atomB" class="imf-atom negative">B</div>
        </div>

        <div class="imf-slider">
            <label for="radiusA">Atom A radius</label>
            <input type="range" id="radiusA" min="20" max="80" value="60">
        </div>

        <div class="imf-slider">
            <label for="radiusB">Atom B radius</label>
            <input type="range" id="radiusB" min="20" max="80" value="60">
        </div>
    </div>
</div>

<p>Example: Na⁺ and Cl⁻ ions. Na⁺ is smaller than K⁺, so the attraction between Na⁺ and Cl⁻ is stronger than K⁺ and Cl⁻, producing a stronger ionic pull. Another example is Mg²⁺ and O²⁻ in MgO, where the small radii of both ions concentrate their charges, creating an extremely strong ionic bond.</p>

<script>
const atomA = document.getElementById("atomA");
const atomB = document.getElementById("atomB");
const radiusAInput = document.getElementById("radiusA");
const radiusBInput = document.getElementById("radiusB");
const atomsContainer = document.getElementById("atomsContainer");
const gauge = document.getElementById("diameterIMFGauge");

function updateAtoms() {
    const radiusA = parseInt(radiusAInput.value);
    const radiusB = parseInt(radiusBInput.value);

    // Set atom circle sizes
    atomA.style.width = radiusA + "px";
    atomA.style.height = radiusA + "px";
    atomA.style.fontSize = Math.max(radiusA/3, 12) + "px";

    atomB.style.width = radiusB + "px";
    atomB.style.height = radiusB + "px";
    atomB.style.fontSize = Math.max(radiusB/3, 12) + "px";

    // Calculate gap based on radii (smaller atoms = closer together)
    const maxGap = 100;
    const avgRadius = (radiusA + radiusB) / 2;
    const minAvgRadius = 20;
    const maxAvgRadius = 80;
    const gap = maxGap * ((avgRadius - minAvgRadius) / (maxAvgRadius - minAvgRadius));
    atomsContainer.style.gap = gap + "px";

    // Calculate IMF strength based on combined radii (smaller radii = stronger IMF)
    const maxRadius = 160; // 80 + 80 max
    const totalRadius = radiusA + radiusB;
    const imfPercent = ((maxRadius - totalRadius) / maxRadius) * 100;
    gauge.style.height = imfPercent + "%";
}

radiusAInput.addEventListener("input", updateAtoms);
radiusBInput.addEventListener("input", updateAtoms);

updateAtoms();
</script>

<h3>C. Ion Charge Effect on Ionic Force Strength</h3>

<p><span class="highlight"> Ions with larger charges attract each other more strongly because the electric pull between them increases as the amount of charge increases.</span></p>

<p>Changing the charge on an ion is like strengthening or weakening a magnet. A +3 ion and a −3 ion pull toward each other much harder than a +1 and −1 pair because more charge means more electrical attraction. Neutral atoms feel very little ionic force, while highly charged ions lock together tightly.</p>

<div class="imf-slider-wrap">

    <!-- FORCE GAUGE -->
    <div class="imf-gauge">
        <div class="imf-gauge-labels">
            <span>strong IMF</span>
            <span>moderate IMF</span>
            <span>weak IMF</span>
        </div>
        <div class="imf-gauge-bar">
            <div id="chargeIMFGauge" class="imf-gauge-fill"></div>
        </div>
    </div>

    <!-- ATOMS + CONTROLS -->
    <div class="imf-slider-panel">

        <div class="imf-atoms-row">
            <div class="atom-col">
                <div id="chargeSymbolA" class="charge-symbol">+1</div>
                <div id="chargeAtomA" class="imf-atom positive">A</div>
            </div>

            <div class="imf-arrow">
                <div class="imf-arrow-symbol">⇄</div>
                <div class="imf-arrow-label">Ionic Force</div>
            </div>

            <div class="atom-col">
                <div id="chargeSymbolB" class="charge-symbol">−1</div>
                <div id="chargeAtomB" class="imf-atom negative">B</div>
            </div>
        </div>

        <!-- CHARGE PICKERS -->
        <div class="charge-select-row">
            <div>
                <label>Atom A charge</label>
                <select id="chargeA">
                    <option>-3</option>
                    <option>-2</option>
                    <option>-1</option>
                    <option selected>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                </select>
            </div>

            <div>
                <label>Atom B charge</label>
                <select id="chargeB">
                    <option>-3</option>
                    <option>-2</option>
                    <option selected>-1</option>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                </select>
            </div>
        </div>

    </div>
</div>

<p>Example: Mg²⁺ and O²⁻ form a very strong ionic compound because both ions carry large charges. This attraction is much stronger than in Na⁺ and Cl⁻, where each ion only has a charge of one.</p>

<script>
const chargeSelectA = document.getElementById("chargeA");
const chargeSelectB = document.getElementById("chargeB");

const chargeAtomAEl = document.getElementById("chargeAtomA");
const chargeAtomBEl = document.getElementById("chargeAtomB");

const symbolA = document.getElementById("chargeSymbolA");
const symbolB = document.getElementById("chargeSymbolB");

const chargeGauge = document.getElementById("chargeIMFGauge");

function updateCharges() {
    const chargeA = parseInt(chargeSelectA.value);
    const chargeB = parseInt(chargeSelectB.value);

    // Update symbols above atoms
    symbolA.textContent = chargeA > 0 ? "+" + chargeA : chargeA;
    symbolB.textContent = chargeB > 0 ? "+" + chargeB : chargeB;

    // Color based on sign
    chargeAtomAEl.className = "imf-atom " + (chargeA > 0 ? "positive" : chargeA < 0 ? "negative" : "neutral");
    chargeAtomBEl.className = "imf-atom " + (chargeB > 0 ? "positive" : chargeB < 0 ? "negative" : "neutral");

    // Ionic force strength - only attractive if opposite signs
    let percent = 0;
    if ((chargeA > 0 && chargeB < 0) || (chargeA < 0 && chargeB > 0)) {
        // Opposite charges attract
        const force = Math.abs(chargeA * chargeB);
        const maxForce = 12; // 3 x 4
        percent = (force / maxForce) * 100;
    }
    // Same sign charges (both + or both -) = no attractive force

    chargeGauge.style.height = percent + "%";
}

chargeSelectA.addEventListener("change", updateCharges);
chargeSelectB.addEventListener("change", updateCharges);

updateCharges();
</script>

<h3>D. Electronegativity's Effect on Dipole Forces</h3>

<p><span class="highlight"> As electronegativity increases toward the top right of the periodic table, bonds become more polar and dipole forces grow stronger becasause the higher the electronegativity, the stronger the pull. Since weaker electronegative elements have a lower pull on electrons by definition, so when you have a highly electronegative element and a low electronegativity there will be a stromger bond becasue one pulls harder while the other accepts the pull more, as opposed to when the electronegativities are similar so the bond is weaker because neither element pulls with severe strnegth while the other lets it happen.</span></p>

<p>On the periodic table,  electronegativity increases as you move to the right across a period and as you move upward in a group. That means atoms in the upper-right corner pull hardest on shared electrons. Drag the dots below to different regions of the periodic table and watch how that changes polarity and dipole strength.</p>

<div class="imf-slider-wrap">

    <!-- FORCE GAUGE -->
    <div class="imf-gauge">
        <div class="imf-gauge-labels">
            <span>strong dipole</span>
            <span>moderate</span>
            <span>weak</span>
        </div>
        <div class="imf-gauge-bar">
            <div id="enIMFGauge" class="imf-gauge-fill"></div>
        </div>
    </div>

    <!-- VISUAL PANEL -->
    <div class="imf-slider-panel">

        <div class="imf-atoms-row en-row">

            <!-- ATOM A -->
            <div class="atom-col">
                <div id="deltaA" class="delta-symbol">δ+</div>
                <div id="enAtomA" class="imf-atom neutral">A</div>

                <div class="ptable">
                    <div class="ptable-blocks">
                        <div class="pt-block-1"></div>
                        <div class="pt-block-18"></div>
                        <div class="pt-period-2-3-left"></div>
                        <div class="pt-period-2-3-right"></div>
                        <div class="pt-period-4-7"></div>
                    </div>
                    <div class="en-trend-arrows en-arrow-right">EN increases →</div>
                    <div class="en-trend-arrows en-arrow-up">EN increases ↑</div>
                    <div id="dotA" class="ptable-dot"></div>
                </div>
                <div class="en-label">Periodic Table</div>
            </div>

            <!-- DIPOLE -->
            <div class="dipole-arrow-wrap">
                <div id="dipoleArrow" class="dipole-arrow">➝</div>
            </div>

            <!-- ATOM B -->
            <div class="atom-col">
                <div id="deltaB" class="delta-symbol">δ−</div>
                <div id="enAtomB" class="imf-atom neutral">B</div>

                <div class="ptable">
                    <div class="ptable-blocks">
                        <div class="pt-block-1"></div>
                        <div class="pt-block-18"></div>
                        <div class="pt-period-2-3-left"></div>
                        <div class="pt-period-2-3-right"></div>
                        <div class="pt-period-4-7"></div>
                    </div>
                    <div class="en-trend-arrows en-arrow-right">EN increases →</div>
                    <div class="en-trend-arrows en-arrow-up">EN increases ↑</div>
                    <div id="dotB" class="ptable-dot"></div>
                </div>
                <div class="en-label">Periodic Table</div>
            </div>

        </div>

    </div>
</div>

<p>Example: Fluorine sits at the top right of the periodic table so it has a extrenely high electronegativity, and in HF, H has extremely small electronegativity, so the bond is extremely strong because the flourine pulls very hard on hydrogen while the hydrogen accepts it.(Large difference in electronegativity means one pulls hard while the other gives up easily, leading to a strong dipole).</p>

<style>
/* MINI PERIODIC TABLE */
.ptable {
    width: 270px;
    height: 140px;
    position: relative;
    margin-top: 8px;
}

/* Periodic table structure using SVG-like divs for exact shape */
.ptable-grid {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: repeat(18, 15px);
    grid-template-rows: repeat(7, 20px);
    gap: 0;
}

/* Individual periodic table cells */
.ptable-cell {
    border: 1px solid #ddd;
    background: #f5f5f5;
}

/* Row 1: H and He */
.ptable-cell.r1c1 { grid-row: 1; grid-column: 1; background: #e3f2fd; }
.ptable-cell.r1c18 { grid-row: 1; grid-column: 18; background: #f3e5f5; }

/* Row 2-3: Groups 1-2 and 13-18 */
.ptable-cell.group-1-2 { background: #e3f2fd; }
.ptable-cell.group-13-18 { background: #fff3e0; }

/* Row 4-7: Transition metals */
.ptable-cell.transition { background: #fce4ec; }

/* Noble gases */
.ptable-cell.noble-gas { background: #f3e5f5; }

/* Periodic table background with characteristic shape */
.ptable::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #fff;
    border: 2px solid #444;
    border-radius: 8px;
    z-index: 0;
}

/* Create the periodic table blocks */
.ptable-blocks {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
}

/* Top row (Period 1) - H on left, He on far right */
.pt-block-1 {
    position: absolute;
    top: 2px;
    left: 2px;
    width: 15px;
    height: 18px;
    background: #ff6b6b;
    border: none;
}

.pt-block-18 {
    position: absolute;
    top: 2px;
    right: 2px;
    width: 15px;
    height: 18px;
    background: #ff6b6b;
    border: none;
}

/* Period 2-3: Left block (groups 1-2) and right block (groups 13-18) */
.pt-period-2-3-left {
    position: absolute;
    top: 20px;
    left: 2px;
    width: 32px;
    height: 40px;
    background: #ff6b6b;
    border: none;
}

.pt-period-2-3-right {
    position: absolute;
    top: 20px;
    right: 2px;
    width: 92px;
    height: 40px;
    background: #ff6b6b;
    border: none;
}

/* Period 4-7: Full width */
.pt-period-4-7 {
    position: absolute;
    top: 60px;
    left: 2px;
    right: 2px;
    bottom: 2px;
    background: #ff6b6b;
    border: none;
}

/* Periodic table label */
.ptable-label {
    position: absolute;
    top: -18px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 11px;
    font-weight: bold;
    color: #1f3a60;
    background: rgba(255,255,255,0.9);
    padding: 2px 8px;
    border-radius: 4px;
    z-index: 3;
    white-space: nowrap;
}

/* Electronegativity trend arrows */
.en-trend-arrows {
    position: absolute;
    font-size: 9px;
    font-weight: bold;
    color: #666;
    z-index: 3;
    background: rgba(255,255,255,0.85);
    padding: 2px 4px;
    border-radius: 3px;
}

.en-arrow-right {
    bottom: auto;
    left: -30px;
    top: 50%;
    transform: translateY(-50%);
    writing-mode: vertical-rl;
    text-orientation: mixed;
}

.en-arrow-up {
    top: 50%;
    right: auto;
    left: -30px;
    transform: translateY(-50%);
    writing-mode: vertical-rl;
    text-orientation: mixed;
}

/* draggable dot */
.ptable-dot {
    width: 16px;
    height: 16px;
    background: crimson;
    border: 2px solid #8b0000;
    border-radius: 50%;
    position: absolute;
    cursor: grab;
    z-index: 4;
    box-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.ptable-dot:active {
    cursor: grabbing;
}

/* Dipole arrow */
.dipole-arrow {
    font-size: 42px;
    transition: transform 0.4s ease;
}

.en-label {
    margin-top: 8px;
    margin-left: 8px;
    font-size: 14px;
    font-weight: bold;
    color: #1f3a60;
}

.delta-symbol {
    font-size: 24px;
    font-weight: bold;
    color: #1f3a60;
    min-height: 30px;
}

.dipole-arrow-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.en-row {
    margin-left: 0 !important;
}
</style>

<script>
const dotA = document.getElementById("dotA");
const dotB = document.getElementById("dotB");

const deltaA = document.getElementById("deltaA");
const deltaB = document.getElementById("deltaB");

const arrow = document.getElementById("dipoleArrow");
const enGauge = document.getElementById("enIMFGauge");

let enA = 2.0;
let enB = 3.5;

function enableDrag(dot, callback) {
    let dragging = false;

    dot.addEventListener("mousedown", () => dragging = true);
    document.addEventListener("mouseup", () => dragging = false);

    document.addEventListener("mousemove", e => {
        if (!dragging) return;

        const box = dot.parentElement.getBoundingClientRect();

        let x = e.clientX - box.left - 8; // center the dot
        let y = e.clientY - box.top - 8;

        // Constrain within periodic table boundaries (with margins)
        const margin = 5;
        const maxX = box.width - 20;
        const maxY = box.height - 20;
        
        x = Math.max(margin, Math.min(maxX, x));
        y = Math.max(margin, Math.min(maxY, y));

        dot.style.left = x + "px";
        dot.style.top = y + "px";

        callback(x / maxX, y / maxY);
    });
}

// convert position → EN trend
function calcEN(xFrac, yFrac) {
    // right = higher, up = higher
    const en = 0.7 + (xFrac * 2.5) + ((1 - yFrac) * 1.5);
    return Math.min(4.0, Math.max(0.7, en));
}

function updateSystem() {
    const diff = Math.abs(enA - enB);
    const percent = (diff / 3.5) * 100;
    enGauge.style.height = percent + "%";

    if (enA > enB) {
        arrow.style.transform = "rotate(180deg)";
        deltaA.textContent = "δ−";
        deltaB.textContent = "δ+";
    } else {
        arrow.style.transform = "rotate(0deg)";
        deltaA.textContent = "δ+";
        deltaB.textContent = "δ−";
    }

    const fade = diff < 0.25 ? 0.25 : 1;
    deltaA.style.opacity = fade;
    deltaB.style.opacity = fade;
}

// Activate dragging
enableDrag(dotA, (x,y)=>{ enA = calcEN(x,y); updateSystem(); });
enableDrag(dotB, (x,y)=>{ enB = calcEN(x,y); updateSystem(); });

// Start positions
dotA.style.left = "50px";
dotA.style.top = "60px";
dotB.style.left = "120px";
dotB.style.top = "20px";

updateSystem();
</script>

<h3>E. Electron Cloud Size & London Dispersion Forces</h3>

<p><span class="highlight">When you have a larger electron cloud you have more electrons on either side of the atom system. Since electrons in LDF compounds are free to roam around either atom becasue neither side has a strong enough side to completely control the electrons, when there are more electrons from the larger cloud, there will be more electrons on each given side at a moment. When there are more electrons on one side, the charges are stronger because electrons are the molecule that creates charge, so when there is more elctrons, each side will have stronger charges, resulting in a stronger LDF attraction between the atoms.</span></p>

<p>Electrons are not locked in place; they move constantly around the nucleus. In large atoms or molecules, there are more electrons so the electron cloud spreads out farther and becomes easier to shift. This makes temporary positive and negative regions form more often, letting nearby particles attract each other. Smaller clouds are tighter and harder to distort, so the forces are weaker.</p>

<div class="imf-slider-wrap">

    <!-- FORCE GAUGE -->
    <div class="imf-gauge">
        <div class="imf-gauge-labels">
            <span>strong dispersion</span>
            <span>moderate</span>
            <span>weak</span>
        </div>
        <div class="imf-gauge-bar">
            <div id="cloudIMFGauge" class="imf-gauge-fill"></div>
        </div>
    </div>

    <!-- VISUAL PANEL -->
    <div class="imf-slider-panel">

        <div class="cloud-row">

            <div class="cloud-atoms-container">
                <div class="cloud-col">
                    <div class="cloud-atom-wrap">
                        <div id="cloudA" class="electron-cloud"></div>
                        <div class="cloud-core">A</div>
                    </div>
                </div>

                <div class="cloud-col">
                    <div class="cloud-atom-wrap">
                        <div id="cloudB" class="electron-cloud"></div>
                        <div class="cloud-core">B</div>
                    </div>
                </div>
            </div>

            <div class="cloud-sliders-container">
                <div class="cloud-col">
                    <label>Electron cloud size</label>
                    <input type="range" id="cloudSizeA" min="40" max="220" value="70">
                </div>

                <div class="cloud-col">
                    <label>Electron cloud size</label>
                    <input type="range" id="cloudSizeB" min="40" max="220" value="70">
                </div>
            </div>

        </div>

    </div>
</div>

<p>Example: When you compare the LDF forces of I2 and F2, Iodine has much more electrons than flourine that orbit the atom. This causes more temporary and stronger temporary dipoles when the electrons shift from side to side becasue there are more charges involved when more electrons are present, so I2 has much stronger LDF forces that F2.</p>

<style>
/* CLOUD VISUALS */
.cloud-row {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.cloud-atoms-container {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    transition: gap 0.3s ease;
    gap: 220px;
}

.cloud-sliders-container {
    display: flex;
    align-items: center;
    justify-content: space-around;
    width: 100%;
    margin-top: 20px;
}

.cloud-col {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.cloud-atom-wrap {
    position: relative;
    width: 180px;
    height: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.cloud-core {
    width: 42px;
    height: 42px;
    background: #444;
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    z-index: 5;
}

/* fuzzy cloud */
.electron-cloud {
    position: absolute;
    border-radius: 50%;
    background: radial-gradient(circle,
        rgba(120,170,255,0.6),
        rgba(120,170,255,0.25),
        rgba(120,170,255,0.05));
    filter: blur(6px);
    transition: width 0.3s ease, height 0.3s ease;
}

/* force flicker */
.cloud-force-lines {
    width: 120px;
    height: 80px;
    background: repeating-linear-gradient(
        90deg,
        rgba(0,0,0,0.2),
        rgba(0,0,0,0.2) 6px,
        transparent 6px,
        transparent 12px);
    opacity: 0.2;
    transition: opacity 0.3s ease;
}

.cloud-force-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}
</style>

<script>
setTimeout(() => {
    const cloudA = document.getElementById("cloudA");
    const cloudB = document.getElementById("cloudB");

    const sizeA = document.getElementById("cloudSizeA");
    const sizeB = document.getElementById("cloudSizeB");

    const cloudGauge = document.getElementById("cloudIMFGauge");
    const atomsContainer = document.querySelector(".cloud-atoms-container");

    function updateClouds() {
        const a = parseInt(sizeA.value);
        const b = parseInt(sizeB.value);

        cloudA.style.width = a + "px";
        cloudA.style.height = a + "px";

        cloudB.style.width = b + "px";
        cloudB.style.height = b + "px";

        // bigger combined clouds → stronger dispersion
        // When both at minimum (40+40=80), no force. When at max (220+220=440), full force
        const minTotal = 80;
        const maxTotal = 440;
        const percent = ((a + b - minTotal) / (maxTotal - minTotal)) * 100;

        cloudGauge.style.height = Math.max(0, percent) + "%";
        
        // larger clouds = stronger forces = atoms get very close
        // max gap at smallest clouds, practically touching at largest clouds
        const maxGap = 220;
        const minGap = 10;
        const gap = maxGap - ((a + b - 80) / 360) * (maxGap - minGap);
        atomsContainer.style.gap = Math.max(minGap, Math.min(maxGap, gap)) + "px";
    }

    if (sizeA && sizeB && cloudA && cloudB && cloudGauge && atomsContainer) {
        sizeA.addEventListener("input", updateClouds);
        sizeB.addEventListener("input", updateClouds);
        updateClouds();
    }
}, 100);
</script></div>

<div class="section">
<h2>4. Hydrogen Bonding as a Special Dipole Force</h2>

<p><span class="highlight"> Hydrogen bonding is techinically a dipole-dipole interaction because in Hydrogen binding, you are bonding atoms with partial charges that do not fully steal electrons; however, hydrogen bonds are special because they occur when you bond Hydrogen(extremely small electronegativity) with either F, O, N, or Cl (extremely strong electronegativity), and since the two differ vastly in electronegativity, the dipole forces involved in hydrogen bonding are extremely strong.</span></p>

<h3>Why Hydrogen Bonding is Special</h3>

<p>Hydrogen bonding is special because it is a particular dipole when hydrogen (extremely weak) is bonded to the four most electronegative elements, causing ectreme electronegativity different and creating a particularly strong dipole bond.</p>

<div class="comparison">
    <div class="comparison-card">
        <h4>Regular Dipole-Dipole</h4>
        <p>δ+ and δ- charges are moderate in size because the electronegativity difference between bonded atoms is not very large.</p>
        <p><b>Example:</b> C-O they both have relatively similar electronegativities - not as strong of a dipole bond</p>
        <p><b>Strength:</b> Medium</p>
    </div>
    <div class="comparison-card">
        <h4>Hydrogen Bonding</h4>
        <p>δ+ on H and δ- on N, O, F, or Cl are VERY large due to vast electronegativity differences (F, O, N, Cl control the electrons easily so they are much more negative).</p>
        <p><b>Examples:</b> H₂O, NH₃, HF (Hydrogens electrons are pulled away strongly by F, O, N, or Cl)</p>
        <p><b>Strength:</b> Much stronger than regular dipoles</p>
    </div>
</div>

<h3>Visual Representation of Hydrogen Bonding</h3>

<svg width="100%" height="280" viewBox="0 0 640 280">
    <!-- Top-left water molecule -->
    <circle cx="100" cy="80" r="35" fill="#CC6644" stroke="#994422" stroke-width="2"/>
    <text x="93" y="90" fill="white" font-size="20" font-weight="bold">O</text>
    <circle cx="100" cy="45" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="94" y="53" fill="#333" font-size="14">H</text>
    <circle cx="100" cy="115" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="94" y="123" fill="#333" font-size="14">H</text>
    <!-- Partial charges -->
    <text x="95" y="95" fill="white" font-size="12">δ-</text>
    <text x="95" y="35" fill="#333" font-size="14">δ+</text>
    <text x="95" y="145" fill="#333" font-size="14">δ+</text>

    <!-- Bottom-left water molecule -->
    <circle cx="90" cy="220" r="35" fill="#CC6644" stroke="#994422" stroke-width="2"/>
    <text x="83" y="230" fill="white" font-size="20" font-weight="bold">O</text>
    <circle cx="90" cy="185" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="84" y="193" fill="#333" font-size="14">H</text>
    <circle cx="90" cy="255" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="84" y="263" fill="#333" font-size="14">H</text>
    <!-- Partial charges -->
    <text x="85" y="235" fill="white" font-size="12">δ-</text>
    <text x="85" y="175" fill="#333" font-size="14">δ+</text>
    <text x="85" y="278" fill="#333" font-size="14">δ+</text>

    <!-- Center water molecule -->
    <circle cx="300" cy="150" r="35" fill="#CC6644" stroke="#994422" stroke-width="2"/>
    <text x="293" y="160" fill="white" font-size="20" font-weight="bold">O</text>
    <circle cx="300" cy="115" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="294" y="123" fill="#333" font-size="14">H</text>
    <circle cx="300" cy="185" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="294" y="193" fill="#333" font-size="14">H</text>
    <!-- Partial charges -->
    <text x="295" y="165" fill="white" font-size="12">δ-</text>
    <text x="295" y="105" fill="#333" font-size="14">δ+</text>
    <text x="295" y="215" fill="#333" font-size="14">δ+</text>

    <!-- Top-right water molecule -->
    <circle cx="500" cy="80" r="35" fill="#CC6644" stroke="#994422" stroke-width="2"/>
    <text x="493" y="90" fill="white" font-size="20" font-weight="bold">O</text>
    <circle cx="500" cy="45" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="494" y="53" fill="#333" font-size="14">H</text>
    <circle cx="500" cy="115" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="494" y="123" fill="#333" font-size="14">H</text>
    <!-- Partial charges -->
    <text x="495" y="95" fill="white" font-size="12">δ-</text>
    <text x="495" y="35" fill="#333" font-size="14">δ+</text>
    <text x="495" y="145" fill="#333" font-size="14">δ+</text>

    <!-- Bottom-right water molecule -->
    <circle cx="510" cy="220" r="35" fill="#CC6644" stroke="#994422" stroke-width="2"/>
    <text x="503" y="230" fill="white" font-size="20" font-weight="bold">O</text>
    <circle cx="510" cy="185" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="504" y="193" fill="#333" font-size="14">H</text>
    <circle cx="510" cy="255" r="18" fill="#A3C1DA" stroke="#7799BB" stroke-width="1.5"/>
    <text x="504" y="263" fill="#333" font-size="14">H</text>
    <!-- Partial charges -->
    <text x="505" y="235" fill="white" font-size="12">δ-</text>
    <text x="505" y="175" fill="#333" font-size="14">δ+</text>
    <text x="505" y="278" fill="#333" font-size="14">δ+</text>

    <!-- Hydrogen bonds (dashed lines) - H to O center connections -->
    <line x1="100" y1="115" x2="300" y2="150" stroke="#333" stroke-width="2" stroke-dasharray="6,4"/>
    <line x1="90" y1="185" x2="300" y2="150" stroke="#333" stroke-width="2" stroke-dasharray="6,4"/>
    <line x1="300" y1="185" x2="510" y2="220" stroke="#333" stroke-width="2" stroke-dasharray="6,4"/>
    <line x1="500" y1="115" x2="300" y2="150" stroke="#333" stroke-width="2" stroke-dasharray="6,4"/>
</svg>

<div class="principle">
<p><b> </b> The dashed line shows a hydrogen bond: a δ+ hydrogen approaches a δ− oxygen on a neighboring molecule. The highly partial negative on the oxygen attracts the partial positive hydrogen, creating a strong dipole bond between molecules.</p>
</div>

</div>

<div class="section">
<h2>5. London Dispersion Forces and Electron Cloud Size</h2>

<p><span class="highlight">.</span></p>

<h3>Why Larger Molecules Have Stronger LDF</h3>

<p>When you have a larger electron cloud you have more electrons electrons in the system and therefore more electrons on either side of the atom system. Since electrons in LDF compounds are free to roam around either atom becasue neither side has a strong enough side to completely control the electrons, when there are more electrons from the larger cloud, there will be more electrons on each given side at a moment. When there are more electrons on one side, the charges are stronger because electrons are the molecule that creates charge, so when there is more elctrons, each side will have stronger charges, resulting in a stronger LDF attraction between the atoms.</p>

<h3>Comparison: Hydrocarbons with Increasing Size</h3>

<table>
<tr>
    <th>Molecule</th>
    <th>Formula</th>
    <th># of Electrons</th>
    <th>Electron Cloud Size</th>
    <th>LDF Strength</th>
    <th>State at Room Temp</th>
    <th>Boiling Point</th>
</tr>
<tr>
    <td>Propane</td>
    <td>C₃H₈</td>
    <td>26</td>
    <td>Small</td>
    <td>Weak</td>
    <td>Gas</td>
    <td>-42°C</td>
</tr>
<tr>
    <td>Octane</td>
    <td>C₈H₁₈</td>
    <td>74</td>
    <td>Medium</td>
    <td>Moderate</td>
    <td>Liquid</td>
    <td>126°C</td>
</tr>
<tr>
    <td>Wax (Octadecane)</td>
    <td>C₁₈H₃₈</td>
    <td>170</td>
    <td>Large</td>
    <td>Strong</td>
    <td>Solid</td>
    <td>316°C</td>
</tr>
</table>

<div class="principle">
<p><b>Explanation:</b> As shown above, it is clear that larger molecules that contain more electrons clearly have stronger London Dispersion Forces because the bliling boints are higher in the larger molecules with more electrons, meaning that the larger molecules require more energy to seperate, proving that larger molecules with more electrons have stronger LDF's.</p>
</div>

<h3> Visualizing London Dispersion Forces </h3>

<p>Watch as the electron cloud shifts between two atoms, shifting the side with less electrons to become positive, which then pulls the negatively charegd electrons back to it - this cycle repeats as each side shifts from negative to positive.</p>

<canvas id="ldfCanvas" width="700" height="400"></canvas>

<p><b>How it works:</b> As electrons shift to one side of an atom, that side becomes δ-  while the other side becomes δ+. This creates a temporary charge that cuases an opposite charge in the neighboring atom, resulting in an attractive force from the positive side and the electrons.</p>

</div>

<div class="section">
<h2>6. Physical States at Room Temperature</h2>

<p><span class="highlight"> Intermolecular forces determine whether a substance is a solid, liquid, or gas at room temperature based on the strength of the bond. Stronger bonds will hold teh atoms together stronger by definition, so they will require more energy to undo those bonds. This means that substances with stronger intermolecular forces are more likely to be solids at room temperature, while those with weaker forces tend to be gases, and those inbetween will be liquids at room temp.</span></p>

<h3>Connection Between IMF Strength and Physical State</h3>

<p>The strength of intermolecular forces determines how much energy (heat) is needed to separate molecules and convert a substance between states:</p>

<ul class="example-list">
    <li><b>Solids:</b> Very strong IMF - molecules are held tightly in fixed positions to to te stronger Bonds</li>
    <li><b>Liquids:</b> Moderate IMF - molecules are close together but can move freely due to moderate strength bonds</li>
    <li><b>Gases:</b> Weak IMF - molecules are far apart and move independently because of weak bonds</li>
</ul>

<table>
<tr>
    <th>Substance</th>
    <th>Main IMF</th>
    <th>IMF Strength</th>
    <th>Physical State</th>
    <th>Reason</th>
</tr>
<tr>
    <td>MgO</td>
    <td>Ionic</td>
    <td>Extremely Strong - Ionic bonds are extremely strong as explained earlier so it requires a lot of  energy(heat) to break them apart into a different state of matter.</td>
    <td>Solid</td>
    <td>Requires extreme heat (2,852°C) to melt</td>
</tr>
<tr>
    <td>Water (H₂O)</td>
    <td>Hydrogen Bonding</td>
    <td>Very Strong - Hydrogen bonds are strong intermolecular forces for the reasons explained earlier, so they require significant energy to break apart into a different state of matter. But they are weaker than ionic bonds, so in this case it is a liquid.</td>
    <td>Liquid</td>
    <td>Requires 100°C to boil</td>
</tr>
<tr>
    <td>Acetone (CH₃COCH₃)</td>
    <td>Dipole-Dipole</td>
    <td>Moderate - consistent partial charges creates moderately strong bonds, stronger than LDF but weaker than hydrogen bonding.</td>
    <td>Liquid</td>
    <td>Boils at 56°C</td>
</tr>
<tr>
    <td>Octane (C₈H₁₈)</td>
    <td>London Dispersion</td>
    <td>Moderate - Larger electron cloud than propane, resulting in stronger temporary charges, but still an LDF force which are weaker than hydrogen bonds and ionic bonds so it has a slightly weak bond, resulting in a liquid at room temp, but only requires slightly more enrgy to turn it to gas.</td>
    <td>Liquid</td>
    <td>LDF strong enough to be liquid</td>
</tr>
<tr>
    <td>Propane (C₃H₈)</td>
    <td>London Dispersion</td>
    <td>Weak - Small electron cloud resulting in weaker temporary charges compared to larger molecules, making the LDF forces weaker and making it extremely easy to break apart, resulting in a gas at room temp.</td>
    <td>Gas</td>
    <td>LDF too weak to hold liquid form</td>
</tr>
</table>

</div>

<div class="section">

<h2>7. How Intermolecular Forces Influence Solubility</h2>

<!-- ================= PART 1 ================= -->

<h3>Like Dissolves Like — Why Some Substances Mix and Others Don't</h3>

<p class="highlight">
<strong>Main Idea:</strong> Substances dissolve best when their molecules attract each other in similar ways. This is becasue when a solvent has the same type of intermolecular force, they can react with each other and pull each other apart, allowing them to mix. If they have different types of intermolecular forces, they won't interact well, so they won't dissolve in each other.
</p>



<p>
 Think of it like magnets: pieces that attract stick together, while pieces that don't… drift apart.
Molecules behave the same way.
</p>

<h4>⚡ Polarity Controls Solubility</h4>

<ul>
<li><b>Polar molecules</b> have slightly positive and negative ends.</li>
<li><b>Nonpolar molecules</b> share electrons evenly.</li>
</ul>

<p>
Because of this, polar molecules are strongly attracted to other polar molecules, while nonpolar molecules mainly interact with other nonpolar molecules.
</p>

<div class="comparison">

<div class="comparison-card">
<h4>Polar + Polar</h4>
<p>✅ Dissolves Well</p>
<p>Opposite partial charges attract and pull particles apart.</p>
<p><b>Example:</b> Sugar in water</p>
</div>

<div class="comparison-card">
<h4>Nonpolar + Polar</h4>
<p>❌ Does NOT Dissolve</p>
<p>Water molecules stick to each other instead of the nonpolar substance.</p>
<p><b>Example:</b> Oil in water</p>
</div>

<div class="comparison-card">
<h4>Polar + Nonpolar</h4>
<p>❌ Does NOT Dissolve</p>
<p>Nonpolar solvents cannot stabilize charged regions.</p>
<p><b>Example:</b> Salt in gasoline</p>
</div>

<div class="comparison-card">
<h4>Nonpolar + Nonpolar</h4>
<p>✅ Dissolves Well</p>
<p>Weak attractions match up and allow mixing.</p>
<p><b>Example:</b> Oil in gasoline</p>
</div>

</div>

<p class="principle">
<strong>Key Takeaway:</strong> Polar substances dissolve in polar solvents, nonpolar substances dissolve in nonpolar solvents — and nonpolar substances generally will not dissolve in water.
</p>

<hr>

<!-- ================= PART 2 ================= -->

<h3>💧 Why Some Ionic Compounds Dissolve in Water and Others Do Not (5)</h3>

<p class="highlight">
<strong>Big Idea:</strong> Water can pull ions apart — but only when its attractions to them are strong enough.
</p>

<p>
Water molecules act like tiny magnets because one end is slightly positive and the other is slightly negative.
When an ionic compound enters water, many water molecules surround each ion:
</p>

<ul>
<li>the oxygen end points toward positive ions</li>
<li>the hydrogen ends point toward negative ions</li>
</ul>

<p>
This helps separate the ions from the solid and keeps them floating freely in solution.
</p>

<div class="comparison">

<div class="comparison-card">
<h4>NaCl (Table Salt)</h4>
<p>Water strongly attracts both ions.</p>
<p>The ions spread into solution.</p>
<p><span style="color: green; font-weight: bold;">✓ Dissolves in Water</span></p>
</div>

<div class="comparison-card">
<h4>MgO (Magnesium Oxide)</h4>
<p>The ions attract each other extremely strongly.</p>
<p>Water struggles to pull them apart.</p>
<p><span style="color: red; font-weight: bold;">✗ Hardly Dissolves</span></p>
</div>

</div>

<div class="principle">
<p><strong>Why MgO Stays Solid:</strong></p>
<ul>
<li>The ions have larger charges.</li>
<li>They are packed very closely together.</li>
<li>The attraction between them is extremely strong.</li>
</ul>

<p>
Because of this, water molecules cannot easily separate the ions, so very little MgO enters solution.
</p>
</div>

</div>

</div>

<script>
// London Dispersion Forces Animation - stationary atoms, electrons orbit and switch sides
const canvas = document.getElementById('ldfCanvas');
const ctx = canvas.getContext('2d');

// Timing and global switch
const switchInterval = 4000; // full left->right->left cycle in 4 seconds
let lastSwitchTime = performance.now();
let globalChargeTarget = 0; // 0 -> left, 1 -> right
let globalBias = 0; // smoothly approaches globalChargeTarget to avoid jumps

// Atom positions (stationary) - moved slightly closer together
const baseLeft = 220;
const baseRight = 480;
const centerY = 180;

class Electron {
    constructor(index) {
        this.index = index;
        this.orbitRadius = 8 + Math.random() * 36;
        this.orbitAngle = Math.random() * Math.PI * 2;
        this.orbitSpeed = (Math.random() * 0.08 + 0.01) * (Math.random() < 0.5 ? 1 : -1);
        this.transition = Math.random() < 0.5 ? 0 : 1; // start side (0 left, 1 right)
        this.x = baseLeft;
        this.y = centerY;
        // static per-electron wobble so speed/behavior doesn't change unpredictably
        this.wobbleX = (Math.random() - 0.5) * 1.4;
        this.wobbleY = (Math.random() - 0.5) * 1.0;
    }

    update(atomPos, now) {
        this.orbitAngle += this.orbitSpeed;
        // Keep orbiting but make each electron's center oscillate continuously
        // between the two atoms while staying biased toward the global target.
        const desired = globalBias;
        const tsec = now * 0.001;

        // continuous base oscillation (0..1) - prevents electrons from freezing
        const baseOsc = 0.5 + 0.5 * Math.sin(tsec * 1.6 + this.index * 0.7);
        // bias toward the currently favored atom so the swarm favors one side
        const biasWeight = 0.55; // 0 = pure oscillation, 1 = stick to desired
        this.transition = baseOsc * (1 - biasWeight) + desired * biasWeight;
        this.transition = Math.max(0, Math.min(1, this.transition));

        // center between atoms based on transition
        let cx = atomPos.left.x * (1 - this.transition) + atomPos.right.x * this.transition;
        let cy = atomPos.left.y * (1 - this.transition) + atomPos.right.y * this.transition;

        // subtle group figure-eight motion (so swarm has coherent movement)
        const phase = tsec * 1.2 + this.index * 0.12;
        const A = 60, B = 22;
        const ox = Math.sin(phase) * A * 0.6;
        const oy = Math.sin(phase) * Math.cos(phase) * B * 0.6;
        cx += ox; cy += oy;

        // individual orbit and static wobble
        const orbitX = Math.cos(this.orbitAngle) * this.orbitRadius;
        const orbitY = Math.sin(this.orbitAngle) * (this.orbitRadius * 0.7);

        this.x = cx + orbitX + this.wobbleX;
        this.y = cy + orbitY + this.wobbleY;
    }

    draw(ctx) {
        ctx.fillStyle = '#4ecdc4';
        ctx.beginPath();
        ctx.arc(this.x, this.y, 3, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#0a9396';
        ctx.font = 'bold 6px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('e⁻', this.x, this.y);
    }
}

// init
const electrons = [];
for (let i = 0; i < 34; i++) electrons.push(new Electron(i));

function atomPositions() {
    return { left: { x: baseLeft, y: centerY }, right: { x: baseRight, y: centerY } };
}

function drawAtom(ctx, x, y, atomLabel) {
    const nucleusRadius = 14;
    ctx.fillStyle = '#ff6b6b';
    ctx.beginPath(); ctx.arc(x, y, nucleusRadius, 0, Math.PI * 2); ctx.fill();
    ctx.strokeStyle = '#c92a2a'; ctx.lineWidth = 2; ctx.stroke();
    ctx.fillStyle = 'white'; ctx.font = 'bold 12px Arial'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(atomLabel, x, y);
}

// legend removed - bottom-left legend is not displayed per user request

function countElectronsOnEachSide(atomPos, electrons) {
    let left = 0, right = 0; const midpoint = (atomPos.left.x + atomPos.right.x) / 2;
    electrons.forEach(e => { if (e.x < midpoint) left++; else right++; });
    return { atom1: left, atom2: right };
}

function drawCharges(ctx, atomPos, electronCounts) {
    const chargeY = Math.min(atomPos.left.y, atomPos.right.y) - 50;
    if (electronCounts.atom1 > electronCounts.atom2) {
        ctx.fillStyle = '#4ecdc4'; ctx.font = 'bold 20px Arial'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText('δ-', atomPos.left.x, chargeY);
        ctx.fillStyle = '#ff6b6b'; ctx.fillText('δ+', atomPos.right.x, chargeY);
    } else if (electronCounts.atom2 > electronCounts.atom1) {
        ctx.fillStyle = '#4ecdc4'; ctx.font = 'bold 20px Arial'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText('δ-', atomPos.right.x, chargeY);
        ctx.fillStyle = '#ff6b6b'; ctx.fillText('δ+', atomPos.left.x, chargeY);
    }
}

function animate() {
    const now = performance.now();
    // flip every 4s
    if (now - lastSwitchTime > switchInterval) {
        globalChargeTarget = 1 - globalChargeTarget;
        lastSwitchTime = now;
        // do NOT set electron.transition instantly - let electrons animate (lerp) to the new side
    }

    // Smoothly move a global bias toward the current charge target so
    // electrons don't jump when the target flips.
    const biasLerp = 0.01; // smaller = slower, smoother
    globalBias += (globalChargeTarget - globalBias) * biasLerp;

    const atomPos = atomPositions();
    electrons.forEach(e => e.update(atomPos, now));

    ctx.fillStyle = '#f8f9fa'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#333'; ctx.font = 'bold 16px Arial'; ctx.textAlign = 'center';
    ctx.fillText('London Dispersion Forces: Electrons Orbit and Shift (continuous group motion)', canvas.width / 2, 25);

    drawAtom(ctx, atomPos.left.x, atomPos.left.y, 'Cl');
    drawAtom(ctx, atomPos.right.x, atomPos.right.y, 'Cl');

    // legend intentionally not drawn

    electrons.forEach(e => e.draw(ctx));

    const counts = countElectronsOnEachSide(atomPos, electrons);
    drawCharges(ctx, atomPos, counts);

    // electron counts removed (visual removed per request)

    ctx.fillStyle = '#666'; ctx.font = '11px Arial'; ctx.textAlign = 'left';
    // bottom-left explanatory text removed per request

    requestAnimationFrame(animate);
}

animate();

// Charge slider -> IMF gauge
function setupImfSliders() {
    const a1 = document.getElementById('chargeA1');
    const a2 = document.getElementById('chargeA2');
    const fill = document.getElementById('imfGaugeFill');
    const arrow = document.getElementById('imfArrow');
    const a1Badge = document.getElementById('a1Charge');
    const a2Badge = document.getElementById('a2Charge');
    const a1Atom = document.getElementById('a1Atom');
    const a2Atom = document.getElementById('a2Atom');
    if (!a1 || !a2 || !fill || !arrow || !a1Badge || !a2Badge || !a1Atom || !a2Atom) return;

    const update = () => {
        const v1 = Number(a1.value);
        const v2 = Number(a2.value);
        const diff = Math.abs(v1 - v2);
        fill.style.height = `${diff}%`;
        
        // Scale arrow size based on IMF strength (diff from 0-100 maps to size 0-72px)
        const arrowSize = (diff / 100) * 72;
        arrow.style.fontSize = `${arrowSize}px`;

        a1Atom.classList.remove('positive', 'negative');
        a2Atom.classList.remove('positive', 'negative');

        if (v1 > v2) {
            arrow.textContent = '←';
            a1Badge.textContent = 'δ−';
            a2Badge.textContent = 'δ+';
            a1Atom.classList.add('negative');
            a2Atom.classList.add('positive');
        } else if (v2 > v1) {
            arrow.textContent = '→';
            a1Badge.textContent = 'δ+';
            a2Badge.textContent = 'δ−';
            a1Atom.classList.add('positive');
            a2Atom.classList.add('negative');
        } else {
            arrow.textContent = '↔';
            a1Badge.textContent = 'δ0';
            a2Badge.textContent = 'δ0';
            a1Atom.classList.add('positive');
            a2Atom.classList.add('positive');
        }
    };

    a1.addEventListener('input', update);
    a2.addEventListener('input', update);
    update();
}

setupImfSliders();
</script>

"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print(f"Open browser at: http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
