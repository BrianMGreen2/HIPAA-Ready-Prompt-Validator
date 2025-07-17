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

"""
Customizing the Prompt Generator with Expanded Inputs & Output Formats
"""

def generate_prompt(patient_id, vitals_data, date_range, symptoms=None, medication_changes=None, provider_notes=None):
    prompt = (f"Between {date_range}, patient with ID {patient_id} reported the following abnormal vital signs:\n"
              f"{vitals_data}\n")
    if symptoms:
        prompt += f"Reported symptoms: {symptoms}\n"
    if medication_changes:
        prompt += f"Recent medication changes: {medication_changes}\n"
    if provider_notes:
        prompt += f"Provider notes: {provider_notes}\n"
    prompt += ("Please summarize the abnormalities and recommend if further review is needed by the healthcare provider. "
               "Include no patient identifiers or sensitive information in your output. Provide clear, actionable summary in bullet points.")
    return prompt

def generate_prompt(patient_id, vitals_data, date_range, output_format="bullet"):
    prompt = (f"Between {date_range}, patient with ID {patient_id} reported the following abnormal vital signs:\n"
              f"{vitals_data}\n")
    if output_format == "table":
        prompt += "Format your summary as a table with columns: Date, Vital Sign, Value, Abnormality.\n"
    elif output_format == "json":
        prompt += "Provide your summary as a JSON object listing abnormalities and recommendations.\n"
    elif output_format == "soap":
        prompt += "Present the summary in SOAP note format.\n"
    else:  # default to bullet
        prompt += "Please summarize abnormalities in bullet points.\n"
    prompt += "Exclude all direct identifiers and sensitive information from your output."
    return prompt

