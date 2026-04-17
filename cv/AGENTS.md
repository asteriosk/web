# AGENTS.md — CV Generator Issues & Patterns

This document captures all known issues, fixes, and patterns discovered during CV generation. Review this **before** making changes to ensure issues are spotted automatically.

---

## 📋 Pre-Flight Checklist

**After any CV change, ALWAYS:**
1. Run `make pdf` and check for LaTeX errors
2. Generate PNG images of all pages: `for i in $(seq 0 N); do magick cv.pdf[$i] -density 200 /tmp/page$((i+1)).png; done`
3. **Visually inspect all pages** for:
   - Text overlapping (especially in nstabbing environments)
   - Extra vertical spacing between items
   - Font size inconsistencies
   - Label overflow in publications
   - Year formatting issues (e.g., "2016-2016" should be "2016")


---

## 🎯 When Making Changes

1. **Check AGENTS.md first** for known patterns
2. **Generate PDF** and look for errors
3. **Create page images** and visually inspect
4. **Compare** with original CV if available
5. **Update this file** with any new issues discovered
6. **Update this file** with the new architectural/file/tooling changes that were made. 

---

*Last updated: 2026-04-16*
