"""Abstact base classes for the `Bijection` and `Bijection` types. Note when implementing
bijections, by convention we try to i) implement the "transform" methods as the
faster/more intuitive approach (compared to the inverse methods); and ii) implement only
the forward methods if an inverse is not available. The `Invert` bijection can be used
to invert the orientation if a fast inverse is desired (e.g. maximum likelihood fitting
of flows).
"""

from abc import abstractmethod

from equinox import Module
from jax import Array


class Bijection(Module):
    """Bijection base class. Similar to :py:class:`~flowjax.distributions.Distribution`,
    bijections have a ``shape`` and a ``cond_shape`` attribute. To allow easy composing
    of bijections, all bijections support passing of conditioning variables (even if
    ignored). Unlike distributions, the ``shape`` attribute can be None, for cases where
    the shape may be unknown, or unimportant (e.g. the
    :py:class:`~flowjax.bijections.tanh.Tanh` bijection is compatible with any shape of
    input).

    The methods of bijections do not generally support passing of additional batch
    dimensions, however, ``jax.vmap`` or ``eqx.filter_vmap`` can be used to vmap
    specific methods if desired, and a bijection can be explicitly vectorised using the
    :py:class:`~flowjax.bijections.jax_transforms.Batch` bijection.

    Bijections are registered as Jax PyTrees (as they are equinox modules), so are
    compatible with normal jax operations.

    Implementing a bijection

        (1) Inherit from ``Bijection``.
        (2) Define the attributes ``shape`` and ``cond_shape``
        (3) Implement the abstract methods ``transform``, ``transform_and_log_det``,
            ``inverse`` and ``inverse_and_log_det``. These should act on
            inputs compatible with the shapes ``shape`` for ``x``, and ``cond_shape``
            for ``condition``.

    """

    shape: tuple[int, ...]
    cond_shape: tuple[int, ...] | None

    @abstractmethod
    def transform(self, x: Array, condition: Array | None = None) -> Array:
        """Apply transformation."""

    @abstractmethod
    def transform_and_log_det(
        self, x: Array, condition: Array | None = None
    ) -> tuple[Array, Array]:
        """Apply transformation and compute log absolute value of the Jacobian determinant."""

    @abstractmethod
    def inverse(self, y: Array, condition: Array | None = None) -> Array:
        """Invert the transformation."""

    @abstractmethod
    def inverse_and_log_det(
        self, y: Array, condition: Array | None = None
    ) -> tuple[Array, Array]:
        """Invert the transformation and compute log absolute value of the Jacobian determinant."""

    def _argcheck(self, x: Array, condition: Array | None = None):
        """Utility argcheck that can be added to bijection methods as required."""
        if self.shape is not None:
            if x.shape != self.shape:
                raise ValueError(f"Expected x.shape {self.shape}, got {x.shape}")

        if self.cond_shape is not None:
            if condition is None:
                raise ValueError("Condition should be provided")
            if condition.shape != self.cond_shape:
                raise ValueError(
                    f"Expected condition.shape {self.cond_shape}, got {condition.shape}"
                )
