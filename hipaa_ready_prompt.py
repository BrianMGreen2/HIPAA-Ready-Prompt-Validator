"""
HIPAA-Ready Prompt Generator for Clinical Care Manager Summary
"""

def generate_prompt(patient_id: str, vitals_data: str, date_range: str) -> str:
    """
    Generates a HIPAA-compliant prompt for summarizing patient-reported vital signs.

    Args:
        patient_id (str): Pseudonymized patient ID (hashed).
        vitals_data (str): Structured vital sign data with abnormalities.
        date_range (str): Date range for the vital signs.

    Returns:
        str: Formatted prompt string ready for submission to an LLM.
    """
    prompt = (f"Between {date_range}, patient with ID {patient_id} reported the following abnormal vital signs:\n"
              f"{vitals_data}\n"
              "Please summarize the abnormalities and recommend if further review is needed by the healthcare provider. "
              "Include no patient identifiers or sensitive information in your output. Provide clear, actionable summary in bullet points.")
    return prompt
