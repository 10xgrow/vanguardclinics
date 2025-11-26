import os
import re

def fix_accordion_display(directory):
    # Pattern to match accordion content divs and add style="display: none;"
    # We're looking for: class="elementor-tab-content elementor-clearfix"
    # and adding: style="display: none;"
    pattern = re.compile(
        r'(<div[^>]*class="elementor-tab-content elementor-clearfix"[^>]*)(data-tab=)',
        re.DOTALL
    )
    
    def add_display_none(match):
        # Check if style attribute already exists
        if 'style=' in match.group(1):
            return match.group(0)  # Don't modify if style already exists
        # Add style="display: none;" before data-tab
        return match.group(1) + ' style="display: none;" ' + match.group(2)
    
    files_modified = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Only process files with accordion
                if 'elementor-accordion' in content:
                    new_content = pattern.sub(add_display_none, content)
                    
                    if content != new_content:
                        print(f"Fixing accordion display in {filepath}")
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        files_modified += 1
    
    print(f"Total files modified: {files_modified}")

if __name__ == "__main__":
    fix_accordion_display("/Users/pranay/Files/10x Grow/vanguard/vanguardclinics/services")
