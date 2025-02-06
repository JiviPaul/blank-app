

import streamlit as st
import spacy
import re

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Example compliance rules
compliance_rules = [
    r"\bdisclaimer\b",  # Check if 'disclaimer' is mentioned
    r"\bthank you\b",   # Check if 'thank you' is used
    r"\bprivacy\b",     # Check if 'privacy' is mentioned
]

# Function to check for compliance
def check_compliance(conversation):
    # Tokenize and clean the conversation using spaCy
    doc = nlp(conversation)

    # Check for the presence of compliance-related terms or phrases
    violations = []
    
    for rule in compliance_rules:
        if not re.search(rule, conversation, re.IGNORECASE):
            violations.append(f"Compliance Violation: '{rule}' is missing or not mentioned.")
    
    # Return any violations found
    if violations:
        return violations
    else:
        return ["Conversation is compliant."]

# Streamlit UI
st.title("Call Center Compliance Check")

st.write(
    "This app checks if a given call center conversation adheres to compliance rules, such as the inclusion of required phrases like 'disclaimer', 'thank you', or 'privacy'."
)

# User input for the conversation
conversation = st.text_area(
    "Enter the conversation text below:",
    height=200,
    placeholder="Type or paste the conversation here..."
)

if st.button("Check Compliance"):
    if conversation:
        # Run the compliance check
        violations = check_compliance(conversation)

        # Display results
        if violations:
            st.write("**Compliance Violations Found:**")
            for violation in violations:
                st.warning(violation)
        else:
            st.success("Conversation is compliant!")
    else:
        st.error("Please enter a conversation to check compliance.")
