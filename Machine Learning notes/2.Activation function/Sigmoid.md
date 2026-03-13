Before ReLU became popular, **Sigmoid** was the standard. It squashes any input value into a tight range between **0 and 1**. 🍔

- **The Logic:** Very large positive numbers become almost 1. Very large negative numbers become almost 0.
    
- **The Math:**
    
    $$f(x) = \frac{1}{1 + e^{-x}}$$
    rarely used in hidden layers today because it can make training very slow for deep networks.