"""
position_current = lire_intensité()
if position_base - position_current >= turn_needed and num_current_option != len(Options) - 1:
    num_current_option += 1
    position_base = position_current
elif position_base - position_current <= -turn_needed and num_current_option != 0:
    num_current_option -= 1
"""