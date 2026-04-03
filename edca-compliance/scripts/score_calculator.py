#!/usr/bin/env python3
"""
EDCA Compliance Score Calculator
Calculates compliance score based on findings.

Usage: python score_calculator.py --high X --medium Y --low Z --applicable N
"""

import argparse


def calculate_score(applicable: int, compliant: int, partial: int, non_compliant: int) -> dict:
    """Calculate compliance score and statistics."""

    if applicable == 0:
        return {"error": "No applicable articles specified"}

    total_findings = partial + non_compliant

    # Weighted score: compliant = 100%, partial = 50%, non-compliant = 0%
    weighted_score = (compliant * 100 + partial * 50) / applicable

    # Risk-weighted penalty (high findings reduce score more)
    # This is a simplified calculation

    return {
        "applicable_articles": applicable,
        "compliant": compliant,
        "partially_compliant": partial,
        "non_compliant": non_compliant,
        "total_findings": total_findings,
        "compliance_percentage": round(weighted_score, 1),
        "compliance_rating": get_rating(weighted_score),
    }


def get_rating(score: float) -> str:
    """Get qualitative rating from score."""
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Fair"
    elif score >= 40:
        return "Poor"
    else:
        return "Critical"


def calculate_risk_stats(high: int, medium: int, low: int) -> dict:
    """Calculate risk statistics."""
    return {
        "high_risk": high,
        "medium_risk": medium,
        "low_risk": low,
        "total_findings": high + medium + low,
        "risk_level": get_overall_risk_level(high, medium),
    }


def get_overall_risk_level(high: int, medium: int) -> str:
    """Determine overall risk level."""
    if high >= 3:
        return "🔴 Critical"
    elif high >= 1 or medium >= 5:
        return "🟡 Elevated"
    elif medium >= 1:
        return "🟡 Moderate"
    else:
        return "🟢 Low"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate EDCA compliance score")
    parser.add_argument("--applicable", type=int, required=True, help="Number of applicable articles")
    parser.add_argument("--compliant", type=int, default=0, help="Number of fully compliant articles")
    parser.add_argument("--partial", type=int, default=0, help="Number of partially compliant articles")
    parser.add_argument("--non-compliant", type=int, default=0, help="Number of non-compliant articles")
    parser.add_argument("--high", type=int, default=0, help="Number of high risk findings")
    parser.add_argument("--medium", type=int, default=0, help="Number of medium risk findings")
    parser.add_argument("--low", type=int, default=0, help="Number of low risk findings")

    args = parser.parse_args()

    score = calculate_score(args.applicable, args.compliant, args.partial, args.non_compliant)
    risk = calculate_risk_stats(args.high, args.medium, args.low)

    print("\n=== Compliance Score ===")
    for key, value in score.items():
        print(f"{key}: {value}")

    print("\n=== Risk Statistics ===")
    for key, value in risk.items():
        print(f"{key}: {value}")