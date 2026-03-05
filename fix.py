with open("C:/Users/abhin/Downloads/abhinaba webpage/abhinaba_crystalline.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_p = '                    <p>18, retro, puts logic first. <span style="font-family: \'Dancing Script\', cursive; font-size: 1.5rem; font-weight: 400; opacity: 0.9; display: block; margin-top: 10px; color: var(--accent-cyan);">Slide in... one taste and you\'ll beg me to stay forever.</span></p>\n'

lines[560:561] = [new_p]

with open("C:/Users/abhin/Downloads/abhinaba webpage/abhinaba_crystalline.html", "w", encoding="utf-8") as f:
    f.writelines(lines)
