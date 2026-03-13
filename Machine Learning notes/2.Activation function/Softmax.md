Instead of looking at one node in isolation, it looks at the outputs of the entire layer and turns them into a set of probabilities that all **add up to 1 (100%)**. 🍕

- **The Logic:** It highlights the largest value (the "winner") and suppresses the smaller ones, ensuring the total confidence equals 1.0.
    
- **The Math:**
    
    $$\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}$$