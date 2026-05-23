"""
fix_svg_classes.py  (v2)
========================
Converts CSS class-based styles in SVG files to inline attributes so that
SharpVectors (used by the WPF host) can render them correctly.

SharpVectors does not reliably parse <defs><style> CSS class rules, so
elements styled only via class="..." appear invisible. This script inlines
the styles directly onto each element.
"""

import os
import re

SVG_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "Freexcel.App.Host", "Resources", "CommandIconsSvg")

# ── Class → CSS property map ─────────────────────────────────────────────────
CLASS_MAP = {
    # Stroke / outline classes (fill:none, stroke:color)
    "s":          {"fill": "none", "stroke": "#242424", "stroke-width": "1.0", "stroke-linecap": "round", "stroke-linejoin": "round"},
    "r":          {"fill": "none", "stroke": "#242424", "stroke-width": "1.0", "stroke-linecap": "round", "stroke-linejoin": "round"},
    "line":       {"fill": "none", "stroke": "#242424", "stroke-width": "1.0", "stroke-linecap": "round", "stroke-linejoin": "round"},
    "thin":       {"fill": "none", "stroke": "#242424", "stroke-width": "1.0", "stroke-linecap": "round", "stroke-linejoin": "round"},
    "heavy":      {"fill": "none", "stroke": "#242424", "stroke-width": "1.0", "stroke-linecap": "round", "stroke-linejoin": "round"},
    "greenLine":  {"fill": "none", "stroke": "#107c41", "stroke-width": "1.0", "stroke-linecap": "round", "stroke-linejoin": "round"},
    "blueLine":   {"fill": "none", "stroke": "#0078d4", "stroke-width": "1.0", "stroke-linecap": "round", "stroke-linejoin": "round"},
    "grid":       {"fill": "none", "stroke": "#5c5c5c", "stroke-width": "1.0", "stroke-linecap": "square"},

    # Fill-only classes
    "g":          {"fill": "#107c41"},
    "green":      {"fill": "#107c41"},
    "g2":         {"fill": "#dff6dd"},
    "palegreen":  {"fill": "#dff6dd"},
    "green2":     {"fill": "#dff6dd"},
    "b":          {"fill": "#0078d4"},
    "blue":       {"fill": "#0078d4"},
    "o":          {"fill": "#f7630c"},
    "orange":     {"fill": "#f7630c"},
    "y":          {"fill": "#ffb900"},
    "yellow":     {"fill": "#ffb900"},
    "paleyellow": {"fill": "#ffb900"},
    "rd":         {"fill": "#d32f2f"},
    "red":        {"fill": "#d32f2f"},
    "p":          {"fill": "#8b5cf6"},
    "purple":     {"fill": "#8b5cf6"},
    "w":          {"fill": "#ffffff"},
    "paper":      {"fill": "#ffffff"},
    "bg":         {"fill": "#ffffff"},
    "k":          {"fill": "#242424"},
    "gray":       {"fill": "#242424"},
    "f":          {"fill": "#f3f2f1"},
    "soft":       {"fill": "#f3f2f1"},
    "paleblue":   {"fill": "#dcecff"},
    "palered":    {"fill": "#ffd7d7"},
    "none":       {"fill": "none"},

    # Text / font classes
    "t":    {"fill": "#242424", "font-family": "Segoe UI,Arial,sans-serif",
             "font-weight": "700", "text-anchor": "middle", "dominant-baseline": "central"},
    "txtb": {"fill": "#242424", "font-family": "Segoe UI,Arial,sans-serif",
             "font-weight": "700", "text-anchor": "middle", "dominant-baseline": "central"},
    "tm":   {"fill": "#242424", "font-family": "Segoe UI,Arial,sans-serif",
             "font-weight": "600", "text-anchor": "middle", "dominant-baseline": "central"},
    "txt":  {"fill": "#242424", "font-family": "Segoe UI,Arial,sans-serif",
             "font-weight": "600", "text-anchor": "middle", "dominant-baseline": "central"},
}


