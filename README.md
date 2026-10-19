# Dasturlash 1, 2

MkDocs (Material) asosidagi kurs sayti. Ma'ruza materiallari `docs/` papkasida.

## Ishga tushirish (Windows PowerShell)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

Brauzerda http://127.0.0.1:8000 manzilini oching.

## Tuzilma

| Yo'l | Vazifasi |
|---|---|
| `mkdocs.yml` | Sayt sozlamalari va navigatsiya |
| `docs/courses/dasturlash/week-NN/` | Haftalik sahifalar |
| `docs/downloads/dasturlash/week-NN/` | Yuklab olinadigan fayllar |
| `Lectures/` | Asl PPTX ma'ruzalar |
| `Lectures/config.yaml` | Kurs sozlamalari: o'qituvchi, universitet, guruh, o'quv yili, slayd uslubi |
| `Lectures/src/week-NN/` | Taqdimot manbasi (`lecture.yaml`); kitob parchalari va yechimlar git'ga kirmaydi |
| `.claude/skills/` | Claude Code ko'nikmalari (sahifa yaratish, tekshirish, nashr qilish) |

`docs/` ichidagi hamma narsa ommaga ochiq bo'lishi mumkin. E'lon qilinmagan yechimlarni `docs/` dan tashqarida saqlang.

## Tekshirish

```powershell
.\.venv\Scripts\python.exe -m mkdocs build --strict
```
