import os
import re

def add_accordion_script(directory):
    # JavaScript to handle accordion clicks
    accordion_script = '''
<script>
// Manual accordion handler for FAQ sections
document.addEventListener('DOMContentLoaded', function() {
    const accordionTitles = document.querySelectorAll('.service-faq .elementor-tab-title');
    
    accordionTitles.forEach(function(title) {
        title.addEventListener('click', function() {
            const contentId = this.getAttribute('aria-controls');
            const content = document.getElementById(contentId);
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            
            // Toggle aria-expanded
            this.setAttribute('aria-expanded', !isExpanded);
            
            // Toggle active class on parent item
            const item = this.closest('.elementor-accordion-item');
            if (item) {
                item.classList.toggle('elementor-active');
            }
            
            // Toggle content display
            if (content) {
                if (isExpanded) {
                    content.style.display = 'none';
                } else {
                    content.style.display = 'block';
                }
            }
        });
    });
});
</script>'''
    
    files_modified = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Only process files with service-faq
                if 'service-faq' in content and accordion_script not in content:
                    # Add script before closing </body> tag
                    new_content = content.replace('</body>', accordion_script + '\n</body>')
                    
                    if content != new_content:
                        print(f"Adding accordion script to {filepath}")
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        files_modified += 1
    
    print(f"Total files modified: {files_modified}")

if __name__ == "__main__":
    add_accordion_script("/Users/pranay/Files/10x Grow/vanguard/vanguardclinics/services")
