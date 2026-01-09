"""
Complaint Drafting Expert System - Usage Guide

This document provides detailed usage instructions and examples for the
PocketFlow-based complaint drafting expert system.
"""

# ============================================================================
# QUICK START
# ============================================================================

# 1. Install dependencies
# pip install -r requirements.txt

# 2. Set up your API key (choose one method):
# export OPENAI_API_KEY='your-key-here'
# OR create a .env file with: OPENAI_API_KEY=your-key-here

# 3. Run the system
# python complaint_drafter.py


# ============================================================================
# PROGRAMMATIC USAGE EXAMPLES
# ============================================================================

from complaint_drafter import ComplaintDraftingExpertSystem

# Example 1: Basic Usage
# ----------------------------------------------------------------------------
def example_1_basic():
    """Simple complaint drafting"""
    
    system = ComplaintDraftingExpertSystem()
    
    case_info = """
    Plaintiff: Jane Doe
    Defendant: Acme Corporation
    
    On December 1, 2024, I was injured at the Acme Corporation facility
    due to their negligent maintenance of the premises. There was a large
    puddle of water with no warning signs, and I slipped and fell, 
    breaking my ankle.
    
    I incurred $25,000 in medical expenses and was unable to work for
    6 weeks, losing $10,000 in wages. The company violated local safety
    codes by failing to maintain the premises.
    """
    
    results = system.draft_complaint(case_info)
    
    print("Final Complaint:")
    print(results.get('final_complaint', 'No complaint generated'))


# Example 2: Accessing Individual Workflow Steps
# ----------------------------------------------------------------------------
def example_2_step_by_step():
    """Access each step of the workflow"""
    
    system = ComplaintDraftingExpertSystem()
    
    case_info = "Your case information here..."
    results = system.draft_complaint(case_info)
    
    # Access each step's output
    facts = results.get('facts_summary', '')
    claims = results.get('legal_claims', '')
    draft = results.get('draft_complaint', '')
    final = results.get('final_complaint', '')
    
    print("Step 1 - Facts:", facts)
    print("Step 2 - Claims:", claims)
    print("Step 3 - Draft:", draft)
    print("Step 4 - Final:", final)


# Example 3: Error Handling
# ----------------------------------------------------------------------------
def example_3_error_handling():
    """Handle potential errors"""
    
    system = ComplaintDraftingExpertSystem()
    
    case_info = "Your case information..."
    
    try:
        results = system.draft_complaint(case_info)
        
        if 'error' in results:
            print(f"Error occurred: {results['error']}")
        else:
            print("Success!")
            # Process results...
            
    except Exception as e:
        print(f"Exception: {e}")


# Example 4: Custom Configuration
# ----------------------------------------------------------------------------
def example_4_custom_config():
    """Use custom API key"""
    
    # Provide API key directly
    system = ComplaintDraftingExpertSystem(api_key='your-custom-key')
    
    # Use the system...
    results = system.draft_complaint("Case info...")


# ============================================================================
# INTERACTIVE MODE
# ============================================================================

# Simply run: python complaint_drafter.py
# The system will prompt you for:
# 1. Information about the parties involved
# 2. Date and location of the incident
# 3. Description of what happened
# 4. Damages suffered
# 5. Relevant laws or regulations

# Then it will process through all workflow steps and display the results.


# ============================================================================
# WORKFLOW DETAILS
# ============================================================================

# Step 1: Gather Facts
# - Extracts parties (plaintiff/defendant)
# - Organizes dates, locations, events
# - Identifies damages and harm
# - Notes relevant laws

# Step 2: Identify Claims
# - Analyzes facts for legal claims
# - Identifies causes of action
# - Specifies legal basis for each claim
# - Maps facts to legal elements

# Step 3: Draft Complaint
# - Creates formal complaint structure:
#   * Caption (court, parties, case number)
#   * Introduction
#   * Parties description
#   * Jurisdiction and venue
#   * Factual allegations
#   * Causes of action (separate counts)
#   * Prayer for relief
#   * Signature block

# Step 4: Review and Refine
# - Reviews draft for strengths/weaknesses
# - Identifies gaps or improvements
# - Produces refined final version


# ============================================================================
# TIPS AND BEST PRACTICES
# ============================================================================

# 1. Provide detailed information:
#    - Be specific about dates, times, locations
#    - Include all relevant parties
#    - Describe events chronologically
#    - Quantify damages when possible

# 2. Include legal context:
#    - Mention relevant laws or regulations
#    - Note any violations or breaches
#    - Identify contractual obligations if applicable

# 3. Review and customize:
#    - Always review AI-generated content
#    - Customize for your specific jurisdiction
#    - Have a legal professional review before filing

# 4. Iterate if needed:
#    - Run multiple times with refined inputs
#    - Compare different versions
#    - Combine the best elements


# ============================================================================
# LIMITATIONS
# ============================================================================

# This system is for drafting assistance only and:
# - Does NOT provide legal advice
# - Should NOT replace consultation with an attorney
# - May not reflect recent legal changes
# - May not cover jurisdiction-specific requirements
# - Requires legal professional review before filing


if __name__ == "__main__":
    print(__doc__)
    print("\nFor more examples, see example.py")
    print("For interactive mode, run: python complaint_drafter.py")
