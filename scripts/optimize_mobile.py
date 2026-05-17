import os
import glob
import re

modules_dir = "/home/gabriel/Downloads/64Gram Desktop/CyberDuo/modules"

print("🚀 Starting Mobile Optimization Script for Module Index Pages...")

# 1. Optimize modulo-*.html files
for filepath in glob.glob(os.path.join(modules_dir, "modulo-*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # A. Make main container padding responsive
    # Matches 'padding: 0 2rem  1.5rem;' or 'padding: 0 2rem 1.5rem;'
    patt_padding = r"padding:\s*0\s+2rem\s+1\.5rem;"
    if re.search(patt_padding, content):
        content = re.sub(patt_padding, "padding: 0 clamp(1rem, 4vw, 2rem) 1.5rem;", content)
        modified = True

    # B. Make submodule item padding responsive
    patt_item_pad = r"padding:\s*1rem\s+1\.5rem;"
    if re.search(patt_item_pad, content):
        content = re.sub(patt_item_pad, "padding: 1rem clamp(1rem, 3vw, 1.5rem); -webkit-tap-highlight-color: transparent;", content)
        modified = True

    # C. Add active scale and tap feedback rules if not already present
    active_style = """
        .submodule-item:active {
            transform: scale(0.98);
            background: rgba(0, 255, 65, 0.05);
        }
    """
    if ".submodule-item:active" not in content:
        # Inject right before </style>
        content = content.replace("</style>", active_style + "\n    </style>")
        modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ Optimized: {os.path.basename(filepath)}")
    else:
        print(f"  ➖ No changes needed: {os.path.basename(filepath)}")

# 2. Optimize blackbox.html
blackbox_path = os.path.join(modules_dir, "blackbox.html")
if os.path.exists(blackbox_path):
    with open(blackbox_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # A. Responsive padding for main-container
    if "padding: 0 1.5rem 5rem;" in content:
        content = content.replace("padding: 0 1.5rem 5rem;", "padding: 0 clamp(1rem, 4vw, 1.5rem) 5rem;")
        modified = True

    # B. Responsive columns for resource-grid
    if "minmax(320px, 1fr)" in content:
        content = content.replace("minmax(320px, 1fr)", "minmax(260px, 1fr)")
        modified = True

    # C. Webkit tap color and active state for resource links
    if ".resource-link {" in content and "-webkit-tap-highlight-color" not in content:
        # Add tap highlight color
        content = content.replace(
            "border: 1px solid transparent;",
            "border: 1px solid transparent;\n            -webkit-tap-highlight-color: transparent;"
        )
        modified = True

    if ".resource-link:active" not in content:
        active_link_style = """
        .resource-link:active {
            transform: scale(0.98);
            background: rgba(255, 255, 255, 0.08);
        }
        """
        content = content.replace("</style>", active_link_style + "\n    </style>")
        modified = True

    if modified:
        with open(blackbox_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  ✅ Optimized: blackbox.html")

print("🎉 Mobile optimization complete!")
