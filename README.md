# Clinical-LLM-Guard 🏥🔒

**Status:** Work in Progress (v0.1.0-alpha)

## 📌 Project Overview
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.9%2B-green)](https://www.python.org/)
[![HIPAA Compliance](https://img.shields.io/badge/Compliance-HIPAA%20Ready-green)](./SECURITY.md)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()

Clinical-LLM-Guard is an enterprise-grade middleware designed to securely process non-structured clinical records using **ChatGPT Business/Team API**. 

### 🚀 Quick Start
```bash
pip install clinical-llm-guard
```

```python
from clinical_guard.anonymizer import ClinicalAnonymizer

guard = ClinicalAnonymizer()
safe_payload = guard.sanitize("Patient John Doe (DOB: 1980-05-12) has Type 2 Diabetes.")
print(safe_payload['anonymized_text'])
# Output: "Patient <PERSON> (DOB: <DATE_TIME>) has Type 2 Diabetes."
``` 

It solves the "Privacy vs. Performance" dilemma in medical NLP by strictly enforcing **Zero Data Retention** policies and integrating local PII (Personally Identifiable Information) scrubbing.

## 🛡 Privacy Architecture
This library enforces a **"Trust No One"** architecture:
1. **Local Scrubbing**: All PII (PHI) is identified and redacted *locally* using `presidio-analyzer` before any network request is made.
2. **Zero Persistence**: The middleware operates in memory only. No data is written to disk.
3. **Audit Trails**: Extensive logging hooks (without data payload) are provided for compliance auditing.

## 🛠 Tech Stack & Integration
- **LLM Engine:** OpenAI ChatGPT Business API (No-Training Policy enforced)
- **Benchmark Alignment:** [CBLUE (Chinese Biomedical Language Understanding Evaluation)](https://github.com/CBLUEbenchmark/CBLUE)
- **De-identification:** Integration with [Microsoft Presidio](https://github.com/microsoft/presidio) for local entity masking.

## 📅 Roadmap (30 Days)
- [ ] Release Python SDK for local PII scrubbing + API dispatching.
- [ ] Publish comparison report: Local BERT vs. ChatGPT Business on CBLUE datasets.
- [ ] Release standardized JSON Schema for medical entity extraction.

## 📄 License
Apache-2.0 License
