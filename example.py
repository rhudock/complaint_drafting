"""
Example usage of the Complaint Drafting Expert System

This script demonstrates how to use the expert system programmatically.
"""

from complaint_drafter import ComplaintDraftingExpertSystem


def example_basic_usage():
    """Demonstrate basic usage of the expert system."""
    
    print("=" * 70)
    print("EXAMPLE: Basic Usage")
    print("=" * 70 + "\n")
    
    # Initialize the system
    system = ComplaintDraftingExpertSystem()
    
    # Prepare case information
    case_info = """
    Plaintiff: John Smith
    Defendant: ABC Corporation
    
    On January 15, 2025, I was working at ABC Corporation's manufacturing facility
    in Chicago, Illinois. I was operating machinery when a safety guard that was
    supposed to be in place was missing. The company had been notified about this
    issue multiple times but failed to repair it.
    
    As a result of the missing safety guard, my hand was caught in the machinery,
    resulting in severe injuries including broken bones and nerve damage. I required
    emergency surgery and three months of physical therapy.
    
    I have incurred over $50,000 in medical bills and lost wages. The company
    violated OSHA workplace safety regulations by failing to maintain proper
    safety equipment.
    """
    
    # Process the complaint
    print("Processing case information...\n")
    results = system.draft_complaint(case_info)
    
    # Display results
    if "error" not in results:
        print("✓ Complaint drafted successfully!")
        print("\nWorkflow completed with the following outputs:")
        for key in results.keys():
            print(f"  - {key}")
    else:
        print(f"✗ Error: {results['error']}")
    
    print("\n" + "=" * 70 + "\n")


def example_custom_workflow():
    """Demonstrate how to customize the expert system."""
    
    print("=" * 70)
    print("EXAMPLE: Custom Workflow")
    print("=" * 70 + "\n")
    
    # Initialize with custom API key if needed
    # system = ComplaintDraftingExpertSystem(api_key="your-custom-key")
    
    system = ComplaintDraftingExpertSystem()
    
    print("The expert system uses a structured workflow:")
    print("  1. Gather and organize facts")
    print("  2. Identify legal claims")
    print("  3. Draft the complaint")
    print("  4. Review and refine")
    print("\nEach step uses LLM prompts to ensure comprehensive coverage.")
    
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    print("\nComplaint Drafting Expert System - Examples\n")
    
    example_basic_usage()
    example_custom_workflow()
    
    print("For interactive mode, run: python complaint_drafter.py")
