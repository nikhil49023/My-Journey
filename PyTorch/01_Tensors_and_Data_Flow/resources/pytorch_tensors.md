# PyTorch Tensors: The Atomic Units of Deep Learning

## 1. What is a Tensor?
A Tensor is a multi-dimensional array, similar to NumPy's ndarray, but with a critical superpower: **GPU Acceleration**.

### Key Attributes:
- **Shape:** The dimensions of the data (e.g., [3, 224, 224] for a color image).
- **Dtype:** The data type (e.g., `float32`, `int64`).
- **Device:** Where the data lives (`cpu` or `cuda`).

## 2. Creation Ops
- `torch.tensor([[1, 2], [3, 4]])` - From existing data.
- `torch.zeros((3, 3))` - Initializing weights.
- `torch.randn((10, 10))` - Random initialization for neural nets.

## 3. The Power of Autograd
PyTorch tracks every operation on a tensor if `requires_grad=True`. This builds a **Dynamic Computational Graph** (DCG).
- `backward()`: Computes the gradient of the loss with respect to all tensors in the graph.
- `grad`: Stores the computed gradient.

## 4. Common Mistakes (The "Gotchas")
- **Shape Mismatch:** Trying to multiply [3x4] with [3x4] (should be [3x4] and [4xN]).
- **Device Mismatch:** Trying to add a CPU tensor to a GPU tensor.
- **In-place Operations:** `x += 1` can sometimes break the autograd graph.
