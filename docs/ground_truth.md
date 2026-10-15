
# LinkWatch Dependency Ground Truth

**Method:** Manually inspected LinkWatch dependency files and PyPI package pages.  
**Date checked:** 15 October 2026

| Package | LinkWatch requirement | Latest version observed | Latest release date | Python 3.12 / 3.13 support | Maintenance evidence / notes |
|---|---|---|---|---|---|
| `requests` | `==2.31.0` | `2.34.2` | 15 May 2026 | Yes / Yes | PyPI lists Python 3.12 and 3.13. Deprecation status not checked. |
| `idna` | `==2.7` | `3.20` | 17 September 2026 | Yes / Yes | PyPI classifies the project as Production/Stable. Upgrade compatibility still needs testing. |
| `click` | `>=7` | `8.5.0` | 26 August 2026 | Yes / Yes | Latest observed version requires Python >=3.10. Minimum version specified, not an exact pin. |
| `chardet` | `==5.2.0` | `7.6.0` | 14 August 2026 | Yes / Yes | Newer release observed. Test compatibility before upgrading. |
| `setuptools` | `==75.8.0` in dependencies; `>=61` in build-system requirements | `84.0.0` | 8 August 2026 | Yes / Yes | Different version constraints in the same project. Latest observed version requires Python >=3.10. |
| `rich` | No version specified | `15.0.0` | 12 April 2026 | Yes / Yes | PyPI lists Python 3.12 and 3.13. Unpinned dependency. |


