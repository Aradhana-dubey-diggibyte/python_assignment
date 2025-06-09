def generate_hacker_rank_logo(thickness: int) -> str:
    # The letter "H" logo with the given thickness
    c = 'H'

    # Top Cone
    logo_lines = []
    for i in range(thickness):
        line = (c * (2 * i + 1)).center(thickness * 2 - 1)
        logo_lines.append(line)

    # Top Pillars
    for i in range(thickness + 1):
        line = (c * thickness).ljust(thickness * 2) + (c * thickness).rjust(thickness * 6)
        logo_lines.append(line)

    # Middle Belt
    for i in range((thickness + 1) // 2):
        line = (c * thickness * 5).center(thickness * 6)
        logo_lines.append(line)

    # Bottom Pillars
    for i in range(thickness + 1):
        line = (c * thickness).ljust(thickness * 2) + (c * thickness).rjust(thickness * 6)
        logo_lines.append(line)

    # Bottom Cone
    for i in range(thickness):
        line = ((c * (thickness * 2 - 1 - 2 * i)).rjust(thickness * 2) ).rjust(thickness * 6)
        logo_lines.append(line)

    return '\n'.join(logo_lines)
