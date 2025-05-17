```python
import os
import argparse

TEMPLATES = {
    "basic_webapp": [
        "src/",
        "public/css/",
        "public/js/",
        "tests/",
        "docs/",
        ".gitignore",
        "README.md"
    ]
}

def generate_structure(output_dir, template):
    for item in TEMPLATES.get(template, []):
        path = os.path.join(output_dir, item)
        
        if item.endswith('/'):
            os.makedirs(path, exist_ok=True)
            print(f"📁 Created directory: {path}")
        else:
            with open(path, 'w') as f:
                f.write("# Auto-generated file")
            print(f"📄 Created file: {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate project structure')
    parser.add_argument('--dir', default='new_project', help='Output directory')
    parser.add_argument('--template', default='basic_webapp', 
                      choices=TEMPLATES.keys(), help='Template name')
    args = parser.parse_args()
    
    generate_structure(args.dir, args.template)
```

---
