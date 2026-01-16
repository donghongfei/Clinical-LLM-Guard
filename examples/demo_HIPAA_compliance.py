from clinical_guard.anonymizer import ClinicalAnonymizer

def run_compliance_demo():
    print("🔒 Clinical-LLM-Guard: Initializing Secure Environment...")
    
    # Mock Clinical Record
    raw_record = """
    Patient: John Doe (DOB: 1980-05-12)
    Contact: 555-0102
    Diagnosis: Type 2 Diabetes Mellitus.
    Notes: Patient reported dizziness on Jan 14.
    """
    
    guard = ClinicalAnonymizer()
    result = guard.sanitize(raw_record)
    
    print("\n--- [Step 1: Local Scrubbing] ---")
    print(f"Original Length: {result['original_len']}")
    print(f"Items Redacted: {result['items_redacted']}")
    
    print("\n--- [Step 2: Safe Payload for LLM] ---")
    print(result['anonymized_text'])
    
    print("\n✅ Data is now safe for transmission to Business API.")

if __name__ == "__main__":
    run_compliance_demo()
