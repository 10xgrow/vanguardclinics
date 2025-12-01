import os
import re

# Configuration
ROOT_DIR = '/Users/pranay/Files/10x Grow/vanguard/vanguardclinics'
NEW_FOOTER_HTML = """<footer class="main-footer">
		<div class="footer-container">
			<div class="footer-brand">
                <img src="/wp-content/images/vanguard-logo.png" alt="Vanguard Clinic Logo" class="footer-logo">
				<p>Your trusted partner in health. Providing modern pharmacy solutions for the Georgetown community.</p>
			</div>
			<div class="footer-col">
				<h4>Quick Links</h4>
				<ul class="footer-links">
					<li><a href="/">Home</a></li>
					<li><a href="/about-us/">About Us</a></li>
					<li><a href="/services/">Services</a></li>
					<li><a href="/contact-us/">Contact</a></li>
				</ul>
			</div>
			<div class="footer-col">
				<h4>Services</h4>
				<ul class="footer-links">
					<li><a href="/services/">Prescriptions</a></li>
					<li><a href="/services/">Consultations</a></li>
					<li><a href="/services/">Vaccinations</a></li>
					<li><a href="/services/">Health Advice</a></li>
				</ul>
			</div>
			<div class="footer-col">
				<h4>Contact</h4>
				<ul class="footer-links">
					<li><a href="tel:289-344-1144">289-344-1144</a></li>
					<li><a href="mailto:info@vanguardrxclinics.ca">info@vanguardrxclinics.ca</a></li>
					<li>Vanguard Pharmacy & Clinics<br> 
					Unit 3, 400 Guelph St<br>
					Georgetown, Ontario L7G 0J2</li>
				</ul>
			</div>
		</div>
		<div class="footer-bottom">
			<p>&copy; <span id="copyright-year"></span> Vanguard Clinic. All rights reserved.</p>
		</div>
	</footer>"""

COPYRIGHT_SCRIPT = """
    <script>
        document.getElementById('copyright-year').textContent = new Date().getFullYear();
    </script>
"""

CSS_LINK = '<link rel="stylesheet" href="/redesign.css">'

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Add CSS if missing
    if 'redesign.css' not in content:
        if '</head>' in content:
            content = content.replace('</head>', f'    {CSS_LINK}\n</head>')
        else:
            print(f"Warning: No </head> tag in {filepath}")

    # 2. Replace Footer
    # Regex to match <footer ...> ... </footer>
    # We use dotall=True to match newlines
    footer_pattern = re.compile(r'<footer[^>]*>.*?</footer>', re.DOTALL | re.IGNORECASE)
    
    if footer_pattern.search(content):
        content = footer_pattern.sub(NEW_FOOTER_HTML, content)
    else:
        print(f"Warning: No <footer> tag found in {filepath}. Appending before </body>.")
        # If no footer, append before </body>
        if '</body>' in content:
            content = content.replace('</body>', f'{NEW_FOOTER_HTML}\n</body>')
        else:
             print(f"Error: No </body> tag in {filepath}")

    # 3. Add Copyright Script
    if 'id="copyright-year"' in content and 'document.getElementById(\'copyright-year\')' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{COPYRIGHT_SCRIPT}\n</body>')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")

def main():
    # Walk through directory
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                # Skip about-us/index.html as it is the source
                if 'about-us/index.html' in os.path.join(root, file):
                    continue
                
                filepath = os.path.join(root, file)
                try:
                    update_file(filepath)
                except Exception as e:
                    print(f"Failed to update {filepath}: {e}")

if __name__ == "__main__":
    main()
