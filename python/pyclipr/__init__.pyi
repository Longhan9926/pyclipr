from typing import Any, Literal, Never, overload

import numpy as np
import numpy.typing as npt


class PathType: ...
Subject: PathType = ...
Clip: PathType = ...


class ClipType: ...
Union: ClipType = ...
Difference: ClipType = ...
Intersection: ClipType = ...
Xor: ClipType = ...


class FillType: ...
EvenOdd: FillType = ...
NonZero: FillType = ...
Positive: FillType = ...
Negative: FillType = ...


class JoinType: ...
Square: JoinType = ...  # FIXME
Round: JoinType = ...  # FIXME
Miter: JoinType = ...


class EndType: ...
Square: EndType = ...  # FIXME
Butt: EndType = ...
Joined: EndType = ...
Polygon: EndType = ...
Round: EndType = ...  # FIXME


clipperVersion: str = ...


class PolyPath:
    def __init__(self) -> Never: ...

    @property
    def level(self) -> int: ...

    @property
    def parent(self) -> PolyPath: ...


class PolyTree:
    def __init__(self) -> Never: ...

    @property
    def isHole(self) -> bool: ...

    @property
    def area(self) -> float: ...

    @property
    def attributes(self) -> npt.NDArray[np.float64]: ...

    @property
    def polygon(self) -> npt.NDArray[np.float64]: ...

    @property
    def children(self) -> list[PolyTree]: ...

    @property
    def count(self) -> int: ...

    def __len__(self) -> int: ...


class PolyTreeD:
    def __init__(self) -> Never: ...

    @property
    def isHole(self) -> bool: ...

    @property
    def area(self) -> float: ...

    @property
    def attributes(self) -> npt.NDArray[np.float64]: ...

    @property
    def polygon(self) -> npt.NDArray[np.float64]: ...

    @property
    def children(self) -> list[PolyTreeD]: ...

    @property
    def count(self) -> int: ...

    def __len__(self) -> int: ...


def polyTreeToPaths64(arg0: PolyTree) -> Any: ...  # TODO
def orientation(path: Any, scaleFactor: float) -> bool: ...  # TODO
def polyTreeToPaths(arg0: PolyTree) -> Any: ...  # TODO
def simplifyPath(path: Any, epsilon: float, isOpenPath: bool = ...) -> Any: ...  # TODO
def simplifyPaths(paths: Any, epsilon: float, isOpenPath: bool = ...) -> Any: ...  # TODO


class Clipper:
    scaleFactor: float
    preserveCollinear: bool

    def addPath(
        self,
        path: npt.NDArray[np.float64],
        pathType: PathType,
        isOpen: bool = ...
    ) -> None: ...

    def addPaths(
        self,
        paths: list[npt.NDArray[np.float64]],
        pathType: PathType,
        isOpen: bool = ...
    ) -> None: ...

    @overload
    def execute(
        self,
        clipType: ClipType,
        fillType: FillType = ...,
        *,
        returnOpenPaths: Literal[False] = ...,
        returnZ: Literal[False] = ...
    ) -> list[npt.NDArray[np.float64]]: ...

    @overload
    def execute(
        self,
        clipType: ClipType,
        fillType: FillType = ...,
        *,
        returnOpenPaths: Literal[False] = ...,
        returnZ: Literal[True] = ...
    ) -> tuple[
        list[npt.NDArray[np.float64]],
        list[npt.NDArray[np.float64]],
        list[npt.NDArray[np.float64]]
    ]: ...

    @overload
    def execute(
        self,
        clipType: ClipType,
        fillType: FillType = ...,
        *,
        returnOpenPaths: Literal[True] = ...,
        returnZ: bool = ...
    ) -> tuple[
        list[npt.NDArray[np.float64]],
        list[npt.NDArray[np.float64]],
        list[npt.NDArray[np.float64]],
        list[npt.NDArray[np.float64]]
    ]: ...

    @overload
    def execute2(
        self,
        clipType: ClipType,
        fillType: FillType = ...,
        *,
        returnOpenPaths: Literal[False] = ...,
        returnZ: bool = ...
    ) -> PolyTreeD: ...

    @overload
    def execute2(
        self,
        clipType: ClipType,
        fillType: FillType = ...,
        *,
        returnOpenPaths: Literal[True] = ...,
        returnZ: bool = ...
    ) -> tuple[
        PolyTreeD,
        list[npt.NDArray[np.float64]],
        list[npt.NDArray[np.float64]]
    ]: ...

    def clear(self) -> None: ...

    def cleanUp(self) -> None: ...


class ClipperOffset:
    scaleFactor: float
    arcTolerance: float
    miterLimit: float
    preserveCollinear: bool

    def addPath(
        self,
        path: npt.NDArray[np.float64],
        joinType: JoinType,
        endType: EndType = ...
    ) -> None: ...

    def addPaths(
        self,
        paths: list[npt.NDArray[np.float64]],
        joinType: JoinType,
        endType: EndType = ...
    ) -> None: ...

    def execute(
        self,
        delta: float
    ) -> list[npt.NDArray[np.float64]]: ...

    def execute2(
        self,
        delta: float
    ) -> PolyTreeD: ...

    def clear(self) -> None: ...


__version__: str = ...
