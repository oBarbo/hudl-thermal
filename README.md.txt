# Hudl Thermal Control — QA Deliverables

This repository contains the QA deliverables for the Embedded Thermal Control System:
- Quality & Validation Strategy (Word doc)
- System diagram
- Python validation scripts:
  - `tests/validate_tacho_vs_pwm.py`
  - `tests/tacho_validation_with_logging.py`
- GitHub Actions workflow: `.github/workflows/firmware_pipeline.yml`
- Traceability matrix: `Traceability_Matrix_Thermal_Control.csv`

## How to run tests locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r tests/requirements.txt
python tests/tacho_validation_with_logging.py