def resolve_classes(class_str: str) -> dict:
    """Merge class properties in order; later class wins for the same property."""
    resolved = {}
    for cls in class_str.split():
        if cls in CLASS_MAP:
            resolved.update(CLASS_MAP[cls])
    return resolved


def attr_value(tag: str, attr: str) -> str | None:
    """Return the value of an XML attribute already present on the tag, or None."""
    m = re.search(r'\b' + re.escape(attr) + r'\s*=\s*["\']([^"\']*)["\']', tag)
    return m.group(1) if m else None


def remove_attr(tag: str, attr: str) -> str:
    """Remove an attribute (name="value" or name='value') from a tag string."""
    return re.sub(r'\s*\b' + re.escape(attr) + r'\s*=\s*(?:"[^"]*"|\'[^\']*\')', '', tag)


def add_attrs(tag: str, props: dict) -> str:
    """
    Inject missing presentation attributes into an SVG open tag.
    Existing explicit attributes on the element are preserved; class-derived
    ones are added only if the attribute isn't already present.
    """
    inject = {k: v for k, v in props.items() if attr_value(tag, k) is None}
    if not inject:
        return tag

    attrs_str = " ".join(f'{k}="{v}"' for k, v in inject.items())
    # Insert before the closing > or />
    tag = re.sub(r'(\s*/>|>)\s*$', f' {attrs_str}\\1', tag.rstrip(), count=1)
    return tag


# ── Element-level transformer ─────────────────────────────────────────────────

OPEN_TAG_RE = re.compile(
    r'(<(?:path|circle|ellipse|rect|line|polyline|polygon|text|tspan|use|g|svg)\b[^>]*?/>|'
    r'<(?:path|circle|ellipse|rect|line|polyline|polygon|text|tspan|use|g|svg)\b[^>]*?>)',
    re.DOTALL
)


def transform_element(tag: str) -> str:
    class_val = attr_value(tag, "class")
    if not class_val:
        return tag

    resolved = resolve_classes(class_val)
    if not resolved:
        # Unknown class(es) only — remove the class attr but add nothing
        # (leaving unknown classes causes SharpVectors warnings)
        tag = remove_attr(tag, "class")
        return tag

    tag = remove_attr(tag, "class")
    tag = add_attrs(tag, resolved)
    return tag


def process_svg(content: str) -> str:
    # Remove the <defs>…</defs> block if it only contained a <style> element
    def strip_style_defs(m):
        inner = m.group(1)
        stripped = re.sub(r'\s*<style[^>]*>.*?</style>\s*', '', inner, flags=re.DOTALL).strip()
        if not stripped:
            return ''
        cleaned = re.sub(r'\s*<style[^>]*>.*?</style>', '', inner, flags=re.DOTALL)
        return f'<defs>{cleaned}</defs>'

    content = re.sub(r'<defs>(.*?)</defs>', strip_style_defs, content, flags=re.DOTALL)

    # Transform each open element tag that has a class attribute
    content = OPEN_TAG_RE.sub(lambda m: transform_element(m.group(0)), content)
    return content


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    svg_dir = os.path.abspath(SVG_DIR)
    files = [f for f in os.listdir(svg_dir) if f.endswith('.svg')]

    fixed = 0
    skipped = 0
    errors = []

    for filename in sorted(files):
        path = os.path.join(svg_dir, filename)
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                original = fh.read()
        except Exception as e:
            errors.append(f"READ  {filename}: {e}")
            continue

        if 'class=' not in original:
            skipped += 1
            continue

        transformed = process_svg(original)

        if transformed == original:
            skipped += 1
            continue

        try:
            with open(path, 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(transformed)
            fixed += 1
        except Exception as e:
            errors.append(f"WRITE {filename}: {e}")

    print(f"Fixed : {fixed}")
    print(f"Skipped (no change needed): {skipped}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
    else:
        print("No errors.")


if __name__ == "__main__":
    main()
