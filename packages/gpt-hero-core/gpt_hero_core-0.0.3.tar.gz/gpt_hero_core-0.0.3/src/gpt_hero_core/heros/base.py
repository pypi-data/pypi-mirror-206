from abc import abstractmethod

from ..plugins.base import _PluginBase
from ..skills.base import SkillBase


class HeroBase(_PluginBase):
    namespace = "hero"

    skills: list[SkillBase] = []

    @abstractmethod
    def mission(self, quest: str) -> str:
        raise NotImplementedError()
