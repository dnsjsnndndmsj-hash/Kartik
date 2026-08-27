import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add placeholder inline chapters for Physics and Chemistry to prevent routing issues
physics_chapters = [
    ('ch1-physical', 'Physical World'),
    ('ch2-units', 'Units and Measurements'),
    ('ch3-motionstraight', 'Motion in a Straight Line'),
    ('ch4-motionplane', 'Motion in a Plane'),
    ('ch5-laws', 'Laws of Motion'),
    # ch6 is already there
    ('ch7-system', 'System of Particles and Rotational Motion'),
    ('ch8-gravitation', 'Gravitation'),
]

physics_html = ""
for ch_id, title in physics_chapters:
    physics_html += f"""
            <div id="physChapterGroup-{ch_id}" class="chapter-group" style="display:none;">
                <h2 class="section-title"><span class="chapter-card-badge" style="position:static; display:inline-block; margin-right:0.3rem;">Phys</span> {title}</h2>
                <div class="section-card">
                    <p style="text-align:center; padding: 4rem; color:var(--text-muted);">
                        <i class="fa-solid fa-person-digging fa-3x" style="margin-bottom:1rem;"></i><br>
                        This chapter is currently under construction. Please check back later.
                    </p>
                </div>
            </div>
    """

chem_chapters = [
    ('ch1-basic', 'Some Basic Concepts of Chemistry'),
    ('ch2-structure', 'Structure of Atom'),
    ('ch3-classification', 'Classification of Elements and Periodicity in Properties'),
    ('ch4-bonding', 'Chemical Bonding and Molecular Structure'),
    ('ch5-states', 'States of Matter'),
    ('ch6-thermodynamics', 'Thermodynamics'),
    ('ch7-equilibrium', 'Equilibrium'),
    ('ch8-redox', 'Redox Reactions'),
    ('ch9-hydrogen', 'Hydrogen'),
]

chem_html = ""
for ch_id, title in chem_chapters:
    chem_html += f"""
            <div id="chemChapterGroup-{ch_id}" class="chapter-group" style="display:none;">
                <h2 class="section-title"><span class="chapter-card-badge" style="position:static; display:inline-block; margin-right:0.3rem;">Chem</span> {title}</h2>
                <div class="section-card">
                    <p style="text-align:center; padding: 4rem; color:var(--text-muted);">
                        <i class="fa-solid fa-person-digging fa-3x" style="margin-bottom:1rem;"></i><br>
                        This chapter is currently under construction. Please check back later.
                    </p>
                </div>
            </div>
    """

# Insert physics
phys_insert = content.find('<div id="physChapterGroup-unitsdimensions"')
if phys_insert != -1:
    content = content[:phys_insert] + physics_html + content[phys_insert:]

# Insert chem
chem_insert = content.find('<div id="chemChapterGroup-moleconcept"')
if chem_insert != -1:
    content = content[:chem_insert] + chem_html + content[chem_insert:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
