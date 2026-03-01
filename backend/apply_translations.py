import os
from pathlib import Path

BACKEND_DIR = Path("c:/InsuranceProject/k-star-destiny/backend")
I18N_FILE = BACKEND_DIR / "saju_i18n.py"

replacements = [
    (
        '''"Your '{u_element}' and their '{i_element}' energy hitting each other is literally a chemical reaction — sparks are absolutely flying."''',
        '''"Your '{u_element}' mixed with their '{i_element}' is literally giving unmatched chemistry. The sparks? Absolutely flying. 💥"'''
    ),
    (
        '''"Your saju charts cancel out each other's weaknesses and MAX OUT synergy — luck literally opens when you two are together. That's the theory."''',
        '''"Your Saju charts literally cover each other's flaws and max out the synergy. You two together? A certified lucky duo. 🍀"'''
    ),
    (
        '''"Tu energía '{u_element}' y la de ellos '{i_element}' chocando es literalmente una reacción química — las chispas están volando pa' todos lados."''',
        '''"Tu '{u_element}' y su '{i_element}' juntos son pura química — literal están saltando chispas y sirviendo fuego. 🔥"'''
    ),
    (
        '''"Sus cartas de saju cancelan las debilidades del otro y MAXIMIZAN la sinergia — la suerte literalmente se abre cuando están juntos. Así es la teoría."''',
        '''"Sus cartas Saju se complementan perfecto y maximizan la sinergia. Juntos son el amuleto de la suerte definitivo, no hay debate. 💅"'''
    ),
    (
        '''"Sua energia '{u_element}' e a deles '{i_element}' se encontrando é literalmente uma reação química — as fagulhas tão voando pra todo lado."''',
        '''"A energia do seu '{u_element}' com a do(a) {idol} ('{i_element}') é uma química de milhões — o choque tá entregando tudo! ✨"'''
    ),
    (
        '''"Seus mapas de saju cancelam as fraquezas um do outro e MAXIMIZAM a sinergia — a sorte literalmente abre quando estão juntos. É a teoria."''',
        '''"Os mapas Saju de vocês se completam perfeitamente e zeram as fraquezas. Juntos, a sorte de vocês simplesmente destrava. Match de milhões! 💖"'''
    )
]

def apply_replacements():
    content = I18N_FILE.read_text(encoding="utf-8")
    
    success_count = 0
    for old_str, new_str in replacements:
        if old_str in content:
            content = content.replace(old_str, new_str)
            success_count += 1
            print(f"✅ Replaced: {old_str[:30]}...")
        else:
            print(f"❌ Not found: {old_str[:30]}...")
            
    if success_count > 0:
        I18N_FILE.write_text(content, encoding="utf-8")
        print(f"🎉 Successfully applied {success_count} replacements.")
    else:
        print("⚠️ No changes made.")

if __name__ == "__main__":
    apply_replacements()
