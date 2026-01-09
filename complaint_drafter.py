"""
Complaint Drafting Expert System using PocketFlow

This module implements an LLM-powered expert system for drafting legal complaints
using the PocketFlow framework for structured workflow management.
"""

import os
from typing import Dict, Any, List
from dotenv import load_dotenv

try:
    from pocketflow import Flow, Step
except ImportError:
    # Fallback if pocketflow has different import structure
    print("Warning: PocketFlow not available. Please install with: pip install pocketflow")
    print("Using mock implementation for demonstration.")
    
    class Step:
        """Mock Step class for demonstration"""
        def __init__(self, name: str, prompt: str, **kwargs):
            self.name = name
            self.prompt = prompt
            self.kwargs = kwargs
    
    class Flow:
        """Mock Flow class for demonstration"""
        def __init__(self, steps: List[Step]):
            self.steps = steps
        
        def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
            """Mock run method - returns sample outputs matching expected structure"""
            print("Mock Flow execution - PocketFlow not installed")
            print("Install PocketFlow for full functionality: pip install pocketflow")
            return {
                "facts_summary": "[Mock] Facts would be extracted and organized here",
                "legal_claims": "[Mock] Legal claims would be identified here",
                "draft_complaint": "[Mock] Draft complaint would be generated here",
                "final_complaint": "[Mock] Final reviewed complaint would be here"
            }

# Load environment variables
load_dotenv()


class ComplaintDraftingExpertSystem:
    """
    Expert system for drafting legal complaints using PocketFlow.
    
    This system uses a multi-step workflow to gather information,
    analyze the case, and draft a comprehensive legal complaint.
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the complaint drafting expert system.
        
        Args:
            api_key: Optional API key for LLM service. If not provided,
                    will attempt to load from OPENAI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            print("Warning: No API key provided. Set OPENAI_API_KEY environment variable.")
        
        self.flow = self._create_complaint_workflow()
    
    def _create_complaint_workflow(self) -> Flow:
        """
        Create the PocketFlow workflow for complaint drafting.
        
        Returns:
            Flow: A PocketFlow workflow with structured steps for complaint drafting.
        """
        steps = [
            Step(
                name="gather_facts",
                prompt="""You are a legal expert assistant helping to gather facts for a complaint.
                
Based on the following information provided by the user, extract and organize the key facts:
- Parties involved (plaintiff and defendant)
- Date and location of the incident
- Description of what happened
- Harm or damages suffered
- Any relevant laws or regulations violated

User information: {user_input}

Provide a structured summary of the facts.""",
                output_key="facts_summary"
            ),
            
            Step(
                name="identify_claims",
                prompt="""You are a legal expert identifying potential legal claims.
                
Based on the following facts, identify potential legal claims and causes of action:

{facts_summary}

For each claim, specify:
1. The legal basis (statute, common law, etc.)
2. The elements that must be proven
3. How the facts support each element

Provide your analysis in a structured format.""",
                output_key="legal_claims"
            ),
            
            Step(
                name="draft_complaint",
                prompt="""You are a legal expert drafting a formal legal complaint.
                
Based on the facts and legal claims identified, draft a formal complaint including:

Facts:
{facts_summary}

Legal Claims:
{legal_claims}

The complaint should include:
1. CAPTION - Court name, parties, case number placeholder
2. INTRODUCTION - Brief overview of the case
3. PARTIES - Description of plaintiff and defendant
4. JURISDICTION AND VENUE - Basis for court jurisdiction
5. FACTUAL ALLEGATIONS - Detailed chronological facts
6. CAUSES OF ACTION - Each legal claim as a separate count
7. PRAYER FOR RELIEF - Specific relief requested
8. SIGNATURE BLOCK

Draft a professional, well-structured complaint following legal formatting conventions.""",
                output_key="draft_complaint"
            ),
            
            Step(
                name="review_and_refine",
                prompt="""You are a senior legal reviewer checking a complaint draft.
                
Review the following complaint draft and provide:
1. Strengths of the complaint
2. Potential weaknesses or gaps
3. Suggestions for improvement
4. Final refined version

Draft Complaint:
{draft_complaint}

Provide your review and the refined final version.""",
                output_key="final_complaint"
            )
        ]
        
        return Flow(steps=steps)
    
    def draft_complaint(self, user_input: str) -> Dict[str, Any]:
        """
        Execute the complaint drafting workflow.
        
        Args:
            user_input: User-provided information about the case including
                       facts, parties, and circumstances.
        
        Returns:
            Dict containing the workflow outputs including facts summary,
            legal claims analysis, draft complaint, and final complaint.
        """
        inputs = {
            "user_input": user_input
        }
        
        try:
            results = self.flow.run(inputs)
            return results
        except Exception as e:
            print(f"Error executing workflow: {e}")
            return {
                "error": str(e),
                "status": "failed"
            }
    
    def draft_complaint_interactive(self):
        """
        Run an interactive session for complaint drafting.
        
        Prompts the user for information and guides them through
        the complaint drafting process.
        """
        print("=" * 70)
        print("COMPLAINT DRAFTING EXPERT SYSTEM")
        print("=" * 70)
        print("\nThis system will help you draft a legal complaint.")
        print("Please provide detailed information about your case.\n")
        
        print("Enter information about your case:")
        print("(Include: parties involved, what happened, when, where,")
        print(" damages suffered, and any relevant laws)")
        print("\nType your response below (press Enter twice when done):")
        
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                if lines:  # Empty line after some input
                    break
        
        user_input = "\n".join(lines)
        
        if not user_input.strip():
            print("\nNo input provided. Exiting.")
            return
        
        print("\n" + "=" * 70)
        print("Processing your case information...")
        print("=" * 70 + "\n")
        
        results = self.draft_complaint(user_input)
        
        if "error" in results:
            print(f"Error: {results['error']}")
            return
        
        # Display results
        print("\n" + "=" * 70)
        print("COMPLAINT DRAFTING RESULTS")
        print("=" * 70 + "\n")
        
        if "facts_summary" in results:
            print("FACTS SUMMARY:")
            print("-" * 70)
            print(results["facts_summary"])
            print()
        
        if "legal_claims" in results:
            print("\nLEGAL CLAIMS ANALYSIS:")
            print("-" * 70)
            print(results["legal_claims"])
            print()
        
        if "draft_complaint" in results:
            print("\nDRAFT COMPLAINT:")
            print("-" * 70)
            print(results["draft_complaint"])
            print()
        
        if "final_complaint" in results:
            print("\nFINAL COMPLAINT:")
            print("-" * 70)
            print(results["final_complaint"])
            print()


def main():
    """Main entry point for the complaint drafting expert system."""
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("=" * 70)
        print("SETUP REQUIRED")
        print("=" * 70)
        print("\nPlease set your OpenAI API key in the environment:")
        print("  export OPENAI_API_KEY='your-api-key-here'")
        print("\nOr create a .env file with:")
        print("  OPENAI_API_KEY=your-api-key-here")
        print("\n" + "=" * 70)
        print("\nContinuing with demo mode (limited functionality)...\n")
    
    # Initialize the expert system
    system = ComplaintDraftingExpertSystem()
    
    # Run interactive mode
    system.draft_complaint_interactive()


if __name__ == "__main__":
    main()
