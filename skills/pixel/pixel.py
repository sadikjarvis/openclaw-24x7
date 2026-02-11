# pixel.py
class Pixel:
    name = "Pixel"
    description = "Generates text/ASCII diagrams or simple workflows"

    def run(self, prompt):
        # Simple example: convert text instructions into ASCII workflow
        lines = prompt.split("->")
        diagram = ""
        for i, step in enumerate(lines):
            step = step.strip()
            if i < len(lines) - 1:
                diagram += f"[{step}] --> "
            else:
                diagram += f"[{step}]"
        return diagram
