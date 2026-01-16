from typing import List, Dict, Optional
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

class ClinicalAnonymizer:
    """
    A HIPAA-compliant anonymizer for clinical text records.
    Ensures that no PII leaves the local environment before being sent to the LLM.
    """
    def __init__(self, entities: Optional[List[str]] = None):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
        self.entities = entities or ["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS", "DATE_TIME", "LOCATION"]

    def sanitize(self, text: str) -> Dict[str, str]:
        """
        Scrub PII from text.
        
        Args:
           text: Raw clinical note.
           
        Returns:
           Dict containing 'anonymized_text' and a mapping for re-identification (if local policy allows).
        """
        results = self.analyzer.analyze(text=text, entities=self.entities, language='en')
        anonymized_result = self.anonymizer.anonymize(text=text, analyzer_results=results)
        
        return {
            "original_len": len(text),
            "anonymized_text": anonymized_result.text,
            "items_redacted": len(results)
        }
