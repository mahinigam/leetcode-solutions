import os, re, urllib.parse

ROOT = os.getcwd()
LANG = {"py": "Python", "java": "Java", "cpp": "C++", "c": "C", "js": "JavaScript",
        "ts": "TypeScript", "cs": "C#", "go": "Go", "rs": "Rust", "kt": "Kotlin",
        "swift": "Swift", "sql": "SQL", "rb": "Ruby", "scala": "Scala", "php": "PHP", "dart": "Dart"}
SKIP = {"readme.md", "notes.md"}

problems = {}

def add(slug, num, path, ext):
    p = problems.setdefault(slug, {"num": None, "files": {}})
    if num and not p["num"]:
        p["num"] = num
    p["files"][ext] = path

for entry in sorted(os.listdir(ROOT)):
    full = os.path.join(ROOT, entry)
    if not os.path.isdir(full) or entry.startswith("."):
        continue
    m = re.match(r"^(\d+)-(.+)$", entry)
    if m:  # LeetHub layout: 0001-two-sum/two-sum.py
        num, slug = int(m.group(1)), m.group(2)
        for f in sorted(os.listdir(full)):
            if f.lower() in SKIP or "." not in f:
                continue
            ext = f.rsplit(".", 1)[-1].lower()
            if ext in LANG:
                add(slug, num, f"{entry}/{f}", ext)
    elif entry == "old-submissions":  # exported layout: two-sum.py
        for f in sorted(os.listdir(full)):
            if "." not in f:
                continue
            slug, ext = f.rsplit(".", 1)
            ext = ext.lower()
            if ext in LANG:
                add(slug, None, f"{entry}/{f}", ext)

def sort_key(item):
    slug, p = item
    return (p["num"] is None, p["num"] or 0, slug)

rows = []
for slug, p in sorted(problems.items(), key=sort_key):
    title = slug.replace("-", " ").title()
    num = p["num"] if p["num"] else "-"
    links = ", ".join(f"[{LANG[e]}]({urllib.parse.quote(path)})" for e, path in sorted(p["files"].items()))
    rows.append(f"| {num} | [{title}](https://leetcode.com/problems/{slug}/) | {links} |")

out = ["# LeetCode Solutions", "",
       f"**{len(problems)} problems solved.** This README updates automatically.", "",
       "| # | Problem | Solutions |", "|---|---------|-----------|"] + rows
with open("README.md", "w") as fh:
    fh.write("\n".join(out) + "\n")
print("README generated with", len(problems), "problems")
