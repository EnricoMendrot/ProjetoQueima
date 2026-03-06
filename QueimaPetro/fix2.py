import os
import re

dirs = ['equipamentos/templates', 'operadores/templates', 'plataforma/templates']
files_to_fix = []
for d in dirs:
    if not os.path.exists(d): continue
    for root, _, files in os.walk(d):
        for file in files:
            if file.endswith('.html'):
                files_to_fix.append(os.path.join(root, file))

for path in files_to_fix:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    content = re.sub(
        r'</button>\s*</div>\s*</div>\s*</div>\s*{%\s*endif\s*%}',
        r'</button>\n          </div>\n        </div>\n      {% endif %}\n      </div>',
        content
    )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {path}")
