from textual.app import App, ComposeResult
from textualeffects.widgets import EffectLabel

class BurnApp(App):
    def compose(self) -> ComposeResult:
        # Use the Burn effect with custom terminal configuration
        # textualeffects usually maps these to the TTE TerminalConfig
        yield EffectLabel(
            "FLAME ON!", 
            effect="Burn", 
            config={
                "terminal_config": {
                    "frame_rate": 220
                }
            }
        )

if __name__ == "__main__":
    BurnApp().run()

