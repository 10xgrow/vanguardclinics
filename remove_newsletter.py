import os
import re

def remove_newsletter_section(directory):
    # Pattern to match the newsletter column containing "Stay up to date"
    # This matches the entire column div that contains the newsletter text and button
    pattern = re.compile(
        r'<div class="elementor-column elementor-col-50 elementor-inner-column elementor-element elementor-element-16d4818"[^>]*>.*?'
        r'Stay up to date with.*?'
        r'</div>\s*</div>\s*</div>',
        re.DOTALL
    )
    
    files_modified = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = pattern.sub('', content)
                
                if content != new_content:
                    print(f"Removing newsletter section from {filepath}")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    files_modified += 1
    
    print(f"Total files modified: {files_modified}")

if __name__ == "__main__":
    remove_newsletter_section("/Users/pranay/Files/10x Grow/vanguard/vanguardclinics")
