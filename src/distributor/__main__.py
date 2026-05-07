from typing import TypeVar

from terminaltexteffects.effects.effect_burn import Burn
from terminaltexteffects.engine.base_effect import BaseEffect


LOGO = """
             ▄▄▄█████▓ ██░ ██ ▓█████                                                                
             ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀                                                                
             ▒ ▓██░ ▒░▒██▀▀██░▒███                                                                  
             ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄                                                                
               ▒██▒ ░ ░▓█▒░██▓░▒████▒                                                               
               ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░                                                               
                 ░     ▒ ░▒░ ░ ░ ░  ░                                                               
               ░       ░  ░░ ░   ░                                                                  
                       ░  ░  ░   ░  ░                                                               
                                                                                                    
▓█████▄  ██▓  ██████ ▄▄▄█████▓ ██▀███   ██▓ ▄▄▄▄    █    ██ ▄▄▄█████▓ ▒█████   ██▀███  
▒██▀ ██▌▓██▒▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒▓█████▄  ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
░██   █▌▒██▒░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▒██▒ ▄██▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░▓█▄   ▌░██░  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██░▒██░█▀  ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒████▓ ░██░▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░██░░▓█  ▀█▓▒▒█████▓   ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░▓  ░▒▓███▀▒░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░ ▒ ░▒░▒   ░ ░░▒░ ░ ░     ░      ░ ▒ ▒░   ░▒ ░ ▒░
 ░ ░  ░  ▒ ░░  ░  ░    ░        ░░   ░  ▒ ░ ░    ░  ░░░ ░ ░   ░      ░ ░ ░ ▒    ░░   ░ 
   ░     ░        ░              ░      ░   ░         ░                  ░ ░     ░     
 ░                                               ░                                     
"""


EFFECT = TypeVar("EFFECT", bound="BaseEffect")


def splash(logotext: str, Animation: type[EFFECT], frame_rate=180) -> str:
    effect = Animation(logotext)
    effect.terminal_config.frame_rate = frame_rate
    last_frame = ""
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
            last_frame = frame
    return last_frame


def main():
    _ = splash(LOGO, Burn, 220)


if __name__ == "__main__":
    main()
