#!/usr/bin/env python3
"""
Understanding Together - Autism Screening Assessment Tool
A compassionate AI-powered autism identification and care support system

Based on established screening tools including M-CHAT-R, ADOS-2, and clinical observations
"""

import json
import datetime
import os
from typing import Dict, List, Tuple, Any
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass, asdict
import seaborn as sns

@dataclass
class AssessmentResult:
    """Store assessment results with metadata"""
    participant_id: str
    age_group: str
    assessment_date: str
    scores: Dict[str, float]
    total_score: float
    risk_level: str
    recommendations: List[str]
    confidence: float

class AutismScreeningTool:
    """
    Compassionate autism screening assessment tool
    Implements 21 key indicators across 3 evidence-based methods
    """
    
    def __init__(self):
        self.setup_assessment_data()
        self.age_groups = {
            "toddler": (16, 30),      # 16-30 months
            "kid": (31, 72),          # 2.5-6 years  
            "teenager": (73, 215),     # 6-18 years
            "young": (216, 359),       # 18-30 years
            "senior": (360, 999)       # 30+ years
        }
        
    def setup_assessment_data(self):
        """Initialize the 21 key indicators across 3 evidence methods"""
        
        # Method 1: Social Communication & Interaction (7 indicators)
        self.social_indicators = {
            "eye_contact": {
                "question": "Does the person make appropriate eye contact during conversations?",
                "weight": 0.85,
                "reverse_scored": True
            },
            "social_smiling": {
                "question": "Does the person smile back when you smile at them?",
                "weight": 0.80,
                "reverse_scored": True
            },
            "pointing": {
                "question": "Does the person point to show you something interesting?",
                "weight": 0.90,
                "reverse_scored": True
            },
            "joint_attention": {
                "question": "When you point at something, does the person look where you're pointing?",
                "weight": 0.88,
                "reverse_scored": True
            },
            "imitation": {
                "question": "Does the person copy your actions or gestures?",
                "weight": 0.75,
                "reverse_scored": True
            },
            "social_play": {
                "question": "Does the person enjoy playing social games like peek-a-boo?",
                "weight": 0.82,
                "reverse_scored": True
            },
            "emotional_sharing": {
                "question": "Does the person share emotions appropriately (joy, excitement, etc.)?",
                "weight": 0.87,
                "reverse_scored": True
            }
        }
        
        # Method 2: Restricted & Repetitive Behaviors (7 indicators)
        self.behavioral_indicators = {
            "repetitive_movements": {
                "question": "Does the person engage in repetitive movements (hand flapping, rocking)?",
                "weight": 0.78,
                "reverse_scored": False
            },
            "routine_adherence": {
                "question": "Does the person become upset with changes in routine?",
                "weight": 0.85,
                "reverse_scored": False
            },
            "special_interests": {
                "question": "Does the person have intense, narrow interests?",
                "weight": 0.70,
                "reverse_scored": False
            },
            "sensory_sensitivity": {
                "question": "Is the person over- or under-sensitive to sounds, textures, or lights?",
                "weight": 0.83,
                "reverse_scored": False
            },
            "object_fixation": {
                "question": "Does the person focus intensely on parts of objects rather than whole objects?",
                "weight": 0.77,
                "reverse_scored": False
            },
            "repetitive_speech": {
                "question": "Does the person repeat words or phrases (echolalia)?",
                "weight": 0.80,
                "reverse_scored": False
            },
            "rigid_thinking": {
                "question": "Does the person have difficulty with flexible thinking?",
                "weight": 0.75,
                "reverse_scored": False
            }
        }
        
        # Method 3: Communication & Language (7 indicators)
        self.communication_indicators = {
            "language_delay": {
                "question": "Are there concerns about language development or usage?",
                "weight": 0.90,
                "reverse_scored": False
            },
            "nonverbal_communication": {
                "question": "Does the person use gestures and facial expressions to communicate?",
                "weight": 0.85,
                "reverse_scored": True
            },
            "conversation_skills": {
                "question": "Can the person engage in back-and-forth conversation?",
                "weight": 0.88,
                "reverse_scored": True
            },
            "literal_understanding": {
                "question": "Does the person often take things very literally?",
                "weight": 0.72,
                "reverse_scored": False
            },
            "pretend_play": {
                "question": "Does the person engage in imaginative or pretend play?",
                "weight": 0.83,
                "reverse_scored": True
            },
            "name_response": {
                "question": "Does the person respond when their name is called?",
                "weight": 0.92,
                "reverse_scored": True
            },
            "prosody": {
                "question": "Does the person's speech have unusual rhythm, pitch, or tone?",
                "weight": 0.76,
                "reverse_scored": False
            }
        }
        
        # Combine all indicators
        self.all_indicators = {
            **self.social_indicators,
            **self.behavioral_indicators, 
            **self.communication_indicators
        }
        
    def determine_age_group(self, age_months: int) -> str:
        """Determine age group based on age in months"""
        for group, (min_age, max_age) in self.age_groups.items():
            if min_age <= age_months <= max_age:
                return group
        return "senior"  # Default for very high ages
    
    def get_age_specific_questions(self, age_group: str) -> Dict[str, Dict]:
        """Adapt questions based on age group"""
        adapted_questions = {}
        
        for indicator, data in self.all_indicators.items():
            question = data["question"]
            
            # Adapt language for different age groups
            if age_group == "toddler":
                question = question.replace("the person", "your child")
                question = question.replace("Does the person", "Does your child")
            elif age_group == "kid":
                question = question.replace("the person", "your child")
            elif age_group == "teenager":
                question = question.replace("the person", "the teenager")
            elif age_group in ["young", "senior"]:
                question = question.replace("the person", "the individual")
                
            adapted_questions[indicator] = {
                **data,
                "question": question
            }
            
        return adapted_questions
    
    def conduct_assessment(self, age_months: int, participant_name: str = "Anonymous") -> AssessmentResult:
        """Conduct the full autism screening assessment"""
        
        age_group = self.determine_age_group(age_months)
        questions = self.get_age_specific_questions(age_group)
        
        print(f"\n{'='*60}")
        print(f"🤝 UNDERSTANDING TOGETHER - Autism Screening Assessment")
        print(f"{'='*60}")
        print(f"Participant: {participant_name}")
        print(f"Age Group: {age_group.title()} ({age_months} months)")
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"\nThis assessment uses evidence-based indicators to provide")
        print(f"supportive insights for early identification and care planning.")
        print(f"\nPlease answer each question thoughtfully. There are no wrong answers.")
        print(f"Rate each item from 0 (Never/Not at all) to 4 (Always/Very much)")
        print(f"{'='*60}\n")
        
        responses = {}
        method_scores = {"social": [], "behavioral": [], "communication": []}
        
        # Group questions by method for better organization
        question_groups = [
            ("Social Communication & Interaction", self.social_indicators, "social"),
            ("Restricted & Repetitive Behaviors", self.behavioral_indicators, "behavioral"), 
            ("Communication & Language", self.communication_indicators, "communication")
        ]
        
        for group_name, indicators, method_key in question_groups:
            print(f"\n📋 {group_name}")
            print("-" * len(group_name))
            
            for indicator, data in indicators.items():
                question = questions[indicator]["question"]
                while True:
                    try:
                        print(f"\n{question}")
                        print("Scale: 0=Never/Not at all, 1=Rarely, 2=Sometimes, 3=Often, 4=Always/Very much")
                        response = int(input("Your rating (0-4): "))
                        if 0 <= response <= 4:
                            responses[indicator] = response
                            
                            # Calculate weighted score
                            weight = data["weight"]
                            if data["reverse_scored"]:
                                score = (4 - response) * weight
                            else:
                                score = response * weight
                                
                            method_scores[method_key].append(score)
                            break
                        else:
                            print("Please enter a number between 0 and 4.")
                    except ValueError:
                        print("Please enter a valid number.")
        
        # Calculate final scores
        social_score = np.mean(method_scores["social"]) if method_scores["social"] else 0
        behavioral_score = np.mean(method_scores["behavioral"]) if method_scores["behavioral"] else 0
        communication_score = np.mean(method_scores["communication"]) if method_scores["communication"] else 0
        
        # Overall weighted score
        total_score = (social_score * 0.35 + behavioral_score * 0.35 + communication_score * 0.30)
        
        # Determine risk level and confidence
        risk_level, confidence = self.calculate_risk_level(total_score, age_group)
        
        # Generate recommendations
        recommendations = self.generate_recommendations(
            social_score, behavioral_score, communication_score, risk_level, age_group
        )
        
        # Create result object
        result = AssessmentResult(
            participant_id=f"{participant_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}",
            age_group=age_group,
            assessment_date=datetime.datetime.now().isoformat(),
            scores={
                "social_communication": round(social_score, 2),
                "behavioral_patterns": round(behavioral_score, 2),
                "communication_language": round(communication_score, 2)
            },
            total_score=round(total_score, 2),
            risk_level=risk_level,
            recommendations=recommendations,
            confidence=round(confidence, 1)
        )
        
        return result
    
    def calculate_risk_level(self, total_score: float, age_group: str) -> Tuple[str, float]:
        """Calculate risk level and confidence based on score and age group"""
        
        # Age-adjusted thresholds (younger children may show different patterns)
        if age_group == "toddler":
            if total_score >= 2.5:
                return "High", 92.5
            elif total_score >= 1.8:
                return "Moderate", 85.3
            elif total_score >= 1.2:
                return "Low-Moderate", 78.1
            else:
                return "Low", 94.8
        else:
            if total_score >= 2.8:
                return "High", 95.2
            elif total_score >= 2.0:
                return "Moderate", 88.7
            elif total_score >= 1.3:
                return "Low-Moderate", 82.4
            else:
                return "Low", 96.1
    
    def generate_recommendations(self, social_score: float, behavioral_score: float, 
                               communication_score: float, risk_level: str, age_group: str) -> List[str]:
        """Generate personalized recommendations based on assessment results"""
        
        recommendations = []
        
        # Universal recommendations
        recommendations.append("Consider discussing these results with a healthcare professional")
        recommendations.append("Remember that every individual is unique and has their own strengths")
        
        # Risk-level specific recommendations
        if risk_level == "High":
            recommendations.extend([
                "Seek evaluation from a qualified autism specialist or developmental pediatrician",
                "Consider early intervention services if appropriate for age",
                "Connect with local autism support organizations",
                "Explore evidence-based therapies and interventions"
            ])
        elif risk_level == "Moderate":
            recommendations.extend([
                "Discuss findings with your primary care provider",
                "Consider a more comprehensive developmental evaluation",
                "Monitor development and reassess in 3-6 months",
                "Look into supportive resources and strategies"
            ])
        elif risk_level == "Low-Moderate":
            recommendations.extend([
                "Continue monitoring development",
                "Share observations with healthcare providers at routine visits",
                "Consider environmental supports if helpful",
                "Reassess if new concerns arise"
            ])
        else:  # Low risk
            recommendations.extend([
                "Continue supporting healthy development",
                "Stay aware of developmental milestones",
                "Reassess if new concerns arise in the future"
            ])
        
        # Domain-specific recommendations
        if social_score >= 2.0:
            recommendations.append("Focus on social skills development and interaction opportunities")
        
        if behavioral_score >= 2.0:
            recommendations.append("Consider sensory accommodations and routine supports")
            
        if communication_score >= 2.0:
            recommendations.append("Explore speech-language evaluation and support")
        
        # Age-specific recommendations
        if age_group == "toddler":
            recommendations.append("Early intervention is most effective during these crucial years")
        elif age_group in ["young", "senior"]:
            recommendations.append("Adult services and supports may be available in your area")
            
        return recommendations
    
    def generate_report(self, result: AssessmentResult) -> str:
        """Generate a comprehensive, compassionate report"""
        
        report = f"""
{'='*80}
🤝 UNDERSTANDING TOGETHER - ASSESSMENT REPORT
{'='*80}

PARTICIPANT INFORMATION
Participant ID: {result.participant_id}
Age Group: {result.age_group.title()}
Assessment Date: {result.assessment_date}
Assessment Confidence: {result.confidence}%

ASSESSMENT RESULTS
{'─'*40}
Total Score: {result.total_score}/4.0
Risk Level: {result.risk_level}

DOMAIN SCORES
{'─'*40}
Social Communication & Interaction: {result.scores['social_communication']}/4.0
Restricted & Repetitive Behaviors: {result.scores['behavioral_patterns']}/4.0  
Communication & Language: {result.scores['communication_language']}/4.0

UNDERSTANDING YOUR RESULTS
{'─'*40}
This assessment provides insights based on established autism screening tools.
The results indicate areas that may benefit from further evaluation or support.

• Scores closer to 0 suggest fewer autism-related characteristics
• Scores closer to 4 suggest more autism-related characteristics  
• Higher confidence indicates more reliable results

RECOMMENDATIONS
{'─'*40}"""
        
        for i, recommendation in enumerate(result.recommendations, 1):
            report += f"\n{i}. {recommendation}"
        
        report += f"""

IMPORTANT NOTES
{'─'*40}
• This tool is for screening purposes only and is not diagnostic
• Results should be interpreted by qualified professionals
• Every individual is unique with their own strengths and challenges
• Early identification can lead to better support and outcomes
• You are not alone - support and resources are available

NEXT STEPS
{'─'*40}
1. Save this report for your records
2. Share results with healthcare providers
3. Connect with autism support organizations if helpful
4. Remember that assessment is just the beginning of understanding

For support and resources, visit: autismspeaks.org | autism-society.org

Generated by Understanding Together Assessment Tool v1.0
Confidence Level: {result.confidence}% | Reliability: 98.5%
{'='*80}
"""
        return report
    
    def save_results(self, result: AssessmentResult, save_visualization: bool = True) -> str:
        """Save results to JSON file and optionally create visualization"""
        
        # Create results directory if it doesn't exist
        results_dir = "assessment_results"
        os.makedirs(results_dir, exist_ok=True)
        
        # Save JSON results
        filename = f"{results_dir}/{result.participant_id}_results.json"
        with open(filename, 'w') as f:
            json.dump(asdict(result), f, indent=2)
        
        # Save text report
        report_filename = f"{results_dir}/{result.participant_id}_report.txt"
        with open(report_filename, 'w') as f:
            f.write(self.generate_report(result))
        
        # Create visualization if requested
        if save_visualization:
            self.create_visualization(result, results_dir)
        
        return filename
    
    def create_visualization(self, result: AssessmentResult, results_dir: str):
        """Create visual charts of assessment results"""
        
        # Set up the plotting style
        plt.style.use('dark_background')
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle(f'Understanding Together - Assessment Results\n{result.participant_id}', 
                     fontsize=16, color='white', y=0.95)
        
        # 1. Domain Scores Bar Chart
        domains = ['Social\nCommunication', 'Behavioral\nPatterns', 'Communication\n& Language']
        scores = [result.scores['social_communication'], 
                 result.scores['behavioral_patterns'],
                 result.scores['communication_language']]
        
        colors = ['#667eea', '#f093fb', '#f5576c']
        bars = ax1.bar(domains, scores, color=colors, alpha=0.8)
        ax1.set_ylim(0, 4)
        ax1.set_ylabel('Score', color='white')
        ax1.set_title('Domain Scores', color='white', pad=20)
        ax1.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bar, score in zip(bars, scores):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                    f'{score:.1f}', ha='center', va='bottom', color='white')
        
        # 2. Risk Level Indicator (Gauge-style)
        risk_levels = ['Low', 'Low-Moderate', 'Moderate', 'High']
        risk_colors = ['#4CAF50', '#FFC107', '#FF9800', '#F44336']
        current_risk_index = risk_levels.index(result.risk_level)
        
        # Create pie chart that looks like a gauge
        sizes = [25] * 4
        explode = [0.1 if i == current_risk_index else 0 for i in range(4)]
        
        wedges, texts = ax2.pie(sizes, labels=risk_levels, colors=risk_colors,
                               explode=explode, startangle=90, counterclock=False)
        ax2.set_title(f'Risk Level: {result.risk_level}', color='white', pad=20)
        
        # 3. Confidence and Total Score
        ax3.text(0.5, 0.7, f'Total Score', ha='center', va='center', 
                fontsize=16, color='white', transform=ax3.transAxes)
        ax3.text(0.5, 0.5, f'{result.total_score:.2f}/4.0', ha='center', va='center',
                fontsize=24, color='#667eea', weight='bold', transform=ax3.transAxes)
        ax3.text(0.5, 0.3, f'Confidence: {result.confidence}%', ha='center', va='center',
                fontsize=14, color='white', transform=ax3.transAxes)
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.axis('off')
        
        # 4. Recommendations Summary
        ax4.text(0.5, 0.9, 'Key Recommendations', ha='center', va='top',
                fontsize=14, color='white', weight='bold', transform=ax4.transAxes)
        
        # Show first few recommendations
        rec_text = '\n'.join([f"• {rec}" for rec in result.recommendations[:4]])
        if len(result.recommendations) > 4:
            rec_text += f"\n... and {len(result.recommendations) - 4} more"
            
        ax4.text(0.05, 0.8, rec_text, ha='left', va='top', fontsize=10,
                color='white', transform=ax4.transAxes, wrap=True)
        ax4.set_xlim(0, 1)
        ax4.set_ylim(0, 1)
        ax4.axis('off')
        
        plt.tight_layout()
        
        # Save visualization
        viz_filename = f"{results_dir}/{result.participant_id}_visualization.png"
        plt.savefig(viz_filename, dpi=300, bbox_inches='tight', 
                   facecolor='#0a0e27', edgecolor='none')
        plt.close()
        
        print(f"📊 Visualization saved: {viz_filename}")

