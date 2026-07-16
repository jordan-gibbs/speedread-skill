# Dependency Audit: acme-web

**Verdict: ship it, with two upgrades first.** Of **214 dependencies**, 209 are healthy, 3 have available patches, and **2 carry known vulnerabilities** you should fix this week.

## Top findings

1. **`image-resize@2.1.0`** has a path-traversal advisory (**CVE-2026-1337**, high). Patched in `2.1.4` — a drop-in upgrade.
2. **`yaml-parse@1.x`** is unmaintained since 2024. Migrate to `yaml-parse-ng`; the API is 95% compatible.
3. Your lockfile pins **14 packages** more than two majors behind. None are urgent, but the gap grows monthly.

## The upgrade path

The two urgent fixes are independent and low-risk:

```bash
npm install image-resize@2.1.4
npm install yaml-parse-ng@3
```

## By the numbers

| Category | Count |
| --- | --- |
| Total dependencies | 214 |
| Healthy | 209 |
| Patchable advisories | 3 |
| Known vulnerabilities | 2 |

> Numbers as of the last lockfile commit. Re-run the audit after upgrading.

---

That's the whole report. Press **R** to reread it, or **D** to see the document view.
