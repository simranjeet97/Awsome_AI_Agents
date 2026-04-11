import pathlib
import re

def load_skill_instructions(skill_dir: pathlib.Path) -> str:
    """
    Manually load instructions from a SKILL.md file.
    Parses the file and returns everything after the YAML frontmatter.
    """
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        raise FileNotFoundError(f"Skill file not found: {skill_file}")
    
    content = skill_file.read_text()
    
    # Remove YAML frontmatter if present
    # Matches --- [metadata] ---
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    
    if match:
        instructions = content[match.end():].strip()
    else:
        instructions = content.strip()
        
    return instructions
