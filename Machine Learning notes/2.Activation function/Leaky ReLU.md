**Leaky ReLU** is designed to ensure neurons never completely "die." Instead of turning negative values into a hard zero, it gives them a tiny, tiny slope (usually 0.01). 💧

- **The Logic:** Positive values stay the same. Negative values are shrunk significantly but not eliminated.
    
- **The Math:** $f(x) = \max(0.01x, x)$