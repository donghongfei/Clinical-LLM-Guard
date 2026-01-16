# Clinical-LLM-Guard 🏥🔒

**Status:** Work in Progress (v0.1.0-alpha)

## 📌 Project Overview
Clinical-LLM-Guard is an open-source middleware designed to securely process non-structured clinical records using **ChatGPT Business/Team API**. 

It solves the "Privacy vs. Performance" dilemma in medical NLP by strictly enforcing **Zero Data Retention** policies and integrating local PII (Personally Identifiable Information) scrubbing.

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
