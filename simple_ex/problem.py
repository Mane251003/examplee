def problem():
    
    LRS_Transactional_Cost=0.9
    LRS_Hot_Cost=0.5
    if LRS_Transactional_Cost > LRS_Hot_Cost:

        recommendation = False 

        savings = LRS_Transactional_Cost - LRS_Hot_Cost

        return f"Recommendation: HOT TIER (Savings: ${savings}:.6f) per unit)"

    else:

        recommendation = True 
        return "Recommendation: Stick with TRANSACTIONAL tier (Hot tier would cost more)"