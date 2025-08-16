def calculate_performance(returns):
    cumulative_return = (1 + returns).prod() - 1
    annualized_return = (1 + cumulative_return) ** (252 / len(returns)) - 1
    volatility = returns.std() * (252 ** 0.5)
    sharpe_ratio = annualized_return / volatility if volatility != 0 else 0
    
    return {
        'cumulative_return': cumulative_return,
        'annualized_return': annualized_return,
        'volatility': volatility,
        'sharpe_ratio': sharpe_ratio
    }