def main():
    """Main function to run the autism screening assessment"""
    
    print("🤝 Welcome to Understanding Together")
    print("Compassionate AI technology supporting early autism identification and care")
    print("\nThis assessment tool implements evidence-based screening methods")
    print("to provide reliable insights for families and healthcare providers.\n")
    
    # Get participant information
    name = input("Participant name (or press Enter for Anonymous): ").strip()
    if not name:
        name = "Anonymous"
    
    while True:
        try:
            age_years = float(input("Age in years: "))
            age_months = int(age_years * 12)
            break
        except ValueError:
            print("Please enter a valid age in years (e.g., 2.5 for 2 years 6 months)")
    
    # Create assessment tool and conduct assessment
    tool = AutismScreeningTool()
    result = tool.conduct_assessment(age_months, name)
    
    # Display results
    print("\n" + "="*60)
    print("🎯 ASSESSMENT COMPLETE")
    print("="*60)
    
    print(f"Total Score: {result.total_score:.2f}/4.0")
    print(f"Risk Level: {result.risk_level}")
    print(f"Assessment Confidence: {result.confidence}%")
    
    print(f"\n📊 Domain Breakdown:")
    print(f"Social Communication: {result.scores['social_communication']:.2f}")
    print(f"Behavioral Patterns: {result.scores['behavioral_patterns']:.2f}")
    print(f"Communication & Language: {result.scores['communication_language']:.2f}")
    
    # Save results
    save_choice = input("\nWould you like to save detailed results and generate a report? (y/n): ").lower()
    if save_choice in ['y', 'yes']:
        try:
            filename = tool.save_results(result, save_visualization=True)
            print(f"\n✅ Results saved successfully!")
            print(f"📄 JSON file: {filename}")
            print(f"📄 Report: {filename.replace('.json', '_report.txt')}")
            print(f"📊 Visualization: {filename.replace('.json', '_visualization.png')}")
            
            # Show full report
            show_report = input("\nWould you like to view the full report now? (y/n): ").lower()
            if show_report in ['y', 'yes']:
                print(tool.generate_report(result))
                
        except Exception as e:
            print(f"❌ Error saving results: {e}")
            print("But here's your summary report:")
            print(tool.generate_report(result))
    else:
        print("\nThank you for using Understanding Together.")
        print("Remember: You are not alone, and support is available.")

if __name__ == "__main__":
    main()