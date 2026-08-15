# Unison Hardware

System hardware architecture, stable interfaces, BOM data, open design sources,
and qualification plans for incremental Unison systems and the target 2027/2028
generation.

This repository begins with requirements and interfaces, not premature part
selection. No design here is certified for mains power, medical use, life
safety, RF compliance, fabrication, or installation unless a revision-specific
qualification record explicitly says so.

Hardware licensing is not yet selected. See `LICENSE-STATUS.md` before copying,
fabricating, or redistributing design material.

Run `python scripts/validate.py` before proposing interface or BOM changes. CI
runs the same structural validation; engineering qualification remains a
separate evidence requirement.

The current concept package includes modular blade interfaces, budgetary BOM
history, power and thermal envelopes, enclosure requirements, open design-source
conventions, and an executable deferred qualification plan. After the interim
workstation is installed, begin with `python scripts/collect_gpu_baseline.py
--output evidence/gpu-baseline.json`. Load and resilience qualification commands
fail closed until named fixtures and measurement adapters are configured.
