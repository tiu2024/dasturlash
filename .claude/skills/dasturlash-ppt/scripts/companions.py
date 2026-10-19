"""Live-coding files for a lecture spec: livecode/starter, livecode/solution and a README.

These stay private (gitignored). After class, the teacher can give the solution files to
/practice-page as "the programs solved in class".
"""
from pathlib import Path


def livecode_files(spec: dict, root: Path):
    lc = spec.get("livecode") or {}
    written = []
    for f in lc.get("files") or []:
        name = f.get("name")
        if not name:
            continue
        for folder in ("starter", "solution"):
            content = f.get(folder, f.get("both"))
            if content is None:
                continue
            p = root / folder / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(str(content).rstrip("\n") + "\n", encoding="utf-8")
            written.append(p)

    meta = spec.get("meta", {})
    lines = [f"# Jonli kodlash: {meta.get('title', '')}", ""]
    lines += ["- `starter/` — jonli kodlash va mashq shu fayllardan boshlanadi.",
              "- `solution/` — darsdan keyingi tayyor variant.", ""]
    if lc.get("run"):
        lines += ["Ishga tushirish:", "", "```", str(lc["run"]), "```", ""]
    for sd in spec.get("slides", []):
        if sd.get("type") == "livecode":
            lines += [f"## Jonli kodlash: {sd.get('title', '')}", ""] + [f"- {g}" for g in sd.get("goals", [])] + [""]
        if sd.get("type") == "activity":
            lines += [f"## Mashq: {sd.get('title', '')}", ""] + \
                     [f"{i}. {s}" for i, s in enumerate(sd.get("steps", []), start=1)] + [""]
    root.mkdir(parents=True, exist_ok=True)
    readme = root / "README.md"
    readme.write_text("\n".join(lines), encoding="utf-8")
    written.append(readme)
    return written
